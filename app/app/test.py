"""
Unit tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test the add function."""
        result = calc.add(5, 6)

        self.assertEqual(result, 11)

    def test_substract_number(self):
        """Teste the substract function"""
        result = calc.substract(10, 15)

        self.assertEqual(result, 5)
