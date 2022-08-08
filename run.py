from flask import Flask, render_template, redirect, url_for, request
import json

app = Flask(__name__)

@app.route('/<filepath>/<path>')
def main(filepath, path):
    if path == "index":
        with open('news.json','r') as f:
            news = json.load(f)
        return render_template(f'{filepath}/{path}.html',news=news)
    if path == 'blog':
        with open('blog.json','r') as f:
            blog = json.load(f)
        return render_template(f'{filepath}/{path}.html', blog=blog)
    return render_template(f'{filepath}/{path}.html')

@app.route('/.well-known/acme-challenge/B0ft-qLPlZyLTQRjFCiizzcY3HNQsXCZLpi7tcVKwCA')
def ssl_encrypt():
    return 'B0ft-qLPlZyLTQRjFCiizzcY3HNQsXCZLpi7tcVKwCA.58JW9ifPlEl4EL0CKnG3usMi_ppUDlDClVn9Ny8ke2o'

@app.route('/blog/<page>')
def blog(page):
    return render_template(f'blog/{page}.html')

@app.route('/news/<page>')
def news(page):
    return render_template(f'news/{page}.html')

@app.route('/')
def noaddress():
    return redirect(url_for('main',filepath='home',path='index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=7002)