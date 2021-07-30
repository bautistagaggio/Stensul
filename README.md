# Company
Automation tasks for hiring process

**Project Synopsis**
------------------------------

Pytest is a test framework for python that helps to collect tests from a project, select tests to run and mark them for runtime behavior. This project applies the concept of Page Object Model, which is really useful for reducing code duplication and significantly improves test case maintenance. On this paradigm, web pages are represented as classes, and the various elements on each page are defined as variables within the class scope. The various levels of abstraction makes it easy for anyone that lacks selenium knowledge to create automated tests.

**Components**
------------------------------
**Stensul/Tests/tests.py**  - The class Test_Items contains all the automoted tests for http://immense-hollows-74271.herokuapp.com/. This class inherits the properties and generic methods from the BasePage class, where all the selenium stuff it's encapsulated. Each time a test is conducted, an object of the HomePage class is created, thus its methods are accesed.

**Stensul/basePage.py** - Contains the BasePage class

**Stensul/config.py** - Hosts the TestData class, which includes all the hardcoded data used on the execution of the tests.

**Stensul/homePage.py** - The HomePage class it's located in this file, this class wraps up all the web elements locations as static variables, being a tuple that indicates the way that will be use to locate them (Xpath, Id, Class, etc) and their reference of the correspondent element on the actual webpage. Besides, the actions that will be perform with these elements are allocated also in this class.

**Stensul/conftest.py** - Where the init_driver fixture is located, this fixture sets up the instance of the driver.

**Stensul/test_base.py** - The BaseTest class it's simply a bridge between the init_driver fixture and Test_Items class. Being passed as a parameter, everytime a test on this class is executed, the fixture is called through the BaseTest class.

**Stensul/requirements.txt** - Where all the dependencies to run the tests are located. (symbolic)

**Stensul/dockerfile** - First attempt to build a docker image, in order tu run these tests on a CI / CD pipeline.







