# Ecommerce Backend

A REST API for a simple ecommerce store built with [FastAPI](https://fastapi.tiangolo.com/). Users can register, log in, browse products, manage a shopping cart, and place orders. Data is stored in SQLite via SQLAlchemy.

## Features

- **User authentication** — Register, login, and JWT bearer tokens (30-minute expiry)
- **Products** — Create, list, fetch by ID, and delete products
- **Shopping cart** — Add items, view cart, and remove items (per authenticated user)
- **Orders** — Place an order from the cart and view order history

## Tech Stack

| Layer        | Technology                          |
| ------------ | ----------------------------------- |
| Framework    | FastAPI                             |
| ORM          | SQLAlchemy                          |
| Database     | SQLite (`database.db`)              |


## Project Structure

```
ecommerce/
├── app/
│   ├── main.py                 # FastAPI app and router registration
│   ├── database.py             # SQLite engine and session
│   ├── models.py               # SQLAlchemy models
│   ├── schemas.py              # Pydantic request/response schemas
│   ├── hashing.py              # Password hashing utilities
│   ├── authentication/
│   │   ├── auth_router.py      # Register and login
│   │   ├── oauth2.py           # Bearer token dependency
│   │   └── token.py            # JWT create/verify
│   └── routers/
│       ├── product_router.py
│       ├── cart_router.py
│       └── order_router.py
├── requirements.txt
└── database.db                 # Created automatically on first run
```

## Prerequisites

- Python 3.10+ (3.13 tested)
- `pip`

## Installation

1. Clone or download this repository.

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

From the project root (`ecommerce/`):

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- **Base URL:** `http://127.0.0.1:8000`
- **Interactive docs (Swagger):** `http://127.0.0.1:8000/docs`
- **Alternative docs (ReDoc):** `http://127.0.0.1:8000/redoc`

On startup, SQLAlchemy creates tables in `database.db` if they do not exist.

## Authentication

Protected routes require a JWT in the `Authorization` header:

```http
Authorization: Bearer <access_token>
```

1. **Register** — `POST /user/register` with `name`, `email`, and `password`.
2. **Login** — `POST /user/login` with `email` and `password`. The response includes `access_token` and `token_type` (`bearer`).
3. Use the token on endpoints that require authentication (cart, orders, and some product routes).

## API Endpoints

### Home

| Method | Path | Auth | Description        |
| ------ | ---- | ---- | ------------------ |
| GET    | `/`  | No   | Health check       |

### Users (`/user`)

| Method | Path            | Auth | Description              |
| ------ | --------------- | ---- | ------------------------ |
| POST   | `/user/register` | No  | Create a new user        |
| POST   | `/user/login`    | No  | Login and receive JWT    |

### Products (`/product`)

| Method | Path           | Auth | Description                    |
| ------ | -------------- | ---- | ------------------------------ |
| POST   | `/product/`    | Yes  | Add a product                  |
| GET    | `/product/`    | No   | List all products              |
| GET    | `/product/{id}`| No   | Get one product by ID          |
| DELETE | `/product/{id}`| Yes  | Delete a product by ID         |

**Create product body:**

```json
{
  "name": "Widget",
  "price": 19.99,
  "stock": 100,
  "discription": "A useful widget"
}
```

### Cart (`/cart`)

| Method | Path          | Auth | Description              |
| ------ | ------------- | ---- | ------------------------ |
| POST   | `/cart/add`   | Yes  | Add item to cart         |
| GET    | `/cart/`      | Yes  | List current user's cart |
| DELETE | `/cart/{id}`  | Yes  | Remove a cart line item  |

**Add to cart body:**

```json
{
  "product_id": 1,
  "quantity": 2
}
```

### Orders (`/orders`)

| Method | Path            | Auth | Description                          |
| ------ | --------------- | ---- | ------------------------------------ |
| POST   | `/orders/place` | Yes  | Checkout cart into an order          |
| GET    | `/orders/`      | Yes  | List current user's orders           |

Placing an order calculates the total from cart items, creates `Order` and `OrderItem` records, and clears the user's cart.

## Data Models

- **User** — `name`, `email`, hashed `password`
- **Product** — `name`, `price`, `stock`, `discription`
- **Cart** — Links `user_id`, `product_id`, and `quantity`
- **Order** — `user_id`, `total_amount`, `create_at`
- **OrderItem** — Line items for each order (`product_id`, `quantity`, `price`)

## Example Workflow

1. Register: `POST /user/register`
2. Login: `POST /user/login` → save `access_token`
3. Add products: `POST /product/` (with Bearer token)
4. Browse: `GET /product/`
5. Add to cart: `POST /cart/add` (with Bearer token)
6. Checkout: `POST /orders/place` (with Bearer token)
7. View orders: `GET /orders/` (with Bearer token)

## Configuration Notes

- The database file path is set in `app/database.py` as `sqlite:///./database.db`.
- JWT settings (`SECRET_KEY`, `ALGORITHM`, `ACCESS_TOKEN_EXPIRE_MINUTES`) live in `app/authentication/token.py`. For production, use environment variables and a strong secret key instead of a hardcoded value.

## License

This project is provided as-is for learning and development. Add a license file if you plan to distribute it.
