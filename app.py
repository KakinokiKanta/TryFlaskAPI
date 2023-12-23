'''
 RasPiにWebサーバを設置する
'''
import json
from flask import Flask, request, redirect

app = Flask(__name__)

# 日本語の有効化
app.json.ensure_ascii = False

# サーバが扱うファイルの設定
JSON_PATH = 'datafiles/bocchi_the_rock.json'

@app.route('/')
def index():
    json_file = open(JSON_PATH, 'r', encoding="utf-8")
    json_obj = json.load(json_file)
    json_file.close()

    return json_obj

'''
 jsonファイルのkeyを指定することで、対応するキャラクターのプロフィールを取得
 key(<name>)
   - guiter_hero: 後藤 ひとり
   - mama: 伊地知 虹夏
   - yamada: 山田 リョウ
   - ikuyo: 喜多 郁代
'''
@app.route("/get_profile/<name>", methods=["GET"])
def profile_get(name):
    json_file = open(JSON_PATH, 'r', encoding="utf-8")
    json_obj = json.load(json_file)
    json_file.close()

    return json_obj[name]

'''
 jsonファイルのkeyを指定することで、対応するキャラクターの画像を取得
 別サイトにリダイレクトすることで、表示
 key(<name>)
   - guiter_hero: 後藤 ひとり
   - mama: 伊地知 虹夏
   - yamada: 山田 リョウ
   - ikuyo: 喜多 郁代
'''
@app.route("/get_image/<name>", methods=["GET"])
def image_get(name):
    json_file = open(JSON_PATH, 'r', encoding="utf-8")
    json_obj = json.load(json_file)
    json_file.close()

    print(json_obj[name]["imageURL"])

    return redirect(json_obj[name]["imageURL"])

# IPアドレスとポート番号の設定
if __name__ == "__main__":

    ip = "127.0.0.1"
    app.run(host=ip, port=8000)
