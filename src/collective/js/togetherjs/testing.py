from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import collective.js.togetherjs


COLLECTIVE_JS_TOGETHERJS = PloneWithPackageLayer(
    zcml_package=collective.js.togetherjs,
    zcml_filename='testing.zcml',
    gs_profile_id='collective.js.togetherjs:testing',
    name="COLLECTIVE_JS_TOGETHERJS")

COLLECTIVE_JS_TOGETHERJS_INTEGRATION = IntegrationTesting(
    bases=(COLLECTIVE_JS_TOGETHERJS, ),
    name="COLLECTIVE_JS_TOGETHERJS_INTEGRATION")

COLLECTIVE_JS_TOGETHERJS_FUNCTIONAL = FunctionalTesting(
    bases=(COLLECTIVE_JS_TOGETHERJS, ),
    name="COLLECTIVE_JS_TOGETHERJS_FUNCTIONAL")
