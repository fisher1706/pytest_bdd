import pytest
from pytest_bdd import scenarios, given, when, then

# Load the feature file
scenarios('../my_features/scenario_first.feature')


# Shared fixture for the account
@pytest.fixture
def account():
    return {"balance": 0}


# Step definition for 'Given The account balance is 100'
@given('The account balance is 100')
def set_initial_balance(account):
    account['balance'] = 100


# Step definition for 'When The account holder withdraws 30'
@when('The account holder withdraws 30')
def withdraw(account):
    account['balance'] -= 30


# Step definition for 'Then The account balance should be 70'
@then('The account balance should be 70')
def check_balance(account):
    assert account['balance'] == 70
