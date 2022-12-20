from flask import Flask, render_template, jsonify

# Import function that requests jobs from database
from database import load_jobs_from_db, load_specific_job

app = Flask(__name__)

@app.route('/')
def index():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)

@app.route('/api/jobs')
def return_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
  job = load_specific_job(id)
  if not job:
    return 'Page Not Found: 404'
  return render_template('job_details.html', job=job)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
