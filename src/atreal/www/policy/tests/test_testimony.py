# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from atreal.www.policy.interfaces import ITestimony
from atreal.www.policy.testing import ATREAL_WWW_POLICY_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class TestimonyIntegrationTest(unittest.TestCase):

    layer = ATREAL_WWW_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='testimony')
        schema = fti.lookupSchema()
        self.assertEqual(ITestimony, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='testimony')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='testimony')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ITestimony.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='testimony',
            id='testimony',
        )
        self.assertTrue(ITestimony.providedBy(obj))
