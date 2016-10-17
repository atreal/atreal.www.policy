# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import atreal.www.policy


class AtrealWwwPolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=atreal.www.policy)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'atreal.www.policy:default')


ATREAL_WWW_POLICY_FIXTURE = AtrealWwwPolicyLayer()


ATREAL_WWW_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ATREAL_WWW_POLICY_FIXTURE,),
    name='AtrealWwwPolicyLayer:IntegrationTesting'
)


ATREAL_WWW_POLICY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ATREAL_WWW_POLICY_FIXTURE,),
    name='AtrealWwwPolicyLayer:FunctionalTesting'
)


ATREAL_WWW_POLICY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ATREAL_WWW_POLICY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='AtrealWwwPolicyLayer:AcceptanceTesting'
)
