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
    products = db.query(Tovar.id, Tovar.title, Tovar.cost).all()
    title = request.form.get("title")
    cost = request.form.get("cost", default=0, type=float)
    id_prod = request.form.get("ID", type=int)
    id_edit_prod = request.form.get("ID_edit", type=int)
    if (request.method == 'POST') and (title is not None) and (cost is not None):
    # Добавление товара
        tovar=Tovar()
        tovar.title=title
        tovar.cost=cost
        db.add(tovar)     # добавляем в бд
        db.commit()
        return redirect("/addTovar")
    if (request.method == 'POST') and (id_prod is not None):
    # Удаление товара
        product = db.query(Tovar).filter(Tovar.id == id_prod ).one()
        db.delete(product)
        db.commit() 
        return redirect("/addTovar")
    if (request.method == 'POST') and (id_edit_prod is not None):
        #Редактирование
        product_edit = db.query(Tovar).get(id_edit_prod)
        title = request.form.get("title_edit")
        cost = request.form.get("cost_edit", type=float)
        product_edit.title=title
        product_edit.cost=cost
        db.add(product_edit)     # добавляем в бд
        db.commit()
        return redirect("/addTovar")
    return render_template('addTovar.html', products = products)

if __name__ == '__main__':
# debug для ошибок 
    app.run(debug=True) 



