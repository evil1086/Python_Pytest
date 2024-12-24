The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
here I have kept hierarchy in below formats:
- PageObjects: This folder/modules contains all the locators and selenium logical code.
- Reports: This folder contains the reports of the execution
- Testdata: Here I have kept all the required test data.
- test: Here actual end to end test files kept, Also here I have kept conftest which having the project configurations.
- Utilities: Here all the common Utilities has been kept to re-utilization of common utilities.
- 