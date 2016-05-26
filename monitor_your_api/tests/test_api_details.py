from unittest import TestCase

import monitor_your_api


class TestMonitor(TestCase):

    def test_is_string(self):
        s = monitor_your_api.api_details.presence_api_details()
        self.assertTrue(isinstance(s, basestring))