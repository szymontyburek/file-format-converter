import os
from strategy_pattern import (
    ExportStrategy,
    TxtStrategy, CsvStrategy, JsonStrategy, MarkdownStrategy,
    HtmlStrategy, IniStrategy, SvgStrategy, RtfStrategy, XmlStrategy
)


# --- Factory ---

class ExportFactory:
    @staticmethod
    def create(format: str) -> ExportStrategy:
        strategies = {
            "txt":      TxtStrategy,
            "csv":      CsvStrategy,
            "json":     JsonStrategy,
            "markdown": MarkdownStrategy,
            "html":     HtmlStrategy,
            "ini":      IniStrategy,
            "svg":      SvgStrategy,
            "rtf":      RtfStrategy,
            "xml":      XmlStrategy,
        }
        if format not in strategies:
            raise ValueError(f"Unknown format: '{format}'")
        return strategies[format]()