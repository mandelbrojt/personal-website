from flask import Flask, render_template, jsonify

# Import function that requests jobs from database
from database import load_jobs_from_db

app = Flask(__name__)

@app.route('/')
def index():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)

@app.route('/api/experience')
def return_experience():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
