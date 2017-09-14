Feature: Picking elements with the mouse should work as expected.

Scenario: Picking an input with the mouse should work correctly
  Given I open the browser on the saved google page
  When I try to pick the element `InputText()`
  Then I get the xpath selector: "//input[@name='q']"

Scenario: Picking and cancelling should work correctly.
  Given I open the browser on the saved google page
  When I start picking elements
  And I cancel picking elements
  Then the state of the browser is correct and accepting commands