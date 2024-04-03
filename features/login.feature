Feature: Login Functionality

  @login1
  Scenario Outline: Testing login functionality with valid email and incorrect password
    Given I navigated to Login page
    When I enter valid email as "<email>" and invalid password as "<password>" into the fields
    And I click on Login button
    Then I should get a proper warning message on password Error for valid email
    Examples:
      |email                     |password          |
      |johncena92424@gmail.com   |Loki@96067832     |


  @login2
  Scenario Outline: Testing login functionality with an invalid email and valid password
    Given I navigated to Login page
    When I enter invalid email as "<email>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get a proper warning message on email Error for valid password
    Examples:
      |email                        |password          |
      |johncenaddd92424@gmail.com   |Loki@9606         |




  @login3
  Scenario Outline: Testing login functionality with valid phone number and invalid password
    Given I navigated to Login page
    When I enter valid phone as "<phone>" and invalid password as "<password>" into the fields
    And I click on Login button
    Then I should get a proper warning message on password Error for valid phone
    Examples:
      |phone                      |password              |
      |8105000676                 |Loki@9606sdas         |


  @login4
  Scenario Outline: Testing login functionality with invalid phone number and valid password
    Given I navigated to Login page
    When I enter invalid phone as "<phone>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get a proper warning message on phone number Error for valid password
    Examples:
      |phone                    |password          |
      |8105000456               |Loki@9606         |

  @login5
  Scenario: Testing login functionality with empty email/phone number and password
    Given I navigated to Login page
    When I enter empty email and empty password into the fields
    And I click on Login button
    Then I should get a proper warning message on email/phone number Error for empty


  @login6
  Scenario: Click on forgot password
    Given I navigated to Login page
    When I clicked on the forgot password
    Then verify that functionality is working properly for forgot password

  @login7
  Scenario Outline: Testing login functionality with invalid email format and valid password
    Given I navigated to Login page
    When I enter invalid email format as "<email>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get a proper warning message on email error for invalid email format
    Examples:
      |email                    |password          |
      |johncena92424gmail@.com  |Loki@9606         |

  @login8
  Scenario: Click on signup
    Given I navigated to Login page
    When I clicked on the signup
    Then verify that functionality is working properly for signups

  @login9
  Scenario Outline: Testing login functionality with valid email and empty password
    Given I navigated to Login page
    When I enter valid email as "<email>" and empty password into the fields
    And I click on Login button
    Then I should get a proper warning message on password error for empty password/valid email
    Examples:
      |email                    |
      |johncena92424gmail@.com  |
  @login10
  Scenario Outline: Testing login functionality with valid phone number and empty password
    Given I navigated to Login page
    When I enter valid phone as "<phone>" and empty password into the fields
    And I click on Login button
    Then I should get a proper warning message on password error for empty password/valid phone
    Examples:
      |phone        |
      |81050000676  |

  @login11
  Scenario Outline: Login functionality with valid email and password
    Given I navigated to Login page
    When I enter valid email as "<email>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get logged in for valid email and password
    Examples:
      |email                     |password      |
      |johncena92424@gmail.com   |Loki@9606     |


  @login12
  Scenario Outline: Testing login functionality with valid phone number and password
    Given I navigated to Login page
    When I enter valid phone as "<phone>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get logged in for valid phone and password
    Examples:
      |phone                        |password          |
      |8105000676                   |Loki@9606         |