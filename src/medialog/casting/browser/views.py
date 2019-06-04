#from zope.interface import implements, Interface
from Products.Five import BrowserView
#from plone import api
from datetime import date


class IActorView(BrowserView):
    """collection view"""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_age(self):
        #Maybe show half year ?
        #div / mod ?
        days_in_year = 365.2425
        return int((date.today() - self.context.born).days / days_in_year)



class FolderView(BrowserView):
    pass

    
