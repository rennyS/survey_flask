from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Add cascade='all, delete' to delete associated questions when a questionnaire is deleted
    questions = db.relationship('Question', back_populates='questionnaire', cascade='all, delete')

    # Add cascade='all, delete' to delete associated assessments when a questionnaire is deleted
    assessments = db.relationship('Assessment', back_populates='questionnaire', cascade='all, delete')

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    score_if_yes = db.Column(db.Integer, nullable=False)
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'), nullable=False)
    questionnaire = db.relationship('Questionnaire', back_populates='questions')

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    threat_actor_name = db.Column(db.String(100), nullable=False)
    total_score = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'), nullable=False)
    questionnaire = db.relationship('Questionnaire', back_populates='assessments')
