# Instagram Likes Predictor

**Instagram Likes Predictor** is a machine learning-based web application that estimates the expected number of likes and the time since posting for an Instagram post, based on the number of followers.  
The project combines a simple predictive model with a clean and simple streamlit interface.

---

## Project Overview

- **Goal:** Predict Instagram engagement metrics based on basic input features.
- **Model:** Random Forest Regressor trained on publicly available engagement datasets.
- **App:** Developed using Streamlit with custom CSS for a soft, minimal, and user-friendly interface

---

## Tech Stack

- **Python 3.12**
- **Streamlit** (Frontend & App Framework)
- **Scikit-Learn** (Machine Learning)
- **Pandas, NumPy** (Data Handling)
- **Matplotlib, Seaborn** (EDA Visualizations)
- **Google Colab** (Model Training)

---

## Folder Structure
- `dataset/`  
  Dataset (csv) used for this project.

- `notebook/`  
  Colab notebook (includes code for taining the model).

- `model/`  
  .pkl model generated after training

- `app/`  
  streamlit app (app.py)
  
- `venv/`  
  already created virtual environment with installed requirements.

---
## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yeshapan/instagram-likes-predictor.git
cd instagram-likes-predictor
```

### 2. Activate the Virtual Environment
```bash
# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On MacOS/Linux
source venv/bin/activate
```

### 3. Install the Required Packages
```bash
pip install -r requirements.txt
```

### 4. Run the streamlit app
```bash
streamlit run app/app.py
```

> *Developed with passion for technology — coffee.compile ☕ by Yesha.*
