from zope.interface import directlyProvides
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from plone import api
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('medialog.casting')


def format_size(size):
    return size.encode('ascii', 'ignore')


def EtnisitetVocabulary(context):
    settings = api.portal.get_registry_record('medialog.casting.interfaces.IMedialogCastingSettings.etnisitet')
    if settings:
        terms = [ SimpleTerm(value=pair, token=format_size(pair), title=pair) for pair in settings ]
    return SimpleVocabulary(terms)

directlyProvides(EtnisitetVocabulary, IVocabularyFactory)


def EyeColorVocabulary(context):
    settings = api.portal.get_registry_record('medialog.casting.interfaces.IMedialogCastingSettings.eyecolor')
    if settings:
        terms = [ SimpleTerm(value=pair, token=format_size(pair), title=pair) for pair in settings ]
    return SimpleVocabulary(terms)

directlyProvides(EyeColorVocabulary, IVocabularyFactory)


def HairColorVocabulary(context):
    settings = api.portal.get_registry_record('medialog.casting.interfaces.IMedialogCastingSettings.haircolor')
    if settings:
        terms = [ SimpleTerm(value=pair, token=format_size(pair), title=pair) for pair in settings ]
    return SimpleVocabulary(terms)

directlyProvides(HairColorVocabulary, IVocabularyFactory)


def LanguageVocabulary(context):
    settings = api.portal.get_registry_record('medialog.casting.interfaces.IMedialogCastingSettings.language')
    if settings:
        terms = [ SimpleTerm(value=pair, token=format_size(pair), title=pair) for pair in settings ]
    return SimpleVocabulary(terms)

directlyProvides(LanguageVocabulary, IVocabularyFactory)


def DriverLicenceVocabulary(context):
    settings = api.portal.get_registry_record('medialog.casting.interfaces.IMedialogCastingSettings.driverlicence')
    if settings:
        terms = [ SimpleTerm(value=pair, token=format_size(pair), title=pair) for pair in settings ]
    return SimpleVocabulary(terms)

directlyProvides(DriverLicenceVocabulary, IVocabularyFactory)
