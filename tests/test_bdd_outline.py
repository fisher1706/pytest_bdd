from pathlib import Path
from pytest_bdd import scenario, given, when, then, parsers

feature_file_dir = "../my_features"
feature_file = "scenario_outline.feature"

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE: Path = BASE_DIR.joinpath(feature_file_dir).joinpath(feature_file)


@given(parsers.parse("There are {start:d} cucumbers"), target_fixture="cucumbers")
def existing_cucumbers(start):
    return dict(start=start)


@when(parsers.parse("I deposit {deposit:d} cucumbers"))
def deposit_cucumbers(cucumbers, deposit):
    cucumbers["deposit"] = deposit
    print(cucumbers)


@when(parsers.parse("I withdraw {withdraw:d} cucumbers"))
def withdraw_cucumbers(cucumbers, withdraw):
    cucumbers["withdraw"] = withdraw
    print(cucumbers)


@then(parsers.parse("I should have {final:d} cucumbers"))
def final_cucumbers(cucumbers, final):
    assert cucumbers["start"] + cucumbers["deposit"] - cucumbers["withdraw"] == final


@scenario(FEATURE_FILE, "Scene outline tests")
def test_outline():
    pass
