import unittest
from unittest.mock import patch, Mock
from listings import get_properties

class TestGetProperties(unittest.TestCase):
    
    def test_invalid_address_type(self):
        """Test that non-string address raises ValueError"""
        with self.assertRaises(ValueError):
            get_properties(123, 10)

    def test_invalid_coordinates(self):
        """Test that invalid coordinate types raise ValueError"""
        with self.assertRaises(ValueError):
            get_properties("Bangalore", 10, "12.9716", 77.5946)
        with self.assertRaises(ValueError):
            get_properties("Bangalore", 10, 12.9716, "77.5946")

    @patch('listings.build_headers')
    @patch('listings.build_search_body')
    @patch('listings.fetch_from_api')
    @patch('listings.extract_listing_data')
    def test_successful_property_fetch(self, mock_extract, mock_fetch, mock_build_body, mock_headers):
        """Test successful property fetch with valid parameters"""
        # Setup mock returns
        mock_headers.return_value = {"mock": "headers"}
        mock_build_body.return_value = {"mock": "payload"}
        mock_fetch.return_value = {"mock": "response"}
        mock_extract.return_value = [["1", "Test Property", "Test Page", "100"]]
        
        # Test with just address
        result = get_properties("Silvassa", 30)
        
        # Verify all mocks were called correctly
        mock_headers.assert_called_once()
        mock_build_body.assert_called_once_with(
            "Silvassa", 30, "2025-03-27", "2025-03-29", None, None
        )
        mock_fetch.assert_called_once()
        mock_extract.assert_called_once()
        
        # Verify the result
        self.assertEqual(result, [["1", "Test Property", "Test Page", "100"]])

    @patch('listings.build_headers')
    @patch('listings.build_search_body')
    @patch('listings.fetch_from_api')
    @patch('listings.extract_listing_data')
    def test_property_fetch_with_coordinates(self, mock_extract, mock_fetch, mock_build_body, mock_headers):
        """Test property fetch with coordinates"""
        # Setup mock returns
        mock_headers.return_value = {"mock": "headers"}
        mock_build_body.return_value = {"mock": "payload"}
        mock_fetch.return_value = {"mock": "response"}
        mock_extract.return_value = [["1", "Test Property", "Test Page", "100"]]
        
        # Test with coordinates
        result = get_properties("Bangalore", 20, 12.9716, 77.5946)
        
        # Verify build_search_body was called with coordinates
        mock_build_body.assert_called_once_with(
            "Bangalore", 20, "2025-03-27", "2025-03-29", 12.9716, 77.5946
        )
        
        # Verify the result
        self.assertEqual(result, [["1", "Test Property", "Test Page", "100"]])

if __name__ == '__main__':
    unittest.main()