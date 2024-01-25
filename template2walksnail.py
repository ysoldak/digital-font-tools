from pathlib import Path
from PIL import Image
from sys import argv

CHAR_WIDTH_ORIG = 12
CHAR_HEIGHT_ORIG = 18

SCALE_FACTOR = 3

CHAR_WIDTH = CHAR_WIDTH_ORIG * SCALE_FACTOR
CHAR_HEIGHT = CHAR_HEIGHT_ORIG * SCALE_FACTOR

COLS_PER_ROW = 16
ROWS_PER_PAGE = 16
PAGES = 2

def makeTransparent(img):
    for x in range(img.width):
        for y in range(img.height):
            if img.getpixel((x, y)) == (127, 127, 127, 255):
                img.putpixel((x, y), (0, 0, 0, 0))

def main():
    src_img_path = Path(argv[1])
    src_img = Image.open(src_img_path)

    img_24 = Image.new(
        "RGBA", (CHAR_WIDTH_ORIG*2, CHAR_HEIGHT_ORIG*2*512), (0, 0, 0, 0)
    )
    img_36 = Image.new(
        "RGBA", (CHAR_WIDTH_ORIG*3, CHAR_HEIGHT_ORIG*3*512), (0, 0, 0, 0)
    )

    for row in range(0, ROWS_PER_PAGE*PAGES, 1):
        for col in range(0, COLS_PER_ROW, 1):
            x1 = col * CHAR_WIDTH
            y1 = row * CHAR_HEIGHT
            x2 = x1 + CHAR_WIDTH
            y2 = y1 + CHAR_HEIGHT

            char_img = src_img.crop((x1,y1,x2,y2))
            makeTransparent(char_img)
            img_36.paste(char_img, (0, row*COLS_PER_ROW*CHAR_HEIGHT + col*CHAR_HEIGHT))

            char_img_24 = char_img.resize((CHAR_WIDTH_ORIG*2, CHAR_HEIGHT_ORIG*2), Image.Resampling.NEAREST)
            img_24.paste(char_img_24, (0, row*COLS_PER_ROW*CHAR_HEIGHT + col*CHAR_HEIGHT))

    dst_path_prefix = str(src_img_path.parent) + "/" + src_img_path.stem + "_walksnail"
    img_24.save(dst_path_prefix + "_24.png")
    img_36.save(dst_path_prefix + "_36.png")

if __name__ == "__main__":
    main()
