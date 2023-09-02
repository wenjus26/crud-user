from flask import render_template, request, redirect, url_for, flash
from app import app, db, User, UserForm

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
        flash('User added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_user.html', form=form)

@app.route('/edit_user/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get(id)
    form = UserForm()
    if form.validate_on_submit():
        user.username = form.username.data
        db.session.commit()
        flash('User updated successfully!', 'success')
        return redirect(url_for('index'))
    form.username.data = user.username
    return render_template('edit_user.html', form=form, user=user)

@app.route('/delete_user/<int:id>', methods=['GET', 'POST'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/create_tables')
def create_tables():
    db.create_all()
    return 'Tables created successfully!'
