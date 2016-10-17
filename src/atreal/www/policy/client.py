# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.supermodel import model


class IClient(model.Schema):
    """Schema for client content type"""

    model.load('models/client.xml')
