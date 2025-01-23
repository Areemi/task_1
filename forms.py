from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired

class VehicleForm(FlaskForm):
    brand = StringField('Brand', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    num_doors = IntegerField('Number of Doors', validators=[DataRequired()])
    has_sidecar = BooleanField('Has Sidecar')
    type = SelectField('Type', choices=[('car', 'Car'), ('motorcycle', 'Motorcycle')], validators=[DataRequired()])
    submit = SubmitField('Submit')