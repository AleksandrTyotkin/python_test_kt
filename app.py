from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///type_eq.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

class Type_eq(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	type_equipments = db.Column(db.Text, nullable=False)
	mask_serial = db.Column(db.Text)
	
	
	def __repr__(self):
		return '<Type_eq %r>' % self.id;



class Equip(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	code_type = db.Column(db.Integer)             #db.ForeignKey('type_eq.id') для установки связи между таблиц
	number_serial = db.Column(db.Text, nullable=False)
	
	
	def __repr__(self):
		return '<Equip %r>' % self.id;
 

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == "POST":
		type_equipments = request.form['type_equipments']
		number_serial = request.form['number_serial']

		equip = Equip(number_serial=number_serial)
		type_eq = Type_eq(type_equipments=type_equipments)

		#equips_exam = Equip.query.order_by(Equip.id).all()
		counter_number = 0
		sel_number = Equip.query.all()
		for i in sel_number:
			if i.number_serial == number_serial:
				counter_number += 1
				if counter_number > 0:
					return "Такой уже есть"
					break
		else:
			try:
				db.session.add(equip)
				db.session.commit()
				db.session.add(type_eq)
				db.session.commit()
				return redirect('/about')
			except:
				return "Что-то пошло не так"
	else: 
		return render_template("index.html");


@app.route('/about')
def about():
	equips = Equip.query.order_by(Equip.id).all()
	type_eqs = Type_eq.query.order_by(Type_eq.id).all()
	return render_template("about.html", equips=equips, type_eqs=type_eqs);


'''@app.route('/user/<string:name>/<int:id>')
def user(name, id):
	return "User page: " + name + " - " + str(id);'''


if __name__ == "__main__":
	app.run(debug=True)