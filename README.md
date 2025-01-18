# LLM-Powered Performance Metrics

This project is a Python-based tool that interacts with the Groq LLM API to fetch and process user queries regarding business metrics. It is designed to analyze user inputs, extract relevant data (like company, metrics, and time periods), and output structured information in JSON format.

## Features

- Allows users to input queries about business metrics.
- Uses the Groq LLM API to process and analyze queries.
- Handles multiple companies and comparison requests in a single query.
- Provides structured JSON output with company, metric, and time period information.
- Automatically calculates default dates (e.g., one year ago to today) when not specified.

## Installation

To run this project locally, follow the steps below:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/sanketmudaraddi/llm-performance-metrics.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd llm-performance-metrics
   ```

3. **Set up your Groq API Key**:

   Obtain your API key from Groq and set it in the `API_KEY` variable inside `llm_app.py`.

4. **Run the script**:

   You can now run the application with:

   ```bash
   python llm_app.py
   ```

## Usage

Once the application is running, you will be prompted to enter a query. Here are some examples of queries you can try:

- `Get me Flipkart's GMV for last one year`
- `Compare Flipkart with Amazon`
- `Get Amazon's revenue for 2023`

The program will output a structured JSON response, which includes the company, metric, and time period.

### Example Output:

```json
[
  {
    "entity": "Flipkart",
    "parameter": "GMV",
    "startDate": "2024-01-19",
    "endDate": "2025-01-18"
  }
]
```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit pull requests. All contributions are welcome!

---



