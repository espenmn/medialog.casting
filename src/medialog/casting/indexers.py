#from DateTime import DateTime
from plone.indexer import indexer
from medialog.casting.behaviors import IActorBehavior
from datetime import date
#from datetime import datetime
#from datetime import timedelta
#from DateTime import DateTime

@indexer(IActorBehavior)
def ageIndexer(obj):
    #born is required, so I dont think we need to check for it
    days_in_year = 365.2425
    age = int((date.today() - obj.born).days / days_in_year)
    return str("%02d" % age)


@indexer(IActorBehavior)
def titleIndexer(obj):
    if hasattr(obj, 'first_name') and hasattr(obj, 'last_name'):
        return '{0} {1}'.format(obj.first_name, obj.last_name)
    else:
        return 'NN'

@indexer(IActorBehavior)
def heightIndexer(obj):
    return str("%03d" % obj.height)

@indexer(IActorBehavior)
def weightIndexer(obj):
    return str("%03d" % obj.weight)


#@indexer(IActorBehavior)
#def sortable_titleIndexer(obj):
#    return obj.first_name + ' ' + obj.last_name

#@indexer(IActorBehavior)
#def TitleIndexer(obj):
#    #fields are required, so I dont think we need to check for it
#    return obj.first_name + ' ' + obj.last_name
