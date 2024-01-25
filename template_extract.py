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

def main():
    tmpl_path = Path(argv[1])
    tmpl_img = Image.open(tmpl_path)

    start = int(argv[2], 16) # in HEX notation: 0xZXY <- Z = page, X = row, Y = column
    end = int(argv[3], 16)

    dst_path = tmpl_path.stem + "_extracted.png"
    if len(argv) > 4:
        dst_path = Path(argv[4])

    dst_img = Image.new("RGBA", (CHAR_WIDTH*COLS_PER_PAGE, CHAR_HEIGHT*ROWS_PER_PAGE*PAGES), (127, 127, 127, 255))


    for ch in range(0, COLS_PER_PAGE*ROWS_PER_PAGE*PAGES, 1):
        if ch < start or ch > end:
            continue

        col = ch % COLS_PER_PAGE
        row = int(ch / COLS_PER_PAGE)

        x1 = col * CHAR_WIDTH
        y1 = row * CHAR_HEIGHT
        x2 = x1 + CHAR_WIDTH
        y2 = y1 + CHAR_HEIGHT

        # print("Extracting char %d at (%d, %d)" % (ch, col, row))

        char_img = tmpl_img.crop((x1,y1,x2,y2))
        dst_img.paste(char_img, (col * CHAR_WIDTH, row * CHAR_HEIGHT))

    dst_img.save(dst_path)

if __name__ == "__main__":
    main()
