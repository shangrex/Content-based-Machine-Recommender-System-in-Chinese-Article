from flask import Flask, render_template, request, jsonify
from src.func.run_poet_search import poet_search
from src.func.run_poet_atr import poet_atr
from src.func.run_poet_cnt_spa import poet_cnt
from src.func.run_ming_cnt import ming_recommend
from src.func.run_ming_name import ming_name
from src.func.run_novel_name import novel_name
from src.func.run_novel_atr import novel_author
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
    shtml = "<p><span class=\"w3-tag\">paragraphs match</span>"
    for i in rst_cnt:
        shtml += "<p>"
        shtml += "<strong>"+str(i[1])+"</strong>" + '<br>' +str(i[2]) + '-' + str(i[3])
        if type(i[4]) != type(float) and str(i[4]) != "nan":
            shtml += '<br>' +'tags'+ str()
        shtml += "</p>"
    
    shtml += "<p><span class=\"w3-tag\">author match</span>"
    for i in rst_atr:
        shtml += "<p>"
        shtml += "<strong>"+str(i[0])+"</strong>" + '<br>' +str(i[1]) + '-' + str(i[2])
        if type(i[3]) != type(float) and str(i[3]) != "nan":
            shtml += '<br>' +'tags'+ str()
        shtml += "</p>"

    shtml += "<p><span class=\"w3-tag\">title match</span>"
    for i in rst_tit:
        shtml += "<p>"
        shtml += "<strong>"+str(i[0])+"</strong>" + '<br>' +str(i[1]) + '-' + str(i[2])
        if type(i[3]) != type(float) and str(i[3]) != "nan":
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

@app.route('/mingyan/recommend/', methods=['POST'])
def mingyan_recommend():
    print("recommending mingyan...")
    print(request.get_json('keywords')['keywords'])
    rst = ming_recommend(request.get_json('keywords')['keywords'])
    shtml = ""
    for i in rst:
        shtml += "<p>"
        shtml += "<strong>"+str(i[1])+"</strong>" + '<br>' +str(i[2]) + '-' + str(i[3])
        shtml += "</p>"
        
    return jsonify({"success": 200, "rst": shtml})


@app.route('/mingyan/name/', methods=['POST'])
def mingyan_name():
    print("recommending name...")
    print(request.get_json('keywords')['keywords'])
    rst = ming_name(request.get_json('keywords')['keywords'])
    shtml = ""
    for i in rst:
        shtml += "<p>"
        shtml += "<strong>"+str(i)+"</strong>"
        shtml += "</p>"
        
    return jsonify({"success": 200, "rst": shtml})


@app.route('/novel/name/', methods=['POST'])
def novel_recommend_name():
    print("recommending novel's name...")
    print(request.get_json('keywords')['keywords'])
    rst = novel_name(request.get_json('keywords')['keywords'])
    shtml = ""
    for i in rst:
        shtml += "<p>"
        shtml += "<strong>"+str(i[0])+"</strong>"
        shtml += "</p>"
        
    return jsonify({"success": 200, "rst": shtml})


@app.route('/novel/author/', methods=['POST'])
def novel_recommend_author():
    print("recommending novel's author...")
    print(request.get_json('keywords')['keywords'])
    rst = novel_author(request.get_json('keywords')['keywords'])
    shtml = ""
    for i in rst:
        shtml += "<p>"
        shtml += "<strong>"+str(i[0])+"</strong>"
        shtml += "</p>"
        
    return jsonify({"success": 200, "rst": shtml})

if __name__ == '__main__':
    app.run()