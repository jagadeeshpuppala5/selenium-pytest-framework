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