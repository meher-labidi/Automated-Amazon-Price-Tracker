
# Amazon Price Tracker


This Amazon Price Tracker script allows you to monitor the price of a specific product on Amazon and receive email notifications when the price falls below a specified threshold. It uses BeautifulSoup for web scraping and smtplib for sending email alerts.


## Features

- Tracks the price of a specified Amazon product.

- Sends an email alert when the price drops below a defined threshold.

- Uses BeautifulSoup for parsing HTML and smtplib for sending emails.


## Requirements

- Python 3.x

- `requests` library

- `beautifulsoup4` library

- `lxml` library

- `smtplib` (included in Python standard library)


## Installation

1. Clone the repository:
    ```sh

    git clone https://github.com/yourusername/amazon-price-tracker.git
    ```

2. Navigate to the project directory:

   ```sh

    cd amazon-price-tracker
    ```

4. Install the required libraries:
    ```sh

    pip install requests beautifulsoup4 lxml
    ```


## Usage

1. Open the `tracker.py` file and update the following variables with your information:
    
    - `MY_EMAIL`: Your email address.
    
    - `MY_PASSWORD`: Your email password.
    
    - `url`: The URL of the Amazon product you want to track.

    - `BUY_PRICE`: The price threshold for receiving an alert.


2. Run the script:
    ```sh
    python tracker.py
    ```
