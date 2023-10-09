Feature: In Project Updates we adding milestones,newsletters,project_documents

  @coll
  Scenario: Adding mile stone and validating under project updates
#    When click on settings button
    When click on project updates tab
    And in mile stone section click on AddMileStone
    And fill data in MileStone
    Then check Mile stone is added or not
  @coll
  Scenario: Adding news letters and validating under project updates-->news letters
    When click on NewsLetters Tab
    And click on Add NewsLetter button
    And fill data in NewsLetter
    Then check news letter is added or not
  @coll
  Scenario: Adding videos and validating video is added or not under project updates-->videos
    When click on videos Tab
    And click on Add videos Button
    And fill data in videos pop up
    Then check the video is added or not
