# 🔍 Timelytics: Order to Delivery Time Prediction

A lightweight, real-time **Order to Delivery (OTD)** time prediction app built with [Streamlit](https://streamlit.io/), [Scikit-learn](https://scikit-learn.org/), and [XGBoost](https://xgboost.readthedocs.io/). Input order details such as date, location, size, and weight — and get predicted delivery time in days using a pre-trained ensemble ML model.

---

## 🚀 Live Demo

[Click here to try it on Streamlit Cloud](https://mj2210-timelytics-otd-predictor-streamlitapp-xibcqd.streamlit.app/)

---

## 📸 Features

- ✅ Predict delivery time in days
- ✅ ML Ensemble Model (XGBoost + Random Forest + SVM)
- ✅ Input: Day, month, size, weight, location, distance
- ✅ Output: Wait time prediction
- ✅ Clean and responsive UI (built with Streamlit)
- ✅ Model loaded dynamically from Google Drive

---

## 🛠️ Installation

```
git clone https://github.com/mJ2210/timelytics-otd-predictor.git
cd timelytics-otd-predictor
python -m venv venv
.\venv\Scripts\Activate.ps1  # Or use source venv/bin/activate for macOS/Linux
pip install -r requirements.txt
streamlit run streamlitApp.py

📦 Requirements
These are listed in requirements.txt
streamlit
scikit-learn>=1.3.2
xgboost
numpy
pandas
Pillow
requests

📁 Folder Structure
timelytics-otd-predictor/
├── streamlitApp.py           # Streamlit UI application
├── retrain_model.py          # Optional script to regenerate the model
├── requirements.txt          # Python dependencies
├── assets/
│   └── supply_chain_optimisation.jpg
├── data/
│   └── olist_sellers_dataset.csv
└── README.md                 # Project overview

📂 Model Hosting
The ensemble model is downloaded from Google Drive at runtime, keeping the repo lightweight and GitHub-compliant. This ensures version compatibility and avoids pushing large files.

🙌 Credits
Scikit-learn
XGBoost
Streamlit
Google Drive API

⭐ Like this project?
Star ⭐ the repo, fork it, or share it with your peers to support open-source supply chain innovation!
