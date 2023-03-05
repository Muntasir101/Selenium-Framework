"""
In this file, we first activate the virtual environment using the source command.
We then install the required Python packages by running pip install -r requirements.txt.

We run the tests using pytest and generate an Allure report by passing the --alluredir option to pytest.
This tells pytest to store the test results in the specified directory (./allure-results in this case).

We then generate an HTML report from the Allure results using the allure generate command.
This command takes the --clean option to delete any existing report data before generating a new report, and the -o option to specify the output directory (./allure-report in this case).

Finally, we open the HTML report in a web browser using the allure open command.
This command opens the report in the default web browser on the system.

"""