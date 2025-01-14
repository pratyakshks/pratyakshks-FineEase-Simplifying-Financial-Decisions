# FineEase- Simplifying Financial Decisions

## Abstract  
The Intelligent Banking Platform leverages **Machine Learning (ML)** and **Natural Language Processing (NLP)** to simplify financial decision-making for users. The platform provides tailored recommendations based on user inputs, such as bank account information, loan preferences, and financial goals. It includes personalized banking and loan recommendations, sentiment analysis for user reviews, and real-time financial market analytics to enhance decision-making and financial literacy.  

Key features:  
- **Personalized Bank and Loan Recommendations**: Tailored suggestions based on user data.  
- **Sentiment Analysis Module**: Insights into banking products using NLP to classify customer reviews as neutral, negative, or positive.  
- **EMI Calculator Module**: Graphical representation of loan repayment schedules.  
- **Real-Time Market Dashboard**: Market trend analysis powered by **TradingView API** for better investment decisions.  

## Table of Contents  
1. [Introduction](#introduction)  
2. [Features](#features)  
3. [Problem Statement](#problem-statement)  
4. [Objectives](#objectives)  
5. [Methodology](#methodology)  
6. [Architecture](#architecture)  
7. [Technologies Used](#technologies-used)  
8. [How to Run](#how-to-run)  
9. [Future Scope](#future-scope)  
10. [Contributors](#contributors)  

---

## Introduction  
Managing personal finances has become increasingly complex due to the vast range of banking services, loan products, and investment tools available today. This project addresses these challenges by providing a smart, user-friendly platform that delivers personalized financial guidance using ML and NLP.  

---

## Features  
- **Personalized Recommendations**: Uses keyword-based filtering and user data for tailored bank account and loan options.  
- **Sentiment Analysis**: Evaluates customer feedback for banking products using NLP techniques.  
- **Market Dashboard**: Provides real-time insights into financial markets, including top gainers, losers, and active stocks.  
- **EMI Calculator**: Calculates and visualizes loan repayment schedules.  
- **Interactive UI**: Allows users to input preferences and view recommendations dynamically.  

---

## Problem Statement  
Individuals face several challenges in managing finances:  
1. Overwhelming options for banking, loans, and investments.  
2. Uncertainty in assessing loan eligibility.  
3. Lack of personalized investment guidance.  
4. Difficulty in understanding financial market trends.  

This project bridges these gaps by offering data-driven, intuitive solutions for personalized financial decision-making.  

---

## Objectives  
- Analyze user data for personalized bank and loan recommendations.  
- Implement sentiment analysis for enhanced recommendations using NLP.  
- Use ML for real-time analysis of financial market trends.  

---

## Methodology  

### 1. Personalized Bank Recommendations  
- **Data Collection**: Gathered from major banks (ICICI, HDFC, Axis, SBI) and users.  
- **Algorithm**: Keyword-based filtering matches user preferences with banking products.  

### 2. Sentiment Analysis  
- Preprocess user reviews using **NLTK** for tokenization, stop-word removal, and lemmatization.  
- Classify feedback as positive, neutral, or negative using **SentimentIntensityAnalyzer**.  

### 3. Financial Market Dashboard  
- Integrated real-time data using **TradingView API**.  
- Displays top gainers, losers, and stock indices on an interactive dashboard.  

### 4. EMI Module  
- Calculates monthly repayment using user input for loan amount, interest rate, and duration.  
- Visualizes repayment schedules via graphs.  

---

## Architecture  

### 1. Data Collection Layer  
- Bank and loan data collected from online resources.  
- User input preferences recorded dynamically.  

### 2. Data Processing Layer  
- Data cleaning ensures uniformity and handles missing values.  
- Feature engineering maps user inputs to dataset attributes for personalized recommendations.  

### 3. Recommendation Engine  
- Text-based filtering for account and loan suggestions.  

### 4. Sentiment Analysis Module  
- NLP-based sentiment classification of user feedback.  

### 5. Financial Market Dashboard  
- Real-time insights using **TradingView API** widgets.  

### 6. Frontend User Interface  
- Built with **HTML, CSS, and JavaScript**.  
- Dynamic filtering and EMI calculation modules integrated.  

---

## Technologies Used  
- **Programming Languages**: Python, JavaScript  
- **Frameworks**: Flask (Backend), NLTK, TradingView API  
- **Frontend**: HTML, CSS, JavaScript  
- **Libraries**: NumPy, Pandas, Matplotlib  
- **APIs**: TradingView API  

---

## How to Run  

### Prerequisites  
- Python 3.x  
- Flask  
- Required Python libraries (`pip install -r requirements.txt`)  

### Steps  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-repo/intelligent-banking-platform.git  
   cd intelligent-banking-platform

2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  

3. Run the Flask server:  
   ```bash  
   python app.py  

4. Open the platform in your browser:  
   ```bash  
   http://127.0.0.1:5000  
