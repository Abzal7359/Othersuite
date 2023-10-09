Feature: creating Assignment rules in Assignment Rules ->Leads
  @rule @sett @coll
  Scenario: creating one rule and  validating rule created or not
    When click on leads under Assignment Rules
    When click on Add new _rule
    And fill details rule_name and integration_type is _source
    And fill source details and select users and click _save
    Then validate rule added or _not
  @rule @sett @coll
  Scenario: perform drag and drop action and validated in leads under Assignment Rules
    When drag and drop the created rule one position _minus
    Then validate it is droped or _not
  @rule @sett @coll
  Scenario: disable the rule and check it gone to last in list or not in leads under Assignment Rules
    When click disable button on created _rule
    Then check the rule is in bootom in list or _not
  @rule @sett @coll
  Scenario: now delete the rule and check rule is deleted or not in leads under Assignment Rules
    When click on delete option on rule and _delete
    Then validate rule is deleted or not by checking the rule name in rule _list
  @rule @sett @coll
  Scenario: create one rule without rule name and validate rule not to be created in leads under Assignment Rules
    When click on Add new _rule
    And fill details  integration_type is _source
    And fill source details and select users and click _save
    Then validate rule is not _added
  @rule @sett @coll
  Scenario: creating assigne rule with integration campaign in leads under Assignment Rules
    When click on Add new _rule
    And fill details rule_name integration_type is _Campaign
    And select users and click _save
    Then validate rule added or _not
  @rule @sett @coll
  Scenario: edit the assigne rule in leads under Assignment Rules
    When click on _assigne
    And update details you want to change and click _update
    Then validate the toaster displayed or not after _updation
  @rule @sett @coll
  Scenario: clone the rule you created in leads under Assignment Rules
    When click on clone option of _rule
    And click clone _button
    Then validate by name or in which the text "copy of " is _added
