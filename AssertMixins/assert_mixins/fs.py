# -*- coding: utf-8 -*-
import os

class FsMixin:
    """
    Filesystem-related assertions.
    """
    
    def assertIsFile(self, path, msg=None):
        """
        Asserts() that a given value represents the path of a regular file.
        """
        if not isinstance(path, str):
            raise ValueError(f"Function assertIsFile() was called with the non-string «{repr(path)}».")
        self.assertTrue(os.path.exists(path), msg=msg or f"Path «{path}» does not even exist.")
        self.assertTrue(os.path.isfile(path), msg=msg or f"Path «{path}» is not a regular file!")
    
    def assertIsDirectory(self, path, msg=None):
        """
        Asserts() that a given value represents the path of a directory.
        """
        if not isinstance(path, str):
            raise ValueError(f"Function assertIsDirectory() was called with the non-string «{repr(path)}».")
        self.assertTrue(os.path.exists(path), msg=msg or f"Path «{path}» does not even exist.")
        self.assertTrue(os.path.isdir(path), msg=msg or f"Path «{path}» is not a directory!")
