# 🏥 Patient Management API — FastAPI + Pydantic Practice

A hands-on practice project exploring **FastAPI** and **Pydantic** for building robust, data-validated REST APIs. This repo demonstrates request validation, computed fields, path/query parameters, error handling, and file-based data persistence.

---

## 📁 Project Structure

```
FASTAPI/
├── fastapi/
│   ├── main.py          # Core FastAPI application
│   └── pateints.json    # JSON "database" for patient records
├── myvenv/               # Python virtual environment
├── pydantic1/            # Standalone Pydantic concept practice
│   ├── computed.py       # @computed_field examples
│   ├── nested.py         # Nested models practice
│   ├── new.py
│   ├── new1.py
│   ├── new2.py
│   └── p.py
└── README.md
```

---

## 🚀 Features

- ✅ **Data validation** using Pydantic `BaseModel` with `Field()` constraints (`gt`, `lt`, `Literal`, examples)
- ✅ **Computed fields** (`@computed_field`) to auto-calculate BMI and health verdict
- ✅ **Path parameters** with metadata (`Path(...)`)
- ✅ **Query parameters** with validation (`Query(...)`)
- ✅ **Custom error handling** using `HTTPException`
- ✅ **JSON file storage** (read/write) simulating a lightweight database
- ✅ **Sorting** patients dynamically by height or BMI

---

## 🧩 Pydantic Model — `Patient`

| Field    | Type      | Validation Rule                     |
|----------|-----------|--------------------------------------|
| `id`     | `str`     | Required                            |
| `name`   | `str`     | Required                            |
| `city`   | `str`     | Required                            |
| `age`    | `int`     | `0 < age < 100`                     |
| `gender` | `Literal` | `'male'`, `'female'`, `'other'`     |
| `height` | `float`   | `> 0` (in meters)                   |
| `weight` | `float`   | `> 0` (in kilograms)                |

### Computed Fields
- **`bmi`** → `weight / (height ** 2)`, rounded to 2 decimals
- **`verdict`** → `underweight` / `normal` / `overweight` based on BMI

---

## 🔌 API Endpoints

| Method | Endpoint             | Description                          |
|--------|-----------------------|---------------------------------------|
| GET    | `/`                   | Welcome message                      |
| GET    | `/about`              | About the developer                  |
| GET    | `/patients`           | Get all patients                     |
| GET    | `/patients/{patient_id}` | Get a single patient by ID       |
| GET    | `/sort`               | Sort patients by `height` or `bmi`   |
| POST   | `/create`             | Create a new patient record          |

### Example: Sort Patients
```
GET /sort?sort_by=bmi&order=desc
```

### Example: Create Patient (Request Body)
```json
{
  "id": "P002",
  "name": "Aarav",
  "city": "Jaipur",
  "age": 25,
  "gender": "male",
  "height": 1.75,
  "weight": 70
}
```

---

## ⚙️ Setup & Run

```bash
# 1. Create & activate virtual environment
python -m venv myvenv
myvenv\Scripts\activate      # Windows
source myvenv/bin/activate   # macOS/Linux

# 2. Install dependencies
pip install fastapi uvicorn

# 3. Run the server
uvicorn main:app --reload

# 4. Open interactive API docs
http://127.0.0.1:8000/docs
```

---

## 🧪 Learning Goals Covered

- Understanding **Pydantic validation** (`Field`, `Annotated`, `Literal`, `gt/lt`)
- Using **`@computed_field`** to derive values dynamically
- Difference between **Path** vs **Query** parameters in FastAPI
- Raising and handling **custom HTTP exceptions**
- Reading/writing **JSON as a mock database**
- Exploring standalone **Pydantic concepts** (`pydantic1/` folder) like nested models and computed fields in isolation

---

## 📌 Notes

- `pateints.json` acts as a simple file-based database (no real DB used).
- `pydantic1/` is a separate sandbox folder for practicing individual Pydantic features before integrating them into the main FastAPI app.
- This project is for **learning purposes** — not production-ready (no auth, no persistent DB, no input sanitization beyond Pydantic).

---

## 👨‍💻 Developer

**Veer Pratap** — Practicing FastAPI & Pydantic for building type-safe, validated REST APIs.

---

### 📚 Next Steps To Explore
- [ ] Add PUT/DELETE endpoints for full CRUD
- [ ] Add pagination for `/patients`
- [ ] Integrate a real database (SQLite/PostgreSQL)
- [ ] Add authentication (OAuth2 / JWT)
- [ ] Write unit tests with `pytest` + `TestClient`

