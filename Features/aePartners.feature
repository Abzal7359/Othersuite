Feature: checking functinality of partners
  @last
  Scenario: Adding partner and validate
    When click on setting to go back to dadshboard
    And click on partners
    And click add partner
    And fill details with new mail and phone
    |email     |phone       |firstname       |lastname     |
    |prashant1@gmail.com     |7032936567       |Ram     |Pawan     |
    Then validate partner is added or not
  @last
  Scenario: Adding duplicate same mail and validate

    When click add partner
    And fill details with same mail and other phone
    |phone |
    |9177731154      |
    Then validate the toaster message of duplicate
  @last
  Scenario: Adding dupliacte other mail and same phone

    When click add partner
    And fill details with other mail and same phone
    |email |
    |apoorva896@gmail.com      |
    Then validate the toaster message of duplicate
  @last
  Scenario: edit the partner and check changes reflected or not
    When click on edit button on partner
    And edit details phone
    |phonenumb|
    |8032996368         |
    Then validate updates got reflected or not

