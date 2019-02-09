# python-api-testing
Example API testing framework in Python using Behave library for BDD.

## Setup
It's recommended you run a Python Virtual Environment in Python 3.7.2 or higher.

In your environment please run `pip install behave`

If you want to use Docker please ensure this is installed as well as docker compose.


## Testing
If you are running the tests by your IDE or terminal please checkout and run the API webservice: https://bitbucket.org/aaronmwilliams/user-exercises-rest/src/master/.

Please note currently you will have to amend the URI for the API service as the default is http://api:8080.

Execute all tests by running the following command in the project root `behave` 

## Reporting
The default Behave test result gets generated in `plain.output` file.

## Linting
Please ensure you have the `pylint` plugin installed and running on your IDE.

## Docker
To save you from having to install Python and the dependencies you can run the tests by running the docker compose file
run `docker-compose up --exit-code-from tests` in the project root. This will run the API service and then the tests.

## Jenkins
If the Jenkins file is used it will build the docker image and then run docker compose which kicks off the tests.

## To-Do
- ~~Move the API service to docker-compose~~
- ~~Adding to Jenkins~~
- Add to TravisCI
- Better test reports