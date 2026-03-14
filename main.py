import os
import export
from ConvertFactory import ConvertFactory
from ConvertStrategy import FileConverter

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

# --- FILE CONVERSION IMPLEMENTATION ---
def main_convert():
    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    ext_aliases = {"jpeg": "jpg"}

    files = [f for f in os.listdir("input") if os.path.isfile(os.path.join("input", f))]
    if not files:
        print("No files found in input/ folder.")
        return

    extensions = set()
    for f in files:
        ext = os.path.splitext(f)[1].lower().lstrip(".")
        ext = ext_aliases.get(ext, ext)
        if ext:
            extensions.add(ext)

    conversions = []
    for ext in sorted(extensions):
        targets = ConvertFactory.get_targets(ext)
        for target in targets:
            conversions.append((ext, target))

    if not conversions:
        print("No supported conversions available for the files in input/.")
        return

    print("\nAvailable conversions:")
    for i, (source, target) in enumerate(conversions, 1):
        print(f"  {i}. {source} -> {target}")

    choice = input("\nSelect a conversion (enter number): ").strip()
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(conversions):
        print(f"Invalid choice. Please enter a number between 1 and {len(conversions)}.")
        choice = input("Select a conversion (enter number): ").strip()

    source_ext, target_ext = conversions[int(choice) - 1]
    strategy = ConvertFactory.create(source_ext, target_ext)
    converter = FileConverter(strategy)

    for f in files:
        ext = os.path.splitext(f)[1].lower().lstrip(".")
        ext = ext_aliases.get(ext, ext)
        if ext == source_ext:
            converter.convert(os.path.join("input", f))

if __name__ == "__main__":
    #TODO: remove old export related classes, functions, files, etc. (ex: ExportFactory class, export.py file, etc.)
    #TODO: create unit test(s) to verify factory pattern output based on input format
    # main_without_design_patterns()
    # main_with_design_patterns()
    main_convert()