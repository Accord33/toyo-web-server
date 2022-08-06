from flask import Flask, render_template, redirect, url_for, request
import json

app = Flask(__name__)

@app.route('/<filepath>/<path>')
def main(filepath, path):
    if path == "index":
        with open('news.json','r') as f:
            news = json.load(f)
        return render_template(f'{filepath}/{path}.html',news=news)
    return render_template(f'{filepath}/{path}.html')

@app.route('/news/<page>')
def news(page):
    return render_template(f'news/{page}.html')

@app.route('/')
def noaddress():
    return redirect(url_for('main',filepath='home',path='index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=7002)