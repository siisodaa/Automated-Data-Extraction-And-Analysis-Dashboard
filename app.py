from flask import Flask, render_template, jsonify
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = Flask(__name__)

# Route to display dashboard
@app.route('/')
def dashboard():
    return render_template("dashboard.html")

# Route to provide data for Plotly charts
@app.route('/data')
def data():
    df = pd.read_csv("data.csv")  # Load the scraped data

    # Generate example data for a chart (update with your actual analysis)
    fig = px.bar(df, x="Column1", y="Column2", title="Data Analysis")
    graphJSON = fig.to_json()
    return jsonify(graphJSON)

if __name__ == "__main__":
    app.run(debug=True)
