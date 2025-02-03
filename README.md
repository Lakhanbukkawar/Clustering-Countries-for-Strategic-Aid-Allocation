# Clustering Countries for Strategic Aid Allocation

## Problem Statement

HELP International is an international humanitarian NGO committed to fighting poverty and providing essential relief to people in underdeveloped countries, particularly during times of disasters and natural calamities.

Recently, HELP International raised $10 million in funding, and the CEO is tasked with making a strategic decision on how to allocate these resources effectively. The goal is to identify and prioritize countries that are in the greatest need of aid. As a Data Scientist, your responsibility is to categorize countries based on socio-economic and health factors, which will guide the allocation process to ensure the most effective use of the funds.

## Objective

The project’s objective is to use data-driven analysis to categorize countries and identify those in urgent need of financial assistance. By leveraging socio-economic and health data, we aim to provide actionable insights for the optimal distribution of the $10 million funds to the most deserving countries.

### Key Needs

- **Strategic Resource Allocation**: Maximize the impact of the $10 million by prioritizing countries that need aid the most, ensuring efficient resource distribution.
- **Data-Driven Decision Making**: Transition from traditional, subjective decision-making methods to evidence-based approaches, enhancing the precision and impact of aid distribution.
- **Targeted Intervention**: Tailor aid initiatives to address the specific challenges of countries at different stages of development, improving outcomes in poverty alleviation and community development.

### Practical Use of the Solution

- **Country Categorization**: The model will segment countries based on key socio-economic and health indicators, enabling a clear prioritization of nations in need.
- **Strategic Decision Support**: The insights will assist the CEO in making informed, data-driven decisions regarding how to allocate aid resources effectively.
- **Resource Optimization**: By focusing on countries with the greatest need, the model ensures that every dollar of aid has the highest potential for positive impact.

## Why This Approach Was Used

In this project, clustering techniques were selected to address the challenge of identifying countries that require aid based on a diverse set of socio-economic and health indicators. Traditional methods of aid allocation often rely on expert opinions or arbitrary thresholds, which may not fully capture the complexity of each country's situation. By using unsupervised learning, specifically clustering, we gain several advantages:

1. **Data-Driven Grouping**: Clustering automatically segments countries into meaningful groups based on the patterns in the data, reducing bias and ensuring that decisions are based on objective criteria.
2. **Handling Complexity**: Socio-economic and health data includes various dimensions that are often highly correlated. Clustering techniques can handle these multi-dimensional data points and identify natural groupings, something that traditional statistical methods might struggle with.
3. **Scalability**: Clustering allows us to apply the same approach to any number of countries or variables. As more data becomes available, the model can be retrained or adjusted to account for new factors, ensuring the model remains scalable and adaptable.
4. **Unsupervised Learning**: Since the data does not come with pre-labeled categories (e.g., countries already marked as "needing aid"), unsupervised learning was the natural choice. It lets us uncover hidden structures in the data without needing predefined labels.
5. **Clear Prioritization**: Clustering helps group countries with similar characteristics, making it easier to prioritize aid. For example, countries with high child mortality, low income, and poor health spending may be grouped together, signaling that these nations require more immediate support.
6. **Transparency and Accountability**: The use of clustering models ensures that the allocation process is transparent. Stakeholders can trace the decisions back to the data and understand the factors influencing aid distribution.

## Dataset Overview

