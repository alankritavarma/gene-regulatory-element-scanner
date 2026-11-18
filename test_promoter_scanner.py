import unittest
from promoter_scanner import clean_sequence, is_valid, find_positions, get_gc_content


class ScannerTests(unittest.TestCase):
    def test_clean_sequence(self):
        self.assertEqual(clean_sequence(" atg c "), "ATGC")

    def test_valid_sequence(self):
        self.assertTrue(is_valid("ATGC"))
        self.assertFalse(is_valid("ATGN"))

    def test_find_positions(self):
        self.assertEqual(find_positions("TATATATA", "TATA"), [1, 3, 5])

    def test_gc_content(self):
        self.assertEqual(get_gc_content("ATGC"), 50.0)


if __name__ == "__main__":
    unittest.main()
