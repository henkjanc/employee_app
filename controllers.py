from flask import Flask, render_template, redirect, abort, jsonify
from models import engine, db_session, Base, Department, Employee
app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/employees')


@app.route('/employees')
def list():
    employees = Employee.query.all()

    return render_template('index.html',employees=employees)


@app.route('/employees/<id>')
def get(id):
    employee = Employee.query.get(id)

    return jsonify(employee.dict())
