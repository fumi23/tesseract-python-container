from pytesseract import pytesseract
from PIL import Image
import os

if __name__ == '__main__':

    # 1枠の縦横ピクセル
    w = 80;
    h = [65, 65, 65];

    # 原点
    origin_x = 320;
    origin_y = 0;

    # 枠線を除去するマージンピクセル。縦横共通。
    margin_w = 20;
    margin_h = 15;

    img = Image.open(os.path.dirname(os.path.abspath(__file__)) + "/sample3.png", "r");

    leftpos_x = origin_x;
    for pos_x in range(0, 3):
        # 読み取るマスの左上位置
        leftpos_x -= w + margin_w;
        leftpos_y = origin_y + margin_h;
        for pos_y in range(0, 3):
            # 該当のマスをトリミング
            crop = img.crop((leftpos_x, leftpos_y, leftpos_x + w, leftpos_y + h[pos_y]));

            # インストールしたtesseractコマンドのパス
            pytesseract.tesseract_cmd = "/usr/bin/tesseract";

            # -psm 8は1文字判定のフラグ
            result = pytesseract.image_to_string(crop, config="-psm 10", lang="eng+jpn");

            print(result, end='\n' if pos_y == 2 else ',');

            # 次に読み取るマスの左上位置 (y-coord)
            leftpos_y += h[pos_y] + margin_h;
