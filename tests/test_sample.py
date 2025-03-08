import unittest
from unittest.mock import patch

import pytest

import yrs_commons
from yrs_commons.sample_main import MyClass, my_function
from yrs_commons.sample import utility_function

def test_imports():
    """Test that all expected functions and classes are importable."""
    from yrs_commons import MyClass, my_function, utility_function
    
    # Test that imported items are of correct type
    assert isinstance(MyClass(), MyClass)
    assert callable(my_function)
    assert callable(utility_function)


@pytest.mark.unit
class TestMyPackage(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.my_class = MyClass()
    
    def test_version(self):
        """Test if version is correctly set."""
        self.assertEqual(yrs_commons.__version__, "0.1.0")
    
    def test_my_class(self):
        """Test MyClass initialization and methods."""
        # Test initialization
        self.assertIsInstance(self.my_class, MyClass)
        self.assertEqual(self.my_class.value, "Hello from MyClass!")
        
        # Test greet method
        self.assertEqual(self.my_class.greet(), "Hello from MyClass!")
    
    def test_my_function(self):
        """Test my_function returns correct string."""
        self.assertEqual(my_function(), "Hello from my_function!")
    
    def test_utility_function(self):
        """Test utility_function returns correct string."""
        self.assertEqual(utility_function(), "This is a utility function")

@pytest.mark.unit
class TestCommandLine(unittest.TestCase):
    @patch('builtins.print')
    def test_main_function(self, mock_print):
        """Test the command-line interface."""
        from yrs_commons.sample_main import main
        main()
        mock_print.assert_called_with("This runs when package is called from command line")

# Additional test cases for edge cases and error handling
@pytest.mark.unit
class TestEdgeCases(unittest.TestCase):
    def test_my_class_attribute_modification(self):
        """Test that MyClass attributes can be modified."""
        obj = MyClass()
        obj.value = "Modified value"
        self.assertEqual(obj.greet(), "Modified value")
    
    def test_multiple_instances(self):
        """Test that multiple instances of MyClass are independent."""
        obj1 = MyClass()
        obj2 = MyClass()
        
        obj1.value = "Modified value"
        self.assertEqual(obj1.greet(), "Modified value")
        self.assertEqual(obj2.greet(), "Hello from MyClass!")

# Integration tests
@pytest.mark.integration
class TestIntegration(unittest.TestCase):
    def test_full_workflow(self):
        """Test a complete workflow using multiple package components."""
        # Create instance and modify it
        obj = MyClass()
        self.assertEqual(obj.greet(), "Hello from MyClass!")
        
        # Use standalone function
        self.assertEqual(my_function(), "Hello from my_function!")
        
        # Use utility function
        self.assertEqual(utility_function(), "This is a utility function")
