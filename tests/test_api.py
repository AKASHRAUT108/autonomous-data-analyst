import requests


BASE_URL = "http://127.0.0.1:8000"


def test_root():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"


def test_analytics_status():
    response = requests.get(f"{BASE_URL}/analytics/status")
    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["available_files"] > 0


def test_analytics_summary():
    response = requests.get(f"{BASE_URL}/analytics/summary")
    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["rows"] > 0
    assert "Metric" in data["columns"]
    assert "Value" in data["columns"]


def test_customer_segments():
    response = requests.get(f"{BASE_URL}/analytics/segments")
    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["rows"] > 0


def test_products():
    response = requests.get(f"{BASE_URL}/analytics/products")
    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["rows"] > 0


def test_countries():
    response = requests.get(f"{BASE_URL}/analytics/countries")
    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["rows"] > 0


def test_ml_opportunities():
    response = requests.get(f"{BASE_URL}/analytics/ml-opportunities")
    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["rows"] > 0


def test_recommendations():
    response = requests.get(f"{BASE_URL}/analytics/recommendations")
    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["rows"] > 0


def test_insights():
    response = requests.get(f"{BASE_URL}/analytics/insights")
    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["rows"] > 0


def test_high_value_customers():
    response = requests.get(
        f"{BASE_URL}/analytics/high-value-customers"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["count"] > 0
    assert len(data["customers"]) > 0


def test_ai_revenue_question():
    response = requests.get(
        f"{BASE_URL}/analytics/ask",
        params={"question": "What is the total revenue?"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["question_type"] == "revenue"
    assert "revenue" in data["answer"].lower()


def test_ai_customer_question():
    response = requests.get(
        f"{BASE_URL}/analytics/ask",
        params={"question": "How many customers are there?"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["question_type"] == "customer_count"


def test_ai_orders_question():
    response = requests.get(
        f"{BASE_URL}/analytics/ask",
        params={"question": "How many orders are there?"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["question_type"] == "orders"


def test_ai_unknown_question():
    response = requests.get(
        f"{BASE_URL}/analytics/ask",
        params={"question": "What is the weather today?"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["question_type"] == "unknown"