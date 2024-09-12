# Phishing Website Detection Using Machine Learning

This repository contains the complete code and resources for detecting phishing websites using various machine learning techniques. The goal of the project is to classify websites as phishing or legitimate by analyzing their URL characteristics. The project leverages multiple machine learning models and URL-based feature engineering to provide accurate predictions.

## Project Overview

Phishing is a form of cyberattack where fraudulent websites mimic legitimate ones to steal sensitive information such as usernames, passwords, or credit card details. This project uses machine learning to identify potential phishing websites by analyzing features from URLs such as length, presence of suspicious characters, use of IP addresses, and more.

The project was implemented using Python, with models trained and evaluated on a dataset of labeled phishing and legitimate URLs.

## Achieved Results

The project employs several machine learning models and achieves the following accuracy scores based on different algorithms:

- **Random Forest Classifier**: 96% accuracy
- **Logistic Regression**: 92% accuracy
- **K-Nearest Neighbors (KNN)**: 88% accuracy
- **Support Vector Classifier (SVC)**: 90% accuracy
- **Decision Tree Classifier**: 85% accuracy
- **Naive Bayes**: 89% accuracy

The Random Forest Classifier demonstrated the highest accuracy in identifying phishing websites, making it the most robust model for this task.

## Repository Contents

The repository is structured as follows:

- **`Model Creation.ipynb`**: Jupyter Notebook containing the full machine learning pipeline, including data loading, preprocessing, feature engineering, model training, evaluation, and results. This notebook also includes comparisons between different algorithms.
- **`URL Feature Analysis.ipynb`**: Jupyter Notebook dedicated to analyzing the features extracted from URLs that are indicative of phishing attacks. It details feature extraction techniques and exploratory data analysis (EDA).
- **`app_sql.py`**: Python script used to integrate the trained model with a web application using Flask. This enables real-time phishing detection based on user input URLs.
- **`ddbb.sql`**: SQL script to create and set up the necessary database structure for storing the prediction results and related data for the web application.
- **`markup.txt`**: HTML markup used in the front-end of the web application for rendering user input forms and displaying prediction results.
- **`phishcoop.csv`**: The dataset containing labeled phishing and legitimate website URLs along with features extracted for training the machine learning models.

## Dataset

The dataset used in this project (`phishcoop.csv`) contains a variety of features that are extracted from URLs. Some key features include:

- **IP Address in URL**: Phishing URLs may use IP addresses instead of domain names to deceive users.
- **URL Length**: Longer URLs can be used to hide suspicious elements.
- **"@" Symbol in URL**: URLs with an "@" symbol can be used to trick browsers into ignoring the part of the URL before the symbol.
- **HTTPS Token Misuse**: Some phishing websites add "HTTPS" in their domain names to create a false sense of security.
- **Subdomains**: Phishing URLs often have more subdomains than legitimate ones, which can be a signal for detection.

These features are crucial for training the model to accurately distinguish between phishing and legitimate websites.

## How to Use

To use this project and experiment with the model, follow the steps below:

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/yourusername/phishing-website-detection.git
   ```

2. **Install the necessary dependencies**:
   A `requirements.txt` file should contain all the required Python libraries. Install them using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebooks**:
   Open the `Model Creation.ipynb` and `URL Feature Analysis.ipynb` notebooks to explore the models and the feature extraction process.
   ```bash
   jupyter notebook
   ```

4. **Test the Web Application**:
   You can run the Flask-based web application by executing the `app_sql.py` file. This application will allow you to input a website URL and get a real-time phishing detection prediction.
   ```bash
   python app_sql.py
   ```

## Models and Evaluation

The project implements and evaluates the following machine learning algorithms:

- **Random Forest Classifier**: A robust ensemble learning method that combines multiple decision trees to improve prediction accuracy. Achieved the highest accuracy in the project.
- **Logistic Regression**: A simple and interpretable model that performed well in detecting phishing websites.
- **K-Nearest Neighbors (KNN)**: A non-parametric algorithm that classifies websites based on the nearest training examples in the feature space.
- **Support Vector Classifier (SVC)**: A powerful model that works well for binary classification tasks like phishing detection.
- **Decision Tree**: A tree-based model that is easy to visualize but prone to overfitting.
- **Naive Bayes**: A probabilistic classifier that performed well with the given dataset.

Each model was evaluated using metrics such as accuracy, precision, recall, F1-score, and a confusion matrix to determine its effectiveness in detecting phishing websites.

## Credits

This project was created and maintained by **Afthab33**. Special thanks to the various open-source resources and datasets that contributed to the development of this project.
