
from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("template.html")

@app.route("/process", methods=["POST"])
def process_file():
    # Check if the post request has the file part
    if 'csvfile' not in request.files:
        return jsonify(error="No file part"), 400
    file = request.files['csvfile']
    
    # Check if the user did not select a file
    if file.filename == '':
        return jsonify(error="No selected file"), 400

    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file)
        # Filter rows based on keywords
        keywords = ["Failed", "Exception"]
        mask = df.applymap(lambda x: any([kw in str(x) for kw in keywords])).any(axis=1)
        filtered_df = df[mask]
        return filtered_df.to_html(index=False)
    except Exception as e:
        # Return a more detailed error message
        return jsonify(error=f"An error occurred: {str(e)}"), 500

if __name__ == "__main__":
    app.run(debug=True)
