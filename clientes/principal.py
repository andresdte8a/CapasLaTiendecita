from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class clientes(db.Model):
   id = db.Column('clientes_id', db.Integer, primary_key = True)
   nombre = db.Column(db.String(100))
   apellido = db.Column(db.String(100))
   direccion = db.Column(db.String(200))
   telefono = db.Column(db.String(10))

   def __init__(self, nombre, apellido, direccion,telefono):
       self.nombre = nombre
       self.apellido = apellido
       self.direccion = direccion
       self.telefono = telefono

@app.route('/')
def show_all():
   return render_template('show_all.html', clientes = clientes.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['nombre'] or not request.form['apellidos'] or not request.form['direccion']:
         flash('Please enter all the fields', 'error')
      else:
         cliente = clientes(request.form['nombre'], request.form['apellidos'],request.form['direccion'], request.form['telefono'])

         db.session.add(cliente)
         db.session.commit()
         flash('Cliente Agregado Exitosamente')
         return redirect(url_for('show_all'))
   return render_template('new.html')

@app.route("/update", methods=["POST"])
def update():
    nombre = request.form.get("oldnombre")
    cliente = clientes.query.filter_by(nombre=nombre).first()
    return render_template('update.html', result = cliente, oldnombre = nombre)

@app.route("/update_record", methods=["POST"])
def update_record():
    nombre = request.form.get("oldnombre")
    cliente = clientes.query.filter_by(nombre=nombre).first()
    cliente.nombre = request.form['nombre']
    cliente.apellidos = request.form['apellidos']
    cliente.direccion = request.form['direccion']
    cliente.telefono = request.form['telefono']
    db.session.commit()
    return redirect('/')

@app.route("/delete", methods=["POST"])
def delete():
    nombre = request.form.get("oldnombre")
    cliente = clientes.query.filter_by(nombre=nombre).first()
    db.session.delete(cliente)
    db.session.commit()
    return redirect("/")

if __nombre__ == '__main__':
   db.create_all()
   app.run(debug = True)
