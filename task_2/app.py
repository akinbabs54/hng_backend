from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

# Create a new person
@app.route('/api', methods=['POST'])
def add_person():
    data = request.get_json()
    name = data.get('name')
    
    if not name:
        return jsonify({'message': 'Name is required'}), 400
    
    new_person = Person(name=name)
    db.session.add(new_person)
    db.session.commit()
    response = {"status": "success",
                'message': 'Person added successfully',
                'data': new_person }
    return jsonify(response), 201

# Get a person by ID
@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    person = Person.query.get_or_404(user_id)
    return jsonify({'name': person.name}), 200

# Update a person by ID
@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    person = Person.query.get_or_404(user_id)
    data = request.get_json()
    name = data.get('name')
    
    if not name:
        return jsonify({'message': 'Name is required'}), 400
    
    person.name = name
    db.session.commit()
    
    return jsonify({'message': 'Person updated successfully'}), 200

# Delete a person by ID
@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    person = Person.query.get_or_404(user_id)
    db.session.delete(person)
    db.session.commit()
    
    return jsonify({'message': 'Person deleted successfully'}), 200

# Get a person by name
@app.route('/api/name/<name>', methods=['GET'])
def get_person_by_name(name):
    person = Person.query.filter_by(name=name).first()
    if person is None:
        return jsonify({'message': 'Person not found'}), 404
    return jsonify({'name': person.name}), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
