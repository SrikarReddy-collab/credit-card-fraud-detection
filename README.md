# 💳 AI Credit Card Fraud Detection Using XGBoost

## 📌 Project Overview

Credit card fraud is a major problem in digital payments. This project uses Machine Learning to identify potentially fraudulent credit card transactions.

An **XGBoost classification model** is trained on a credit card transaction dataset to classify transactions as **Fraud (1)** or **Normal (0)**. A Streamlit web application allows users to upload a CSV file, predict transaction results, view fraud statistics, and download the prediction report.

## 🎯 Objectives

- Detect potentially fraudulent credit card transactions using Machine Learning.
- Train and evaluate an XGBoost classification model.
- Build an interactive web dashboard using Streamlit.
- Display fraud predictions, transaction statistics, and a fraud distribution chart.
- Allow users to download prediction results as a CSV file.

## 🛠️ Technologies Used

- **Python** – Main programming language
- **Pandas** – Data processing and analysis
- **Scikit-learn** – Data splitting and model evaluation
- **XGBoost** – Fraud classification model
- **Joblib** – Saving and loading the trained model
- **Streamlit** – Interactive web dashboard
- **Matplotlib** – Data visualization
- **Jupyter Notebook** – Model training and experimentation

## 📂 Project Structure

```text
credit-card-fraud-detection/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   └── creditcard.csv
│
├── models/
│   ├── random_forest_model.pkl
│   └── xgboost_model.pkl
│
└── notebook/
    └── EDA.ipynb
```

*The dataset and model files are shown for reference. Large datasets and generated files do not necessarily need to be committed to GitHub.*

## 📊 Dataset

This project uses a credit card transaction dataset containing **284,807 transactions and 31 columns**, including the target column `Class`.

- **Class = 0:** Normal transaction
- **Class = 1:** Fraudulent transaction
- **Features:** Transaction variables, including `Time`, `Amount`, and anonymized features `V1` to `V28`.

The dataset is highly imbalanced because fraudulent transactions are much less common than normal transactions.

## ⚙️ Machine Learning Workflow

1. Load and explore the transaction dataset.
2. Analyze the dataset using Pandas and visualization techniques.
3. Separate the input features and target column.
4. Split the data into training and testing sets using an 80:20 ratio.
5. Train an XGBoost classification model.
6. Evaluate the model using accuracy, precision, recall, F1-score, and ROC-AUC.
7. Save the trained model using Joblib.
8. Load the model in the Streamlit application.
9. Upload a CSV file and generate transaction predictions.
10. View the results and download them as a CSV report.

## 📈 Model Performance

The trained XGBoost model achieved the following results on the test dataset:

| Evaluation Metric | Score |
|---|---:|
| Accuracy | 99.96% |
| Precision | 92.13% |
| Recall | 83.67% |
| F1-Score | 87.70% |
| ROC-AUC | 97.33% |

These results are based on the project's 80:20 train-test split. Accuracy alone can be misleading for imbalanced fraud datasets, so precision, recall, F1-score, and ROC-AUC are also reported.

## 🚀 Features of the Web Application

- Upload transaction data in CSV format.
- Preview the uploaded dataset.
- Display the number of predicted fraud and normal transactions.
- Visualize the predicted transaction distribution.
- View transactions classified as potentially fraudulent.
- Display fraud probability for each transaction.
- Download the complete prediction results as a CSV file.

**Note:** The dashboard performs batch predictions on uploaded data. Its predictions are not a guarantee that a transaction is fraudulent, and the application is not connected to a live banking or payment system.

## 💻 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/SrikarReddy-collab/credit-card-fraud-detection.git
```

### 2. Open the project folder

```bash
cd credit-card-fraud-detection
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If dependencies are not fully listed in `requirements.txt`, install the required packages:

```bash
pip install streamlit pandas scikit-learn xgboost joblib matplotlib
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser. If it does not open automatically, use the local URL displayed in the terminal, usually `http://localhost:8501`.

## 📥 How to Use

1. Start the Streamlit application.
2. Upload a CSV file containing the required transaction features.
3. Review the uploaded data.
4. Click **Predict Fraud**.
5. View the predicted fraud and normal transaction counts.
6. Review the transactions classified as potentially fraudulent.
7. Download the prediction results as a CSV file.

The uploaded CSV must contain the same input features, with compatible names and structure, that were used to train the model. The `Class` target column is not required for prediction.

## 🔮 Future Improvements

- Compare XGBoost with additional classification algorithms.
- Tune model parameters to improve fraud detection.
- Add confusion matrix and precision-recall visualizations.
- Improve feature validation and error handling.
- Deploy the application to a cloud hosting platform.
- Explore real-time fraud detection through a secure payment-system integration.

## 👨‍💻 Author

**Srikar Reddy Lenkala**

- GitHub: [SrikarReddy-collab](https://github.com/SrikarReddy-collab)
- Project Repository: [Credit Card Fraud Detection](https://github.com/SrikarReddy-collab/credit-card-fraud-detection)

## 📄 Disclaimer

This project is developed for educational and demonstration purposes. Predictions should not be treated as confirmed fraud decisions or used as the sole basis for real financial transactions.
