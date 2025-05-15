# Selenium Test Framework

This is a test automation framework built with Python, Selenium, and Pytest.

## Prerequisites

- Python 3.10
- pip (Python package installer)
- Chrome and/or Firefox browser installed

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

### Browser Options
- Run tests in Chrome (default):
  ```bash
  pytest --browser=chrome
  ```
- Run tests in Firefox:
  ```bash
  pytest --browser=firefox
  ```
- Run tests in headless mode:
  ```bash
  pytest --headless
  ```
- Combine browser and headless options:
  ```bash
  pytest --browser=chrome --headless
  ```

### Parallel Execution
To run tests in parallel using pytest-xdist:
```bash
# Run tests using 4 parallel processes
pytest -n 4

# Run tests using auto-detected number of CPU cores
pytest -n auto
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

### Combining Options
You can combine different options:
```bash
# Run smoke tests in parallel using Chrome in headless mode
pytest -m smoke -n 4 --browser=chrome --headless
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
- Browser options are configured in `conftest.py`
- Parallel execution requires pytest-xdist package
