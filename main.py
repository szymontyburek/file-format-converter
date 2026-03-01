import export

document = {
    "title": "Monthly Yield Report",
    "author": "John Doe",
    "rows": [
        ["Location", "Total", "Passed", "Rejected", "Yield"],
        ["AZ",        93234,   81387,    11847,      "87.2%"],
        ["CA",        59712,   48975,    10737,      "82.0%"]
    ]
}

# --- NO DESIGN PATTERN IMPLEMENTATION ---
def main_without_design_patterns():
    formats = ["txt", "csv", "json", "markdown", "html", "svg", "rtf", "xml"]
    format = input(f"Enter export format ({', '.join(formats)}): ").strip().lower()
    while format not in formats:
        print(f"Invalid format: '{format}'. Please enter one of: {', '.join(formats)}.")
        format = input(f"Enter export format ({', '.join(formats)}): ").strip().lower()

    if format == "txt":
        export.export_txt(document)
    elif format == "csv":
        export.export_csv(document)
    elif format == "json":
        export.export_json(document)
    elif format == "markdown":
        export.export_markdown(document)
    elif format == "html":
        export.export_html(document)
    elif format == "svg":
        export.export_svg(document)
    elif format == "rtf":
        export.export_rtf(document)
    elif format == "xml":
        export.export_xml(document)

# --- DESIGN PATTERN IMPLEMENTATION ---
from factory_pattern import ExportFactory
from strategy_pattern import DocumentExporter
def main_with_design_patterns():
    formats = ["txt", "csv", "json", "markdown", "html", "svg", "rtf", "xml"]
    format = input(f"Enter export format ({', '.join(formats)}): ").strip().lower()
    while format not in formats:
        print(f"Invalid format: '{format}'. Please enter one of: {', '.join(formats)}.")
        format = input(f"Enter export format ({', '.join(formats)}): ").strip().lower()

    strategy = ExportFactory.create(format)  # Factory decides WHAT to create
    exporter = DocumentExporter(strategy) # Strategy decides HOW to export
    exporter.export(document)

if __name__ == "__main__":
    # main_without_design_patterns()
    main_with_design_patterns()