# Copied verbatim from https://github.com/Knifa/mcm2img/tree/templates
# Edited outputs

from pathlib import Path
from PIL import Image
from sys import argv


CHAR_WIDTH = 12
CHAR_HEIGHT = 18

CHAR_COUNT_X = 16
CHAR_COUNT_Y = 16

SRC_SCALE_FACTOR = 3

CHAR_WIDTH_PX = CHAR_WIDTH * SRC_SCALE_FACTOR
CHAR_HEIGHT_PX = CHAR_HEIGHT * SRC_SCALE_FACTOR

DST_PAGES = 2
DST_HD_SCALE_FACTOR = 2 / 3
DST_CHAR_COUNT = CHAR_COUNT_X * CHAR_COUNT_Y * DST_PAGES

def makeTransparent(img):
    for x in range(img.width):
        for y in range(img.height):
            if img.getpixel((x, y)) == (127, 127, 127, 255):
                img.putpixel((x, y), (0, 0, 0, 0))

def main():
    src_img_path = Path(argv[1])
    src_img = Image.open(src_img_path)
    src_pages = int(src_img.height / CHAR_HEIGHT_PX / CHAR_COUNT_Y)

    dst_img = Image.new(
        "RGBA", (CHAR_WIDTH_PX, CHAR_HEIGHT_PX * DST_CHAR_COUNT), (0, 0, 0, 0)
    )

    for j in range(0, CHAR_COUNT_Y * src_pages, 1):
        for i in range(0, CHAR_COUNT_X, 1):
            x1 = i * CHAR_WIDTH_PX
            y1 = j * CHAR_HEIGHT_PX
            x2 = x1 + CHAR_WIDTH_PX
            y2 = y1 + CHAR_HEIGHT_PX

            char_img = src_img.crop(
                (
                    x1,
                    y1,
                    x2,
                    y2,
                )
            )
            makeTransparent(char_img)

            dst_img.paste(char_img, (0, (j * CHAR_COUNT_Y + i) * CHAR_HEIGHT_PX))

    dst_path_dir = str(src_img_path.parent) + "/" + src_img_path.stem + "_wtfos"
    Path(dst_path_dir).mkdir(parents=True, exist_ok=True)
    
    dst_path_prefix = dst_path_dir + "/font"

    # dst_img.save(dst_path_prefix + "_all.png")
    # dst_img_hd = dst_img.resize(
    #     (
    #         int(dst_img.width * DST_HD_SCALE_FACTOR),
    #         int(dst_img.height * DST_HD_SCALE_FACTOR),
    #     ),
    #     Image.Resampling.LANCZOS,
    # )
    # dst_img_hd.save(dst_path_prefix + "_all_hd.png")

    for i in range(DST_PAGES):
        page_img = dst_img.crop(
            (
                0,
                (CHAR_HEIGHT_PX * CHAR_COUNT_Y * CHAR_COUNT_Y) * i,
                dst_img.width,
                (CHAR_HEIGHT_PX * CHAR_COUNT_Y * CHAR_COUNT_Y) * (i + 1),
            )
        )

        page_img_hd = page_img.resize(
            (
                int(page_img.width * DST_HD_SCALE_FACTOR),
                int(page_img.height * DST_HD_SCALE_FACTOR),
            ),
            Image.Resampling.LANCZOS,
        )

        if i >= 1:
            suffix = f"_{i + 1}"
        else:
            suffix = ""

        # page_img.save(f"{dst_path_prefix}{suffix}_36.png")
        # page_img_hd.save(f"{dst_path_prefix}{suffix}_24.png")
        Path(f"{dst_path_prefix}{suffix}.bin").write_bytes(page_img.tobytes("raw", "RGBA"))
        Path(f"{dst_path_prefix}_hd{suffix}.bin").write_bytes(page_img_hd.tobytes("raw", "RGBA"))


if __name__ == "__main__":
    main()
