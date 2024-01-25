from pathlib import Path
from PIL import Image
from sys import argv

CHAR_WIDTH_ORIG = 12
CHAR_HEIGHT_ORIG = 18

SCALE_FACTOR = 3

CHAR_WIDTH = CHAR_WIDTH_ORIG * SCALE_FACTOR
CHAR_HEIGHT = CHAR_HEIGHT_ORIG * SCALE_FACTOR

COLS_PER_PAGE = 16
ROWS_PER_PAGE = 16
PAGES = 2

def isEmpty(img, x1, y1, x2, y2):
    for x in range(x1, x2, 1):
        for y in range(y1, y2, 1):
            if img.getpixel((x, y)) != (127, 127, 127, 255):
                return False
    return True

def main():
    first_img_path = Path(argv[1])
    first_img = Image.open(first_img_path)

    second_img_path = Path(argv[2])
    second_img = Image.open(second_img_path)

    dst_path = str(first_img_path.parent) + "/" + first_img_path.stem +  "_" +  second_img_path.stem + "_merged.png"
    if len(argv) > 3:
        dst_path = Path(argv[3])
    
    dst_img = Image.new("RGBA", (CHAR_WIDTH*COLS_PER_PAGE, CHAR_HEIGHT*ROWS_PER_PAGE*PAGES), (0, 0, 0, 0))

    for row in range(0, ROWS_PER_PAGE*PAGES, 1):
        for col in range(0, COLS_PER_PAGE, 1):
            x1 = col * CHAR_WIDTH
            y1 = row * CHAR_HEIGHT
            x2 = x1 + CHAR_WIDTH
            y2 = y1 + CHAR_HEIGHT

            # if row == 0 and col == 0:
            #     print(first_img.getpixel((0, 0)))

            char_img = first_img.crop((x1,y1,x2,y2))
            if not isEmpty(second_img, x1, y1, x2, y2):
                char_img = second_img.crop((x1,y1,x2,y2))

            dst_img.paste(char_img, (col * CHAR_WIDTH, row * CHAR_HEIGHT))

    dst_img.save(dst_path)

if __name__ == "__main__":
    main()
