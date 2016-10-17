# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from atreal.www.policy.testing import ATREAL_WWW_POLICY_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that atreal.www.policy is properly installed."""

    layer = ATREAL_WWW_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if atreal.www.policy is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'atreal.www.policy'))

    def test_browserlayer(self):
        """Test that IAtrealWwwPolicyLayer is registered."""
        from atreal.www.policy.interfaces import (
            IAtrealWwwPolicyLayer)
        from plone.browserlayer import utils
        self.assertIn(IAtrealWwwPolicyLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ATREAL_WWW_POLICY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['atreal.www.policy'])

    def test_product_uninstalled(self):
        """Test if atreal.www.policy is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'atreal.www.policy'))

    def test_browserlayer_removed(self):
        """Test that IAtrealWwwPolicyLayer is removed."""
        from atreal.www.policy.interfaces import \
            IAtrealWwwPolicyLayer
        from plone.browserlayer import utils
        self.assertNotIn(IAtrealWwwPolicyLayer, utils.registered_layers())
