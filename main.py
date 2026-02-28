import os
import csv
import json
import configparser
import xml.etree.ElementTree as ET

document = {
    "title": "Monthly Yield Report",
    "author": "John Doe",
    "rows": [
        ["Location", "Total", "Passed", "Rejected", "Yield"],
        ["AZ",        93234,   81387,    11847,      "87.2%"],
        ["CA",        59712,   48975,    10737,      "82.0%"]
    ]
}

def export_txt(document):
    filename = f"exports/{document['title']}.txt"
    with open(filename, "w") as f:
        f.write("=== TXT EXPORT ===\n")
        f.write(f"Title:  {document['title']}\n")
        f.write(f"Author: {document['author']}\n")
        f.write("-" * 40 + "\n")
        for row in document["rows"]:
            f.write("  |  ".join(str(cell).ljust(12) for cell in row) + "\n")
        f.write("=" * 40 + "\n")
    print(f"Exported TXT to {filename}")


def export_csv(document):
    filename = f"exports/{document['title']}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        for row in document["rows"]:
            writer.writerow(row)
    print(f"Exported CSV to {filename}")

def export_json(document):
    filename = f"exports/{document['title']}.json"
    with open(filename, "w") as f:
        json.dump(document, f, indent=2)
    print(f"Exported JSON to {filename}")


def export_markdown(document):
    filename = f"exports/{document['title']}.md"
    with open(filename, "w") as f:
        rows = document["rows"]
        header = rows[0]
        f.write("| " + " | ".join(str(cell) for cell in header) + " |\n")
        f.write("| " + " | ".join("---" for _ in header) + " |\n")
        for row in rows[1:]:
            f.write("| " + " | ".join(str(cell) for cell in row) + " |\n")
    print(f"Exported Markdown to {filename}")


def export_html(document):
    filename = f"exports/{document['title']}.html"
    with open(filename, "w") as f:
        rows = document["rows"]
        f.write(f"<!DOCTYPE html>\n<html>\n<head><title>{document['title']}</title></head>\n<body>\n")
        f.write(f"<h1>{document['title']}</h1>\n<p>Author: {document['author']}</p>\n")
        f.write("<table border='1'>\n<thead>\n<tr>")
        for cell in rows[0]:
            f.write(f"<th>{cell}</th>")
        f.write("</tr>\n</thead>\n<tbody>\n")
        for row in rows[1:]:
            f.write("<tr>")
            for cell in row:
                f.write(f"<td>{cell}</td>")
            f.write("</tr>\n")
        f.write("</tbody>\n</table>\n</body>\n</html>")
    print(f"Exported HTML to {filename}")


def export_ini(document):
    filename = f"exports/{document['title']}.ini"
    config = configparser.ConfigParser()
    config["metadata"] = {"title": document["title"], "author": document["author"]}
    header = document["rows"][0]
    for i, row in enumerate(document["rows"][1:]):
        config[f"row_{i}"] = {str(header[j]): str(row[j]) for j in range(len(header))}
    with open(filename, "w") as f:
        config.write(f)
    print(f"Exported INI to {filename}")


def export_svg(document):
    filename = f"exports/{document['title']}.svg"
    rows = document["rows"]
    col_w, row_h, pad = 120, 30, 8
    width = col_w * len(rows[0])
    height = row_h * len(rows)
    with open(filename, "w") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">\n')
        for r, row in enumerate(rows):
            for c, cell in enumerate(row):
                x, y = c * col_w, r * row_h
                fill = "#4a90d9" if r == 0 else ("#f0f0f0" if r % 2 == 0 else "#ffffff")
                text_color = "white" if r == 0 else "black"
                f.write(f'  <rect x="{x}" y="{y}" width="{col_w}" height="{row_h}" fill="{fill}" stroke="#999"/>\n')
                f.write(f'  <text x="{x + pad}" y="{y + row_h - pad}" font-size="12" fill="{text_color}">{cell}</text>\n')
        f.write("</svg>")
    print(f"Exported SVG to {filename}")


def export_rtf(document):
    filename = f"exports/{document['title']}.rtf"
    rows = document["rows"]
    with open(filename, "w") as f:
        f.write("{\\rtf1\\ansi\n")
        f.write(f"{{\\b {document['title']}}}\\par\n")
        f.write(f"Author: {document['author']}\\par\n\\par\n")
        for i, row in enumerate(rows):
            line = "  |  ".join(str(cell) for cell in row)
            if i == 0:
                f.write(f"{{\\b {line}}}\\par\n")
            else:
                f.write(f"{line}\\par\n")
        f.write("}")
    print(f"Exported RTF to {filename}")


def export_xml(document):
    filename = f"exports/{document['title']}.xml"
    root = ET.Element("document")
    metadata = ET.SubElement(root, "metadata")
    ET.SubElement(metadata, "title").text = document["title"]
    ET.SubElement(metadata, "author").text = document["author"]
    rows_el = ET.SubElement(root, "rows")
    header = document["rows"][0]
    for row in document["rows"][1:]:
        row_el = ET.SubElement(rows_el, "row")
        for i, cell in enumerate(row):
            ET.SubElement(row_el, str(header[i]).replace(" ", "_")).text = str(cell)
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(filename, encoding="unicode", xml_declaration=True)
    print(f"Exported XML to {filename}")

#TO DO: create seperate files that contain logic in main.py with strategy and factory design patterns. create a different file for each design pattern
#TO DO: remove .claude folder, .git folder, readme.md, claude.md file, and all files from exports folder

def main():
    formats = ["txt", "csv", "json", "markdown", "html", "ini", "svg", "rtf", "xml"]
    format = input(f"Enter export format ({', '.join(formats)}): ").strip().lower()
    while format not in formats:
        print(f"Invalid format: '{format}'. Please enter one of: {', '.join(formats)}.")
        format = input(f"Enter export format ({', '.join(formats)}): ").strip().lower()

    if format == "txt":
        export_txt(document)
    elif format == "csv":
        export_csv(document)
    elif format == "json":
        export_json(document)
    elif format == "markdown":
        export_markdown(document)
    elif format == "html":
        export_html(document)
    elif format == "ini":
        export_ini(document)
    elif format == "svg":
        export_svg(document)
    elif format == "rtf":
        export_rtf(document)
    elif format == "xml":
        export_xml(document)

if __name__ == "__main__":
    main()