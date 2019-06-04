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
    return int((date.today() - obj.born).days / days_in_year)

@indexer(IActorBehavior)
def titleIndexer(obj):
    if hasattr(self, 'first_name') and hasattr(self, 'last_name'):
        return self.first_names + ', ' + self.last_name
    else:
        return ''
