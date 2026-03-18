# File Format Converter

A private, local alternative to online conversion tools for common image format conversions.

- Keeps data private — files never leave your machine
- Supports batch processing — convert all files in a folder at once
- Has no file size limits
- Works offline
- Produces consistent, reliable output every time

## How to Run

1. Install dependencies:

```bash
pip install Pillow playwright htmldocx
playwright install chromium
```

2. Place image file(s) in the `input/` folder.
3. Run the script:

```bash
python main.py
```

4. Select a conversion from the numbered list when prompted.
5. Converted files appear in the `output/` folder with the same name and new extension.

## How to Run Tests

```bash
python -m unittest tests/test_convert_factory.py
```

## Supported Conversions

| # | Conversion |
|---|-----------|
| 1 | PNG → JPG |
| 2 | JPG → PNG |
| 3 | WEBP → PNG |
| 4 | WEBP → JPG |
| 5 | PNG → WEBP |
| 6 | JPG → WEBP |
| 7 | GIF → PNG |
| 8 | GIF → JPG |
| 9 | PNG → GIF |
| 10 | JPG → GIF |
| 11 | BMP → PNG |
| 12 | BMP → JPG |
| 13 | PNG → BMP |
| 14 | JPG → BMP |
| 15 | HTML → PDF |
| 16 | HTML → DOCX |

## Dependencies

- Python 3.10+
- [Pillow](https://pypi.org/project/Pillow/)
- [Playwright](https://pypi.org/project/playwright/) (+ Chromium — installed via `playwright install chromium`)
- [htmldocx](https://pypi.org/project/htmldocx/)
