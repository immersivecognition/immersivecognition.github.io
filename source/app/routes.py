from flask import render_template, url_for
from app import application
import os
import markdown2

CONTENT = "content"

def path_to_md(base, filename):
    md_path = os.path.join(CONTENT, base)
    md = markdown2.markdown_path(os.path.join(md_path, filename), extras=["metadata"])
    md.href = base + '/' + os.path.splitext(filename)[0]
    return md


def get_mds(base):
    files = [f for f in os.listdir(os.path.join(CONTENT, base)) if f.lower().endswith(".md")]
    mds = [path_to_md(base, f) for f in files]
    return mds


@application.route('/')
@application.route('/index.html')
def index():
    return render_template('index.html')


@application.route('/projects')
def projects():
    return render_template('projects.html', projects=get_mds('projects'))


@application.route('/projects/<name>')
def project(name):
    project = path_to_md("projects", name + '.md')
    return render_template('project.html', project=project)


@application.route('/people')
def people():
    return render_template('people.html', people=get_mds('people'))


@application.route('/people/<name>')
def person(name):
    person = path_to_md("people", name + '.md')
    print(person.metadata)
    return render_template('person.html', person=person)


@application.route('/contact')
def contact():
    return render_template('contact.html')