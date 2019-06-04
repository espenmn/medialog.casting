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

#@indexer(IActorBehavior)
#def sortable_titleIndexer(obj):
#    return obj.first_name + ' ' + obj.last_name

#@indexer(IActorBehavior)
#def TitleIndexer(obj):
#    #fields are required, so I dont think we need to check for it
#    return obj.first_name + ' ' + obj.last_name
