from flask_wtf import Form
from wtforms import TextAreaField, TextField, SubmitField
from wtforms.validators import DataRequired, InputRequired

class MoodButtons(Form):
    anger = SubmitField('Angry')
    joy = SubmitField('Happy')
    sadness = SubmitField('Sad')

class MoodText(Form):
    text = TextAreaField('Mood')
    startButton = SubmitField("Submit")

class PlaylistButton(Form):
	playlist = SubmitField("make playlist")
	name = TextField("playlist name", [InputRequired()])
