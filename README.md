## **Boosting Marketing Efficiency: A Predictive Web App for Bank Campaigns**

**Live App Demo:** [**bank-deposit-prediction.streamlit.app**](https://thisishan-bank-deposit-prediction.streamlit.app/)


![Bank Deposit Prediction App Screenshot](../bank-deposit/app_screenshot.png)

### **Project Summary**
Banks spend significant marketing budget on broad, untargeted campaigns, leading to inefficient budget spend and high customer acquisition costs. This project builds and deploys a machine learning model that transforms marketing from a wide net into a precision spear, predicting which customers are most likely to subscribe to a term deposit.

### **Key Findings & Recommended Strategy**
The final model, a tuned Random Forest classifier, identified key predictors like client balance, age, and past campaign success. Based on a precision-recall analysis, the recommended **"Balanced Strategy"** delivers a strong **ROI of 205.3%** while still capturing a significant portion of potential subscribers.

For a detailed walkthrough of the analysis and business scenarios, 
[**View the full PDF Report: Boosting Marketing Efficiency.pdf**](./Boosting%20Marketing%20Efficiency.pdf)

### **Project Navigation**
- [**01_data_cleaning_and_EDA:**](./notebooks/01_data_cleaning_and_EDA.ipynb) This notebook covers the full data cleaning process and exploratory analysis. 
- [**02_feature_engineering_and_modeling:**](./notebooks/02_feature_engineering_and_modeling.ipynb) This notebook covers techniques applied for feature engineering and model training.
- [**03_business_impact_and_conclusion:**](./notebooks/03_business_impact_and_conclusion.ipynb) This notebook covers business analytics and the overall conclusion.

### **Technology Stack & Methods**
- **Technology:** Python, Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib, Joblib
- **Methods:** Data Cleaning & EDA, Feature Engineering (One-Hot Encoding), Class Imbalance Handling (SMOTE), Predictive Modeling (Logistic Regression, Random Forest, XGBoost), Hyperparameter Tuning (GridSearchCV), Model Evaluation.

### **Setup & How to Run**
1. Clone the repository to your local machine.
2. Create and activate a new virtual environment
3. Install the required dependencies in 'pip install -r requirements.txt'
4. To run the web locally: 'streamlit run app.py'

#### Data Source
*S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014*