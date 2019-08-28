import unittest

class MyTestCase(unittest.TestCase) :
    
    @unittest.skip("demonstrating skipping")
    def test_nothing(self) :
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1,3),"not support in this version")

    def test_format(self) :
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self) :
        pass
    
    def test_maybe_skipped(self) :
        if not external_resource_available() :
            self.skipTest("external resource not available")
        pass