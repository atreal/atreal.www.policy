# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.supermodel import model


class ITeam_member(model.Schema):
    """Schema for team_member content type"""

    model.load('models/team_member.xml')
