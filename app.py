# Load the dependencies
from flask import Flask, render_template, request, jsonify
import plotly.express as px
import pandas as pd

# Create a Flask application
app = Flask(__name__)

# Load combined data
population_density_df = pd.read_csv('cleaned_data/combined_population_density.csv')
commute_df = pd.read_csv('cleaned_data/combined_commute.csv')
employment_df = pd.read_csv('cleaned_data/combined_employment.csv')
housing_df = pd.read_csv('cleaned_data/combined_housing.csv')
income_df = pd.read_csv('cleaned_data/combined_income.csv')
poverty_df = pd.read_csv('cleaned_data/combined_poverty.csv')   
edu_df = pd.read_csv('cleaned_data/combined_education.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    metric = request.form['metric']
    if metric == 'population_density':
        fig = px.bar(population_density_df, x='City', y='Population Density', title='Population Density Overview')
    elif metric == 'commute':
        fig = px.bar(commute_df, x='City', y='Commute Time', title='Commute Time by City')
    elif metric == 'employment':
        fig = px.bar(employment_df, x='City', y='Employment Rate', title='Employment Rate by City')
    elif metric == 'housing':
        fig = px.box(housing_df, x='City', y='Median Home Price', title='Median Home Price by City')
    elif metric == 'income':
        fig = px.bar(income_df, x='City', y='Median Household Income', title='Median Household Income by City')
    elif metric == 'poverty':
        fig = px.bar(poverty_df, x='City', y='Poverty Rate', title='Poverty Rate by City')
    elif metric == 'education':
        fig = px.box(edu_df, x='City', y='Education Level', title='Education Levels by City')
    graphJSON = fig.to_json()
    return graphJSON

if __name__ == '__main__':
    app.run(debug=True)