"""
Strategy module for image file conversions.

Defines the abstract ConvertStrategy base class and 15 concrete strategy
implementations for converting between image formats (PNG, JPG, WEBP, GIF, BMP)
and documents (HTML → PDF, HTML → DOCX).
Uses the Strategy design pattern to encapsulate each conversion algorithm.
"""

from abc import ABC, abstractmethod
from PIL import Image
from pathlib import Path
from playwright.sync_api import sync_playwright
from htmldocx import HtmlToDocx
from docx import Document
import vtracer
import os

os.makedirs("output", exist_ok=True)

# --- Abstract Strategy ---

class ConvertStrategy(ABC):
    """Abstract base class for all image conversion strategies."""

    @abstractmethod
    def convert(self, input_path):
        """Convert an image file at the given path to a new format.

        Args:
            input_path: Path to the source image file.
        """
        pass


# --- Concrete Strategies ---

class PngToJpgStrategy(ConvertStrategy):
    """Converts PNG images to JPG format."""
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.jpg"
        img.convert("RGB").save(output_path)
        print(f"Converted {input_path} → {output_path}")


class JpgToPngStrategy(ConvertStrategy):
    """Converts JPG images to PNG format."""
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.png"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class WebpToPngStrategy(ConvertStrategy):
    """Converts WEBP images to PNG format."""
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.png"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class WebpToJpgStrategy(ConvertStrategy):
    """Converts WEBP images to JPG format."""
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.jpg"
        img.convert("RGB").save(output_path)
        print(f"Converted {input_path} → {output_path}")


class PngToWebpStrategy(ConvertStrategy):
    """Converts PNG images to WEBP format."""
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.webp"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class JpgToWebpStrategy(ConvertStrategy):
    """Converts JPG images to WEBP format."""
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.webp"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class GifToPngStrategy(ConvertStrategy):
    """Converts GIF images to PNG format."""
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.png"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class GifToJpgStrategy(ConvertStrategy):
    """Converts GIF images to JPG format."""
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.jpg"
        img.convert("RGB").save(output_path)
        print(f"Converted {input_path} → {output_path}")


class PngToGifStrategy(ConvertStrategy):
    """Converts PNG images to GIF format."""
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.gif"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class JpgToGifStrategy(ConvertStrategy):
    """Converts JPG images to GIF format."""
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.gif"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class BmpToPngStrategy(ConvertStrategy):
    """Converts BMP images to PNG format."""
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.png"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class BmpToJpgStrategy(ConvertStrategy):
    """Converts BMP images to JPG format."""
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.jpg"
        img.convert("RGB").save(output_path)
        print(f"Converted {input_path} → {output_path}")


class PngToBmpStrategy(ConvertStrategy):
    """Converts PNG images to BMP format."""
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.bmp"
        img.convert("RGB").save(output_path)
        print(f"Converted {input_path} → {output_path}")


class JpgToBmpStrategy(ConvertStrategy):
    """Converts JPG images to BMP format."""
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.bmp"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class PngToSvgStrategy(ConvertStrategy):
    """Converts PNG images to SVG format using vtracer vectorization."""
    def convert(self, input_path):
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.svg"
        vtracer.convert_image_to_svg_py(
            input_path,
            output_path,
            colormode="color",
            filter_speckle=4,
            color_precision=6,
            corner_threshold=60,
            mode="polygon",
        )
        print(f"Converted {input_path} → {output_path}")


class HtmlToPdfStrategy(ConvertStrategy):
    """Converts HTML files to PDF format using a headless Chromium browser."""
    def convert(self, input_path):
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.pdf"
        file_uri = Path(input_path).resolve().as_uri()
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(file_uri, wait_until="networkidle")
            page.pdf(path=output_path)
            browser.close()
        print(f"Converted {input_path} → {output_path}")


class HtmlToDocxStrategy(ConvertStrategy):
    """Converts HTML files to DOCX (Microsoft Word) format."""
    def convert(self, input_path):
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.docx"
        with open(input_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        doc = Document()
        parser = HtmlToDocx()
        parser.add_html_to_document(html_content, doc)
        doc.save(output_path)
        print(f"Converted {input_path} → {output_path}")


# --- Context ---

class FileConverter:
    """Context class that delegates file conversion to a ConvertStrategy.

    Uses the Strategy pattern to decouple the conversion algorithm
    from the code that invokes it.
    """

    def __init__(self, strategy: ConvertStrategy):
        """Initialize with a specific conversion strategy.

        Args:
            strategy: A ConvertStrategy instance that defines the conversion behavior.
        """
        self.strategy = strategy

    def convert(self, input_path):
        """Convert the file at input_path using the assigned strategy.

        Args:
            input_path: Path to the source image file.
        """
        self.strategy.convert(input_path)
