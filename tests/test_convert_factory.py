"""Unit tests for ConvertFactory.get_available_formats()."""

import unittest
from classes.ConvertFactory import ConvertFactory


class TestGetTargets(unittest.TestCase):
    """Verify that get_available_formats() returns the correct target formats for each source format."""

    def test_png_targets(self):
        targets = ConvertFactory.get_available_formats("png")
        self.assertEqual(targets, ["jpg", "webp", "gif", "bmp"])

    def test_jpg_targets(self):
        targets = ConvertFactory.get_available_formats("jpg")
        self.assertEqual(targets, ["png", "webp", "gif", "bmp"])

    def test_webp_targets(self):
        targets = ConvertFactory.get_available_formats("webp")
        self.assertEqual(targets, ["png", "jpg"])

    def test_gif_targets(self):
        targets = ConvertFactory.get_available_formats("gif")
        self.assertEqual(targets, ["png", "jpg"])

    def test_bmp_targets(self):
        targets = ConvertFactory.get_available_formats("bmp")
        self.assertEqual(targets, ["png", "jpg"])

    def test_html_targets(self):
        targets = ConvertFactory.get_available_formats("html")
        self.assertEqual(targets, ["pdf", "docx"])

    def test_unsupported_format(self):
        targets = ConvertFactory.get_available_formats("tiff")
        self.assertEqual(targets, [])


if __name__ == "__main__":
    unittest.main()