You can access the dataset via the following [Google Drive link](https://drive.google.com/file/d/1IRQWbO9m-c93XjDsbtt2nqv5RVldVPzj/view?usp=drive_link).

### Data Description

- **Country**: Name of the country.
- **Child_mort**: Deaths of children under 5 years of age per 1,000 live births.
- **Exports**: Exports of goods and services per capita, as a percentage of GDP per capita.
- **Health**: Total health spending per capita, as a percentage of GDP per capita.
- **Imports**: Imports of goods and services per capita, as a percentage of GDP per capita.
- **Income**: Net income per person.
- **Inflation**: Measurement of the annual growth rate of GDP.
- **Life_expec**: The average number of years a newborn child is expected to live, assuming current mortality patterns remain constant.
- **Total_fer**: The number of children born to each woman, assuming current age-fertility rates.
- **Gdpp**: GDP per capita, calculated as Total GDP divided by the total population.

## Approach

### Block 1: Data Visualization with Tableau

Effective data visualization plays a crucial role in understanding the socio-economic and health conditions of countries. Using Tableau, we can create dynamic dashboards to gain valuable insights for aid allocation.

#### Suggested Visualizations

- **Overall Development**:  
  - *Heatmap*: Visualize the development levels across countries using indicators like **Life_expec** and **Income**.
  - *Scatter Plot Matrix*: Examine the relationships between all variables to identify clusters or trends.

- **Health and Mortality**:  
  - *Bar Chart*: Compare child mortality rates across countries.
  - *Scatter Plot*: Assess the relationship between **Life_expec** and **Health** spending.

- **Economic Indicators**:  
  - *Histogram*: Understand the distribution of **Income** across countries.
  - *Scatter Plot*: Examine the relationship between **Exports** and **Imports** as percentages of GDP.

These visualizations provide an interactive way to explore the data, helping to identify patterns and outliers that could influence aid allocation decisions.

### Block 2: Exploratory Data Analysis (EDA) and Hypothesis Testing

In this step, we delve deeper into the dataset to uncover hidden insights and validate hypotheses.

#### Key EDA Steps

- **Data Cleaning**: Address missing values through imputation techniques (e.g., mean/median filling) and handle outliers using IQR or winsorization.
- **Univariate Analysis**: Explore the distribution of numerical features (e.g., **Child_mort**, **Income**, **Life_expec**) using histograms, box plots, and KDE plots.
- **Bivariate Analysis**: Investigate correlations and relationships between variables using scatter plots and correlation matrices.

#### Hypothesis Testing

- **Health Spending and Life Expectancy**: Test if higher health spending leads to increased life expectancy.
- **Income and Child Mortality**: Analyze the correlation between income levels and child mortality rates.
- **Inflation and Economic Stability**: Examine if higher inflation correlates with lower GDP per capita.

### Block 3: Machine Learning Modeling

We employ unsupervised machine learning techniques to categorize countries based on their socio-economic and health factors. This allows us to determine which countries are in greatest need of aid.

#### Data Preprocessing

- **Missing Value Imputation**: Apply appropriate imputation methods for missing data.
- **Normalization**: Standardize numerical features to ensure equal contribution to clustering.
- **Feature Engineering**: Generate new features based on thresholds or ratios (e.g., **Exports/Imports** ratio).

#### Clustering Models

- **K-Means Clustering**: Group countries into predefined clusters based on their development needs.
- **Hierarchical Clustering**: Create a hierarchical structure of clusters to explore different levels of granularity.
- **DBSCAN**: Identify clusters of arbitrary shapes and handle outliers effectively.

#### Model Evaluation

Use evaluation metrics such as the **Silhouette Coefficient** to assess clustering performance. Visualization techniques like PCA can help understand the separation of clusters.

### Block 4: Deployment

After training and evaluating the model, we deploy the solution via a Flask API for real-time predictions. This allows stakeholders to input country-specific data and receive aid allocation recommendations.

#### Steps for Deployment

1. **Environment Setup**: Create a virtual environment and install necessary libraries, such as Flask and scikit-learn.
2. **Model Serialization**: Serialize the trained model using pickle or joblib for efficient loading.
3. **API Development**: 
   - Define API endpoints to handle country data input.
   - Preprocess incoming data and make predictions using the model.
   - Return a JSON response with the predicted cluster/category.

4. **Web Interface (Optional)**: A simple web interface can be created for stakeholders to interact with the API.

## Benefits

- **Maximized Impact**: Ensure the most effective use of resources by directing aid to countries with the greatest need.
- **Efficient Resource Utilization**: Optimize the allocation of $10 million to maximize positive outcomes.
- **Improved Accountability**: Ensure transparency in decision-making through data-driven insights.

## Requirements

The following libraries are required for running this project. You can install them by using the `requirements.txt` file:

## Conclusion

This project demonstrates how data science techniques, specifically clustering, can aid in the strategic allocation of resources to improve lives across the globe. By categorizing countries based on socio-economic and health indicators, we provide actionable insights to help HELP International make informed, data-driven decisions in their fight against poverty.