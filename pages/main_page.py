from flask import Blueprint
from flask import render_template, request
import random

from data import db_session
from data.__all_models import *

blueprint = Blueprint(
    'main_page', __name__,
    template_folder='templates',
    static_folder='static'
)


@blueprint.route('/')
def main_page():
    return render_template('main.html', title="Главная")


@blueprint.route('/registration/')
def registration():
    return render_template('registration.html', title="Выбор класса")


@blueprint.route('/test/<string:_class>', methods=['GET', 'POST'])
def test(_class):
    db_sess = db_session.create_session()
    n = db_sess.query(Class).filter(Class.number == _class).first().id
    try:
        questions = random.sample((db_sess.query(Question).filter(Question.id_class == n).all()), k=3)
        answers = db_sess.query(Answer).filter(Answer.id_question.in_(list(q.id for q in questions))).all()
    except:
        return render_template('registration.html', title="Выбор класса")
    db_sess.commit()
    if request.method == 'GET':
        return render_template('test.html', title="Тест", _class=_class, test=questions, answers=answers)
    elif request.method == 'POST':
        right_answers = dict([(i.id_question, str(i.body)) for i in db_sess.query(Answer).
                             filter(Answer.id_question.in_(list(q.id for q in questions))).filter(Answer.status).all()])
        user_answers = []
        for i in range(1, len(questions) + 1):
            try:
                user_answers.append(int(request.form.get(f'{i}')))
            except:
                continue
        print(user_answers)
        user_answers = dict([(i.id_question, str(i.body)) for i in db_sess.query(Answer).
                            filter(Answer.id.in_(user_answers)).all()])
        print(user_answers, right_answers)
        return results(questions, user_answers, right_answers)


@blueprint.route('/results/')
def results(questions, user_answers, right_answers):
    return render_template('results.html', title="Результаты",
                           test=questions, user=user_answers, right=right_answers)
