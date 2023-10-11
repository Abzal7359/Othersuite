Feature: validating Email Templates functionlaity
  Scenario: Add Email template and validate in send email the template added or not
    When click on settings gear image
    And click on email templates and Add template
    And fill email template details
    And save email template
    And go to leads list and click bulk actions send mail
    Then Verify whether the template you created is present in the templates selection

  Scenario: Delete the template and validate template deleted or not
    When close modal
    And click on settings gear image
    And click on email templates
    And click on delete on email template
    Then validate email template deleted or not











#    //form/div[1]/div[1]/div/div[2]//*[name()='svg']