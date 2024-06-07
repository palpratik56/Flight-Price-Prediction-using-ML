from flask_wtf import FlaskForm
import pandas as pd
from wtforms import SelectField, DateField, TimeField, IntegerField, SubmitField
from wtforms.validators import DataRequired

#getting the data
tr = pd.read_csv('data/train.csv')
val = pd.read_csv('data/val.csv')
X_data = pd.concat([tr,val], axis=0).drop(columns='price')

class input(FlaskForm):
    airline = SelectField('Airline', choices=X_data.airline.unique().tolist(),
                          validators=[DataRequired()])
    doj = DateField('Date of journey', validators=[DataRequired()] )
    src  = SelectField('Source', choices=X_data.source.unique().tolist(),
                       validators=[DataRequired()])
    des  = SelectField('Destination', choices=X_data.destination.unique().tolist(),
                       validators=[DataRequired()])
    dep = TimeField('Departure Time',validators=[DataRequired()])
    arr = TimeField('Arrival Time',validators=[DataRequired()])
    dur = IntegerField('Duration', validators=[DataRequired()])
    tos = IntegerField('Total Stops', validators=[DataRequired()])
    addinfo = SelectField('Additional info', 
    choices=X_data.additional_info.unique().tolist(), validators=[DataRequired()])

    sub = SubmitField('Get Fare')