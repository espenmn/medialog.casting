# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s medialog.casting -t test_actor.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src medialog.casting.testing.MEDIALOG_CASTING_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/medialog/casting/tests/robot/test_actor.robot
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

Scenario: As a site administrator I can add a Actor
  Given a logged-in site administrator
    and an add Actor form
   When I type 'My Actor' into the title field
    and I submit the form
   Then a Actor with the title 'My Actor' has been created

Scenario: As a site administrator I can view a Actor
  Given a logged-in site administrator
    and a Actor 'My Actor'
   When I go to the Actor view
   Then I can see the Actor title 'My Actor'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Actor form
  Go To  ${PLONE_URL}/++add++Actor

a Actor 'My Actor'
  Create content  type=Actor  id=my-actor  title=My Actor

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Actor view
  Go To  ${PLONE_URL}/my-actor
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Actor with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Actor title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
