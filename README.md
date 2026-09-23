# Autonomous Data Analyst

An end-to-end Data Science and Business Intelligence platform that transforms retail transaction data into automated business insights, customer segmentation, machine-learning analysis, interactive dashboards, and natural-language business analytics.

## 🚀 Live Demo

**Streamlit Application:**
[https://autonomous-data-analyst-1-u0gn.onrender.com](https://autonomous-data-analyst-1-u0gn.onrender.com)

**FastAPI Backend:**
[https://autonomous-data-analyst-gybz.onrender.com](https://autonomous-data-analyst-gybz.onrender.com)

**API Health Check:**
[https://autonomous-data-analyst-gybz.onrender.com/analytics/status](https://autonomous-data-analyst-gybz.onrender.com/analytics/status)

---

## 📌 Overview

The Autonomous Data Analyst is an end-to-end analytics platform built to automate common business-analysis workflows.

The project combines:

* Data analysis and preprocessing
* Exploratory Data Analysis
* RFM customer segmentation
* Machine Learning
* Business Intelligence
* Automated business recommendations
* FastAPI REST APIs
* Streamlit dashboard
* Power BI dashboards
* Natural-language business questions
* Automated testing
* GitHub Actions CI
* Docker
* Cloud deployment

The project demonstrates a complete workflow from business data analysis to a deployed analytics application.

---

## 📊 Key Results

The current analysis contains approximately:

| Metric              | Result |
| ------------------- | -----: |
| Total Revenue       | 18.86M |
| Total Orders        | 53,628 |
| Total Customers     |  5,942 |
| Total Products      |  5,305 |
| Countries Served    |     43 |
| Average Order Value | 351.60 |

---

## ✨ Features

### 📊 Business Analytics

The platform automatically generates:

* Revenue analysis
* Order analysis
* Customer analysis
* Product performance
* Geographic performance
* Average Order Value
* Revenue per Customer
* Business insights
* Business recommendations

### 👥 Customer Segmentation

Customers are segmented using **RFM analysis**:

* Recency
* Frequency
* Monetary Value

Segments include:

* Champions
* Loyal Customers
* Potential Loyalists
* At Risk
* Low Value

### 🤖 Machine Learning

The project evaluates customer-level prediction models using features such as:

* Recency
* Frequency
* Historical Revenue
* Average Order Value
* Transaction Count
* Total Quantity
* Unique Products

Models evaluated:

* Random Forest
* Gradient Boosting
* Linear Regression

Evaluation metrics:

* MAE
* RMSE
* R²

The current models provide a baseline for future model improvement.

### 🧠 AI Business Analyst

The application allows users to ask business questions in natural language.

Example questions:

```text
What is the total revenue?

How many customers are there?

How many orders were placed?

What is the top product?

Which customer segment has the highest average value?
```

The question engine classifies the question and retrieves the corresponding business result through the FastAPI backend.

---

## 📈 Power BI

The project includes Power BI dashboards covering:

* Executive Overview
* Product Performance
* Customer Analytics
* Geographic Analysis
* ML & Customer Opportunities

---

## 🏗️ Architecture

```text
                    UCI Online Retail II
                             │
                             ▼
                    Data Processing & EDA
                             │
                 ┌───────────┼───────────┐
                 ▼           ▼           ▼
                EDA         RFM          ML
                 │           │           │
                 └───────────┼───────────┘
                             ▼
                    Business Insights
                             │
                             ▼
                          FastAPI
                             │
                ┌────────────┼────────────┐
                ▼            ▼            ▼
            Streamlit     Power BI    AI Analyst
                │
                ▼
             Docker
                │
                ▼
             Render
```

---

## 🛠️ Technology Stack

| Category              | Technology          |
| --------------------- | ------------------- |
| Programming           | Python              |
| Data Analysis         | Pandas, NumPy       |
| Visualization         | Matplotlib, Seaborn |
| Machine Learning      | Scikit-learn        |
| API                   | FastAPI             |
| API Server            | Uvicorn             |
| Frontend              | Streamlit           |
| Business Intelligence | Power BI            |
| Testing               | Pytest              |
| CI/CD                 | GitHub Actions      |
| Containerization      | Docker              |
| Deployment            | Render              |
| Version Control       | Git / GitHub        |

---

## 📂 Project Structure

```text
Autonomous Data Analyst/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_profiling.ipynb
│   └── 03_machine_learning.ipynb
│
├── src/
│   ├── analysis/
│   └── api/
│
├── tests/
│   └── test_api.py
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🗃️ Dataset

This project uses the **UCI Online Retail II** dataset.

**Dataset:**
[https://archive.ics.uci.edu/dataset/502/online%2Bretail%2Bii](https://archive.ics.uci.edu/dataset/502/online%2Bretail%2Bii)

The dataset contains retail transactions from a UK-based online retailer over approximately two years.

**Citation:**

> Chen, D. (2012). Online Retail II. UCI Machine Learning Repository. [https://doi.org/10.24432/C5CG6D](https://doi.org/10.24432/C5CG6D)

Raw datasets are excluded from the Git repository.

---

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/AKASHRAUT108/autonomous-data-analyst.git
cd autonomous-data-analyst
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Start FastAPI

```powershell
python -m uvicorn src.api.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

### 5. Start Streamlit

Open another terminal with the virtual environment activated:

```powershell
streamlit run app/streamlit_app.py
```

Application:

```text
http://localhost:8501
```

---

## 🐳 Docker

Build the application:

```powershell
docker compose build
```

Start the services:

```powershell
docker compose up
```

Services:

```text
FastAPI   → http://localhost:8000
Streamlit → http://localhost:8501
```

Stop the services:

```powershell
docker compose down
```

---

## 🔌 API Endpoints

| Endpoint                          | Description              |
| --------------------------------- | ------------------------ |
| `/`                               | API information          |
| `/analytics/summary`              | Business KPI summary     |
| `/analytics/segments`             | Customer segmentation    |
| `/analytics/products`             | Product performance      |
| `/analytics/countries`            | Country performance      |
| `/analytics/ml-opportunities`     | ML opportunities         |
| `/analytics/recommendations`      | Business recommendations |
| `/analytics/insights`             | Business insights        |
| `/analytics/high-value-customers` | High-value customers     |
| `/analytics/status`               | API status               |
| `/analytics/ask`                  | AI Analyst               |

---

## 🧪 Testing

Run the test suite locally:

```powershell
pytest -q
```

The project uses GitHub Actions to automatically:

1. Install dependencies
2. Start the FastAPI server
3. Verify API availability
4. Run the test suite

Current CI workflow:

```text
Git Push
   ↓
GitHub Actions
   ↓
Install Dependencies
   ↓
Start FastAPI
   ↓
Verify API
   ↓
Run Tests
   ↓
PASS
```

---

## ☁️ Deployment

The application is containerized using Docker and deployed on Render.

### Frontend

[https://autonomous-data-analyst-1-u0gn.onrender.com](https://autonomous-data-analyst-1-u0gn.onrender.com)

### Backend

[https://autonomous-data-analyst-gybz.onrender.com](https://autonomous-data-analyst-gybz.onrender.com)

The Streamlit application communicates with the FastAPI backend through the configured `API_URL` environment variable.

---

## 🔮 Future Improvements

Potential future improvements include:

* Advanced forecasting
* Improved customer revenue prediction
* SHAP model explainability
* LLM-powered analytics
* SQL/PostgreSQL integration
* User authentication
* Automated report generation
* Advanced anomaly detection
* More advanced recommendation models
* Automated deployment through CI/CD

---

## 👨‍💻 Author

**Akash Raut**

**GitHub:**
[https://github.com/AKASHRAUT108](https://github.com/AKASHRAUT108)

**Project Repository:**
[https://github.com/AKASHRAUT108/autonomous-data-analyst](https://github.com/AKASHRAUT108/autonomous-data-analyst)

---

## ⭐ Project Status

**End-to-end project with live deployment, Docker support, REST API, Streamlit interface, Power BI analytics, automated testing, and GitHub Actions CI.**
