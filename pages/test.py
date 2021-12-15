from flask import Blueprint
from flask import render_template

blueprint = Blueprint(
    'test', __name__,
    template_folder='templates',
)

test_test = [{"id": 1, "text": "текст", "picture": "images/1.png", "answers": ["1", "2", "3", "4", "5"]},
             {"id": 2, "text": "тексттексттекстекст", "picture": None, "answers": ["a", "b", "c", "d", "e"]},
             {"id": 3, "text": "тексттекст", "picture": None, "answers": ["а", "б", "в", "г", "д"]}]


@blueprint.route('/test/<_class>', methods=['GET', 'POST'])
def test(_class):
    return render_template('test.html', _class=_class, test=test_test)