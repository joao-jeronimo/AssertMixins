# -*- coding: utf-8 -*-
import unittest, assert_mixins
from unittest.mock import Mock, MagicMock

class TestElementaryMixin(unittest.TestCase):
    """
    Test behaviour of class ElementaryMixin.
    """
    
    def test_assertLength(self):
        """
        Method assertLength() should assert the length of built-in non-lazy collections.
        """
        ### Empty collection:
        self.elementary.assertLength([], 0)
        with self.assertRaisesRegex(AssertionError, "Collection length is not 1: []"):
            self.elementary.assertLength([], 1)
        ### Two-element collection:
        self.elementary.assertLength([4, 6], 2)
        with self.assertRaisesRegex(AssertionError, "Collection length is not 0: [4, 6]"):
            self.elementary.assertLength([4, 6], 0)
    
    ############################################################
    ############################################################
    ############################################################
    @classmethod
    def setUpClass(self):
        self.elementary = assert_mixins.ElementaryMixin()
