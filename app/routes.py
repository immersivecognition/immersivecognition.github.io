from flask import render_template, url_for
from app import application
import json


@application.route('/')
@application.route('/index.html')
def index():
    projects = json.load(open("content/projects.json"))
    people = json.load(open("content/people.json"))
    return render_template('index.html', projects=projects, people=people)