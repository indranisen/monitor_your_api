from unittest import TestCase

import monitor_your_api


class TestResourceRequest(TestCase):

    def test_is_string(self):
        s = monitor_your_api.resource_request.presence_resource_request()
        self.assertTrue(isinstance(s, basestring))