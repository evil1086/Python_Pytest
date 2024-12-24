The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
here I have kept hierarchy in below formats:
- PageObjects: This folder/modules contains all the locators and selenium logical code.
- Reports: This folder contains the reports of the execution
- Testdata: Here I have kept all the required test data.
- test: Here actual end to end test files kept, Also here I have kept conftest which having the project configurations.
- Utilities: Here all the common Utilities has been kept to re-utilization of common utilities.


Pytest :
# Each pytest files should be start with test_
# Each method should be start with test_ or end  with _test
# While execution from the CMD/conda prompt we need to  py.test , which will execute whole test under that directory
# py.test -v  - it will add the more details onto the cmd
# py.test -s - It will add more details on to the console
# py.test test_demo1.py -v -s - it will execute specific file
# py.test -m smoke -v -s  : it will execute specific marker methods in the files
# to generate html reporting we need to execute file like
# syntax: py.test --html=report.html
# if you want to build report for single file then py.test demo1.py --html=report.html

# if you are executing via Allure then follow below commands:
- Pytest --alluredir=<Location where you want to keep allure files> test.py
- allure serve <path of allure directory>
