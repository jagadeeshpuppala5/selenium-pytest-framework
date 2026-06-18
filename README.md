# Selenium Pytest Automation Framework

## Tech Stack
- Python
- Selenium WebDriver
- Pytest
- POM
- Logging
- HTML Reports
- Allure Reports

## Project Structure
config/
data/
pages/
tests/
utilities/

## Run Tests
pytest -v

## Smoke Tests
pytest -m smoke

## Regression Tests
pytest -m regression

## Generate HTML Report
pytest --html=reports/report.html --self-contained-html

## Generate Allure Results
pytest --alluredir=allure-results

# Selenium Pytest Automation Framework

## Features

- Selenium WebDriver
- Pytest Framework
- Page Object Model (POM)
- Data Driven Testing
- Logging
- HTML Reports
- Allure Reports
- GitHub Actions CI/CD
- Smoke & Regression Execution
- Screenshot Capture on Failure

## Framework Architecture

Tests
 │
 ▼
Pytest
 │
 ▼
Page Object Model
 │
 ▼
Selenium WebDriver
 │
 ▼
Application Under Test

## CI/CD

GitHub Actions automatically executes the test suite on every push and pull request.