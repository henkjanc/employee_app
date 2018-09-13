from flask import Flask, render_template, redirect, abort, jsonify
from models import engine, db_session, Base, Department, Employee
app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/employee')


@app.route('/employee')
def list():
    employees = Employee.query.all()

    return render_template('index.html',employees=employees)


@app.route('/employee/<id>')
def get(id):
    employee = Employee.query.get(id)
    if employee is None:
        abort(404)
    return render_template('detail.html',employee=employee)

