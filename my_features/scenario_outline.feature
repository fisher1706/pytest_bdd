Feature: Some examole outline scenario

  Scenario Outline: Scene outline tests
    Given There are <start> cucumbers
    When I deposit <deposit> cucumbers
    And I withdraw <withdraw> cucumbers
    Then I should have <final> cucumbers

    Examples:
    | start | deposit | withdraw | final |
    |  12   |    5    |     7    |  10   |
    |  10   |    5    |    20    |  -5   |