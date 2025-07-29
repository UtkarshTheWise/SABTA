import argparse
from SegCloth import segment_clothing
from PIL import Image

def resize_and_fill(image, target_size=(768, 1024), bg_color=(255, 255, 255), is_mask=False):
    target_w, target_h = target_size
    original_w, original_h = image.size

    scale = max(target_w / original_w, target_h / original_h)
    new_size = (int(original_w * scale), int(original_h * scale))
    resized = image.resize(new_size, resample=Image.Resampling.LANCZOS)

    left = (resized.width - target_w) // 2
    top = (resized.height - target_h) // 2
    right = left + target_w
    bottom = top + target_h
    cropped = resized.crop((left, top, right, bottom))

    return cropped.convert("L" if is_mask else "RGB")

def main(input_path):
    image = Image.open(input_path).convert("RGBA")

    # Segment clothing
    result = segment_clothing(img=image, clothes=["Upper-clothes"])
    result.save("segmented.png")

    # Apply white background
    white_bg = Image.new("RGB", result.size, (255, 255, 255))
    white_bg.paste(result, mask=result.getchannel("A"))

    # Create B&W mask from alpha
    alpha = result.getchannel("A")
    mask = alpha.point(lambda p: 255 if p > 20 else 0).convert("L")

    # Resize & center
    resized_rgb = resize_and_fill(white_bg)
    resized_rgb.save("segmented_resized.png")

    resized_mask = resize_and_fill(mask, is_mask=True)
    resized_mask.save("segmented_mask.png")

    print("✅ Saved: segmented_resized.png and segmented_mask.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input cloth image")
    args = parser.parse_args()
    main(args.input)
