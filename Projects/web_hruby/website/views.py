#"front end"
#----------------------------------------------------------------

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

#--------------------------------------------

@views.route('/contacts')
def contacts():
    return render_template("contacts.html", user=current_user)

#--------------------------------------------

@views.route('/about')
def about():
    return render_template("about.html", user=current_user)

#--------------------------------------------


#setting up URL (@route)
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        print_name = request.form.get('print_name')
        url = request.form.get('url')
        amount = request.form.get('amount')
        address = request.form.get('address')
        comment = request.form.get('comment')
    
        amount = 1 if not amount else int(amount)

        if len(print_name) < 2:
            flash('Order name too short!', category='error')
        elif len(url) <7:
            flash('Invalid order url!', category='error')
            #if 'amount' is int() in the db, why it's now str()? ->can't use if condition
        elif int(amount) < 1: 
            flash('Invalid amount of ordered pieces!', category='error')
        elif len(address) < 5:
            flash('Delivery address too short!', category='error')
        elif len(comment) <0:
            flash('You defined a new physic law')
        else:

            new_note = Note(print_name=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Order added succesfully!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})