Feature: Test Basic recipes functionality

  Scenario: Verify that home page opens
    Given User on the home page


  Scenario: Verify that Add new recipe form opens
    Given User on the home page
    When User clicks on Add New Recipe button with xpath "//*[@id="root"]/div/div[1]/div/div[3]/a[1]/i"
    Then Add New Recipe window opens with xpath "/html/body/div[2]"'/html/body/div[2]'/html/body/div[2]"

  Scenario: Verify that User can open Full recipe page
    Given User on the home page
    When User clicks on particular recipe title with xpath "//*[@id="root"]/div/div[1]/div/div[4]/div/div[1]/div/div[2]/a"
    Then Full Recipe View page opens with xpath "//*[@id="root"]/div/div[1]"

  Scenario: Verify that user can add new recipe
    Given User on the home page
    When User clicks on Add New Recipe button with xpath "//*[@id="root"]/div/div[1]/div/div[3]/a[1]/i"
    Then User enter data 'Test recipe adding' to the 'Title' field
    Then User enter 'Test recipe adding' to the 'Description' field
    Then User click on 'Submit' button
    Then User can see a new recipe with 'Test recipe adding' text

