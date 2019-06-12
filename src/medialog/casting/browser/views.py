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
        to_objects = [ref.to_object for ref in refs]
        refers = self.get_referers(self.context)
        from_objects = [ref.from_object for ref in refers]
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

    #def get_images(self, context):
    #    return context.items


    # def get_brains_for_relation_ids(context, relationvalues, sort_key=None, direction='from', depth=0, portal_type=[], language='', keep_original_order=None):
    #     p_catalog = getToolByName(context, 'portal_catalog')
    #     results = []
    #     query = {}
    #
    #     if portal_type:
    #         query['Type'] = portal_type
    #
    #     #no multilanguage in this site
    #     #if language:
    #     #    query['Language'] = language
    #
    #     #log.info('%s Relationvalues ids: %s' % (get_linenumber(), [relationvalue.to_path.split('/')[-1] for relationvalue in relationvalues]))
    #
    #     for relationvalue in relationvalues:
    #         r_path = direction == 'from' and relationvalue.from_path or relationvalue.to_path
    #
    #         for search_depth in range(0, depth+1):
    #             query['path'] = {'query': r_path, 'depth': search_depth}

class FolderView(BrowserView):
    pass
