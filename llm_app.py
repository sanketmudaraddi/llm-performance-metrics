import requests
import datetime
import json

# Constants
LLM_API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = "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"

# Utility Functions
def get_default_dates():
    """
    Calculate default start and end dates:
    - Start date: One year ago from today.
    - End date: Today's date.
    """
    today = datetime.date.today()
    one_year_ago = today - datetime.timedelta(days=365)
    return one_year_ago.isoformat(), today.isoformat()

def call_llm(user_input):
    """
    Call the Groq API using the OpenAI-compatible endpoint to process the user query.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Format the system message to guide the LLM's response format
    system_message = """Please analyze the user's query about business metrics and respond with structured information.
    Extract the following:
    - Company/Entity name
    - Metric/Parameter requested
    - Time period if specified
    Respond in a clear, structured format."""
    
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }

    try:
        response = requests.post(LLM_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Error: {str(e)}")
        if hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}")
        return None

def parse_llm_response(response, query):
    """
    Parse the LLM response and structure it into JSON format.
    """
    # Default dates
    default_start_date, default_end_date = get_default_dates()

    try:
        # Extract the actual response content from Groq API response
        if response and 'choices' in response:
            content = response['choices'][0]['message']['content']
            print("LLM Response:", content)  # Debug print to see raw response

            # Process for multiple entities in comparison
            companies = []
            if "flipkart" in query.lower():
                companies.append("Flipkart")
            if "amazon" in query.lower():
                companies.append("Amazon")
            
            # Check if a specific metric is mentioned
            metric = "GMV" if "gmv" in query.lower() else "Unknown"
            
            # If no metric is mentioned, assume "GMV"
            if metric == "Unknown" and "compare" in query.lower():
                metric = "GMV"

            # Create JSON output for each company in the comparison
            output = []
            for company in companies:
                output.append({
                    "entity": company,
                    "parameter": metric,
                    "startDate": default_start_date,
                    "endDate": default_end_date
                })
            
            return output
    except Exception as e:
        print(f"Error parsing response: {e}")
        return []

    return []

# Main Function
def main():
    print("LLM-Powered Application for Performance Metrics")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Enter your query: ")
        if query.lower() == "exit":
            print("Exiting application. Goodbye!")
            break

        try:
            # Step 1: Call the LLM API
            llm_response = call_llm(query)
            if not llm_response:
                print("Failed to fetch response from LLM.")
                continue

            # Step 2: Parse the response
            json_output = parse_llm_response(llm_response, query)

            # Step 3: Display the output
            print("Structured JSON Output:")
            print(json.dumps(json_output, indent=2))

        except Exception as e:
            print(f"An error occurred: {e}")

# Entry Point
if __name__ == "__main__":
    main()
