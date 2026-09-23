# 🚀 FastAPI + ML Practice — Spam Classifier & Patient Management API

A hands-on learning repo with two projects:

1. **📧 E-Mail/SMS Spam Classifier**: an NLP + Machine Learning model served through both a **Streamlit** web app and a **FastAPI** REST endpoint.
2. **🏥 Patient Management API**: a **FastAPI + Pydantic** project covering validation, computed fields, path/query params, error handling and JSON-file persistence.

---

## 📁 Project Structure

```
.
├── ML Model/
│   ├── app.py             # Streamlit web app for spam prediction
│   ├── api.py             # FastAPI endpoint serving the ML model (POST /predict)
│   ├── model.pkl          # Trained classifier
│   └── vectorizer.pkl     # Fitted TF-IDF / Count vectorizer
│
├── fastapi/
│   ├── main.py            # Patient Management API
│   └── pateints.json      # JSON "database" for patient records
│
├── pydantic1/             # Standalone Pydantic concept practice
│   ├── computed.py        # @computed_field examples
│   ├── nested.py          # Nested models
│   └── new.py, new1.py, new2.py, p.py
│
├── img.png                # Screenshot
└── README.md
```

---

# 📧 Project 1: Spam Classifier (ML Model)

A text classifier that predicts whether an e-mail / SMS message is **Spam** or **Not Spam**.

## 🧠 How It Works

```
Raw text → Tokenize → Remove stop words → Porter Stemming → Vectorize → Model → Spam / Not Spam
```

1. **Tokenize**: extract alphanumeric words using regex
2. **Clean**: remove English stop words and punctuation
3. **Stem**: reduce words to their root using `PorterStemmer`
4. **Vectorize**: convert text to numeric features using the saved `vectorizer.pkl`
5. **Predict**: classify with the saved `model.pkl` (`1` = Spam, `0` = Not Spam)

> ⚠️ The preprocessing in the app/API **must match** the preprocessing used during training, otherwise predictions will be off.

## 🖥️ Streamlit App

```bash
cd "ML Model"
streamlit run app.py
```

Opens at `http://localhost:8501`. Type a message, click **Predict**, and see the result.

## 🔌 ML FastAPI Endpoint

```bash
cd "ML Model"
uvicorn api:app --reload
```

Interactive docs: `http://127.0.0.1:8000/docs`

| Method | Endpoint   | Description                          |
|--------|------------|---------------------------------------|
| POST   | `/predict` | Classify a message as Spam / Not Spam |

**Request**
```json
{
  "text": "Congratulations! You won a free prize. Click here to claim now."
}
```

**Response**
```json
{
  "prediction": 1,
  "label": "Spam"
}
```

### 🐛 Common Pitfall: `Object of type int64 is not JSON serializable`

`model.predict()` returns NumPy types (`numpy.int64`), which Python's JSON encoder can't serialize. Always convert to a native type before returning:

```python
result = int(model.predict(vector_input)[0])
```

Streamlit doesn't hit this because it never serializes the value; it only compares `result == 1`.

---

# 🏥 Project 2: Patient Management API (FastAPI + Pydantic)

A hands-on project exploring **FastAPI** and **Pydantic** for building robust, data-validated REST APIs.

## ✨ Features

- ✅ **Data validation** with Pydantic `BaseModel` and `Field()` constraints (`gt`, `lt`, `Literal`, examples)
- ✅ **Computed fields** (`@computed_field`) to auto-calculate BMI and health verdict
- ✅ **Path parameters** with metadata (`Path(...)`)
- ✅ **Query parameters** with validation (`Query(...)`)
- ✅ **Custom error handling** using `HTTPException`
- ✅ **JSON file storage** (read/write) simulating a lightweight database
- ✅ **Dynamic sorting** of patients by height or BMI

## 🧩 Pydantic Model: `Patient`

| Field    | Type      | Validation Rule                 |
|----------|-----------|----------------------------------|
| `id`     | `str`     | Required                        |
| `name`   | `str`     | Required                        |
| `city`   | `str`     | Required                        |
| `age`    | `int`     | `0 < age < 100`                 |
| `gender` | `Literal` | `'male'`, `'female'`, `'other'` |
| `height` | `float`   | `> 0` (meters)                  |
| `weight` | `float`   | `> 0` (kilograms)               |

**Computed fields**
- **`bmi`** → `weight / (height ** 2)`, rounded to 2 decimals
- **`verdict`** → `underweight` / `normal` / `overweight` based on BMI

## 🔌 API Endpoints

| Method | Endpoint                 | Description                        |
|--------|---------------------------|-------------------------------------|
| GET    | `/`                       | Welcome message                    |
| GET    | `/about`                  | About the developer                |
| GET    | `/patients`               | Get all patients                   |
| GET    | `/patients/{patient_id}`  | Get a single patient by ID         |
| GET    | `/sort`                   | Sort patients by `height` or `bmi` |
| POST   | `/create`                 | Create a new patient record        |

**Sort example**
```
GET /sort?sort_by=bmi&order=desc
```

**Create example**
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

## ▶️ Run

```bash
cd fastapi
uvicorn main:app --reload --port 8001
```

Docs: `http://127.0.0.1:8001/docs`

---

## ⚙️ Setup

```bash
# 1. Create & activate a virtual environment
python -m venv myvenv
myvenv\Scripts\activate          # Windows
source myvenv/bin/activate       # macOS / Linux

# 2. Install dependencies
pip install fastapi uvicorn pydantic streamlit scikit-learn nltk
```

> 💡 The `.pkl` files were created with a specific scikit-learn version. If you see unpickling warnings or errors, install the same version used for training (`pip install scikit-learn==<version>`).

> 💡 Both APIs default to port `8000`. Use `--port` to run them side by side.

---

## 🧪 Learning Goals Covered

- Building an end-to-end **NLP text classification** pipeline
- Serving an ML model through **Streamlit** (UI) and **FastAPI** (REST API)
- Handling **NumPy → JSON serialization** issues
- **Pydantic** validation (`Field`, `Annotated`, `Literal`, `gt/lt`)
- Using **`@computed_field`** to derive values dynamically
- **Path vs Query** parameters in FastAPI
- Raising custom **HTTP exceptions**
- Using JSON as a mock database
- Exploring standalone Pydantic concepts in `pydantic1/`

---

## 📌 Notes

- `pateints.json` acts as a simple file-based database (no real DB used).
- `pydantic1/` is a sandbox for practicing Pydantic features in isolation.
- This repo is for **learning purposes**: no authentication, no persistent database, and no input sanitization beyond Pydantic.

---

## 🔮 Next Steps

- [ ] Share the text preprocessing in one module used by both Streamlit and FastAPI
- [ ] Return spam probability using `predict_proba`
- [ ] Add a `/health` endpoint and model-loading on startup
- [ ] Add PUT/DELETE endpoints and pagination to the Patient API
- [ ] Integrate a real database (SQLite / PostgreSQL)
- [ ] Add authentication (OAuth2 / JWT)
- [ ] Write unit tests with `pytest` + `TestClient`
- [ ] Dockerize and deploy

---

## 👨‍💻 Developer

**Veer Pratap**: practicing FastAPI, Pydantic and ML deployment to build type-safe, validated REST APIs.
