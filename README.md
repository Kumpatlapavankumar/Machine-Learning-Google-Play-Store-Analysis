# 📱 Google Play Store App Success Prediction

This project focuses on predicting the success of Google Play Store apps using machine learning techniques. The goal is to classify apps based on their features like category, ratings, size, type, price, content rating, etc., to determine their potential success.

---

## 📊 Dataset Information

- **Source**: [Kaggle - Google Play Store Dataset](https://www.kaggle.com/datasets/lava18/google-play-store-apps)
- **Total entries**: ~10,000 apps
- **Features include**:
  - App name
  - Category
  - Rating
  - Reviews
  - Size
  - Installs
  - Type (Free/Paid)
  - Price
  - Content Rating
  - Genres
  - Last Updated
  - Android Version

---

## ⚙️ Technologies Used

- **Python 3.8+**
- **Libraries**:
  - `pandas`, `numpy`
  - `matplotlib`, `seaborn`, `plotly`
  - `scikit-learn` (ML models, preprocessing)
  - `xgboost` (for gradient boosting)

---

## 🔍 Exploratory Data Analysis (EDA)

### 1. **Top Categories**
```text
FAMILY, GAME, TOOLS, BUSINESS are the most frequent app categories.
```

### 2. **Content Rating Distribution**

![Content Rating](assets/content_rating_distribution.png)

Most apps are rated for "Everyone", followed by "Teen" and "Mature 17+".

### 3. **Free vs Paid**

![Free vs Paid](assets/free_vs_paid.png)

A large majority of apps are free. Paid apps are fewer and often in specialized categories.

### 4. **Ratings Distribution**

![Rating Distribution](assets/rating_distribution.png)

Ratings are mostly concentrated between 4.0 and 4.7. There are a few outliers below 3.0.

### 5. **Price vs Rating**

![Price vs Rating](assets/price_vs_rating.png)

Most free apps have a wide range of ratings. Paid apps tend to be rated slightly higher on average.

---

## 🧹 Data Preprocessing

- Removed duplicate and null values
- Handled inconsistent formats (like '1,000+' → 1000)
- Converted categorical variables using **Label Encoding** and **One-Hot Encoding**
- Normalized/Standardized numeric columns
- Feature selection based on correlation and variance

---

## 🤖 Model Building

Several classification models were trained to predict app success:

| Model           | Accuracy | F1 Score |
|----------------|----------|----------|
| Logistic Regression | 88%      | 87%      |
| Random Forest        | 90%      | 89%      |
| XGBoost Classifier   | **92%**  | **91%**  |

- The **XGBoost** model achieved the highest accuracy and F1 score.

---

## 📈 Evaluation Metrics

- **Accuracy**: Percentage of correctly classified apps
- **F1 Score**: Harmonic mean of precision and recall
- **Confusion Matrix**: To evaluate false positives and false negatives
- **Classification Report**: Precision, recall, and F1-score per class

---

## 📁 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/google-playstore-app-prediction.git
cd google-playstore-app-prediction
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run the Notebook
```bash
jupyter notebook Google-play-store\ Prediction.ipynb
```

Make sure to download the dataset from Kaggle and place it in the appropriate directory.

---

## 🚀 Future Improvements

- Deploy the model using **Streamlit** or **Flask**
- Add more app metadata (e.g., app permissions, developer info)
- Use deep learning models for regression-based install prediction
- Create a dashboard to visualize predictions live

---

## 🧾 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- Kaggle for providing the dataset
- Scikit-learn and XGBoost for model training
