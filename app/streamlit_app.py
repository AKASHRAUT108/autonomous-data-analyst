














import os
import requests
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Autonomous Data Analyst",
    page_icon="📊",
    layout="wide",
)

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000").rstrip("/")

if "ai_chat_history" not in st.session_state:
    st.session_state.ai_chat_history = []


def api_get(endpoint, timeout=10):
    response = requests.get(f"{API_URL}{endpoint}", timeout=timeout)
    response.raise_for_status()
    return response.json()

def dataframe_from_response(data):
    if isinstance(data, list):
        df = pd.json_normalize(data)
    elif isinstance(data, dict):
        records = None

        for key in (
            "data",
            "customers",
            "opportunities",
            "recommendations",
            "insights",
        ):
            if isinstance(data.get(key), list):
                records = data[key]
                break

        if records is not None:
            df = pd.json_normalize(records)
        else:
            df = pd.json_normalize([data])
    else:
        return pd.DataFrame()

    # Convert any remaining nested values into readable text
    for column in df.columns:
        df[column] = df[column].apply(
            lambda value: (
                ", ".join(map(str, value))
                if isinstance(value, list)
                else str(value)
                if isinstance(value, dict)
                else value
            )
        )

    return df

def summary_metrics(data):
    metrics = {}
    if isinstance(data, dict) and isinstance(data.get("data"), list):
        for row in data["data"]:
            if isinstance(row, dict) and row.get("Metric") is not None:
                metrics[str(row["Metric"]).strip().lower()] = row.get("Value")
    return metrics


st.title("📊 Autonomous Data Analyst")
st.markdown(
    """
    ### AI-Powered Business Intelligence Platform

    Analyze business performance, customer segments, products,
    countries, machine-learning opportunities, and business insights
    from one application.
    """
)

st.divider()
st.subheader("System Status")

try:
    health_data = api_get("/health", timeout=5)
    st.success(f"FastAPI Backend: {health_data.get('status', 'online')}")
except requests.exceptions.RequestException:
    st.error(
        "Unable to connect to FastAPI. "
        "Make sure the backend is running on port 8000."
    )

st.divider()
st.subheader("Analytics Modules")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Business Analytics", "Available")
with col2:
    st.metric("Customer Analytics", "RFM")
with col3:
    st.metric("Product Analytics", "Available")
with col4:
    st.metric("Machine Learning", "Available")


st.divider()
st.subheader("Business Analytics")

try:
    business_data = api_get("/analytics/summary")
    metrics = summary_metrics(business_data)
    st.success("Business analytics loaded successfully.")

    total_revenue = metrics.get("total revenue", 0)
    total_orders = metrics.get("total orders", 0)
    total_customers = metrics.get("total customers", 0)
    total_products = metrics.get("total products", 0)
    total_countries = metrics.get("countries served", 0)
    average_order_value = metrics.get("average order value", 0)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Total Revenue", f"{float(total_revenue):,.2f}")
    with c2:
        st.metric("Total Orders", f"{int(total_orders):,}")
    with c3:
        st.metric("Total Customers", f"{int(total_customers):,}")

    c4, c5, c6 = st.columns(3)
    with c4:
        st.metric("Total Products", f"{int(total_products):,}")
    with c5:
        st.metric("Countries Served", f"{int(total_countries):,}")
    with c6:
        st.metric("Average Order Value", f"{float(average_order_value):,.2f}")

except (requests.exceptions.RequestException, ValueError, TypeError):
    st.warning("Unable to load business analytics.")


st.divider()
st.subheader("Customer Segmentation")
try:
    segment_df = dataframe_from_response(api_get("/analytics/segments"))
    if not segment_df.empty:
        st.dataframe(segment_df, use_container_width=True, hide_index=True)
    else:
        st.info("No customer segment data available.")
except requests.exceptions.RequestException as e:
    st.error(f"Unable to load customer segmentation: {e}")


st.divider()
st.subheader("Product Performance")
try:
    product_df = dataframe_from_response(api_get("/analytics/products"))
    if not product_df.empty:
        st.dataframe(product_df, use_container_width=True, hide_index=True)
    else:
        st.info("No product performance data available.")
except requests.exceptions.RequestException as e:
    st.error(f"Unable to load product performance: {e}")


st.divider()
st.subheader("Geographic Performance")
try:
    country_df = dataframe_from_response(api_get("/analytics/countries"))
    if not country_df.empty:
        st.dataframe(country_df, use_container_width=True, hide_index=True)
    else:
        st.info("No country performance data available.")
except requests.exceptions.RequestException as e:
    st.error(f"Unable to load country performance: {e}")


