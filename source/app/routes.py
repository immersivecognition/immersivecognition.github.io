from flask import render_template, url_for
from app import application
import os
import markdown2
import json
from email_obfuscator import obfuscate

CONTENT = "content"
ALL_PAPERS = json.load(open(os.path.join(CONTENT, 'papers.json'), encoding="utf-8"))
DOMAIN = 'leeds.ac.uk'

def path_to_md(base, filename):
    md_path = os.path.join(CONTENT, base)
    md = markdown2.markdown_path(os.path.join(md_path, filename), extras=["metadata"])
    md.filename = os.path.splitext(filename)[0]
    return md


def get_mds(base):
    files = [f for f in os.listdir(os.path.join(CONTENT, base)) if f.lower().endswith(".md")]
    mds = [path_to_md(base, f) for f in files]
    return mds


def remove_duplicates(lis, key):
    seen = set()
    result = []
    for item in lis:
        if item[key] not in seen:
            result.append(item)
            seen.add(item[key])
    return result


@application.route('/')
@application.route('/index.html')
def index():
    return render_template('index.html')


@application.route('/projects/')
def projects():
    return render_template('projects.html', projects=get_mds('projects'), title='Projects')


@application.route('/projects/<name>/')
def project(name):
    project = path_to_md("projects", name + '.md')
    description = project.metadata.get("description", None)
    return render_template('project.html', project=project, title=project.metadata["name"], description=description)


@application.route('/people/')
def people():
    return render_template('people.html', people=get_mds('people'), title="People")


@application.route('/people/<name>/')
def person(name):
    person = path_to_md("people", name + '.md')
    email = person.metadata.get("email", None)
    email = None if email == None else obfuscate(email + '@' + DOMAIN)
    if 'scholar' in person.metadata and person.metadata['scholar'] in ALL_PAPERS:
        papers = ALL_PAPERS[person.metadata['scholar']]
    else:
        papers = {}
    return render_template('person.html', person=person, papers=papers, email=email, title=person.metadata["name"])


@application.route('/papers/')
def papers():
    flattened_years = {}
    for years_dict in ALL_PAPERS.values():
        for year, papers in years_dict.items():
            if year not in flattened_years:
                flattened_years[year] = []
            flattened_years[year] += papers
    
    for year, papers in flattened_years.items():
        flattened_years[year] = remove_duplicates(papers, 'title')

    return render_template('papers.html', papers=flattened_years, title="Papers")


@application.route('/contact/')
def contact():
    email = 'pscicon'
    return render_template('contact.html', email=obfuscate(email + '@' + DOMAIN), title="Contact")