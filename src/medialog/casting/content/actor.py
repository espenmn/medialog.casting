# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
#from plone.supermodel import model
from zope.interface import implementer
from datetime import date

# from medialog.casting import _


class IActor(model.Schema):
    """ Marker interface and Dexterity Python Schema for Actor    """
    # model.load('actor.xml')


@implementer(IActor)
class Actor(Container):
    """
    """
    @property
    def title(self):
        if hasattr(self, 'first_name') and hasattr(self, 'last_name'):
            return '{0} {1}'.format(self.first_name, self.last_name)
        else:
            return 'NN'

    def setTitle(self, value):
        return

    @property
    def age(self):
        days_in_year = 365.2425
        if hasattr(self, 'born'):
            age = int((date.today() - self.born).days / days_in_year)
            return age
            #return str("%02d" % age)
