Feature: Add documents in settings->project document section
  @coll
  Scenario: Adding document and checking the document added or not
    When click on project documents
    And click on Add document
    And fill details in upload documents pop up
    Then validate document is uploaded or not in project documents