from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from tovar import Tovar, engine
from flask import request, redirect


from sqlalchemy.orm import sessionmaker
 
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

    # сохраняем изменения

app = Flask(__name__)
# engine = create_engine ('postgresql+psycopg2://postgres:example@localhost/MAGaz')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/katalog',methods=['GET'] )
def katalog():
    products = db.query(Tovar.title, Tovar.cost).all()
    print(products)
    return render_template('katalog.html', products = products)
    

@app.route('/korzina')
def korzina():
    return render_template('korzina.html')

@app.route('/addTovar', methods=['GET', 'POST'])
def addTovar():
    if request.method == 'POST':
        title = request.form.get("title")
        cost = request.form.get("cost", default=0, type=float)
        tovar=Tovar()
        tovar.title=title
        tovar.cost=cost
        db.add(tovar)     # добавляем в бд
        db.commit() 
        return redirect("/addTovar")
    return render_template('addTovar.html')

if __name__ == '__main__':
# debug для ошибок 
    app.run(debug=True) 



