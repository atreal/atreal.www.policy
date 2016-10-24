# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.supermodel import model


class IFrontpage(model.Schema):
    """Schema for frontpage content type"""

    model.load('models/frontpage.xml')
