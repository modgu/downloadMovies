from flask import Flask, render_template, request,jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello"

@app.route('/download')
def download():
    download_url = request.args.get('url')
    return render_template('download.html', download_url=download_url)



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
