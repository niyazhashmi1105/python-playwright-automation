**Python Playwright Automation Framework**
This repository contains an automation framework using the Python programming language, leveraging Playwright and pytest for automated web application testing.

**Key Features:**
Playwright Integration: Cross-browser testing using Playwright with support for Chromium, Firefox, and WebKit.
Page Object Model (POM): A structured approach using POM, separating page interactions into reusable classes and methods.
Parallel Test Execution: Support for running tests in parallel, improving execution time and efficiency.
Test Reporting: Generates test reports using pytest-html and Allure for enhanced visibility of test results.

**Directory Structure:**
.github/workflows/: Contains GitHub Actions workflow configurations to automate the test execution pipeline in CI/CD.
locators/: Stores elements or locators used by the Page Object Model classes.
pages/: Contains Page Object Model classes that encapsulate interactions with various pages of the web application.
reports/: Directory to store the generated reports (e.g., HTML reports, Allure reports).
tests/: Contains the test cases that use the page objects and utilities.
utils/: Reusable utility methods or helper functions that assist in the test execution process.
Files:
Dockerfile: Defines the Docker configuration for containerizing the test framework.
conftest.py: A pytest configuration file for setting up fixtures and hooks for test execution.
pytest.ini: A pytest configuration file where command-line options, plugins, and markers are defined.
requirements.txt: Lists all dependencies required for running the tests, such as pytest, pytest-playwright, allure-pytest, etc.
README.md: Placeholder for project description and usage guidelines (expected to be updated).

**How to Run Tests**
Install Dependencies: Make sure to install the required Python dependencies from requirements.txt
pip install -r requirements.txt

Running Tests: Use the following command to run the tests:
pytest

Running Tests in Parallel: To run tests in parallel (e.g., across multiple browsers), use:
pytest -n 3 --browser chromium
This will run the tests on Chromium, Firefox, and WebKit in parallel.

**Generate Allure Report:** 
After running the tests, you can generate an Allure report by running:
allure serve reports/

**Using Docker:** The repository also includes a Docker setup, allowing you to run the tests inside a Docker container:

**Build the Docker Image:**
docker build -t pytest-playwright .

**Run the Docker Container:**
docker run --rm pytest-playwright

**GitHub Actions Integration:** 
The repository contains CI/CD pipeline definitions under .github/workflows/ to automate test execution, ensuring continuous testing and reporting.

**Example Commands:**

**Run Tests on a Specific Browser:**
pytest --browser chromium

**Run Tests with HTML Report:**
pytest --html=reports/report.html

This README outline provides the essential structure and usage for the Playwright automation framework. 
The pytest commands ensure flexibility in running tests across browsers and generating reports for test results.
