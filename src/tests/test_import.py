import unittest
import sys
import os

class TestImport(unittest.TestCase):
    
    def test_can_import_pomerium_client(self):
        """Test that pomerium.client package can be imported from src."""
        # # Add the src directory to the path if not already there
        # src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
        # if src_path not in sys.path:
        #     sys.path.insert(0, src_path)
        
        try:
            import pomerium.client
            # If we get here, the import succeeded
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Failed to import pomerium.client: {e}")
            
if __name__ == "__main__":
    unittest.main()
