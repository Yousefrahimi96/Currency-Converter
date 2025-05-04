# Currency Converter

A simple web-based currency converter built with Streamlit. It allows users to check exchange rates between different currencies and convert amounts from any supported currency to USD.

## Features

- View the exchange rate between any two supported currencies.
- Convert a specified amount from any supported currency to USD.
- Supports a wide range of currencies (sorted alphabetically).

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/currency-converter.git
   cd currency-converter
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. Open your browser and go to `http://localhost:8501` to use the app.

## Usage

### Exchange Rate
1. Select the base currency from the dropdown menu.
2. Select the target currency from the dropdown menu.
3. The exchange rate will be displayed in the format: `1 [base_currency] = [exchange_rate] [target_currency]`.

### Convert to USD
1. Select the currency you want to convert from.
2. Enter the amount you want to convert.
3. The converted amount will be displayed in USD.

## Project Structure

- `app.py`: The main Streamlit application file.
- `src/currency.py`: Contains the list of supported currencies.
- `src/functions.py`: Contains functions to fetch exchange rates and convert currencies.
- `requirements.txt`: Lists the required Python packages.

## API Key

This project uses the [ExchangeRate-API](https://www.exchangerate-api.com/) to fetch exchange rates. The API key is hardcoded in `functions.py` for simplicity. For production use, it's recommended to store the API key as an environment variable.

To use your own API key:
1. Sign up at [ExchangeRate-API](https://www.exchangerate-api.com/) to get a free API key.
2. Replace the hardcoded key in `functions.py` with your own key.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.


## Contact

For any questions or inquiries, please contact yousefrahimi310@gmail.com