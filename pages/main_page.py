from flask import Blueprint
from flask import render_template

blueprint = Blueprint(
    'main_page', __name__,
    template_folder='templates'
)


@blueprint.route('/')
def main_page():
    return render_template('main.html', username="создатель")

