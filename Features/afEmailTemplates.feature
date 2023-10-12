Feature: validating Email Templates functionlaity
  Scenario: Add Email template and validate in send email the template added or not
    When click on settings gear image
    And click on email templates and Add template
    And fill email template details
    And save email template
    And go to leads list and click bulk actions send mail
    Then Verify whether the template you created is present in the templates selection

  Scenario: disable email template and validate that is not showing in mail section
    When close modal
    And click on settings gear image
    And click on email templates
    And click disable on template
    And go to leads list and click bulk actions send mail
    Then Verify whether the template you disabled is not present in the templates selection

  Scenario: edit the template and validate toaster got or not
    When close modal
    And click on settings gear image
    And click on email templates
    And click on edit and update it
    Then validate the toaster of update


  Scenario: Delete the template and validate template deleted or not
    When click on delete on email template
    Then validate email template deleted or not











#    //form/div[1]/div[1]/div/div[2]//*[name()='svg']