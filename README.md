## **Boosting Marketing Efficiency: Drive Targeted Bank Campaigns by Customer Subscription Behavior**

### **Business Problem**
Banks spend significant marketing budget on broad, untargeted campaigns, leading to inefficient budget spend and high customer acquisition costs. With limited marketing resources, they need to identify how to prioritize outreach, thus minimize missed opportunities and wasted effort on uninterested leads. The core challenge is to **transform marketing from a wide net into a precision spear.**

### **Hypothesis & Proposed Solution**
**Hypothesis:** Customers with certain demographic profiles (age, job stability) and positive past campaign reponses are significantly more likely to subscribe to term deposits. A logistic regression model can identify these high-probability segments.

**Proposed Solution:** Build a classification model that generates probability scores for targeted outreach. The core focus is analyzing the business trade-off between **precision and recall** - enabling the bank to choose between high-efficiency campaigns (targeting only top prospects) or broader outreach to maximize total conversions.

### **Key Questions to Answer**
- Which customer attributes are the strongest predictors of term deposit subscription, and how can these insights inform future marketing and targeting strategy?

- What is the quantifiable business trade off between broader outreach campaign (high recall) and targeted marketing strategy (high precision)?

- What is the recommended data-driven strategy based on model performance that the bank should implement to balance maximum marketing ROI with the risk of missing potential conversions?

### **Key Findings**
- **Key Predictors:** The model confirmed that the strongest predictors of a subscription are a client's financial health ('balance', 'housing'/'loan' status), their demographic profile ('age', 'job'), and their history with past campaigns ('poutcome_success'). 

- **Target Demographics:** Younger clients (under 35) and older clients (over 60), particularly students and retirees, showed the highest subscription rates.

- **Strategic Insight:** The outcome of a past campaign ('poutcome_success') was one of the strongest individual signal of a positive outcome. Clients who had previously subscribed converted at a rate substantially higher than any other segment, making them a prime, high-ROI target for re-engagement.

### **The Final Result**

The analysis provided three distinct business strategies based on the precision-recall trade-off. The results are summarized in the notebook 3, using a conservative assumption of a €5 cost per call and €50 value per subscription. 

For a general-purpose campaign requiring both profitable growth and effective market penetration, we recommend **the Balanced Approach.** This strategy, optimized by the F1-score, delivers a strong ROI of 205.3% while still capturing 38.5% of potential subscribers. It provides the most robust and scalable plan for acquiring a healthy number of new customers without an excessive marketing spend.

### **Project Navigation**

- [**01_data_cleaning_and_EDA:**](./notebooks/01_data_cleaning_and_EDA.ipynb) This notebook covers the full data cleaning process and exploratory analysis. 
- [**02_feature_engineering_and_modeling:**](./notebooks/02_feature_engineering_and_modeling.ipynb) This notebook covers techniques applied for feature engineering and model training.
- [**03_business_impact_and_conclusion:**](./notebooks/03_business_impact_and_conclusion.ipynb) This notebook covers business analytics and the overall conclusion.

### **Technology Stack & Methods**
- **Technology:** Python, Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib, Joblib
- **Methods:** Data Cleaning & EDA, Feature Engineering (One-Hot Encoding), Class Imbalance Handling (SMOTE), Predictive Modeling (Logistic Regression, Random Forest, XGBoost), Hyperparameter Tuning (GridSearchCV), Model Evaluation, Precision-Recall Trade-Off Analysis.

### **Setup & How to Run**
1. Clone the repository to your local machine.
2. Create a new virtual environment
3. Install the required dependencies in 'requirements.txt'

#### Data Source

*S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014*