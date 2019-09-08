from flask import Flask, render_template
import mongo

app = Flask(__name__)


@app.route('/')
def index():
    skills_count = mongo.an(mongo.skills)
    skills_list = list(skills_count.keys())
    skills_values = list(skills_count.values())
    return render_template('index.html', skills_list=skills_list, skills_values=skills_values)
