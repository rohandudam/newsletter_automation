#Flask Form To add Data
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, TimeField
from wtforms.fields.core import Label, StringField
from wtforms.validators import DataRequired, Length,ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from . models import Article_category
from datetime import datetime

#Check for fields not empty
def length_check(form,field):
    if len(field.data) == 0:
        raise ValidationError('Fields should not be null')

#This is for category to get value for query_factory used by QuerySelectField
def choice_query():
    return Article_category.query

#To add articles data
class AddArticlesForm(FlaskForm):
    url = StringField(label=('URL: '), validators=[DataRequired()])
    #url= TextField(label=('url'), validators= [DataRequired()])
    title = TextField(label=('Title: '), validators= [DataRequired()])
    description = TextAreaField(label=('Description: '), validators= [ DataRequired(), Length(max=100)])
    time = TimeField(label=('Time: '),format='%H:%M', default=datetime.now(), validators=[ DataRequired()])
    category_id = QuerySelectField(query_factory=choice_query, allow_blank=True,get_label='category_name')
    submit = SubmitField('Add Article')
