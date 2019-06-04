# -*- coding: utf-8 -*-
#from plone.app.textfield import RichText
#from plone.autoform import directives
#from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from ploneconf.site import _
#from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
#from zope.schema.vocabulary import SimpleTerm
#from zope.schema.vocabulary import SimpleVocabulary


class IActor(model.Schema):
    """Dexterity Schema for Actor
    """
