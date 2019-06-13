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
from plone.app.vocabularies.catalog import CatalogSource
from plone.namedfile import field as namedfile
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.i18nmessageid import MessageFactory
from plone.schema import Email
_ = MessageFactory('medialog.casting')


SexVocabulary = SimpleVocabulary(
    [SimpleTerm(value=u'Mann', title=_(u'Mann')),
     SimpleTerm(value=u'Kvinne', title=_(u'Kvinne')),]
    )


class IActorBehavior(model.Schema):
    """ Add actor behavior"""

    first_name = schema.TextLine(
        title = _("Fornavn", default=u"Fornavn"),
    )

    last_name = schema.TextLine(
        title = _("Etternavn", default=u"Etternavn"),
        required = True,
    )

    image =  namedfile.NamedBlobImage(
        title = _("profile_image", default=u"Profil image"),
        required = True,
    )

    sex = schema.Choice(
        title = _("sex", default=u"Kjønn"),
        required = True,
        vocabulary = SexVocabulary
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


    adresse = schema.Text(
        title = _("Adresse", default=u"Adresse"),
        required = False,
    )

    eye_color = schema.Choice(
        title = _("eye_color", default=u"Øyefarge"),
        required = True,
        vocabulary = 'medialog.casting.EyeColorVocabulary'
    )

    hair_color = schema.Choice(
        title = _("hair_color", default=u"Hår farge"),
        required = True,
        vocabulary = 'medialog.casting.HairColorVocabulary'
    )

    etnisitet = schema.List (
        title = _("Etnisitet", default=u"Etnisitet"),
        value_type=schema.Choice(
            title = _("Etnisitet", default=u"Etnisitet"),
            required = False,
            vocabulary =  'medialog.casting.EtnisitetVocabulary'
        )
    )

    language = schema.List (
        title = _("Languages", default=u"Languages"),
        value_type=schema.Choice(
            title = _("Language", default=u"Language"),
            required = False,
            vocabulary = 'medialog.casting.LanguageVocabulary'
        )
    )

    dialekt = schema.TextLine(
        title = _("Dialekt", default=u"Dialekt"),
        required = False,
    )

    height = schema.Int(
        title = _("height", default=u"Høyde i cm"),
        min = 40,
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
            vocabulary = 'medialog.casting.DriverLicenceVocabulary'
        ),
        required=False,
    )


    erfaring = schema.List(
        title = _("Erfaring", default=u"Erfaring"),
        description = _("En pr linje", default=u"En erfaring pr linje"),
        value_type=schema.TextLine(
            title=u'Erfaring',
            required=False,
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


    cv = namedfile.NamedFile(
        title = _("cv", default=u"CV (fil)"),
        required = False,
    )

    video = schema.URI(
        title = _("video", default=u"Video link"),
        required = False,
    )


    relatedItems = RelationList(
        title=_(u'label_related_items', default=u'Prosjekter'),
        default=[],
        value_type=RelationChoice(
            title=u'Prosjekter',
            source=CatalogSource(portal_type=['prosjekt', 'Prosjekt']),
        ),
        required=False,
    )

alsoProvides(IActorBehavior, IFormFieldProvider)


class IRelatedActorBehavior(model.Schema):
    """ Add actor behavior"""

    relatedItems = RelationList(
        title=_(u'label_related_items', default=u'Personer'),
        default=[],
        value_type=RelationChoice(
            title=u'Personer',
            source=CatalogSource(portal_type='Person', 'person'),
        ),
        required=False,
    )

alsoProvides(IRelatedActorBehavior, IFormFieldProvider)
