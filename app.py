# # Load the dependencies
# from flask import Flask, render_template, request, jsonify
# import plotly.express as px
# import pandas as pd

# # Create a Flask application
# app = Flask(__name__)

# # Load combined data
# population_density_df = pd.read_csv('cleaned_data/combined_population_density.csv')
# combined_commute_df = pd.read_csv('cleaned_data/combined_commute.csv')
# employment_df = pd.read_csv('cleaned_data/combined_employment.csv')
# housing_df = pd.read_csv('cleaned_data/combined_housing.csv')
# income_df = pd.read_csv('cleaned_data/combined_income.csv')
# poverty_df = pd.read_csv('cleaned_data/combined_poverty.csv')   
# edu_df = pd.read_csv('cleaned_data/combined_education.csv')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/plot', methods=['POST'])
# def plot():
#     metric = request.form['metric']
#     if metric == 'population_density':
#         fig = px.bar(population_density_df, x='City', y='Population Density', title='Population Density Overview')
#     elif metric == 'commute':
#         fig = px.bar(combined_commute_df, x='City', y='Commute Time', title='Commute Time by City')
#     elif metric == 'employment':
#         fig = px.bar(employment_df, x='City', y='Employment Rate', title='Employment Rate by City')
#     elif metric == 'housing':
#         fig = px.box(housing_df, x='City', y='Median Home Price', title='Median Home Price by City')
#     elif metric == 'income':
#         fig = px.bar(income_df, x='City', y='Median Household Income', title='Median Household Income by City')
#     elif metric == 'poverty':
#         fig = px.bar(poverty_df, x='City', y='Poverty Rate', title='Poverty Rate by City')
#     elif metric == 'education':
#         fig = px.box(edu_df, x='City', y='Education Level', title='Education Levels by City')
#     graphJSON = fig.to_json()
#     return graphJSON

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# Load the datasets from Chicago
chicago_commute_df = pd.read_csv('data_files/chicago_data/chi_cleaned_csv/cleaned_chi_commute.csv')
chicago_unemployment_df = pd.read_csv('data_files/chicago_data/chi_cleaned_csv/cleaned_chi_employment.csv')
chicago_rent_df = pd.read_csv('data_files/chicago_data/chi_cleaned_csv/cleaned_chi_rent.csv')
chicago_income_df = pd.read_csv('data_files/chicago_data/chi_cleaned_csv/cleaned_chi_income.csv')
chicago_edu_df = pd.read_csv('data_files/chicago_data/chi_cleaned_csv/cleaned_chi_edu.csv')
chicago_age_df = pd.read_csv('data_files/chicago_data/chi_cleaned_csv/cleaned_chi_age.csv')
chicago_race_df = pd.read_csv('data_files/chicago_data/chi_cleaned_csv/cleaned_chi_race.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    metric = request.form['metric']
    if metric == 'commute':
        fig = px.bar(chicago_commute_df, x='Category', y='Value', title='Commute Data')
    elif metric == 'unemployment':
        fig = px.bar(chicago_unemployment_df, x='Category', y='Value', title='Unemployment Data')
    elif metric == 'rent':
        fig = px.bar(chicago_rent_df, x='Category', y='Value', title='Rent Data')
    elif metric == 'income':
        fig = px.bar(chicago_income_df, x='Category', y='Value', title='Income Data')
    elif metric == 'education':
        fig = px.bar(chicago_edu_df, x='Category', y='Value', title='Education Data')
    elif metric == 'age':
        fig = px.bar(chicago_age_df, x='Category', y='Value', title='Age Data')
    elif metric == 'race':
        fig = px.bar(chicago_race_df, x='Category', y='Value', title='Race Data')
    graphJSON = fig.to_json()
    return jsonify(graphJSON)

if __name__ == '__main__':
    app.run(debug=True)