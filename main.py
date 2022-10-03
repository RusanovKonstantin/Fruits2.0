from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/katalog')
def katalog():
    return render_template('katalog.html')

@app.route('/korzina')
def korzina():
    return render_template('korzina.html')

if __name__ == '__main__':
# debug для ошибок 
    app.run(debug=True) 


