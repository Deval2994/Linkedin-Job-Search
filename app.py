"""
Description: This Flask app lets users scrape job listings and export the data in JSON, CSV, or Excel formats.
             Users input job details, and the app scrapes the data, displays it, and allows
             downloading the results in the desired format.
"""

from flask import send_file
from fetch_data_by_webscrapping import DataFetcher
from export_data import ExportData
from flask import Flask, render_template, request
import json

app = Flask(__name__)

JSON_FILE_PATH = 'data/job data.json'
CSV_FILE_PATH = 'data/job data.csv'
EXCEL_FILE_PATH = 'data/job data.xlsx'


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
    ExportData(job_df, 'csv')
    ExportData(job_df, 'excel')

    # Return the results to the page (could be JSON, or redirect to another page)
    return render_template('result.html')


@app.route('/display_json')
def display_json():
    # Load the JSON data from the file
    with open('data/job data.json', 'r') as file:
        data = json.load(file)

    # Pass the data to the template
    return render_template('ViewJson.html', data=data)


@app.route('/download_json')
def download_json():
    # Provide the JSON file for download
    return send_file(JSON_FILE_PATH, as_attachment=True)


@app.route('/download_csv')
def download_csv():
    # Provide the CSV file for download
    return send_file(CSV_FILE_PATH, as_attachment=True)


@app.route('/download_excel')
def download_excel():
    # Provide the Excel file for download
    return send_file(EXCEL_FILE_PATH, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
