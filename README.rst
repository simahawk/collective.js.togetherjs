.. contents::

Introduction
============

Basic Plone integration for Mozilla TogetherJS_.

Add it to your Plone instance and install it.

This provides registration for JS resource accessible via

    www.yourdomain.com/++resource++together.js.

and a base viewlet class to be used to include the activation button, like this::

    <browser:viewlet
        name="togetherjs"
        for="*"
        manager="plone.app.layout.viewlets.interfaces.IPortalFooter"
        layer="your.project.interfaces.IBrowserLayer"
        class="collective.js.togetherjs.viewlets.TogetherJS"
        permission="zope2.View"
        />


.. _TogetherJS: https://togetherjs.com/
