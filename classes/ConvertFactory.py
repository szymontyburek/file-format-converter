"""
Factory module for image file conversions.

Maps (source_format, target_format) pairs to the appropriate ConvertStrategy
concrete class using the Factory design pattern.
"""

from classes.ConvertStrategy import (
    ConvertStrategy,
    PngToJpgStrategy, JpgToPngStrategy,
    WebpToPngStrategy, WebpToJpgStrategy,
    PngToWebpStrategy, JpgToWebpStrategy,
    GifToPngStrategy, GifToJpgStrategy,
    PngToGifStrategy, JpgToGifStrategy,
    BmpToPngStrategy, BmpToJpgStrategy,
    PngToBmpStrategy, JpgToBmpStrategy,
    HtmlToPdfStrategy,
)


# --- Factory ---

class ConvertFactory:
    """Factory that creates the appropriate conversion strategy for a given source/target pair."""

    # Maps (source_ext, target_ext) tuples to their corresponding strategy classes
    _strategies = {
        ("png", "jpg"): PngToJpgStrategy,
        ("jpg", "png"): JpgToPngStrategy,
        ("webp", "png"): WebpToPngStrategy,
        ("webp", "jpg"): WebpToJpgStrategy,
        ("png", "webp"): PngToWebpStrategy,
        ("jpg", "webp"): JpgToWebpStrategy,
        ("gif", "png"): GifToPngStrategy,
        ("gif", "jpg"): GifToJpgStrategy,
        ("png", "gif"): PngToGifStrategy,
        ("jpg", "gif"): JpgToGifStrategy,
        ("bmp", "png"): BmpToPngStrategy,
        ("bmp", "jpg"): BmpToJpgStrategy,
        ("png", "bmp"): PngToBmpStrategy,
        ("jpg", "bmp"): JpgToBmpStrategy,
        ("html", "pdf"): HtmlToPdfStrategy,
    }

    @staticmethod
    def create(source_format: str, target_format: str) -> ConvertStrategy:
        """Create and return a ConvertStrategy instance for the given conversion pair.

        Args:
            source_format: The source file extension (e.g., "png").
            target_format: The target file extension (e.g., "jpg").

        Returns:
            ConvertStrategy: An instance of the appropriate concrete strategy.

        Raises:
            ValueError: If the source/target pair is not supported.
        """
        key = (source_format, target_format)
        if key not in ConvertFactory._strategies:
            raise ValueError(f"Unsupported conversion: '{source_format}' -> '{target_format}'")
        return ConvertFactory._strategies[key]()

    @staticmethod
    def get_available_formats(source_format: str) -> list:
        """Return a list of valid target formats for the given source format.

        Args:
            source_format: The source file extension (e.g., "png").

        Returns:
            list: Target format strings available for conversion (e.g., ["jpg", "webp", "gif", "bmp"]).
        """
        targets = []
        for source, target in ConvertFactory._strategies:
            if source == source_format:
                targets.append(target)
        return targets
