from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'Wenjus2001?'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

class UserForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Submit')

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
        return "User added successfully!"
    return render_template('add_user.html', form=form)

@app.route('/get_user/<username>')
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'username': user.username})
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/get_all_users')
def get_all_users():
    users = User.query.all()
    user_list = [{'username': user.username} for user in users]
    return jsonify(user_list)

if __name__ == '__main__':
    with app.app_context():  # Ajoutez cette ligne pour créer un contexte d'application
        if not os.path.exists('users.db'):
            db.create_all()
    app.run(debug=True)
