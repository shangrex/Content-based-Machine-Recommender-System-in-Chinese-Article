from flask import Flask, render_template, request, jsonify
from src.func.run_poet_search import poet_search
from src.func.run_poet_atr import poet_atr
from src.func.run_poet_cnt_spa import poet_cnt
import subprocess
import sys

app=Flask(__name__)

@app.route('/')
def index():
    print(request)
    return render_template("index.html")

@app.route('/', methods=['POST'])
def search():
    print("searching...")
    print(request.form)
    return render_template("index.html")

@app.route('/poem')
def poem():
    print(request)
    return render_template("poem.html")

@app.route('/mingyan')
def mingyan():
    print(request)
    return render_template("mingyan.html")

@app.route('/novel')
def novel():
    print(request)
    return render_template("novel.html")

@app.route('/poem/search/', methods=['POST'])
def poem_search():
    print("searching...")
    print(request.get_json('keywords')['keywords'])
    rst = poet_search(request.get_json('keywords')['keywords'])
    rst_cnt = rst[0]
    rst_atr = rst[1]
    rst_tit = rst[2]
    shtml = ""
    for i in rst_cnt:
        shtml += "<p>"
        shtml += "<strong>"+str(i[1])+"</strong>" + '<br>' +str(i[2]) + '-' + str(i[3])
        if type(i[4]) != type(float) and str(i[4]) != "nan":
            shtml += '<br>' +'tags'+ str()
        shtml += "</p>"
        
    return jsonify({"success": 200, "rst": shtml})

@app.route('/poem/predict/', methods=['POST'])
def poem_predict():
    print("predicting...")
    print(request.get_json('keywords')['keywords'])
    rst = poet_atr(request.get_json('keywords')['keywords'])
    shtml = ""
    st = ['\"', '[', ']', '\'']
    for i in rst:
        shtml += "<p>"
        shtml += "<strong>"+str(i)+"</strong>"
        shtml += "</p>"
        
    return jsonify({"success": 200, "rst": shtml})

@app.route('/poem/recommend/', methods=['POST'])
def poem_recommend():
    print("recommending...")
    print(request.get_json('keywords')['keywords'])
    rst = poet_cnt(request.get_json('keywords')['keywords'])
    shtml = ""
    st = ['\"', '[', ']', '\'']
    for i in rst:
        x = "".join([j for j in i if j not in st])
        shtml += "<p>"
        shtml += "<strong>"+str(x)+"</strong>"
        shtml += "</p>"
        
    return jsonify({"success": 200, "rst": shtml})


if __name__ == '__main__':
    app.run()