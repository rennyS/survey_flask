from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class QuestionnaireForm(FlaskForm):
    name = StringField('Questionnaire Name', validators=[DataRequired()])
    submit = SubmitField('Create')

class QuestionForm(FlaskForm):
    text = StringField('Question Text', validators=[DataRequired()])
    score_if_yes = IntegerField('Score if Yes', validators=[DataRequired()])
    submit = SubmitField('Add Question')

class AssessmentForm(FlaskForm):
    threat_actor_name = StringField('Threat Actor Name', validators=[DataRequired()])
    submit = SubmitField('Submit Assessment')
