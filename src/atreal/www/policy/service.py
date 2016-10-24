# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.supermodel import model


class IService(model.Schema):
    """Schema for service content type"""

    model.load('models/service.xml')
