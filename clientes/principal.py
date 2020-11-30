from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import json
import collections

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Clientes(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   nombre = db.Column(db.String(100))
   apellido = db.Column(db.String(100))
   direccion = db.Column(db.String(200))
   telefono = db.Column(db.String(10))

   def __init__(self, nombre, apellido, direccion,telefono):
       self.nombre = nombre
       self.apellido = apellido
       self.direccion = direccion
       self.telefono = telefono

@app.route('/clientes')
def show_all():
   return render_template('/clientes/show_all.html', clientes = clientes.query.all() )

@app.route('/clientes/get_all', methods = ['GET'])
def get_all():
   data = clientes.query.all()
   user_list = []
   for row in data :
    d = collections.OrderedDict()
    d['id'] = row.id
    d['nombre'] = row.nombre
    d['apellido'] = row.apellido
    d['direccion'] = row.direccion
    d['telefono'] = row.telefono
    user_list.append(d)
   return json.dumps(user_list)

@app.route('/clientes/new', methods = ['GET', 'POST'])
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
   return render_template('/clientes/new.html')

@app.route("/clientes/update", methods=["POST"])
def update():
    nombre = request.form.get("oldnombre")
    cliente = clientes.query.filter_by(nombre=nombre).first()
    return render_template('/clientes/update.html', result = cliente, oldnombre = nombre)

@app.route("/clientes/update_record", methods=["POST"])
def update_record():
    nombre = request.form.get("oldnombre")
    cliente = clientes.query.filter_by(nombre=nombre).first()
    cliente.nombre = request.form['nombre']
    cliente.apellidos = request.form['apellidos']
    cliente.direccion = request.form['direccion']
    cliente.telefono = request.form['telefono']
    db.session.commit()
    return redirect('/clientes')

@app.route("/clientes/delete", methods=["POST"])
def delete():
    nombre = request.form.get("oldnombre")
    cliente = clientes.query.filter_by(nombre=nombre).first()
    db.session.delete(cliente)
    db.session.commit()
    return redirect("/clientes")

if __name__ == "__main__":
   db.create_all()
   app.run(host='0.0.0.0',debug=True)
