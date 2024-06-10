from flask import Flask, render_template, request, redirect, url_for
from models import db, Questionnaire, Question, Assessment
from forms import QuestionnaireForm, QuestionForm, AssessmentForm
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db') 
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.route('/')
def index():
    assessments = Assessment.query.all()
    questionnaires = Questionnaire.query.all()  # Fetch all questionnaires
    return render_template('index.html', assessments=assessments, questionnaires=questionnaires)


@app.route('/delete_questionnaire/<int:questionnaire_id>', methods=['POST'])
def delete_questionnaire(questionnaire_id):
    questionnaire = Questionnaire.query.get_or_404(questionnaire_id)
    db.session.delete(questionnaire)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/view_questions/<int:questionnaire_id>')
def view_questions(questionnaire_id):
    questionnaire = Questionnaire.query.get_or_404(questionnaire_id)
    questions = Question.query.filter_by(questionnaire_id=questionnaire_id).all()
    return render_template('view_questions.html', questionnaire=questionnaire, questions=questions)



@app.route('/create_questionnaire', methods=['GET', 'POST'])
def create_questionnaire():
    form = QuestionnaireForm()
    if form.validate_on_submit():
        questionnaire = Questionnaire(name=form.name.data)
        db.session.add(questionnaire)
        db.session.commit()
        return redirect(url_for('add_questions', questionnaire_id=questionnaire.id))
    return render_template('create_questionnaire.html', form=form)

@app.route('/add_questions/<int:questionnaire_id>', methods=['GET', 'POST'])
def add_questions(questionnaire_id):
    form = QuestionForm()
    if form.validate_on_submit():
        question = Question(
            text=form.text.data,
            score_if_yes=form.score_if_yes.data,
            questionnaire_id=questionnaire_id
        )
        db.session.add(question)
        db.session.commit()
    questions = Question.query.filter_by(questionnaire_id=questionnaire_id).all()
    return render_template('add_questions.html', form=form, questions=questions, questionnaire_id=questionnaire_id)

@app.route('/assess/<int:questionnaire_id>', methods=['GET', 'POST'])
def assess(questionnaire_id):
    questionnaire = Questionnaire.query.get_or_404(questionnaire_id)
    form = AssessmentForm()
    if form.validate_on_submit():
        total_score = sum(
            question.score_if_yes for question in questionnaire.questions
            if request.form.get(f'question_{question.id}') == 'yes'
        )
        assessment = Assessment(
            threat_actor_name=form.threat_actor_name.data,
            total_score=total_score,
            questionnaire_id=questionnaire_id
        )
        db.session.add(assessment)
        db.session.commit()
        return redirect(url_for('view_assessment', assessment_id=assessment.id))
    return render_template('assess.html', form=form, questionnaire=questionnaire)

@app.route('/assessment/<int:assessment_id>')
def view_assessment(assessment_id):
    assessment = Assessment.query.get_or_404(assessment_id)
    return render_template('view_assessment.html', assessment=assessment)

@app.route('/start_assessment/<int:questionnaire_id>', methods=['GET', 'POST'])
def start_assessment(questionnaire_id):
    # Fetch the questionnaire from the database
    questionnaire = Questionnaire.query.get_or_404(questionnaire_id)

    if request.method == 'POST':
        # Calculate the total score based on user responses
        total_score = 0
        for question in questionnaire.questions:
            # Assuming the form input names are like 'question_1', 'question_2', etc.
            user_response = request.form.get(f'question_{question.id}')
            if user_response == 'yes':
                total_score += question.score_if_yes
        threat_actor_name = request.form.get('threat_actor_name', 'Unknown Threat Actor')
        # Save the assessment in the database
        assessment = Assessment(
            threat_actor_name=threat_actor_name,
            total_score=total_score,
            questionnaire_id=questionnaire_id
        )
        
        db.session.add(assessment)
        db.session.commit()

        # Redirect to the view assessment page for the newly created assessment
        return redirect(url_for('view_assessment', assessment_id=assessment.id))

    # Render the assessment form
    return render_template('start_assessment.html', questionnaire=questionnaire)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
