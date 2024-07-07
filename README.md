# ah.nl Automation Testing with Selenium and Pytest

## Project Overview

This project automates the testing of functionalities on the [ah.nl](https://www.ah.nl/) website. Using Python, Selenium, and Pytest, it covers various aspects of the website's functionality, including search, product selection, and comparison of product details.

## Features

- Automated browser interaction using Selenium WebDriver.
- Comprehensive test cases covering search functionalities, product selection, and validation of product details.
- Implementation of Page Object Model (POM) for better code organization and maintenance.
- Cross-browser compatibility for enhanced test coverage.
- Detailed logging and reporting of test results.

## Setup and Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/zhorko/pytest-ah.nl.git
    cd pytest-ah.nl
    ```

2. **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download and install the browser drivers:**
    - Download the appropriate drivers for the browsers you intend to test:
        - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for Chrome.
        - [GeckoDriver](https://github.com/mozilla/geckodriver/releases) for Firefox.
    - Ensure the drivers are in your system's PATH.

## Running the Tests

1. **Execute the test suite:**
    ```bash
    pytest tests/
    ```

2. **Run tests in a specific browser:**
    To run tests in a different browser, update the `browser` field in the `config.json` file. The available options are:

    - `Firefox`
    - `Chrome`
    - `Headless Chrome`
    - `Headless Firefox`

    Modify `config.json` to specify the desired browser, and then run the tests:
    ```json
    {
      "browser": "Chrome"  # or Firefox, Headless Chrome, Headless Firefox
    }
    ```

3. **Generate a test report:**
    ```bash
    pytest tests\ --html-report=./report --title='TITLE'
    ```

## Test Data

The test data is maintained in the `data/test_data.json` file, which includes details such as search queries, expected product names, and other parameters required for testing various functionalities of the ah.nl website.

## Key Files

- **`tests/`**: Contains the main test cases.
- **`pages/`**: Page objects for different parts of the application, such as the homepage, search results page, and product details page.
- **`data/`**: JSON files for test data.
- **`utils/`**: Utility scripts and helper functions.
- **`.gitignore`**: Configured to exclude unnecessary files and directories to keep the repository clean.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
