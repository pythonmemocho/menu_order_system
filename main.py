from flask import Flask,render_template,request,url_for
from data import *

app = Flask(__name__)

#トータルを計算する関数
#リストを引数として受ける
def get_sum(data1,data2) -> int:
    total = 0
    for i,j in zip(data1,data2):
        total += int(i.get_price()) * int(j)
    return total

#インデックスページ（メニューページ）
@app.route("/")
def index():
    return render_template(
        "index.html",
        #data.pyでインスタンス化したクラスのリストを設定
        menu=menu
        )

#合計金額表示ページ
@app.route("/form",methods=['POST'])
def form():
    #index.htmlで入力したcountをリストで受け取る
    #getlist()を用いるとリストで値を受け取れる
    count = request.form.getlist('count')
    
    #トータル金額を返す関数を実行
    total = get_sum(menu,count)
    
    return render_template(
        "form.html", 
        #menuリストとcountリストをdataに渡す
        data=zip(menu,count),
        #トータル金額をtotalに渡す
        total=total
        )

if __name__ == "__main__":
    app.run(debug=True)

