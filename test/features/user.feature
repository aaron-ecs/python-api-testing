Feature: User
 	As user
 	I want to POST and GET my user details
 	So I can create and view them on the frontend

  Scenario Outline: Create User
        Given I am <name> with postcode <postcode>
        When I create my details
        Then the response code is 200

    Examples:
          | name                  | postcode         |
          | Aaron                 | PE20 1LG         |
          | James                 | AA14DN           |
          | Fred-WilliamsO'riley  | B R14R T         |
          | A                     | AAAAAAAA         |

    Scenario: User Not Found
      Given I attempt to view a user which does not exist
      Then the response code is 404
