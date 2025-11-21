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
        self.elementaryTc.assertLength([], 0)
        with self.assertRaisesRegex(AssertionError, r"Collection length is not 1: \[\]"):
            self.elementaryTc.assertLength([], 1)
        ### Two-element collection:
        self.elementaryTc.assertLength([4, 6], 2)
        with self.assertRaisesRegex(AssertionError, r"Collection length is not 0: \[4, 6\]"):
            self.elementaryTc.assertLength([4, 6], 0)
    
    def test_assertEmpty(self):
        """
        Method assertEmpty() should assert that a collection is empty for non-lazy collections.
        """
        self.elementaryTc.assertEmpty([])
        with self.assertRaisesRegex(AssertionError, r"Collection is not empty: \[4\]"):
            self.elementaryTc.assertEmpty([4])
        with self.assertRaisesRegex(AssertionError, r"Collection is not empty: \[4, 6\]"):
            self.elementaryTc.assertEmpty([4, 6])
    
    def test_assertLength_honors_msg(self):
        """
        Method assertLength() should honor msg arg when providaded.
        """
        with self.assertRaisesRegex(AssertionError, r"my msg"):
            self.elementaryTc.assertLength([4, 6], 0, msg="my msg")
    
    ############################################################
    ############################################################
    ############################################################
    @classmethod
    def setUpClass(self):
        ElementaryTestCase = type("ElementaryTestCase", (
            unittest.TestCase,
            assert_mixins.ElementaryMixin,
            ), {})
        self.elementaryTc = ElementaryTestCase()
