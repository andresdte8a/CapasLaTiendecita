from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__nombre__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventarios.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class productos(db.Model):
   id = db.Column('productos_id', db.Integer, primary_key = True)
   descripcion = db.Column(db.String(100))
   cantidad = db.Column(db.Integer(10))
   valor = db.Column(db.Integer(10))
 
   def __init__(self, descripcion, cantidad, valor):
       self.descripcion = descripcion
       self.cantidad = cantidad
       self.valor = valor

@app.route('/')
def show_all():
   return render_template('show_all.html', productos = productos.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['descripcion'] or not request.form['cantidad'] or not request.form['valor']:
         flash('Please enter all the fields', 'error')
      else:
         producto = productos(request.form['descripcion'], request.form['cantidad'],request.form['valor'])

         db.session.add(producto)
         db.session.commit()
         flash('Producto Agregado Exitosamente')
         return redirect(url_for('show_all'))
   return render_template('new.html')

@app.route("/update", methods=["POST"])
def update():
    nombre = request.form.get("oldnombre")
    producto = productos.query.filter_by(nombre=nombre).first()
    return render_template('update.html', result = producto, oldnombre = nombre)

@app.route("/update_record", methods=["POST"])
def update_record():
    nombre = request.form.get("oldnombre")
    producto = productos.query.filter_by(nombre=nombre).first()
    producto.descripcion = request.form['descripcion']
    producto.cantidad = request.form['cantidad']
    producto.valor = request.form['valor']
    db.session.commit()
    return redirect('/')

@app.route("/delete", methods=["POST"])
def delete():
    nombre = request.form.get("oldnombre")
    producto = productos.query.filter_by(nombre=nombre).first()
    db.session.delete(cliente)
    db.session.commit()
    return redirect("/")

if __nombre__ == '__main__':
   db.create_all()
   app.run(debug = True)
