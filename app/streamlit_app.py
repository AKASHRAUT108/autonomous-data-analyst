import requests
import pandas as pd
import streamlit as st



API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="Autonomous Data Analyst",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Autonomous Data Analyst")

st.markdown(
    """
    ### AI-Powered Business Intelligence Platform

    Analyze business performance, customer segments,
    products, countries, and machine-learning opportunities
    from one application.
    """
)


st.divider()


# --------------------------------------------------
# Backend Status
# --------------------------------------------------

st.subheader("System Status")


try:

    response = requests.get(
        f"{API_URL}/health",
        timeout=5
    )

    if response.status_code == 200:

        health_data = response.json()

        st.success(
            f"FastAPI Backend: {health_data.get('status', 'online')}"
        )

    else:

        st.error(
            f"FastAPI returned status code {response.status_code}"
        )


except requests.exceptions.RequestException:

    st.error(
        "Unable to connect to FastAPI. "
        "Make sure the backend is running on port 8000."
    )


st.divider()


# --------------------------------------------------
# Application Modules
# --------------------------------------------------

st.subheader("Analytics Modules")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        label="Business Analytics",
        value="Available"
    )


with col2:

    st.metric(
        label="Customer Analytics",
        value="RFM"
    )


with col3:

    st.metric(
        label="Product Analytics",
        value="Available"
    )


with col4:

    st.metric(
        label="Machine Learning",
        value="Available"
    )


st.divider()


st.info(
    "Streamlit is successfully connected to the FastAPI backend."
)

# --------------------------------------------------
# Business Analytics
# --------------------------------------------------

# --------------------------------------------------
# Business Analytics
# --------------------------------------------------

st.subheader("Business Analytics")

try:

    response = requests.get(
        f"{API_URL}/analytics/summary",
        timeout=10
    )

    if response.status_code == 200:

        business_data = response.json()

        st.success("Business analytics loaded successfully.")

        # ----------------------------------------------
        # Extract KPI values
        # ----------------------------------------------

        total_revenue = business_data.get("total_revenue", 0)
        total_orders = business_data.get("total_orders", 0)
        total_customers = business_data.get("total_customers", 0)
        total_products = business_data.get("total_products", 0)
        total_countries = business_data.get("total_countries", 0)
        average_order_value = business_data.get(
            "average_order_value",
            0
        )

        # ----------------------------------------------
        # KPI Row 1
        # ----------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Revenue",
                f"{total_revenue:,.2f}"
            )

        with col2:
            st.metric(
                "Total Orders",
                f"{total_orders:,}"
            )

        with col3:
            st.metric(
                "Total Customers",
                f"{total_customers:,}"
            )

        # ----------------------------------------------
        # KPI Row 2
        # ----------------------------------------------

        col4, col5, col6 = st.columns(3)

        with col4:
            st.metric(
                "Total Products",
                f"{total_products:,}"
            )

        with col5:
            st.metric(
                "Countries",
                f"{total_countries:,}"
            )

        with col6:
            st.metric(
                "Average Order Value",
                f"{average_order_value:,.2f}"
            )

    else:

        st.warning(
            f"Business analytics returned status code "
            f"{response.status_code}"
        )

except requests.exceptions.RequestException as e:

    st.error(
        f"Unable to load business analytics: {e}"
    )

# --------------------------------------------------
# Customer Segmentation
# --------------------------------------------------

st.divider()

st.subheader("Customer Segmentation")

try:

    response = requests.get(
        f"{API_URL}/analytics/segments",
        timeout=10
    )

    if response.status_code == 200:

        segment_data = response.json()

        st.success("Customer segmentation data loaded successfully.")

        # ----------------------------------------------
        # Convert API response into a dataframe
        # ----------------------------------------------

        if isinstance(segment_data, list):

            segment_df = pd.DataFrame(segment_data)

        elif isinstance(segment_data, dict):

            # Handle APIs that return {"data": [...]}
            if isinstance(segment_data.get("data"), list):

                segment_df = pd.DataFrame(
                    segment_data["data"]
                )

            else:

                segment_df = pd.DataFrame(
                    [segment_data]
                )

        else:

            segment_df = pd.DataFrame()

        # ----------------------------------------------
        # Display table
        # ----------------------------------------------

        if not segment_df.empty:

            st.dataframe(
                segment_df,
                use_container_width=True
            )

        else:

            st.info("No customer segment data available.")

    else:

        st.warning(
            f"Customer segmentation returned "
            f"status code {response.status_code}"
        )

