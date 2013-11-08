from plone.app.layout.viewlets.common import ViewletBase

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class TogetherJS(ViewletBase):

    index = ViewPageTemplateFile('viewlet.pt')
