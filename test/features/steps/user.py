"""
Test script for the /api/users/ end point. Tests cover POST, GET & 404
"""
import json
from behave import given, when, then
import requests

_BASE_URL = "http://192.168.1.149:8080/api/users/"
USER_PAYLOAD = "{}"
RESPONSE = {}


@given("I am {name} with postcode {postcode}")
def build_user_payload(self, name, postcode):
    """ Creates JSON payload to post """
    self.USER_PAYLOAD = '{"name": "%s", "postcode": "%s"}' % (name, postcode)


@given("I attempt to view a user which does not exist")
def get_unknown_user(self):
    """ Calls GET endpoint with a an unknown user """
    self.RESPONSE = get_user(_BASE_URL + "9999")


@when("I create my details")
def create_user(self):
    """ Posts user and saves response JSON """
    print(self.USER_PAYLOAD + " LLLLLLLL")
    self.RESPONSE = get_user(_BASE_URL + str(post_user(self.USER_PAYLOAD)["id"]))


@then('The response code is {status_code}')
def assert_response(self, status_code):
    """ Asserts status code of the response after user is created """
    assert self.RESPONSE.status_code == int(status_code)


def get_user(url):
    """ Generic method to call GET endpoint and return response """
    return requests.get(url)


def post_user(payload):
    """
    Test support method to post a new user and return the response JSON
    :param payload:  JSON
    """
    response = requests.post(_BASE_URL, json=json.loads(payload))
    return response.json()