except requests.exceptions.RequestException as e:

    st.error(
        f"Unable to load customer segmentation: {e}"
    )

    # --------------------------------------------------
# Product Performance
# --------------------------------------------------

st.divider()

st.subheader("Product Performance")

try:

    response = requests.get(
        f"{API_URL}/analytics/products",
        timeout=10
    )

    if response.status_code == 200:

        product_data = response.json()

        st.success("Product performance data loaded successfully.")

        if isinstance(product_data, list):

            product_df = pd.DataFrame(product_data)

        elif isinstance(product_data, dict):

            if isinstance(product_data.get("data"), list):

                product_df = pd.DataFrame(
                    product_data["data"]
                )

            else:

                product_df = pd.DataFrame(
                    [product_data]
                )

        else:

            product_df = pd.DataFrame()

        if not product_df.empty:

            st.dataframe(
                product_df,
                use_container_width=True
            )

        else:

            st.info("No product performance data available.")

    else:

        st.warning(
            f"Product performance returned "
            f"status code {response.status_code}"
        )

except requests.exceptions.RequestException as e:

    st.error(
        f"Unable to load product performance: {e}"
    )

    # --------------------------------------------------
# Product Performance
# --------------------------------------------------

st.divider()

st.subheader("Product Performance")

try:

    response = requests.get(
        f"{API_URL}/analytics/products",
        timeout=10
    )

    if response.status_code == 200:

        product_data = response.json()

        st.success("Product performance data loaded successfully.")

        if isinstance(product_data, list):

            product_df = pd.DataFrame(product_data)

        elif isinstance(product_data, dict):

            if isinstance(product_data.get("data"), list):

                product_df = pd.DataFrame(
                    product_data["data"]
                )

            else:

                product_df = pd.DataFrame(
                    [product_data]
                )

        else:

            product_df = pd.DataFrame()

        if not product_df.empty:

            st.dataframe(
                product_df,
                use_container_width=True
            )

        else:

            st.info("No product performance data available.")

    else:

        st.warning(
            f"Product performance returned "
            f"status code {response.status_code}"
        )

except requests.exceptions.RequestException as e:

    st.error(
        f"Unable to load product performance: {e}"
    )

    # --------------------------------------------------
# Country Performance
# --------------------------------------------------

st.divider()

st.subheader("Geographic Performance")

try:

    response = requests.get(
        f"{API_URL}/analytics/countries",
        timeout=10
    )

    if response.status_code == 200:

        country_data = response.json()

        st.success("Country performance data loaded successfully.")

        if isinstance(country_data, list):

            country_df = pd.DataFrame(country_data)

        elif isinstance(country_data, dict):

            if isinstance(country_data.get("data"), list):

                country_df = pd.DataFrame(
                    country_data["data"]
                )

            else:

                country_df = pd.DataFrame(
                    [country_data]
                )

        else:

            country_df = pd.DataFrame()

        if not country_df.empty:

            st.dataframe(
                country_df,
                use_container_width=True
            )

        else:

            st.info("No country performance data available.")

    else:

        st.warning(
            f"Country performance returned "
            f"status code {response.status_code}"
        )

except requests.exceptions.RequestException as e:

    st.error(
        f"Unable to load country performance: {e}"
    )
    # --------------------------------------------------
# Business Recommendations
# --------------------------------------------------

st.divider()

st.subheader("Business Recommendations")

try:

    response = requests.get(
        f"{API_URL}/analytics/recommendations",
        timeout=10
    )

    if response.status_code == 200:

        recommendation_data = response.json()

        st.success(
            "Business recommendations loaded successfully."
        )

        if isinstance(recommendation_data, list):

            recommendation_df = pd.DataFrame(
                recommendation_data
            )

            if not recommendation_df.empty:

                st.dataframe(
                    recommendation_df,
                    use_container_width=True
                )

        elif isinstance(recommendation_data, dict):

            if isinstance(
                recommendation_data.get("data"),
                list
            ):

                recommendation_df = pd.DataFrame(
                    recommendation_data["data"]
                )

                st.dataframe(
                    recommendation_df,
                    use_container_width=True
                )

            else:

                for key, value in recommendation_data.items():

                    st.markdown(
                        f"### {key}"
                    )

                    st.write(value)

        else:

            st.info(
                "No business recommendations available."
            )

    else:

        st.warning(
            f"Recommendations returned "
            f"status code {response.status_code}"
        )

