Apartment Finding Bot
=====================

The **Apartment Finding Bot** is a Python-based web scraper that simplifies the process of searching for rental properties on Zillow. Designed for individuals who want to streamline their apartment hunting experience, this bot automates the tedious task of searching, filtering, and organizing rental property information. It even integrates with Google Forms to neatly store and manage results for further review.

* * * * *

Features
--------

-   **Dynamic URL Handling**: Customizable search based on user input for city, state, minimum price, and maximum price.
-   **Pagination Support**: Automatically scrapes multiple pages of listings to gather comprehensive results.
-   **User-Agent Randomization**: Avoids request blocks by simulating real user behavior with random user-agent headers.
-   **Data Extraction**: Retrieves key information, including:
    -   Property Address
    -   Monthly Rent Price
    -   Direct Link to the Listing
-   **Error Handling**: Gracefully skips over missing or malformed data in listings and provides detailed error messages for debugging.
-   **Google Forms Integration**: Automatically submits scraped property data to a specified Google Form for easy organization and accessibility.

* * * * *

How It Works
------------

1.  **Input Search Criteria**:
    -   The bot prompts users for:
        -   **Minimum Price**
        -   **Maximum Price**
        -   **City**
        -   **State**
2.  **Scrape Zillow**:
    -   It dynamically constructs a Zillow search URL based on user input and extracts relevant property details from the listings.
    -   Handles pagination to ensure all relevant listings are captured.
3.  **Submit to Google Forms**:
    -   Each scraped listing is automatically submitted to a Google Form, ensuring an organized and accessible format for further review.

* * * * *

Technical Highlights
--------------------

-   **Libraries Used**:
    -   `Selenium`: For automated interaction with Google Forms.
    -   `BeautifulSoup`: For parsing HTML and extracting property details.
    -   `Requests`: For making HTTP requests to Zillow.
    -   `Fake-UserAgent`: For generating randomized user-agent strings.
-   **Cross-Platform Support**:
    -   Dynamically configures ChromeDriver using `webdriver_manager`, eliminating the need for manual setup.
-   **Error Handling**:
    -   Captures and logs errors such as missing data, failed HTTP requests, or Selenium-related issues.

* * * * *

Setup Instructions
------------------

1.  **Install Python**:

    -   Ensure Python 3.x is installed on your system.
2.  **Clone the Repository**:

    bash

    Copy code

    `git clone https://github.com/bjkim0426/apartment_finding_bot.git
    cd apartment_finding_bot`

3.  **Install Dependencies**:

    -   Create a virtual environment and activate it:

        bash

        Copy code

        `python3 -m venv venv
        source venv/bin/activate  # On macOS/Linux
        venv\Scripts\activate     # On Windows`

    -   Install the required packages:

        bash

        Copy code

        `pip install -r requirements.txt`

4.  **Run the Script**:

    bash

    Copy code

    `python main.py`

5.  **Provide Search Criteria**:

    -   Enter the minimum price, maximum price, city, and state when prompted.

* * * * *

Example Output
--------------

Here's an example of what the bot retrieves:

Address: Redmond Apartments, 9200 Redmond Woodinville Rd NE #A301, Redmond, WA 98052

Price: $1,943

Link: https://www.zillow.com/homedetails/9200-Redmond-Woodinville-Rd-NE-A301

----------------------------------------

Address: Spectra | 17620 NE 69th Ct, Redmond, WA

Price: $1,850+ Studio

Link: https://www.zillow.com/homedetails/17620-NE-69th-Ct-Spectra


* * * * *

Future Improvements
-------------------

-   **Multi-Platform Support**:
    -   Extend scraping capabilities to other rental platforms like Craigslist or Realtor.com.
-   **Continuous Monitoring**:
    -   Implement scheduled scraping to periodically update listings.
-   **Database Integration**:
    -   Store scraped data in a database for advanced querying and reporting.
-   **User Notifications**:
    -   Add email or SMS alerts for newly listed properties matching the user's criteria.

* * * * *

Disclaimer
----------

This project is for educational purposes and personal use only. Scraping websites may violate their terms of service. Use this tool responsibly and ensure compliance with applicable rules and regulations.
