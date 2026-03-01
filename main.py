#TO DO: remove .claude folder, .git folder, .gitignore file, readme.md file, claude.md file, and all files from exports folder

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
def main_without_design():
    formats = ["txt", "csv", "json", "markdown", "html", "ini", "svg", "rtf", "xml"]
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
    elif format == "ini":
        export.export_ini(document)
    elif format == "svg":
        export.export_svg(document)
    elif format == "rtf":
        export.export_rtf(document)
    elif format == "xml":
        export.export_xml(document)

if __name__ == "__main__":
    main_without_design()