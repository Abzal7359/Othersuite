Feature: Editing project details and validating data changed or not
  @sett
  Scenario: editing project details
    When click on the settings button
    And click on edit button
    And fill details which are editable
    |location                 |projectname                   |TotalArea              |description           |
    |Hyderabad, Telangana, India |Swargseema                |65600              |luxary villas with greenary |
    And edit contact details
    |phonenumberone       |phonenumbertwo     |emailone         |emailtwo               |
    |8229498763          |8289098274       | adeva12@gmail.com  |bnaveen34@gmail.com    |
    And select Amenities in edit
    And image uploading and clicking update button
    Then check all editied details got updated or not