except requests.exceptions.RequestException as e:

    st.error(
        f"Unable to load recommendations: {e}"
    )

    # --------------------------------------------------
# Business Insights
# --------------------------------------------------

st.divider()

st.subheader("Business Insights")

try:

    response = requests.get(
        f"{API_URL}/analytics/insights",
        timeout=10
    )

    if response.status_code == 200:

        insights_data = response.json()

        st.success(
            "Business insights loaded successfully."
        )

        if isinstance(insights_data, list):

            for index, insight in enumerate(
                insights_data,
                start=1
            ):

                st.info(
                    f"Insight {index}: {insight}"
                )

        elif isinstance(insights_data, dict):

            if isinstance(
                insights_data.get("data"),
                list
            ):

                for index, insight in enumerate(
                    insights_data["data"],
                    start=1
                ):

                    st.info(
                        f"Insight {index}: {insight}"
                    )

            else:

                for key, value in insights_data.items():

                    st.markdown(
                        f"### {key}"
                    )

                    st.write(value)

        else:

            st.write(insights_data)

    else:

        st.warning(
            f"Business insights returned "
            f"status code {response.status_code}"
        )

except requests.exceptions.RequestException as e:

    st.error(
        f"Unable to load business insights: {e}"
    )

    # --------------------------------------------------
# Business Insights
# --------------------------------------------------

st.divider()

st.subheader("Business Insights")

try:

    response = requests.get(
        f"{API_URL}/analytics/insights",
        timeout=10
    )

    if response.status_code == 200:

        insights_data = response.json()

        st.success(
            "Business insights loaded successfully."
        )

        if isinstance(insights_data, list):

            for index, insight in enumerate(
                insights_data,
                start=1
            ):

                st.info(
                    f"Insight {index}: {insight}"
                )

        elif isinstance(insights_data, dict):

            if isinstance(
                insights_data.get("data"),
                list
            ):

                for index, insight in enumerate(
                    insights_data["data"],
                    start=1
                ):

                    st.info(
                        f"Insight {index}: {insight}"
                    )

            else:

                for key, value in insights_data.items():

                    st.markdown(
                        f"### {key}"
                    )

                    st.write(value)

        else:

            st.write(insights_data)

    else:

        st.warning(
            f"Business insights returned "
            f"status code {response.status_code}"
        )

except requests.exceptions.RequestException as e:

    st.error(
        f"Unable to load business insights: {e}"
    )

    # --------------------------------------------------
# High-Value Customers
# --------------------------------------------------

st.divider()

st.subheader("Top High-Value Customers")

try:

    response = requests.get(
        f"{API_URL}/analytics/high-value-customers",
        timeout=10
    )

    if response.status_code == 200:

        high_value_data = response.json()

        st.success(
            "High-value customer data loaded successfully."
        )

        if isinstance(high_value_data, list):

            high_value_df = pd.DataFrame(
                high_value_data
            )

        elif isinstance(high_value_data, dict):

            if isinstance(
                high_value_data.get("data"),
                list
            ):

                high_value_df = pd.DataFrame(
                    high_value_data["data"]
                )

            else:

                high_value_df = pd.DataFrame(
                    [high_value_data]
                )

        else:

            high_value_df = pd.DataFrame()

        if not high_value_df.empty:

            st.dataframe(
                high_value_df,
                use_container_width=True
            )

        else:

            st.info(
                "No high-value customer data available."
            )

    else:

        st.warning(
            f"High-value customers returned "
            f"status code {response.status_code}"
        )

except requests.exceptions.RequestException as e:

    st.error(
        f"Unable to load high-value customers: {e}"
    )

    # --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Autonomous Data Analyst | "
    "FastAPI + Streamlit + Machine Learning + Power BI"
)

st.caption(
    "End-to-end Business Intelligence Platform"
)

st.divider()

st.header("Machine Learning Opportunities")

