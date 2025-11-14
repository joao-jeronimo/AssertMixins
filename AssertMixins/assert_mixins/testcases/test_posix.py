# -*- coding: utf-8 -*-
import unittest, assert_mixins
from unittest.mock import Mock, MagicMock

class TestPosixMixin(unittest.TestCase):
    """
    Test behaviour of class PosixMixin.
    """
    
    def test_assertPosixSuccess(self):
        """
        Method assertPosixSuccess() must fail if and only if provided with a non-zero.
        """
        self.posixTc.assertPosixSuccess(0)
        with self.assertRaises(AssertionError): self.posixTc.assertPosixSuccess(1)
        with self.assertRaises(AssertionError): self.posixTc.assertPosixSuccess(-1)
        with self.assertRaises(AssertionError): self.posixTc.assertPosixSuccess(2)
    def test_assertPosixFailure(self):
        """
        Method assertPosixFailure() must fail if and only if provided with a zero.
        """
        with self.assertRaises(AssertionError): self.posixTc.assertPosixFailure(0)
        self.posixTc.assertPosixFailure(1)
        self.posixTc.assertPosixFailure(-1)
        self.posixTc.assertPosixFailure(2)
    
    ############################################################
    ############################################################
    ############################################################
    @classmethod
    def setUpClass(self):
        PosixTestCase = type("PosixTestCase", (
            unittest.TestCase,
            assert_mixins.PosixMixin,
            ), {})
        self.posixTc = PosixTestCase()
