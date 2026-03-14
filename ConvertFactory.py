from ConvertStrategy import (
    ConvertStrategy, PngStrategy
)


# --- Factory ---

class ConvertFactory:
    @staticmethod
    def create(format: str) -> ConvertStrategy:
        strategies = {
            "png": PngStrategy,
        }
        if format not in strategies:
            raise ValueError(f"Unknown format: '{format}'")
        return strategies[format]()