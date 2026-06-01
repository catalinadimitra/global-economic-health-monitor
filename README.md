# Global Economic Health Monitor

An end-to-end data engineering and analytics pipeline designed to ingest, clean, process, analyze, and predict macroeconomic indicators leveraging World Bank public data.

## Project Architecture

The architecture maps out a complete big data and analytics lifecycle across distinct layers:

1. Data Acquisition Layer: Custom Python scripts connecting directly to the World Bank REST API to stream raw country indicator data.
2. Big Data Processing Layer: DuckDB integration to showcase local, column-store big data framework scaling and relational aggregations.
3. Preprocessing & Feature Engineering Layer: Multi-stage data transformations including targeted country income categorization and time-lag computation utilizing Pandas.
4. Machine Learning & Predictive Analytics Layer: Comparative baseline modeling evaluating Linear Regression and RandomForestRegressor metrics to identify key drivers of global GDP variance.
5. Interactive Business Intelligence Layer: A live Tableau Public dashboard compiling choropleth geographic mappings and cross-filtered historical macroeconomic trend timelines.

## Data Schema & Engineered Metrics

The dataset maps the following metrics across global economic zones from 2000 to present:
* `gdp_growth`: Annual percentage growth rate of Gross Domestic Product.
* `gdp_growth_lag1` / `gdp_growth_lag2`: Historical time lags capturing economic momentum.
* `inflation`: Consumer price inflation index.
* `unemployment`: Total unemployment as a percentage of the labor force.
* `govt_debt_pct_gdp`: Central government debt indicators.
* `income_group`: Low, middle, and high-income country classifications.

## Installation & Setup

Ensure Python 3.9+ is installed on your local system environment.

1. Clone the repository:
   git clone <your-repository-url>

2. Install the necessary data science dependencies:
   pip install pandas scikit-learn requests matplotlib seaborn duckdb

3. Execution order for notebooks and scripts:
   * Run `src/data_collection.py` to extract raw API indicator lines.
   * Open and run `notebooks/01_preprocessing.ipynb` to clean data structures.
   * Open and run `notebooks/01b_spark_processing.ipynb` to verify the big data relational aggregation table.
   * Open and run `notebooks/02_eda.ipynb` and `notebooks/03_modeling.ipynb` for analytics.

## Key Findings & Business Value

### 1. Feature Dominance & Economic Momentum
Predictive modeling experiments successfully isolated the core drivers of global growth variance. The feature importance mapping from the `RandomForestRegressor` revealed that **historical economic trajectory (`gdp_growth_lag1`) is the single most critical predictor of future GDP outcomes**. It significantly outranked static, structural national features such as total central government debt or unemployment ratios. This proves that short-term economic momentum and policy trajectory hold far greater predictive value for business intelligence than long-term structural debt constraints.

### 2. Macroeconomic Risk & Structural Volatility Profiles
Exploratory data analysis uncovered a distinct structural trade-off between economic stability and development velocity across income cohorts:
* **High-Income Economies:** Exhibit structurally lower average annual GDP growth rates but maintain maximum resilience with tightly bounded variance, shielding them from severe macroeconomic shocks.
* **Emerging & Low-Income Markets:** Offer significantly higher growth ceilings, yet suffer from severe volatility profiles. These regions are uniquely vulnerable to rapid inflation spikes and external shocks (such as the 2020 global downturn), highlighting higher risk profiles for foreign direct investment.

### 3. Predictive Framework Nuances
The comparison between standard linear algorithms and ensemble methods exposed the complexity of global economic forecasting. While a basic Linear Regression struggled to capture non-linear market shocks, the Random Forest architecture successfully minimized residual errors during training by prioritizing non-linear feature combinations (such as co-dependencies between inflation spikes and debt-to-GDP levels). This demonstrates that global economic health forecasting requires robust machine learning frameworks capable of handling multi-variable, non-linear interactions rather than simple historical averages.