st.divider()
st.header("Machine Learning Opportunities")
try:
    ml_data = api_get("/analytics/ml-opportunities")
    if isinstance(ml_data, dict) and ml_data.get("status") == "success":
        opportunities = ml_data.get("opportunities", [])
        if opportunities:
            st.dataframe(
                pd.DataFrame(opportunities),
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.info("No ML opportunity records available.")
    else:
        st.warning("ML opportunity analysis returned no data.")
except requests.exceptions.RequestException as e:
    st.error(f"Unable to load ML opportunities: {e}")


st.divider()
st.header("Business Recommendations")
try:
    recommendation_data = api_get("/analytics/recommendations")
    if (
        isinstance(recommendation_data, dict)
        and recommendation_data.get("status") == "success"
    ):
        recommendations = recommendation_data.get("recommendations", [])
        if recommendations:
            for item in recommendations:
                st.subheader(item.get("area", "Business"))
                st.write(f"**Priority:** {item.get('priority', 'Medium')}")
                st.write(item.get("recommendation", ""))
                st.divider()
        else:
            st.info("No business recommendations available.")
    else:
        st.warning("Business recommendations returned no data.")
except requests.exceptions.RequestException as e:
    st.error(f"Unable to load recommendations: {e}")


st.divider()
st.header("Business Insights")
try:
    insights_data = api_get("/analytics/insights")
    if (
        isinstance(insights_data, dict)
        and insights_data.get("status") == "success"
    ):
        insights = insights_data.get("insights", [])
        if insights:
            for item in insights:
                st.subheader(item.get("insight_category", "General"))
                c1, c2 = st.columns(2)
                with c1:
                    st.metric(item.get("metric", "Metric"), item.get("value", 0))
                with c2:
                    st.write(item.get("business_interpretation", ""))
        else:
            st.info("No business insights available.")
    else:
        st.warning("Business insights returned no data.")
except requests.exceptions.RequestException as e:
    st.error(f"Unable to load business insights: {e}")


st.divider()
st.header("High-Value Customers")
try:
    customer_data = api_get("/analytics/high-value-customers")
    if (
        isinstance(customer_data, dict)
        and customer_data.get("status") == "success"
    ):
        customers = customer_data.get("customers", [])
        if customers:
            st.dataframe(
                pd.DataFrame(customers),
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.info("No high-value customer data available.")
    else:
        st.warning("High-value customer endpoint returned no data.")
except requests.exceptions.RequestException as e:
    st.error(f"Unable to load high-value customers: {e}")


st.divider()
st.header("🤖 AI Business Analyst")
st.write("Ask questions about your business data using natural language.")

example_questions = [
    "What is the total revenue?",
    "How many customers are there?",
    "What is the top product?",
    "Which customer segment has the highest value?",
    "How many orders are there?",
]

selected_question = st.selectbox(
    "Choose an example question",
    ["Select a question"] + example_questions,
)

question = st.text_input(
    "Or enter your own question",
    placeholder="Example: What is the total revenue?",
)

if selected_question != "Select a question" and not question:
    question = selected_question

if st.button("Ask Analyst"):
    if not question.strip():
        st.warning("Please enter or select a question.")
    else:
        try:
            response = requests.get(
                f"{API_URL}/analytics/ask",
                params={"question": question},
                timeout=10,
            )

            if response.status_code == 200:
                result = response.json()

                if result.get("status") == "success":
                    answer = result.get("answer", "No answer returned.")
                    st.success("Analysis complete")
                    st.markdown("### Answer")
                    st.info(answer)
                    st.caption(
                        f"Detected operation: "
                        f"{result.get('question_type', 'unknown')}"
                    )

                    st.session_state.ai_chat_history.append(
                        {
                            "question": question,
                            "answer": answer,
                            "question_type": result.get(
                                "question_type", "unknown"
                            ),
                        }
                    )
                else:
                    st.error(
                        result.get(
                            "message",
                            result.get(
                                "answer",
                                "Unable to process the question.",
                            ),
                        )
                    )
            else:
                st.error(
                    f"AI Analyst returned status code {response.status_code}"
                )

        except requests.exceptions.RequestException as e:
            st.error(f"Could not connect to FastAPI: {e}")


if st.session_state.ai_chat_history:
    st.divider()
    st.subheader("📜 Previous Analysis")

    if st.button("🗑️ Clear Analysis History"):
        st.session_state.ai_chat_history = []
        st.rerun()

    for i, chat in enumerate(
        reversed(st.session_state.ai_chat_history),
        start=1,
    ):
        with st.expander(f"Question {i}: {chat['question']}"):
            st.markdown(f"**Question:** {chat['question']}")
            st.markdown(f"**Answer:** {chat['answer']}")
            st.caption(
                f"Operation: {chat.get('question_type', 'unknown')}"
            )


st.divider()
st.caption(
    "Autonomous Data Analyst | "
    "FastAPI + Streamlit + Machine Learning + Power BI"
)
st.caption("End-to-end Business Intelligence Platform")
