#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Install the required Python packages
pip install -r requirements.txt

# Run the tests with pytest and generate an Allure report
pytest --alluredir=./allure-results

# Generate an HTML report from the Allure results
allure generate --clean -o ./allure-report ./allure-results

# Open the HTML report in a web browser
allure open ./allure-report

