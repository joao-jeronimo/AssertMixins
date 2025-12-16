# -*- coding: utf-8 -*-
import unittest, assert_mixins, shutil, os
from unittest.mock import Mock, MagicMock

class TestFsMixin(unittest.TestCase):
    """
    Test behaviour of class FsMixin.
    """
    
    def test_assertPathExists(self):
        """
        Method assertPathExists() must fail if and only if the provided path does not exist.
        """
        with self.assertRaisesRegex(ValueError, r"Function assertPathExists\(\) was called with the non-string «0»"):
            self.fsTc.assertPathExists(0)
        with self.assertRaisesRegex(AssertionError, r"False is not true : Path «/tmp/unit_testing_assert_mixins/TestFsMixin/non_existing_entry» does not exist"):
            self.fsTc.assertPathExists("/tmp/unit_testing_assert_mixins/TestFsMixin/non_existing_entry")
        self.fsTc.assertPathExists("/tmp/unit_testing_assert_mixins/TestFsMixin/sample_empty_folder")
        self.fsTc.assertPathExists("/tmp/unit_testing_assert_mixins/TestFsMixin/sample_thingy_folder")
        self.fsTc.assertPathExists("/tmp/unit_testing_assert_mixins/TestFsMixin/sample_thingy_folder/thing")
    def test_assertPathNotExists(self):
        """
        Method assertPathNotExists() must fail if and only if the provided path is a string and exists.
        """
        with self.assertRaisesRegex(ValueError, r"Function assertPathNotExists\(\) was called with the non-string «0»"):
            self.fsTc.assertPathNotExists(0)
        with self.assertRaisesRegex(AssertionError, r"True is not false : Path «/tmp/unit_testing_assert_mixins/TestFsMixin/sample_empty_folder» exist"):
            self.fsTc.assertPathNotExists("/tmp/unit_testing_assert_mixins/TestFsMixin/sample_empty_folder")
        with self.assertRaisesRegex(AssertionError, r"True is not false : Path «/tmp/unit_testing_assert_mixins/TestFsMixin/sample_thingy_folder» exist"):
            self.fsTc.assertPathNotExists("/tmp/unit_testing_assert_mixins/TestFsMixin/sample_thingy_folder")
        with self.assertRaisesRegex(AssertionError, r"True is not false : Path «/tmp/unit_testing_assert_mixins/TestFsMixin/sample_thingy_folder/thing» exist"):
            self.fsTc.assertPathNotExists("/tmp/unit_testing_assert_mixins/TestFsMixin/sample_thingy_folder/thing")
        self.fsTc.assertPathNotExists("/tmp/unit_testing_assert_mixins/TestFsMixin/non_existing_entry")
    
    def test_assertIsFile(self):
        """
        Method assertIsFile() must fail if and only if the provided path does not represent a regular file.
        """
        with self.assertRaisesRegex(ValueError, r"Function assertIsFile\(\) was called with the non-string «0»"):
            self.fsTc.assertIsFile(0)
        with self.assertRaisesRegex(AssertionError, r"False is not true : Path «/tmp/unit_testing_assert_mixins/TestFsMixin/non_existing_entry» does not even exist"):
            self.fsTc.assertIsFile("/tmp/unit_testing_assert_mixins/TestFsMixin/non_existing_entry")
        with self.assertRaisesRegex(AssertionError, r"False is not true : Path «/tmp/unit_testing_assert_mixins/TestFsMixin/sample_empty_folder» is not a regular file"):
            self.fsTc.assertIsFile("/tmp/unit_testing_assert_mixins/TestFsMixin/sample_empty_folder")
        with self.assertRaisesRegex(AssertionError, r"False is not true : Path «/tmp/unit_testing_assert_mixins/TestFsMixin/sample_thingy_folder» is not a regular file"):
            self.fsTc.assertIsFile("/tmp/unit_testing_assert_mixins/TestFsMixin/sample_thingy_folder")
        self.fsTc.assertIsFile("/tmp/unit_testing_assert_mixins/TestFsMixin/sample_thingy_folder/thing")
    
    def test_assertIsDirectory(self):
        """
        Method assertIsDirectory() must fail if and only if the provided path does not represent a directory.
        """
        with self.assertRaisesRegex(ValueError, r"Function assertIsDirectory\(\) was called with the non-string «0»"):
            self.fsTc.assertIsDirectory(0)
        with self.assertRaisesRegex(AssertionError, r"False is not true : Path «/tmp/unit_testing_assert_mixins/TestFsMixin/non_existing_entry» does not even exist"):
            self.fsTc.assertIsFile("/tmp/unit_testing_assert_mixins/TestFsMixin/non_existing_entry")
        with self.assertRaisesRegex(AssertionError, r"False is not true : Path «/tmp/unit_testing_assert_mixins/TestFsMixin/sample_thingy_folder/thing» is not a directory"):
            self.fsTc.assertIsDirectory("/tmp/unit_testing_assert_mixins/TestFsMixin/sample_thingy_folder/thing")
        self.fsTc.assertIsDirectory("/tmp/unit_testing_assert_mixins/TestFsMixin/sample_empty_folder")
        self.fsTc.assertIsDirectory("/tmp/unit_testing_assert_mixins/TestFsMixin/sample_thingy_folder")
    
    ############################################################
    ############################################################
    ############################################################
    @classmethod
    def setUpClass(self):
        FsTestCase = type("FsTestCase", (
            unittest.TestCase,
            assert_mixins.FsMixin,
            ), {})
        self.fsTc = FsTestCase()
        ### Create some files and folders for testing:
        # The shell:
        if os.path.exists("/tmp/unit_testing_assert_mixins/TestFsMixin"):
            shutil.rmtree("/tmp/unit_testing_assert_mixins/TestFsMixin", ignore_errors=False, onerror=None)
        os.makedirs("/tmp/unit_testing_assert_mixins/TestFsMixin", exist_ok=True)
        # The contents:
        os.makedirs("/tmp/unit_testing_assert_mixins/TestFsMixin/sample_empty_folder", exist_ok=True)
        os.makedirs("/tmp/unit_testing_assert_mixins/TestFsMixin/sample_thingy_folder", exist_ok=True)
        with open("/tmp/unit_testing_assert_mixins/TestFsMixin/sample_thingy_folder/thing", "w") as conts:
            conts.write("papapa")
