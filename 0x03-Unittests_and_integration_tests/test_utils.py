#!/usr/bin/env python3
"""Defines test classes to test fuctions in ./utils."""
import unittest
from unittest.mock import patch, Mock
from utils import get_json
from utils import memoize
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """"Unittest for the function utils.access_nested_map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function returns the expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    @parameterized.expand(
        [
            ({}, ("a",), "KeyError('a')")
            ({"a": 1}, ("a", "b"), "KeyError('b')")
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """"Test access_neste_map raises KeyError for none existing keys"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(repr(e.exception), expected)


class TestGetJson(unittest.TestCase):
    """implement the TestGetJson.test_get_json method to test that utils.get_json"""

    @parameterized.expand(
        [
            ('http://example.com', {"payload": True}),
            ('http://holberton.io', {"payload": False})
        ]
    )
    def test_get_json(self, url, expected):
        """Test that returns the expected result"""
        res_mock = Mock()
        res_mock.json.return_value = expected
        with patch('requests.get', return_value=res_mock):
            self.assertEqual(get_json(url), expected)
            res_mock.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Unittest for function util.memoize"""

    def test_memoize(self):
        """Test the function util.memoize"""

        class TestClass:

            def a_method(self):
                """Returns 42"""
                return 42
            
            @memoize
            def a_property(self):
                """Returns memopized property"""
                return self.a_method()
        
        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            obj = TestClass()
            obj.a_property
            obj.a_property
            mocked.assert_called_once()