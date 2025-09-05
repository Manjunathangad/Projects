Feature: User Login

Background: common steps # Runs first everytime for each sceanrios (Used for common sceanrio that will run everytime)
  Given launch chrome browser
  # Given launch firefox browser

  Scenario: Successful login
    When open HP
    Then verify the logo and close browser

# Feature: User Login with multi parameters

#   Scenario Outline: Scenario Outline Successful login
#     Given launch browser
#     When open HP
#     And enter "<un>" and "<pw>"
#     Then verify the logo and close browser

#     Examples:
#       | un              | pw        |
#       | mveerannaangadi | Admin@123 |



# Before Hooks # Runs before the scenario
# After Hooks # Runs after the scenario


