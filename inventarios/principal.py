from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventarios.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class productos(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   descripcion = db.Column(db.String(100))
   cantidad = db.Column(db.Integer())
   valor = db.Column(db.Integer())
 
   def __init__(self, descripcion, cantidad, valor):
       self.descripcion = descripcion
       self.cantidad = cantidad
       self.valor = valor

@app.route('/inventarios')
def show_all():
   return render_template('/inventarios/show_all.html', productos = productos.query.all() )

@app.route('/inventarios/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['descripcion'] or not request.form['cantidad'] or not request.form['valor']:
         flash('Please enter all the fields', 'error')
      else:
         producto = productos(request.form['descripcion'], request.form['cantidad'],request.form['valor'])

         db.session.add(producto)
         db.session.commit()
         flash('Producto Agregado Exitosamente')
         return redirect(url_for('/inventarios/show_all'))
   return render_template('/inventarios/new.html')

@app.route("/inventarios/update", methods=["POST"])
def update():
    nombre = request.form.get("oldnombre")
    producto = productos.query.filter_by(nombre=nombre).first()
    return render_template('/inventarios/update.html', result = producto, oldnombre = nombre)

@app.route("/inventarios/update_record", methods=["POST"])
def update_record():
    nombre = request.form.get("oldnombre")
    producto = productos.query.filter_by(nombre=nombre).first()
    producto.descripcion = request.form['descripcion']
    producto.cantidad = request.form['cantidad']
    producto.valor = request.form['valor']
    db.session.commit()
    return redirect('/inventarios')

if __name__ == '__main__':
   db.create_all()
   app.run(host='0.0.0.0',debug=True)
