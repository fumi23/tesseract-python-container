from pytesseract import pytesseract
from PIL import Image
import os

if __name__ == '__main__':

    # 1枠の縦横ピクセル
    w = 30;
    h = [150, 61, 52, 47, 49, 173, 350];

    # 原点
    origin_x = 712;
    origin_y = 62;

    # 枠線を除去するマージンピクセル。縦横共通。
    margin_w = 5;
    margin_h = 2;

    # 数
    count_x = 19;
    count_y = 7;

    img = Image.open(os.path.dirname(os.path.abspath(__file__)) + "/namelist.png", "r");

    leftpos_x = origin_x;
    for pos_x in range(0, count_x):
        # 読み取るマスの左上位置
        leftpos_x -= w + margin_w;
        leftpos_y = origin_y + margin_h;
        print(pos_x + 1, end=': ');
        for pos_y in range(0, count_y):
            # 該当のマスをトリミング
            crop = img.crop((leftpos_x, leftpos_y, leftpos_x + w, leftpos_y + h[pos_y]));

            # インストールしたtesseractコマンドのパス
            pytesseract.tesseract_cmd = "/usr/bin/tesseract";

            # -psm 8は1文字判定のフラグ
            result = pytesseract.image_to_string(crop, config="-psm 1", lang="eng+jpn");

            print(result, end='\n' if pos_y == count_y - 1 else ',');

            # 次に読み取るマスの左上位置 (y-coord)
            leftpos_y += h[pos_y] + margin_h;
