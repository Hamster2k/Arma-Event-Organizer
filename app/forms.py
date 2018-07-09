from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, SubmitField
from wtforms.validators import DataRequired


# Form to create new events with
class NewEventForm(FlaskForm):
    event_name = StringField('event name', validators=[DataRequired()])
    event_datetime = DateTimeField('event date and time, format = \'Y-m-D H:M:S\'', validators=[DataRequired()])
    event_briefing = TextAreaField('event briefing', validators=[DataRequired()])
    event_submit = SubmitField('submit')
