# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s atreal.www.policy -t test_testimony.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src atreal.www.policy.testing.ATREAL_WWW_POLICY_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_testimony.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Testimony
  Given a logged-in site administrator
    and an add testimony form
   When I type 'My Testimony' into the title field
    and I submit the form
   Then a testimony with the title 'My Testimony' has been created

Scenario: As a site administrator I can view a Testimony
  Given a logged-in site administrator
    and a testimony 'My Testimony'
   When I go to the testimony view
   Then I can see the testimony title 'My Testimony'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add testimony form
  Go To  ${PLONE_URL}/++add++Testimony

a testimony 'My Testimony'
  Create content  type=Testimony  id=my-testimony  title=My Testimony


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the testimony view
  Go To  ${PLONE_URL}/my-testimony
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a testimony with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the testimony title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
