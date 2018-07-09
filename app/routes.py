from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import NewEventForm


@app.route('/')
@app.route('/index')
def index():
    title = "Arma Event Organizer"

    return render_template('index.html', title=title)


@app.route('/event', methods=['GET', 'POST'])
def event():
    form = NewEventForm()
    if form.validate_on_submit():
        # Todo generate edit link, save event data
        flash('Event \"{}\" created. please wait for an admin to validate it.'.format(
            form.event_name.data))
        return redirect(url_for('created'))
    return render_template('event.html', title='New Event', form=form)


@app.route('/created')
def created():
    return render_template('created.html', title='Success')
