# Selenium Test Framework

This is a test automation framework built with Python, Selenium, and Pytest.

## Prerequisites

- Python 3.10
- pip (Python package installer)

## Setup Instructions

1. Install Python 3.10:
   - For macOS:
     ```bash
     brew install python@3.10
     ```
   - For Windows:
     - Download Python 3.10 installer from [python.org](https://www.python.org/downloads/)
     - Run the installer and ensure to check "Add Python to PATH"

2. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

### Basic Test Execution
To run all tests:
```bash
pytest
```

### Running Specific Test Categories
- Run smoke tests:
  ```bash
  pytest -m smoke
  ```
- Run regression tests:
  ```bash
  pytest -m regression
  ```

### Test Reports

#### HTML Report
After test execution, an HTML report will be generated at `reports/report.html`. Open this file in your web browser to view the test results.

#### Allure Report
1. After test execution, Allure results will be generated in `reports/allure-results`
2. To view the Allure report:
   ```bash
   # Install Allure command-line tool if not already installed
   # For macOS:
   brew install allure
   
   # Generate and open Allure report
   allure serve reports/allure-results
   ```

## Project Structure
- `test_cases/`: Contains all test files
- `reports/`: Contains test execution reports
  - `report.html`: HTML test report
  - `allure-results/`: Allure report data

## Additional Information
- Test markers are defined in `pytest.ini`
- Smoke tests are quick sanity checks
- Regression tests are comprehensive test suites
