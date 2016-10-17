# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.supermodel import model


class ITestimony(model.Schema):
    """Schema for testimony content type"""

    model.load('models/testimony.xml')
