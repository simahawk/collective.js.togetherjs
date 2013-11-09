.. contents::

Introduction
============

Basic Plone integration for Mozilla TogetherJS_.

Add it to your Plone instance and install it.

This provides registration for JS resource accessible via

    www.yourdomain.com/++resource++together.js.

and a viewlet that inject the button for enabling TogetherJS.

Rendering of JS and viewlet are subject to registry settings via:

    collective.js.togetherjs.interfaces.ISettings.enabled

An helper view `@@togetherjs` is registered to get settings, like::

    <tal:block define="helpers context/@@togetherjs"
           condition="helpers/enabled">
           [...]
    </tal:block>

You can override this view for your own needs.


.. _TogetherJS: https://togetherjs.com/
