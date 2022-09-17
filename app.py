from flask import Flask, request, render_template

import utils
FILE_DIR = 'candidates.json'
data = utils.load_candidates(FILE_DIR)

app = Flask(__name__)


@app.route("/")
def page_index():
    result = ''
    candidates_list = utils.load_candidates(FILE_DIR)
    return render_template('all.html', list=candidates_list)


@app.route("/candidates/<int:pk>")
def page_candidates(pk):
    result = utils.et_by_pk(pk)
    return render_template('card.html', candidate=result, pk=pk)


@app.route("/search/<candidate_name>")
def page_candidates_by_name(candidate_name):
    result = utils.get_by_name(candidate_name)
    how_many = len(result)
    return render_template('search.html', search_result=result, number=how_many)


@app.route("/skill/<skill_name>")
def page_candidates_by_skills(skill_name):
    result = utils.get_by_skill(skill_name)
    how_many = len(result)
    not_found = None
    return render_template('skills.html',
                           search_result=result,
                           number=how_many,
                           not_found=not_found,
                           skill=skill_name)

app.run()

