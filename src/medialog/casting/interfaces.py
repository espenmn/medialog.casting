# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface
from z3c.form import interfaces
from zope import schema
from zope.interface import alsoProvides
#from plone.directives import form
from plone.supermodel import model
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.casting')


class IMedialogCastingLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""



class IMedialogCastingSettings(model.Schema):
    """Adds settings to medialog.controlpanel
    """

    model.fieldset(
        'casting',
        label=_(u'Unik Casting'),
        fields=[
             'etnisitet',
             'languages',
             'haircolor',
             'eyecolor',
             'driverlicence'
        ],
     )

    etnisitet = schema.List(
        title = _("label_etnisitet", default=u"Etnisitet"),
        value_type=schema.TextLine()
    )

    languages = schema.List(
        title = _("label_elanguages", default=u"Språk"),
        value_type=schema.TextLine()
    )

    haircolor = schema.List(
        title = _("label_hair_color", default=u'Hårfarge'),
        value_type=schema.TextLine()
    )

    eyecolor = schema.List(
        title = _("label_eye_color", default=u"Øyefarge"),
        value_type=schema.TextLine()
    )

    driverlicence = schema.List(
        title = _("label_drivers_licence", default=u"Førerkort"),
        value_type=schema.TextLine()
    )

alsoProvides(IMedialogCastingSettings, IMedialogControlpanelSettingsProvider)
