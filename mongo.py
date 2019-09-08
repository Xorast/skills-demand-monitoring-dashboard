import os
import nltk
from pymongo import MongoClient

MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client.job_ads


skills = ['python', 'linux', 'react', 'api', 'flask',
          'django', 'oop', 'postgres', 'sql', 'nosql',
          'aws', 'azure', 'html', 'css', 'javascript',
          'java', 'docker', 'testing', 'agile', 'graduate', 'junior', 'senior', 'pandas', 'numpy']


def analysis(text, filter):
    words = nltk.tokenize.word_tokenize(text)
    filtered = [w for w in words if w in filter]
    freq_ = nltk.FreqDist(filtered)
    return freq_.most_common(len(filter))


def an(skills):
    skills_count = {skill: 0 for skill in skills}
    stored_ads = db.developer.find()
    for ad in stored_ads:
        freq = analysis(ad['text'].lower(), skills)
        for skill in freq:
            skills_count[skill[0]] += skill[1]
    skills_count = {skill: skills_count[skill] for skill in sorted(skills_count, key=skills_count.get, reverse=True)}
    return skills_count
