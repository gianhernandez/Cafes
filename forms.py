from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


#Form to add new cafes
class AddForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    map_url = StringField('Map URL:', validators=[DataRequired()])
    img_url = StringField('Image URL:', validators=[DataRequired()])
    location = StringField('Location:', validators=[DataRequired()])
    has_sockets = BooleanField('Sockets Available?')
    has_toilet = BooleanField('Restroom Available?')
    has_wifi = BooleanField('Wifi Available?')
    can_take_calls = BooleanField('Can Take Calls?')
    seats = StringField('Seats:', validators=[DataRequired()])
    coffee_price = StringField('Coffee Price:', validators=[DataRequired()])
    submit = SubmitField('Submit')

