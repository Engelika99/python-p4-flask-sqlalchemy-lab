#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate
from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_details(id):
    animal = Animal.query.filter(Animal.id == id).first()
    if animal is None:
        response_body = '<h1>Animal not found</h1>'
        response = make_response(response_body, 404)
        return response
    
    response_body = f'<h1>Animal ID: {animal.id}</h1>'
    response_body += '<ul>'
    response_body += f'<ul>Name: {animal.name}</ul>'
    response_body += f'<ul>Species: {animal.species}</ul>'
    response_body += f'<ul>Zookeeper: {animal.zookeeper.name}</ul>'
    response_body += f'<ul>Enclosure: {animal.enclosure.environment}</ul>'
    response_body += '</ul>'
    
    response = make_response(response_body, 200)
    return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    if zookeeper is None:
        response_body = '<h1>Zookeeper not found</h1>'
        response = make_response(response_body, 404)
        return response
    
    response_body = f'<h1>Zookeeper ID: {zookeeper.id}</h1>'
    response_body += '<ul>'
    response_body += f'<ul>Name: {zookeeper.name}</ul>'
    response_body += f'<ul>Birthday: {zookeeper.birthday}</ul>'
    response_body += '<ul>Animals:</ul>'
    response_body += '<ul>'
    for animal in zookeeper.animals:
        response_body += f'<ul>{animal.name}</ul>'
    response_body += '</ul>'
    response_body += '</ul>'
    
    response = make_response(response_body, 200)
    return response

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    if enclosure is None:
        response_body = '<h1>Enclosure not found</h1>'
        response = make_response(response_body, 404)
        return response
    
    response_body = f'<h1>Enclosure ID: {enclosure.id}</h1>'
    response_body += '<ul>'
    response_body += f'<ul>Environment: {enclosure.environment}</ul>'
    response_body += f'<ul>Open to Visitors: {enclosure.open_to_visitors}</ul>'
    response_body += '<ul>Animals:</ul>'
    response_body += '<ul>'
    for animal in enclosure.animals:
        response_body += f'<ul>{animal.name}</ul>'
    response_body += '</ul>'
    response_body += '</ul>'
    
    response = make_response(response_body, 200)
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
