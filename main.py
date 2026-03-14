"""
Main entry point for the image file conversion tool.

Scans the input/ folder for image files, presents available conversion
options to the user, and converts the selected files to the output/ folder.
"""

import os
from ConvertFactory import ConvertFactory
from ConvertStrategy import FileConverter

# Maps alternative extensions to their canonical form
EXT_ALIASES = {"jpeg": "jpg"}

def get_input_files():
    """Ensure input/ and output/ directories exist and return a list of files in input/.

    Returns:
        list: Filenames found in the input/ directory (empty list if none).
    """
    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    files = [f for f in os.listdir("input") if os.path.isfile(os.path.join("input", f))]
    if not files:
        print("No files found in input/ folder.")
    return files

def get_available_conversions(files):
    """Determine which conversions are available based on the file types present.

    Extracts unique file extensions from the input files, normalizes them
    using EXT_ALIASES, and queries the ConvertFactory for supported target formats.

    Args:
        files: List of filenames from the input/ directory.

    Returns:
        list: Tuples of (source_ext, target_ext) representing available conversions.
    """
    extensions = set()
    for f in files:
        ext = os.path.splitext(f)[1].lower().lstrip(".")
        ext = EXT_ALIASES.get(ext, ext)  # Normalize alias (e.g., "jpeg" -> "jpg"), or keep as-is
        if ext:
            extensions.add(ext)

    conversions = []
    for ext in sorted(extensions):
        targets = ConvertFactory.get_targets(ext)
        for target in targets:
            conversions.append((ext, target))

    if not conversions:
        print("No supported conversions available for the files in input/.")
    return conversions

def prompt_conversion_choice(conversions):
    """Display available conversions and prompt the user to select one.

    Shows a numbered list of source -> target conversion options and
    validates the user's input until a valid selection is made.

    Args:
        conversions: List of (source_ext, target_ext) tuples.

    Returns:
        tuple: The selected (source_ext, target_ext) pair.
    """
    print("\nAvailable conversions:")
    for i, (source, target) in enumerate(conversions, 1):
        print(f"  {i}. {source} -> {target}")

    choice = input("\nSelect a conversion (enter number): ").strip()
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(conversions):
        print(f"Invalid choice. Please enter a number between 1 and {len(conversions)}.")
        choice = input("Select a conversion (enter number): ").strip()

    return conversions[int(choice) - 1]

def convert_files(files, source_ext, target_ext):
    """Convert all files matching source_ext to the target format.

    Uses the Factory pattern to obtain the appropriate conversion strategy
    and the Strategy pattern to execute the conversion for each matching file.

    Args:
        files: List of filenames from the input/ directory.
        source_ext: The source file extension to filter by (e.g., "png").
        target_ext: The desired target file extension (e.g., "jpg").
    """
    strategy = ConvertFactory.create(source_ext, target_ext)  # Factory decides WHAT strategy to create
    converter = FileConverter(strategy)  # Strategy decides HOW to convert

    for f in files:
        ext = os.path.splitext(f)[1].lower().lstrip(".")
        ext = EXT_ALIASES.get(ext, ext)
        if ext == source_ext:
            converter.convert(os.path.join("input", f))

def main():
    """Orchestrate the file conversion workflow.

    1. Retrieve files from the input/ folder.
    2. Determine available conversions based on file types.
    3. Prompt the user to select a conversion.
    4. Convert all matching files and place results in output/.
    """
    files = get_input_files()
    if not files:
        return

    conversions = get_available_conversions(files)
    if not conversions:
        return

    source_ext, target_ext = prompt_conversion_choice(conversions)
    convert_files(files, source_ext, target_ext)

if __name__ == "__main__":
    #TODO: create unit test(s) to verify factory pattern output based on input format
    #TODO: refactor README.md to include instructions for: running tests & running the program with sample input files
    #TODO: refactor list comprehension in ConvertFactory.get_targets() to be more readable
    #TODO: remove excess files and folders (ex: claude.md, .vscode, .git, .gitignore, etc.)
    #TODO: provide sample input files for testing
    #TODO: empty output folder
    main()