try:
    response = requests.get(
        f"{API_URL}/analytics/ml-opportunities",
        timeout=10
    )

    if response.status_code == 200:
        data = response.json()

        if data.get("status") == "success":
            opportunities = data.get("opportunities", [])

            st.success("ML opportunity analysis loaded successfully.")

            if opportunities:
                df_ml = pd.DataFrame(opportunities)

                st.dataframe(
                    df_ml,
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.info("No ML opportunity records available.")
        else:
            st.warning("ML opportunity analysis returned no data.")
    else:
        st.warning(
            f"ML opportunity endpoint returned status code "
            f"{response.status_code}"
        )

except requests.exceptions.RequestException as e:
    st.error(f"Unable to connect to ML endpoint: {e}")


st.divider()

st.header("Business Recommendations")

try:
    response = requests.get(
        f"{API_URL}/analytics/recommendations",
        timeout=10
    )

    if response.status_code == 200:
        data = response.json()

        if data.get("status") == "success":

            recommendations = data.get("recommendations", [])

            st.success(
                "Business recommendations loaded successfully."
            )

            if recommendations:

                for recommendation in recommendations:

                    area = recommendation.get(
                        "area",
                        "Business"
                    )

                    priority = recommendation.get(
                        "priority",
                        "Medium"
                    )

                    recommendation_text = recommendation.get(
                        "recommendation",
                        ""
                    )

                    st.subheader(area)

                    st.write(
                        f"**Priority:** {priority}"
                    )

                    st.write(
                        recommendation_text
                    )

                    st.divider()

            else:
                st.info(
                    "No business recommendations available."
                )

        else:
            st.warning(
                "Business recommendations returned no data."
            )

    else:
        st.warning(
            f"Recommendations endpoint returned "
            f"status code {response.status_code}"
        )

except requests.exceptions.RequestException as e:
    st.error(
        f"Unable to connect to recommendations endpoint: {e}"
    )

    st.divider()

st.header("Business Insights")

try:
    response = requests.get(
        f"{API_URL}/analytics/insights",
        timeout=10
    )

    if response.status_code == 200:

        data = response.json()

        if data.get("status") == "success":

            insights = data.get("insights", [])

            st.success(
                "Business insights loaded successfully."
            )

            if insights:

                for insight in insights:

                    category = insight.get(
                        "insight_category",
                        "General"
                    )

                    metric = insight.get(
                        "metric",
                        "Metric"
                    )

                    value = insight.get(
                        "value",
                        0
                    )

                    interpretation = insight.get(
                        "business_interpretation",
                        ""
                    )

                    st.subheader(category)

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric(
                            metric,
                            value
                        )

                    with col2:
                        st.write(
                            interpretation
                        )

            else:
                st.info(
                    "No business insights available."
                )

        else:
            st.warning(
                "Business insights returned no data."
            )

    else:
        st.warning(
            f"Insights endpoint returned "
            f"status code {response.status_code}"
        )

except requests.exceptions.RequestException as e:
    st.error(
        f"Unable to connect to insights endpoint: {e}"
    )

    st.divider()

st.header("Business Insights")

try:
    response = requests.get(
        f"{API_URL}/analytics/insights",
        timeout=10
    )

    if response.status_code == 200:

        data = response.json()

        if data.get("status") == "success":

            insights = data.get("insights", [])

            st.success(
                "Business insights loaded successfully."
            )

            if insights:

                for insight in insights:

                    category = insight.get(
                        "insight_category",
                        "General"
                    )

                    metric = insight.get(
                        "metric",
                        "Metric"
                    )

                    value = insight.get(
                        "value",
                        0
                    )

                    interpretation = insight.get(
                        "business_interpretation",
                        ""
                    )

                    st.subheader(category)

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric(
                            metric,
                            value
                        )

                    with col2:
                        st.write(
                            interpretation
                        )

            else:
                st.info(
                    "No business insights available."
                )

        else:
            st.warning(
                "Business insights returned no data."
            )

    else:
        st.warning(
            f"Insights endpoint returned "
            f"status code {response.status_code}"
        )

except requests.exceptions.RequestException as e:
    st.error(
        f"Unable to connect to insights endpoint: {e}"
    )

    st.divider()

st.header("High-Value Customers")

try:
    response = requests.get(
        f"{API_URL}/analytics/high-value-customers",
        timeout=10
    )

    if response.status_code == 200:

        data = response.json()

        if data.get("status") == "success":

            customers = data.get(
                "customers",
                []
            )

            st.success(
                "High-value customer analysis loaded successfully."
            )

            if customers:

                df_customers = pd.DataFrame(
                    customers
                )

                st.dataframe(
                    df_customers,
                    use_container_width=True,
                    hide_index=True
                )

            else:
                st.info(
                    "No high-value customer data available."
                )

        else:
            st.warning(
                "High-value customer endpoint returned no data."
            )

    else:
        st.warning(
            f"High-value customer endpoint returned "
            f"status code {response.status_code}"
        )

except requests.exceptions.RequestException as e:
    st.error(
        f"Unable to connect to high-value customer endpoint: {e}"
    )