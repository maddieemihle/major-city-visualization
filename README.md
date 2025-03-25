# Data Analysis & Visualization for Metropolitan City Metrics

This project is a part of the [Virtual Data Bootcamp at Vanderbilt University](https://bootcamps.vanderbilt.edu) with EdX. 

### Group Members 
* Madison Mihle
* Kat Hardy
* Rohan Pathak
* Travis Rogers
* Rodrigo Sosa

## Project Objective
The objective of this project was to analyze and visualize four key metrics across the top five major U.S. cities to gain insights into their demographic, economic, social, and quality-of-life characteristics. By examining data such as population distribution, economic performance, health behaviors, and racial demographics, the project aimed to:

* Identify Trends and Patterns: Highlight how cities differ in terms of economic stability, health outcomes, and population diversity.
* Understand Urban Challenges: Explore disparities in metrics like income, unemployment, and health behaviors to identify areas where cities face challenges.
* Support Data-Driven Decision Making: Provide policymakers, urban planners, and stakeholders with actionable insights to address inequalities and improve quality of life.
* Promote Public Awareness: Use visualizations like tables, maps, and charts to make complex data accessible and engaging for a broader audience.

By integrating these metrics, the project helps show the interconnectedness of economic, demographic, and social metric factors to prove which city would be considered the "best" possible city to live in. 

### Methods Used
* Descriptive Statistics 
* Data Visualization

### Tools and Technologies Used
* Python: For data cleaning, analysis, and static visualizations.
* Pandas: For data manipulation and preparation.
* Jupyter Notebook: For exploratory data analysis.
* Matplotlib/Seaborn: For static visualizations.
* Plotly/D3.js: For interactive charts.
* Leaflet.js: For interactive maps.
* HTML/CSS: For structuring and styling the dashboard.
* JSON: For storing and transferring cleaned data.

## Introduction
It is defined by the [U.S. Census Bureau](https://www.census.gov) (2020) that a metropolitan city consists of ____ or higher in population. These urban cities are dynamic hubs of economic activity, cultural diversity, and social interaction. But what makes the "perfect city,” and what are the ultimate qualities that make these cities what they are today? There are several challenges that various cities face in regard to population growth, economic disparities, health outcomes, and other demographics. Using these factors is essential for policymakers, urban planners, and stakeholders to make informed decisions for the quality of life for residents. 

This project focuses on analyzing and visualizing key metrics across five major US cities: Chicago, Houston, New York, Los Angeles, and Phoenix. By examining demographic, economic, housing, and quality of life metrics (given by the U.S. Census Bureau), we aim to uncover trends, disparities, and correlations that define the unique characteristics of each city, specifically around the time of the last U.S. Census in 2020. 

The analysis leverages data from reliable sources, including the U.S. Census Bureau and public health databases, to answer critical questions such as:

* Which cities have higher population density? Does that affect economic stability, health outcomes, and quality of life? 
* If a city is larger, will there be a higher median income but a higher unemployment rate? How do these cities differ in terms of economic stability? 
* What are the key factors influencing population diversity and quality of life? (i.e., if a city is larger, will it have a higher median age and education level?)
* How does city size relate to poverty rates and median rent? 

Through interactive and static visualizations, including maps, tables, and various charts, the goal is to provide insights that foster a deeper understanding of urban challenges and opportunities, ultimately contributing to developing more equitable and sustainable cities.

## Project Description

### Part 1: Define the Objective 
As a group, we discussed various topics related to metropolitan cities and how we can analyze them by laying out the project’s goal (analyzing and visualizing key metrics) across the five major U.S. cities as defined by the [U.S. Census Database](https://www.census.gov). 

Questions were identified to be answered, such as trends, disparities, and correlation among the metrics.

### Part 2: Data Collection 
Raw data was gathered for our five major cities (Chicago, New York, LA, Phoenix, and Houston) from the 2020 [U.S. Census Database](https://www.census.gov). (Note: also sourced below). We used various criteria and table codes to pull the tables within the four metrics. After codes were found, the data was cleaned and organized into new CSV files. 

Metric Codes: 
* ACS Median Age: Table DP05 
* Racial Demographics: Table DP05
* Education Level: S1501
* Median Household Income: S1901
* Unemployment Rate: Table S2301
* Median Rent: DP04
* Commute Time: S0801
* Health Outcomes: pulled directly from Data Commons 
* Air Quality Index: pulled directly from the EPA website

### Part 3: Data Cleaning & Preparation 
The raw data was loaded into Python using Pandas to perform data cleaning tasks, such as: 
* Handling missing or inconsistent values
* Standardize column names and formats 
* Filter data to include only relevant metrics and the year of 2020

After the data was saved to new "cleaned" CSV files (located within each city_data folder) and JSON files for further analysis and visualization. 

### Part 4: Exploratory Data Analysis  
After cleaned datasets were loaded and previewed into the Master Analysis Jupyter Notebook, an analysis was performed to look at descripive statistics to understand the distribution of each metric within five cities. Trends were identified, as well as any correlations within the data. Visualization using Matplotlib and Seaborn was used to validate the data. 

### Part 5: Data Visualization 
Interactive and static visualizations were created to represent the data. Some of the static visualizations included Matplotlib and Seaborn for bar charts, line graphs, and scatter plots. The interactive visualizations included Plotly, D3.js, and Leaflet.js for dynamic charts and maps. Bubble maps were used to represent population density, line graphs for health trends and behaviors, and tables to display economic and demographic data. 

### Part 6: Create a Separate HTML file for Visualization 
An HTML file was created to serve as a dashboard for visualizing the data using HTML and CSS for layout and styling. For the interactive visualizations, D3.js and Leaflet.js were used for the following: 
* Dropdown menus for selecting city metrics (i.e., selecting one city to see the metrics for income, health behaviors, age, etc.)
* Interactive maps with bubble markers and population density 
* Tables generated based on user selections 

The cleaned JSON files were lined to the HTML file for dynamic loading. JavaScript was also used to fetch the appropriate JSON file based on the user’s selection to update the table or map via Lealet.js.

### Part 7: Analyze and Interpret Results
The visualizations were analyzed to identify key insights: 
* Trends in economic stability, quality of life, population density and dispersion, health behaviors, and demographics.
* Disparities between cities regarding income, unemployment, and health outcomes.
* Correlations between metrics.

The findings were summarized to answer the project’s key questions.

## Results & Analysis 
The analysis reveals significant trends, disparities, and correlations across the five major U.S. cities (Chicago, Houston, New York, Los Angeles, and Phoenix) in terms of demographic, economic, housing, and quality of life demographic metrics.

### Demographic Metrics 
Demographic metrics provide a strong understanding of the population composition within urban areas, offering insights into age distribution, racial diversity, and educational attainment. These metrics are critical for analyzing the social fabric of cities and their potential for growth and inclusivity.

This visualization highlights the five cities under analysis, showcasing their population sizes and exploring factors contributing to their growth. The results are as follows:

#### **Growth Distribution**:

Based on the conclusions drawn and results, New York City has the largest population, significantly outpacing the other five cities, while Phoenix has the smallest population among the five cities. NYC’s size presents unique challenges for infrastructure, housing, and public services. However, cities like Phoenix and Houston show higher population growth rates, indicating their appeal as emerging urban hubs.

#### **Median Age and Education Level by Population Density**:
When looking at Population growth, it was found that: 
1. **Population Density and Median Age**:
   - Cities with higher population density, such as New York and Chicago, tend to have slightly higher median ages than less dense cities like Phoenix and Houston.
    - This could indicate that denser cities attract older populations due to factors like established careers, access to amenities, or higher living costs that younger individuals may avoid.

2. **Population Density and Education Level**:
    - Cities with higher population density, such as New York and Chicago, also exhibit higher percentages of individuals with a bachelor's degree or higher.
    - This suggests that denser cities may have better access to educational institutions or attract highly educated individuals due to job opportunities in specialized fields.

3. **Inverse Relationship for Less Dense Cities**:
    - Less dense cities like Phoenix and Houston have lower education levels and younger populations. These cities may attract younger individuals due to affordability and job opportunities in industries requiring less formal education.

Conclusion: Higher population density correlates with higher education levels and slightly older populations. This highlights the role of urbanization in shaping demographic and educational patterns, with denser cities serving as hubs for education and career-driven individuals.

![Population Density](https://github.com/maddieemihle/major-city-visualization/blob/main/Images/median_age_and_education_level.png?raw=true)


### Economic Metrics 
Economic metrics provide valuable insights into a city’s financial health and stability. Analyzing data such as Median Household Income and Unemployment Rate can assess the economic disparities and opportunities within urban areas. These metrics allow us to explore the relationship between city size and economic performance. 

#### **Median Household Income vs Unemployment Rate**:
When looking at the visualization, it can be inferred that cities with a higher population density have a high median income but also relatively higher unemployment. Ex: 
- **New York**: High population density and high median income, but also a relatively higher unemployment rate compared to other cities.
- **Chicago**: Moderate population density and income, with a mid-range unemployment rate.
- **Phoenix**: Low population density, moderate income, and the lowest unemployment rate among the cities.
- **Los Angeles**: Moderate population density and income, with a slightly higher unemployment rate.
- **Houston**: Low population density, lower income, and a relatively low unemployment rate.

This shows that high-density cities (e.g., New York) face challenges such as higher unemployment rates, possibly due to competition, the cost of living, or economic disparities.

![Median Household Income vs Unemployment](https://github.com/maddieemihle/major-city-visualization/blob/main/Images/median_income_vs_unemployment_rate.png?raw=true)

Conclusion: while higher-income cities may have lower unemployment rates, other factors like population density, cost of living, and economic structure also play significant roles. Policymakers should consider these dynamics when addressing unemployment and income disparities in urban areas.

### Housing Metrics 
The visualization of poverty rate and median rent by population density rank provides insights into the relationship between urban density, economic conditions, and housing affordability. The results are as follows: 

#### **Median Age and Education Level by Population Density**:
When looking at the visualization, it can be inferred that cities with lower population density (e.g., Houston and Phoenix) tend to have slightly higher poverty rates compared to denser cities like New York and Chicago. However, median rent increases with population density. For example, New York, the most densely populated city, has the highest median rent, while Houston, the least dense, has the lowest. High-density cities like New York and Los Angeles face a dual challenge of high rents and significant poverty rates, highlighting affordability issues for low-income residents.

![Median Rent](https://github.com/maddieemihle/major-city-visualization/blob/main/Images/poverty_rate_and_median_rent.png?raw=true)

Conclusion: the visualization shows the complex interplay between population density, poverty, and housing costs, emphasizing the need for tailored strategies to address economic and housing challenges in different urban contexts.

### Quality of Life Metrics 
Quality of life is a multifaceted concept encompassing various factors influencing the well-being and satisfaction of individuals within a city. Using data from the 2020 Census Database, the American Community Survey (ACS) by the U.S. Census Bureau, and the Environmental Protection Agency (EPA) Air Quality Index report, this analysis examines key metrics such as commute time, health behaviors, and air quality. These metrics provide valuable insights into the sustainability and livability of urban environments. The results are as follows: 

#### **Commute Time**:
Cities like New York use public transportation significantly more, while cities like Houston and Phoenix depend more on personal vehicles. This could also suggest that more "urbanized" cities are more walking-friendly based on well-thought-out city planning. 

![Commute Time](https://github.com/maddieemihle/major-city-visualization/blob/main/Images/commute_modes_by_city.png?raw=true)

#### **Health Behaviors**:
Health behaviors provide critical insights into the well-being and lifestyle choices of populations within urban areas. The data highlights key metrics such as obesity rates, smoking prevalence, physical activity levels, and sleep patterns. These behaviors are directly linked to chronic diseases, mental health, and overall quality of life. The results are as follows: 

1. **Obesity and Physical Inactivity**: Cities like Houston and Phoenix show higher rates of obesity and physical inactivity, which are linked to poorer health outcomes.
2. **Smoking and Binge Drinking**: Chicago has notable rates of smoking and binge drinking, indicating areas for public health intervention.
3. **Sleep Patterns**:** New York City, known as "the city that never sleeps," has a higher percentage of adults reporting insufficient sleep.

![Health Behaviors](https://github.com/maddieemihle/major-city-visualization/blob/main/Images/health_behaviors.png?raw=true)

#### **Air Quality Index**:
The data on the number of good air quality days versus bad air quality days provides insights into the environmental conditions of the analyzed counties. Here are some insights: 

1. **Environmental Quality**:
   - Counties with a higher number of good air quality days (e.g., New York) indicate better environmental conditions, likely due to stricter pollution controls, better urban planning, or favorable geographic factors.
   - Counties with more bad air quality days (e.g., Maricopa County (Phoenix)) may face challenges such as industrial emissions, vehicle pollution, or unfavorable weather patterns that trap pollutants.

2. **Urbanization and Pollution**:
    - Urbanized areas like Los Angeles, despite having a significant number of good days, still show a notable number of bad air quality days, reflecting the impact of high population density, traffic, and industrial activities.

3. **Health Implications**:
    - Counties with more bad air quality days may have higher risks of respiratory and cardiovascular diseases among residents, emphasizing the need for public health interventions.

4. **Geographic and Climatic Factors**:
    - Geographic features like valleys (e.g., Los Angeles) can trap pollutants, leading to worse air quality days. Conversely, areas with favorable wind patterns or less industrial activity may experience better air quality.

![AQI Good](https://github.com/maddieemihle/major-city-visualization/blob/main/Images/good_air_quality_days_by_county.png?raw=true)

![AQI Bad](https://github.com/maddieemihle/major-city-visualization/blob/main/Images/bad_air_quality_days_by_county.png?raw=true)

## Conclusion
Each city has its own strengths and weaknesses. New York has high economic opportunities but significant income inequality and housing challenges. Los Angeles, with its diverse and economically proven city, faces high unemployment and health behavior concerns. Houston, with its rapid growth and diversity but growing health behavior concerns and "commuteability". Chicago with its economic challenges. Phoenix, with its emerging, growing urban hub, faces challenges with infrastructure. 

By leveraging insights from demographic, economic, health, and racial metrics, policymakers and stakeholders can develop targeted strategies to improve quality of life and foster sustainable growth in urban areas.

### Challenges 
One challenge we faced during this was the amount of information given within a dataset from the U.S. Census Database. This called for various cleaning methods and figuring out which "deeper" metrics would be best for each. While the datasets were specific, most of the information given did not pertain and would need to be sorted into separate CSV files in the end. However, once we were able to get it sorted, we were able to analyze and get the data into our database fairly quickly. We also had several other metrics and were planning on selecting 10 major metropolitan cities. We quickly discovered that it was easier to pick the top 5 cities based on population. We believe this provided more powerful insight to help us look further into our data and findings. 

## Datasets Used: 
U.S. Census Bureau: 
* ACS Median Age: [Table DP05](https://data.census.gov/table?q=DP05&y=2020)
* Racial Demographics: [Table DP05](https://data.census.gov/table?q=DP05&y=2020)
* Education Level: [Table S1501](https://data.census.gov/table?q=S1501&y=2020)
* Median Household Income: [Table S1901](https://data.census.gov/table?q=S1901&y=2020)
* Unemployment Rate: [Table S2301](https://data.census.gov/table?q=S2301&y=2020)
* Median Rent: DP04[Table DP04](https://data.census.gov/table?q=DP04&y=2020)
* Commute Time: S0801 [Table S0801](https://data.census.gov/table?q=S0801&y=2020)
* Environmental Protection Agency: [Air Quality Index](https://aqs.epa.gov/aqsweb/airdata/download_files.html)
* City Health Behaviors
    * [Chicago](https://datacommons.org/place/geoId/1714000?category=Health)
    * [New York](https://datacommons.org/place/geoId/3651000?category=Health)
    * [LA](https://datacommons.org/place/geoId/0644000?category=Health)
    * [Phoenix](https://datacommons.org/place/geoId/0455000?category=Health)
    * [Houston](https://datacommons.org/place/geoId/4835000?category=Health)


## Featured Notebooks/Analysis
* [Master Notebook](https://github.com/maddieemihle/major-city-visualization/blob/main/Master%20Analysis.ipynb)
* [HTML File](https://github.com/maddieemihle/major-city-visualization/blob/main/data_files/index.html)
* [HTML Map](https://github.com/maddieemihle/major-city-visualization/blob/main/data_files/map.html)
* [Chicago Notebook](https://github.com/maddieemihle/major-city-visualization/blob/main/data_files/chicago_data/chicago_dataset.ipynb)
* [Houston Notebook](https://github.com/maddieemihle/major-city-visualization/blob/main/data_files/houston_data/Houston_cleaned.ipynb)
* [New York Notebook](https://github.com/maddieemihle/major-city-visualization/blob/main/data_files/ny_data/New%20York.ipynb)
* [LA](https://github.com/maddieemihle/major-city-visualization/blob/main/data_files/la_data/Los%20Angeles%20Code.ipynb)
* [Phoenix](https://github.com/maddieemihle/major-city-visualization/blob/main/data_files/phoenix_data/data_cleaning_phoenix.ipynb)

## Slideshow Presentation Link

## Sources Cited 

Data Commons. (2023). City Health Behaviors. Retrieved from https://datacommons.org.

D3.js. (2023). Data-Driven Documents. Retrieved from https://d3js.org.

Leaflet.js. (2023). Interactive Maps. Retrieved from https://leafletjs.com.

National Geographic Society. (2023). Population Density. Retrieved from [https://education.nationalgeographic.org/resource/population-density](https://education.nationalgeographic.org/resource/population-density).

Plotly. (2023). Interactive Data Visualization. Retrieved from https://plotly.com.

Python Software Foundation. (2023). Python Language Reference, version 3.10. Retrieved from https://www.python.org.

U.S. Census Bureau. (2020). Population Density: A Measurement of Population per Unit Area. Retrieved from [https://www.census.gov](https://www.census.gov).

U.S. Census Bureau. (2020). Table S1501: Educational Attainment. Retrieved from https://data.census.gov/table?q=S1501&y=2020.

U.S. Census Bureau. (2020). Table DP05: ACS Demographic and Housing Estimates. Retrieved from https://data.census.gov.

U.S. Census Bureau. (2020). Table S1901: Income in the Past 12 Months (in 2020 Inflation-Adjusted Dollars). Retrieved from https://data.census.gov/table?q=S1901&y=2020.

U.S. Census Bureau. (2020). Table S2301: Employment Status. Retrieved from https://data.census.gov/table?q=S2301&y=2020.

U.S. Census Bureau. (2020). Table DP04: Selected Housing Characteristics. Retrieved from https://data.census.gov/table?q=DP04&y=2020.

U.S. Census Bureau. (2020). Table S0801: Commuting Characteristics by Sex. Retrieved from https://data.census.gov/table?q=S0801&y=2020.

U.S. Environmental Protection Agency. (2025). Download data files. Air Quality System (AQS). Retrieved March 21, 2025, from https://aqs.epa.gov/aqsweb/airdata/download_files.html

Visual Studio Code. (2023). Code Editor. Retrieved from https://code.visualstudio.com.

