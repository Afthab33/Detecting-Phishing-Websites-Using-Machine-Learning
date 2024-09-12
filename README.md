# Phishing Website Detection Using Machine Learning

This repository contains code and resources related to detecting phishing websites using machine learning. The project uses various URL-based features to train models that can predict whether a website is phishing or legitimate. The main model creation is done in the `Model Creation.ipynb` file.

## Achieved Results

Several machine learning models were tested on the dataset, yielding the following accuracy rates:

- **Random Forest Classifier**: Achieved 96% accuracy.
- **Logistic Regression**: Achieved 92% accuracy.
- **K-Nearest Neighbors (KNN)**: Achieved 88% accuracy.
- **Support Vector Classifier (SVC)**: Achieved 90% accuracy.
- **Decision Tree Classifier**: Achieved 85% accuracy.
- **Naive Bayes**: Achieved 89% accuracy.

## Repository Contents

- **Model Creation.ipynb**: Jupyter Notebook that contains the full code for model creation and training using different machine learning algorithms.
- **URL Feature Analysis.ipynb**: Jupyter Notebook for analyzing features of the URLs to help determine phishing characteristics.
- **app_sql.py**: Python script used to connect the model to a web application for real-time phishing website prediction.
- **ddbb.sql**: SQL file for setting up the database used by the application to store predictions and related data.
- **markup.txt**: Markup file for generating the front-end or storing additional HTML-based content.
- **phishcoop.csv**: The dataset used for training and testing the machine learning models. This dataset contains features extracted from website URLs that determine whether a site is phishing or legitimate.

## Dataset

The dataset used in this project, `phishcoop.csv`, consists of URL-based features such as:

- **IP Address in URL**: Whether the domain contains an IP address.
- **URL Length**: Length of the URL, which can indicate phishing.
- **"@" Symbol**: The presence of the "@" symbol, which may signify phishing.
- **HTTPS Token**: Incorrect usage of HTTPS in the URL.
- **Subdomains**: The number of subdomains in the URL, which can indicate suspicious activity.

These features are used to train machine learning models that predict whether a given URL is phishing or legitimate.

## How to Use

1. Clone or download the repository:
   ```bash
   git clone https://github.com/yourusername/phishing-website-detection.git
   ```
2. Ensure that you have Jupyter Notebook and the required dependencies installed. Install any missing dependencies with:
   ```bash
   pip install -r requirements.txt
   ```
3. Open the `Model Creation.ipynb` file in Jupyter Notebook to view and run the model creation code:
   ```bash
   jupyter notebook
   ```
4. You can also explore `URL Feature Analysis.ipynb` to see how features were extracted and analyzed.

## Models and Evaluation

The project experimented with several models, including:

- Random Forest Classifier
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Classifier (SVC)
- Decision Tree
- Naive Bayes

These models were evaluated based on their accuracy, precision, recall, and F1-score on the testing dataset.

## Credits

This repository was created and maintained by **Afthab33**. Special thanks to all resources and tools used during the development of this project.
