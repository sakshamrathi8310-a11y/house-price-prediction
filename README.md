# 🏠 Bengaluru House Price Prediction

## 📌 Project Description

This project is a **Machine Learning-based web application** that predicts house prices in Bengaluru based on user inputs such as location, square footage, number of bedrooms, bathrooms, and balconies.

The system uses a **Linear Regression model** trained on a cleaned dataset and provides real-time predictions through an interactive **Streamlit interface**.

---

## 🚀 Key Features

* 📊 Predict house prices instantly
* 📍 Location-based prediction using one-hot encoding
* 🧠 Machine Learning model (Linear Regression)
* 🌐 Interactive UI built with Streamlit
* ⚡ Fast and real-time predictions

---

## 🛠️ Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Pickle (for model saving/loading)

---

## 📂 Project Structure

```id="k9a2lm"
House-Price-Prediction/
│── app.py                 # Streamlit web app
│── train_model.py         # Model training script
│── House_price_prediction_model.pkl  # Trained model
│── cleaned_data_csv       # Dataset
│── README.md
```

---

## ⚙️ How It Works

### 1️⃣ Data Preprocessing

* Removed unnecessary columns (`Unnamed: 0`)
* Converted categorical data (location) into numerical using **one-hot encoding**

### 2️⃣ Model Training

* Algorithm: Linear Regression
* Train-Test Split: 80% training, 20% testing
* Model trained using `scikit-learn`

### 3️⃣ Prediction System

* User inputs:

  * Location
  * Square Feet
  * Bathrooms
  * Balconies
  * Bedrooms

* Input is converted into model format and prediction is generated.

---

## ▶️ How to Run the Project

1. Clone the repository:

```id="q1v8pa"
git clone https://github.com/your-username/house-price-prediction.git
```

2. Go to project folder:

```id="n8xk2z"
cd house-price-prediction
```

3. Install dependencies:

```id="z4f1lx"
pip install -r requirements.txt
```

4. Run the Streamlit app:

```id="d9c3rm"
streamlit run app.py
```

---

## 📊 Model Performance

* Model Used: Linear Regression
* Evaluation Metric: R² Score
* The model provides reasonably accurate predictions based on available features.

---

## 📈 Future Improvements

* Use advanced models (Random Forest, XGBoost)
* Add more features (area type, property age)
* Deploy project online (Streamlit Cloud / AWS)
* Improve UI design

---

## 👨‍💻 Author

**Saksham Rathi**
B.Tech CSE | Data Science Enthusiast

---

## ⭐ Conclusion

This project demonstrates the practical implementation of Machine Learning in real estate price prediction. It highlights data preprocessing, model training, and deployment using an interactive web interface.

---
