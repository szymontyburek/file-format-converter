import os
from strategy_pattern import (
    ExportStrategy,
    TxtStrategy, CsvStrategy, JsonStrategy, MarkdownStrategy,
    HtmlStrategy, IniStrategy, SvgStrategy, RtfStrategy, XmlStrategy,
    DocumentExporter,
    document
)


# --- Factory ---

class ExportStrategyFactory:
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


# --- Main ---

def main():
    formats = ["txt", "csv", "json", "markdown", "html", "ini", "svg", "rtf", "xml"]
    format = input(f"Enter export format ({', '.join(formats)}): ").strip().lower()
    while format not in formats:
        print(f"Invalid format: '{format}'. Please enter one of: {', '.join(formats)}.")
        format = input(f"Enter export format ({', '.join(formats)}): ").strip().lower()

    os.makedirs("exports", exist_ok=True)
    strategy = ExportStrategyFactory.create(format)  # Factory decides WHAT to create
    exporter = DocumentExporter(strategy)             # Strategy decides HOW to export
    exporter.export(document)


if __name__ == "__main__":
    main()
