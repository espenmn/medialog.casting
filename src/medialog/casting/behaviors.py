# -*- coding: utf-8 -*-
from zope import schema
from zope.interface import alsoProvides
from plone.supermodel import model
from zope.interface import Interface
from zope.interface import implements
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.namedfile import field as namedfile
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.i18nmessageid import MessageFactory
from plone.schema import Email
_ = MessageFactory('medialog.casting')


FALLBACK_TIMEZONE = 'UTC'
from datetime import date
from datetime import datetime
from datetime import timedelta
from DateTime import DateTime

#We will need to compute age of each actor
today = datetime.now()


SexVocabulary = SimpleVocabulary(
    [SimpleTerm(value=u'Man', title=_(u'Mann')),
     SimpleTerm(value=u'Woman', title=_(u'Kvinne')),]
    )

EyeColorVocabulary = SimpleVocabulary(
    [SimpleTerm(value=u'blue', title=_(u'Blå')),
     SimpleTerm(value=u'green', title=_(u'Grønn')),
     SimpleTerm(value=u'brown', title=_(u'Brun')),
     SimpleTerm(value=u'dark', title=_(u'Mørk')),
     SimpleTerm(value=u'blue-green', title=_(u'Blå-grønn')),
     SimpleTerm(value=u'blue-grey', title=_(u'Blå-grå')),]
    )

HairColorVocabulary = SimpleVocabulary(
    [SimpleTerm(value=u'blond', title=_(u'Blond')),
     SimpleTerm(value=u'red', title=_(u'Rød')),
     SimpleTerm(value=u'black', title=_(u'Svart')),
     SimpleTerm(value=u'brown', title=_(u'Blå')),
     SimpleTerm(value=u'grey', title=_(u'Grå')),
     SimpleTerm(value=u'bold', title=_(u'Skallet')),]
    )

EtnisitetVocabulary = SimpleVocabulary(
    [SimpleTerm(value=u'african', title=_(u'Afrikansk')),
     SimpleTerm(value=u'scandinavian', title=_(u'Skandinavisk')),]
    )

LanguageVocabulary = SimpleVocabulary(
    [SimpleTerm(value=u'norsk', title=_(u'Norsk')),
     SimpleTerm(value=u'urdu', title=_(u'Urdu')),]
    )

DriverLicenceVocabulary = SimpleVocabulary(
    [SimpleTerm(value=u'a1', title=_(u'Motorsykkel (klasse A1)')),
     SimpleTerm(value=u'a2', title=_(u'Motorsykkel (klasse A2)')),
     SimpleTerm(value=u'a', title=_(u'Motorsykkel (klasse A)')),
     SimpleTerm(value=u'b', title=_(u'Personbil (klasse B og B 96)')),
     SimpleTerm(value=u'be', title=_(u'Personbil med tilhenger (BE)')),
     SimpleTerm(value=u'c1', title=_(u'Lastebil (klasse C og CE)')),
     SimpleTerm(value=u'd1', title=_(u'Minibuss (klasse D1 og D!E)')),
     SimpleTerm(value=u'd', title=_(u'Buss (Klasse D og DE)')),
     SimpleTerm(value=u't', title=_(u'Traktor')),
     SimpleTerm(value=u's', title=_(u'Snøscooter')),]
    )


class Actor(Interface):
    """Person content class"""
    #@property
    def title(self):
        if hasattr(self, 'first_name') and hasattr(self, 'last_name'):
            return self.first_names + ', ' + self.last_name
        else:
            return ''

    def setTitle(self, value):
        return

    #@property
    def age(self):
        #calculate age from today - date born
        if hasattr(self, 'born'):
            days_in_year = 365.2425
            age = int((date.today() - born).days / days_in_year)
            return age
        else:
            return None

    def setAge(self, value):
        return




class IActorBehavior(model.Schema):
    """ Add actor behavior"""

    last_name = schema.TextLine(
        title = _("Etternavn", default=u"Etternavn"),
        required = True,
    )

    first_name = schema.TextLine(
        title = _("Fornavn", default=u"Fornavn"),
    )

    sex = schema.Choice(
        title = _("sex", default=u"Kjønn"),
        required = True,
        vocabulary = SexVocabulary
    )

    image =  namedfile.NamedBlobImage(
        title = _("profile_image", default=u"Profil image"),
        required = True,
    )

    cv = namedfile.NamedFile(
        title = _("cv", default=u"CV (fil)"),
        required = False,
    )

    video = schema.URI(
        title = _("video", default=u"Video link"),
        required = False,
    )

    adress = schema.Text(
        title = _("Adresse", default=u"Adresse"),
        required = False,
    )

    phone = schema.TextLine(
        title = _("phone", default=u"Telefon"),
        required = False,
    )

    email = Email(
        title = _("email", default=u"E-post"),
        required = False,
    )

    born = schema.Date(
        title = _("born", default=u"Fødselsdato"),
    )

    eye_color = schema.Choice(
        title = _("eye_color", default=u"Øyefarge"),
        required = True,
        vocabulary = EyeColorVocabulary
    )

    hair_color = schema.Choice(
        title = _("hair_color", default=u"Hår farge"),
        required = True,
        vocabulary = HairColorVocabulary
    )

    etnisitet = schema.Choice(
        title = _("Etnisitet", default=u"Eetnisitet"),
        required = False,
        vocabulary = EtnisitetVocabulary
    )

    language = schema.Choice(
        title = _("Language", default=u"Language"),
        required = False,
        vocabulary = LanguageVocabulary
    )

    height = schema.Int(
        title = _("height", default=u"Høyde i cm"),
        min = 80,
        max = 240
    )

    weight = schema.Int(
        title = _("Vekt", default=u"Vekt i kilo"),
        min = 25,
        max = 180
    )

    driving_licence = schema.List(
        title = _("driver_lincence", default=u"Førerkort"),
        value_type=schema.Choice(
            title=u'Lisenstype',
            vocabulary = DriverLicenceVocabulary
        ),
                required=False,
    )

    shoe_size = schema.TextLine(
        title = _("shoe_size", default=u"Skostørrelse"),
        required = False,
    )

    jacket_size = schema.TextLine(
        title = _("jacket_size", default=u"Jakkestørrelse"),
        required = False,
    )

    trousers_size = schema.TextLine(
        title = _("trousers_size", default=u"Buksestørrelse"),
        required = False,
    )

    relatedItems = RelationList(
        title=_(u'label_related_items', default=u'Prosjekter'),
        default=[],
        value_type=RelationChoice(
            title=u'Prosjekter',
            vocabulary='plone.app.vocabularies.Catalog'
        ),
        required=False,
    )

alsoProvides(IActorBehavior, IFormFieldProvider)


#    age = schema.Int(
#        title = _("age", default=u"Alder"),
#        required = False,
#        description = _("help_alder",
#            default="calculated age"),
#    )
