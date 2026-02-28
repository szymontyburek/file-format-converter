#TO DO: remove .claude folder, .git folder, .gitignore file, readme.md file, claude.md file, and all files from exports folder

import os
from factory_pattern import ExportFactory
from strategy_pattern import DocumentExporter

document = {
    "title": "Monthly Yield Report",
    "author": "John Doe",
    "rows": [
        ["Location", "Total", "Passed", "Rejected", "Yield"],
        ["AZ",        93234,   81387,    11847,      "87.2%"],
        ["CA",        59712,   48975,    10737,      "82.0%"]
    ]
}

def main():
    formats = ["txt", "csv", "json", "markdown", "html", "ini", "svg", "rtf", "xml"]
    format = input(f"Enter export format ({', '.join(formats)}): ").strip().lower()
    while format not in formats:
        print(f"Invalid format: '{format}'. Please enter one of: {', '.join(formats)}.")
        format = input(f"Enter export format ({', '.join(formats)}): ").strip().lower()

    os.makedirs("exports", exist_ok=True)
    strategy = ExportFactory.create(format)  # Factory decides WHAT to create
    exporter = DocumentExporter(strategy) # Strategy decides HOW to export
    exporter.export(document)


if __name__ == "__main__":
    main()
