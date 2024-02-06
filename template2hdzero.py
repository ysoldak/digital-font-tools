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

def main():
    src_img_path = Path(argv[1])
    src_img = Image.open(src_img_path)

    dst_img = src_img

    dst_path_prefix = str(src_img_path.parent) + "/" + src_img_path.stem + "_hdzero"
    dst_img.save(dst_path_prefix + ".bmp")

if __name__ == "__main__":
    main()
