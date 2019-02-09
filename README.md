# python-api-testing
Example API testing framework in Python using Behave library for BDD.

## Setup
It's recommended you run a Python Virtual Environment in Python 3.7.2 or higher.

In your environment please run `pip install behave`

Please checkout and run the following API webservice: https://bitbucket.org/aaronmwilliams/user-exercises-rest/src/master/. Please note currently you will have to amend the URI for the API service as the default is http://192.168.1.149:8080.

## Testing
Execute all tests by running the following command in the project root `behave` 

## Reporting
The default Brhave test result gets generated in `plain.output` file

## Linting
Please ensure you have the `pylint` plugin installed and running on your IDE.

## Docker
To save you from having to install Python and the dependencies you can run the tests by building the docker image.
Run `docker build .` in the project root.

## Jenkins
The Jenkins file will build the docker image and run the tests against whatever URL is used in this project.

## To-Do
- Move the API service to docker-compose
- ~~Adding to Jenkins~~
- Add to TravisCI
- Better test reports