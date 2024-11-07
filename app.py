from flask import Flask, render_template, request
from fetch_data_by_webscrapping import DataFetcher
from export_data import ExportData
import confedential as c  # Assuming confedential stores your LinkedIn credentials
from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('WebPage.html')


@app.route('/fetch_jobs', methods=['POST'])
def fetch_jobs():
    # Your scraping code here
    username = request.form['username']
    password = request.form['password']
    job_title = request.form['job_title']
    job_location = request.form['job_location']
    size = request.form['size']

    # Process the data and fetch jobs (example logic)
    jobs = DataFetcher(username, password, job_title, job_location, int(size))
    job_df = jobs.data_frame

    ExportData(job_df)

    # Return the results to the page (could be JSON, or redirect to another page)
    return render_template('result.html')


@app.route('/display_json')
def display_json():
    # Load the JSON data from the file
    with open('data/job data.json', 'r') as file:
        data = json.load(file)

    # Pass the data to the template
    return render_template('ViewJson.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
