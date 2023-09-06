# Data Dog Error Filtering Tool

## Description
The Data Dog Error Filtering Tool allows users to upload logs in CSV format and filters out exceptions, failures, and errors. Built using Flask, it provides an interactive web interface to process and view the filtered results.

## Structure
- `flask_app.py`: The main Flask application file.
- `keywords_flask_app.py`: Contains logic for keyword filtering (exceptions, failures, errors).
- `templates`: Directory containing the HTML templates used by the Flask application.

## Installation
1. Ensure you have Python and Flask installed.
2. Clone or download the repository.
3. Navigate to the project directory.
4. Install any required packages using pip:
```
pip install -r requirements.txt
```
(Note: The actual dependencies would need to be listed in a `requirements.txt` file, which is not currently provided.)

## Usage
1. Run the Flask application:
```
python flask_app.py
```
2. Navigate to the provided localhost URL in your web browser.
3. Use the web interface to upload your CSV log files.
4. Click on the "Filter" button to process the logs and view the filtered results containing exceptions, failures, and errors.



*pip install Flask pandas*

*python keywords_flask_app.py*

*Then go to http://127.0.0.1:5000/*

