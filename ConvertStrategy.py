from abc import ABC, abstractmethod
from PIL import Image
import os

os.makedirs("output", exist_ok=True)

# --- Abstract Strategy ---

class ConvertStrategy(ABC):
    @abstractmethod
    def convert(self, input_path):
        pass


# --- Concrete Strategies ---

class PngToJpgStrategy(ConvertStrategy):
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.jpg"
        img.convert("RGB").save(output_path)
        print(f"Converted {input_path} → {output_path}")


class JpgToPngStrategy(ConvertStrategy):
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.png"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class WebpToPngStrategy(ConvertStrategy):
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.png"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class WebpToJpgStrategy(ConvertStrategy):
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.jpg"
        img.convert("RGB").save(output_path)
        print(f"Converted {input_path} → {output_path}")


class PngToWebpStrategy(ConvertStrategy):
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.webp"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class JpgToWebpStrategy(ConvertStrategy):
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.webp"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class GifToPngStrategy(ConvertStrategy):
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.png"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class GifToJpgStrategy(ConvertStrategy):
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.jpg"
        img.convert("RGB").save(output_path)
        print(f"Converted {input_path} → {output_path}")


class PngToGifStrategy(ConvertStrategy):
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.gif"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class JpgToGifStrategy(ConvertStrategy):
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.gif"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class BmpToPngStrategy(ConvertStrategy):
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.png"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


class BmpToJpgStrategy(ConvertStrategy):
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.jpg"
        img.convert("RGB").save(output_path)
        print(f"Converted {input_path} → {output_path}")


class PngToBmpStrategy(ConvertStrategy):
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.bmp"
        img.convert("RGB").save(output_path)
        print(f"Converted {input_path} → {output_path}")


class JpgToBmpStrategy(ConvertStrategy):
    def convert(self, input_path):
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"output/{filename}.bmp"
        img.save(output_path)
        print(f"Converted {input_path} → {output_path}")


# --- Context ---

class FileConverter:
    def __init__(self, strategy: ConvertStrategy):
        self.strategy = strategy

    def convert(self, input_path):
        self.strategy.convert(input_path)