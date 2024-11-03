from pathlib import Path
import pytest
from pytest_bdd import scenario, given, when, then

feature_file_dir = "../my_features"
feature_file = "scenario_first.feature"

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE: Path = BASE_DIR.joinpath(feature_file_dir).joinpath(feature_file)


"""
pytest_configure: 
This is a special hook function provided by pytest. It is executed once when the pytest framework starts running 
the tests. You can use it to set configurations or variables that should be shared across the test suite.
pytest.AMN = 0: 
Here, AMN is an attribute added to the pytest module (since pytest is an object). 
This makes AMN globally available during the test session, so it can be accessed or modified in different test cases.
"""


def pytest_configure():
    pytest.AMN = 0


@given("The account balance is 100")
def current_balance():
    pytest.AMT = 100


@when("The account holder withdraws 30")
def withdraw_amount():
    pytest.AMT = pytest.AMT - 30


@then("The account balance should be 70")
def final_balance():
    assert pytest.AMT == 70


@scenario(feature_name=FEATURE_FILE, scenario_name="Withdrawal of money")
def test_withdrawal_one():
    print(f"\ndir: {BASE_DIR}")
    print(f"\nfeature: {FEATURE_FILE}")

    print("End of withdrawal test one")


@scenario("../my_features/scenario_first.feature", "Withdrawal of money")
def test_withdrawal_two():
    print(f"\ndir: {BASE_DIR}")
    print(f"\nfeature: {FEATURE_FILE}")

    print("End of withdrawal test two")
