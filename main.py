import os
from ConvertFactory import ConvertFactory
from ConvertStrategy import FileConverter

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
    #TODO: refactor main_convert() into separate functions, and call those functions from main()
    #TODO: create unit test(s) to verify factory pattern output based on input format
    #TODO: remove excess files and folders (ex: claude.md, .vscode, .git, .gitignore, etc.)
    main_convert()