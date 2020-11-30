from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import json
import collections

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
@app.route('/inventarios/get_all', methods = ['GET'])
def get_all():
   data = inventarios.query.all()
   user_list= []
   for row in data :
      d = collections.OrderedDict()
      d['id'] = row.id
      d['descripcion'] = row.descripcion
      d['cantidad0'] = row.cantidad
      d['valor'] = row.valor
      user.list.append(d)
      return json.dumps(user_list)

@app.route('/inventarios/new', methods = ['GET', 'POST'])
def new():
   data = inventarios.query.new()
   user_list = []

   if request.method == 'POST':
      if not request.form['descripcion'] or not request.form['cantidad'] or not request.form['valor']:
         flash('Please enter all the fields', 'error')
      else:
         d = collections.OrderedDict()

         producto = productos(request.form['descripcion'], request.form['cantidad'],request.form['valor'])

         db.session.add(producto)
         db.session.commit()
         flash('Producto Agregado Exitosamente')
         return redirect(url_for('/inventarios/show_all'))
   return render_template('/inventarios/new.html')

@app.route("/inventarios/update", methods=["POST"])
def update():
    descripcion = request.form.get("olddescripcion")
    producto = productos.query.filter_by(descripcion=descripcion).first()
    return render_template('/inventarios/update.html', result = producto, olddescripcion = descripcion)

@app.route("/inventarios/update_record", methods=["POST"])
def update_record():
    descripcion = request.form.get("olddescripcion")
    producto = productos.query.filter_by(descripcion=descripcion).first()
    producto.descripcion = request.form['descripcion']
    producto.cantidad = request.form['cantidad']
    producto.valor = request.form['valor']
    db.session.commit()
    return redirect('/inventarios')

@app.route("/inventarios/delete", methods=["POST"])
def delete() :
   descripcion = request.form.get("olddescripcion")
   producto = productos.query.filter_by(descripcion=descripcion).first()
   db.session.delete(producto)
   db.session.commit()
   return redirect("/inventarios")
   
if __name__ == '__main__':
   db.create_all()
   app.run(host='0.0.0.0',debug=True)
