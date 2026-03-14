from ConvertStrategy import (
    ConvertStrategy,
    PngToJpgStrategy, JpgToPngStrategy,
    WebpToPngStrategy, WebpToJpgStrategy,
    PngToWebpStrategy, JpgToWebpStrategy,
    GifToPngStrategy, GifToJpgStrategy,
    PngToGifStrategy, JpgToGifStrategy,
    BmpToPngStrategy, BmpToJpgStrategy,
    PngToBmpStrategy, JpgToBmpStrategy,
)


# --- Factory ---

class ConvertFactory:
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
    }

    @staticmethod
    def create(source_format: str, target_format: str) -> ConvertStrategy:
        key = (source_format, target_format)
        if key not in ConvertFactory._strategies:
            raise ValueError(f"Unsupported conversion: '{source_format}' -> '{target_format}'")
        return ConvertFactory._strategies[key]()

    @staticmethod
    def get_targets(source_format: str) -> list:
        return [target for source, target in ConvertFactory._strategies if source == source_format]
