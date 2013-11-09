#-*- coding: utf-8 -*-

from zope.interface import Interface
from zope import schema


class ILayer(Interface):
    """ browser layer
    """


class ISettings(Interface):
    """ plone.registry settings
    """

    enabled = schema.Bool(
        title=u"Enable TogetherJS",
        default=True
    )


