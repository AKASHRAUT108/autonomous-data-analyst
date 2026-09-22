def classify_question(question: str) -> str:
    """
    Classify a business question into an analytical category.
    """

    question = question.lower().strip()

    # Revenue questions
    if any(
        phrase in question
        for phrase in [
            "total revenue",
            "revenue",
            "sales"
        ]
    ):
        return "revenue"

    # Customer count questions
    if (
        "customer" in question
        and any(
            word in question
            for word in [
                "count",
                "many",
                "number",
                "how much"
            ]
        )
    ):
        return "customer_count"

    # Product questions
    if any(
        phrase in question
        for phrase in [
            "top product",
            "best product",
            "highest product",
            "product performance"
        ]
    ):
        return "top_product"

    # Customer segment questions
    if any(
        phrase in question
        for phrase in [
            "segment",
            "customer segment",
            "customer group"
        ]
    ):
        return "segment"

    # Order questions
    if any(
        phrase in question
        for phrase in [
            "total orders",
            "number of orders",
            "how many orders",
            "orders"
        ]
    ):
        return "orders"

    # Country questions
    if any(
        phrase in question
        for phrase in [
            "top country",
            "best country",
            "country performance",
            "countries"
        ]
    ):
        return "country"

    return "unknown"