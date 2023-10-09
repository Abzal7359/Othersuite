Feature: creating assigne rule in opportunity and checking rule is created or not
  @rule @sett @coll
  Scenario:checking default assignment working or not
    When click on opportunity in Assignmnet Rules
    And deselect all assignes
    And check last deselcted person is selected or not after refresh page
    And now select another assigne
    Then valiadte assigne added or not in default assignment
  @rule @sett @coll
  Scenario: create one rule and validate rule created or not
    When click on Add new rule
    And fill details rule_name and integration_type is source
    And fill source details and select users and click save
    Then validate rule added or not
  @rule @sett @coll
  Scenario: perform drag and drop action and validated
    When drag and drop the created rule one position minus
    Then validate it is droped or not
  @rule @sett @coll
  Scenario: disable the rule and check it gone to last in list or not
    When click disable button on created rule
    Then check the rule is in bootom in list or not
  @rule @sett @coll
  Scenario: now delete the rule and check rule is deleted or not
    When click on delete option on rule and delete
    Then validate rule is deleted or not by checking the rule name in rule list
  @rule @sett @coll
  Scenario: create one rule without rule name and validate rule not to be created
    When click on Add new rule
    And fill details  integration_type is source
    And fill source details and select users and click save
    Then validate rule is not added

  @rule @sett @coll
  Scenario: creating assigne rule with integration campaign
    When click on Add new rule
    And fill details rule_name integration_type is Campaign
    And select users and click save
    Then validate rule added or not
  @rule @sett @coll
  Scenario: edit the assigne rule
    When click on assigne
    And update details you want to change and click update
    Then validate the toaster displayed or not after updation

  @rule @sett @coll
  Scenario: clone the rule you created
    When click on clone option of rule
    And click clone button
    Then validate by name or in which the text "copy of " is added


