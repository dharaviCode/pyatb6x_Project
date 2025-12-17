#1. (pip install pytest) run this into terminal to install pytest
#2. if we want to use pytest then we need to have a proper structure
# test files : test_*.py
# test functions : test_*
# test classes : Test*
# test method in classes : test_*

# so this file name "Lab_183_pyTest.py" will not be detected by pyTest.
# we should have naming convention as "test_Lab_184_pyTest.py" which will be then recognized by pytest

#So now every function that you create will be treated as a test case

#pytest -v (Verbose output) with source location of file will run the test cases (functions)

#So if after test case creation and execution we need to have a "report" created for the pass/fail,
# this we can achieve by using "allure" which creates a very beautiful organized report.

#3. Install allure command in terminal - [pip install allure-pytest]
#4. To see the results :
#   install node.js on your system
#   install allure-commandline by this command in cmd - [nmp -g install allure-commandline]
#   If allure is installed then it should give version - [allure --version]

#5. Now we can add the @allure.title and @allure.description to all the TCs giving extra info about
#   the TCs which will be attached to the test cases.

#6. Run all the TCs from the source, but this will not generate the report
#7. Now run command in terminal: [ -- alluredir allure-results ]
#   [ pytest src/ex_25_Allure_PyTest/test_Lab186_Allure.py --alluredir allure-results ]
#   "allure-results" folder will be created inside the project

#8. Now to see the report in html format use the command - [allure serve allure-results ]

#9. So now working with the real API request we need a module called "Requests" in python.
#   HTTP methods (GET, PUT, POST, PATCH, DELETE...) will be handled by "Requests" module.
#   Requests - HTTP library

