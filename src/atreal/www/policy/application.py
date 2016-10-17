# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.supermodel import model


class IApplication(model.Schema):
    """Schema for application content type"""

    model.load('models/application.xml')
