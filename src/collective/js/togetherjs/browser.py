#-*- coding: utf-8 -*-

from zope.component import getUtility

from plone.registry.interfaces import IRegistry
from plone.memoize import view

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView

from collective.js.togetherjs.interfaces import ISettings


def get_settings():
    registry = getUtility(IRegistry)
    return registry.forInterface(ISettings)


class Helpers(BrowserView):

    @property
    @view.memoize_contextless
    def settings(self):
        return get_settings()

    def enabled(self):
        return self.settings.enabled
