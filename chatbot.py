financial_data = {
    "total_revenue": "394.33 billion USD (Apple, FY 2023)",
    "net_income_change": "Decreased by 2.8% from FY 2022 to FY 2023 (Apple)",
    "total_assets": "352.75 billion USD (Apple, FY 2023)",
    "total_liabilities": "267.98 billion USD (Apple, FY 2023)",
    "cash_flow_ops": "110.54 billion USD (Apple, FY 2023)"
}
def simple_chatbot(user_query):
    if user_query.lower() == "what is the total revenue?":
        return financial_data["total_revenue"]
    elif user_query.lower() == "what is the net income change over the last year?":
        return financial_data["net_income_change"]
    elif user_query.lower() == "what is the current total assets?":
        return financial_data["total_assets"]
    elif user_query.lower() == "how much are the total liabilities?":
        return financial_data["total_liabilities"]
    elif user_query.lower() == "what’s the cash flow from operating activities?":
        return financial_data["cash_flow_ops"]
    else:
        return "Sorry, I can only provide information on predefined queries."


# Example interaction
if __name__ == "__main__":
    while True:
        user_input = input("Ask me a financial question (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        response = simple_chatbot(user_input)
        print(response)
