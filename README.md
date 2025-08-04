# 🏠 Bengaluru House Price Prediction – Internship Task 1

This project was completed as part of my internship. I built a machine learning pipeline to predict house prices in Bengaluru based on location, size, total square footage, and number of bathrooms. The dataset contains over 13,000 records of real estate listings.

---

## 📌 Key Highlights

- ✅ Cleaned messy and incomplete data  
- ✅ Engineered features like `bhk`, `price_per_sqft`, `luxury_flag`  
- ✅ Removed outliers using domain logic and standard deviation  
- ✅ Reduced location dimensionality with grouping  
- ✅ Trained and evaluated two models:  
  - **Linear Regression**  
  - **Random Forest Regressor**

---

## 📊 Model Performance

| Model              | R² Score | RMSE   | MAE   |
|-------------------|----------|--------|-------|
| Linear Regression | 0.852    | 39.04  | 19.10 |
| Random Forest     | 0.800    | 45.00  | 16.00 |

> 📌 *Linear Regression had better fit (R²), while Random Forest had lower average error (MAE).*

---

## 📈 Visualizations

- BHK distribution
- Price per square foot distribution
- Actual vs Predicted Price (Scatter Plot)
- Heatmap of feature correlations
- Top 10 most expensive locations

---

## 📁 Files Included

- `task1_bangalore_house_price_prediction.ipynb` – Main code notebook
- `columns.json` – Metadata for features used in prediction
- 📦 `bangalore_home_price_model.pkl` – [Download from Google Drive](https://drive.google.com/your_model_link)

---

## 🛠️ Tools Used

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Joblib (for saving models)
- Jupyter Notebook

---

## 📣 About This Task

This task demonstrated practical machine learning workflow:  
from raw data preprocessing, feature engineering, visualization, to model building and evaluation – all done in a clean Jupyter Notebook environment.

---
