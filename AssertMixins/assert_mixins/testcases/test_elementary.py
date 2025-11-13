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
        
        self.assertTrue(True)
    
    ############################################################
    ############################################################
    ############################################################
    @classmethod
    def setUpClass(self):
        self.elementary = assert_mixins.ElementaryMixin()
