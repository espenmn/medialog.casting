# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import medialog.casting


class MedialogCastingLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=medialog.casting)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.casting:default')


MEDIALOG_CASTING_FIXTURE = MedialogCastingLayer()


MEDIALOG_CASTING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_CASTING_FIXTURE,),
    name='MedialogCastingLayer:IntegrationTesting',
)


MEDIALOG_CASTING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_CASTING_FIXTURE,),
    name='MedialogCastingLayer:FunctionalTesting',
)


MEDIALOG_CASTING_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIALOG_CASTING_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MedialogCastingLayer:AcceptanceTesting',
)
