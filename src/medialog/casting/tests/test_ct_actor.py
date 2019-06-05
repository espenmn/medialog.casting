# -*- coding: utf-8 -*-
from medialog.casting.content.actor import IActor  # NOQA E501
from medialog.casting.testing import MEDIALOG_CASTING_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class ActorIntegrationTest(unittest.TestCase):

    layer = MEDIALOG_CASTING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Folder',
            self.portal,
            'actor',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_actor_schema(self):
        fti = queryUtility(IDexterityFTI, name='Actor')
        schema = fti.lookupSchema()
        self.assertEqual(IActor, schema)

    def test_ct_actor_fti(self):
        fti = queryUtility(IDexterityFTI, name='Actor')
        self.assertTrue(fti)

    def test_ct_actor_factory(self):
        fti = queryUtility(IDexterityFTI, name='Actor')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IActor.providedBy(obj),
            u'IActor not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_actor_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Actor',
            id='actor',
        )

        self.assertTrue(
            IActor.providedBy(obj),
            u'IActor not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_actor_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Actor')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_actor_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Actor')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'actor_id',
            title='Actor container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
