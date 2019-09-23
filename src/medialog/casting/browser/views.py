#from zope.interface import implements, Interface
from Products.Five import BrowserView
#from plone import api
from datetime import date
from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
from collections import OrderedDict

from pp.client.plone.browser.compatible import InitializeClass
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class ActorPdfView(BrowserView):
    """ Converter view for Bok.
    """
    template = ViewPageTemplateFile('actor_pdf.pt')

    def __call__(self, *args, **kw):
        transformations = (
            'makeImagesLocal',
            'convertFootnotes',
            'removeCrapFromHeadings',
            'fixHierarchies',
        )

        return self.template(self.context)

InitializeClass(ActorPdfView)



class OneChapterView(BrowserView):
    """ PDF Converter view for one chapter.
    """
    template = ViewPageTemplateFile('one_chapter.pt')

    def __call__(self, *args, **kw):
        transformations = (
            'makeImagesLocal',
            'convertFootnotes',
            'removeCrapFromHeadings',
            'fixHierarchies',
        )

        return self.template(self.context)

InitializeClass(OneChapterView)




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

    def get_relateditems(self):
        refs = (self.context.relatedItems)
        to_objects = [ref.to_object for ref in refs if not ref.isBroken()]
        refers = self.get_referers(self.context)
        from_objects = [ref.from_object for ref in refers if not ref.isBroken()]
        ref_list = to_objects + from_objects
        return OrderedDict( (x,1) for x in ref_list ).keys()
        #return ref_list

    def get_referers(self, context = None):
        """ Return a list of backreference relationvalues
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        rel_items = list(catalog.findRelations(rel_query))
        return rel_items


class ProsjektView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('prosjekt_view.pt')

    def __call__(self):
        return self.index()

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_relateditems(self):
        refs = (self.context.relatedItems)
        to_objects = [ref.to_object for ref in refs if not ref.isBroken()]
        refers = self.get_referers(self.context)
        from_objects = [ref.from_object for ref in refers if not ref.isBroken()]
        ref_list = to_objects + from_objects
        return OrderedDict( (x,1) for x in ref_list ).keys()

    def get_referers(self, context = None):
        """ Return a list of backreference relationvalues
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        rel_items = list(catalog.findRelations(rel_query))
        return rel_items
