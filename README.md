# News Headline Classifier
This is a supervised NLP classification project built based on a scraped dataset from nairaland. The goal of the project is to train a classifier to predict the category news headlines belong to whether it's politics, sports, education or business.

--- 
## Project Overview
Through web scraping, I was able to collect 5,739 headlines across several categories including Politics, Sports and Education. 
The dataset contains 3 columns with 5,739 records. Columns include: 
- headline : news headlines across 6 categories
- category : the category each headline belong
- link : news link for each headline

---

## Features
The dataset contains **3 columns** with **5,739 records**. Columns include: 
- headline : news headlines across 6 categories
- category : the category each headline belong
- link : news link for each headline
The dataset is available on (kaggle)[https://www.kaggle.com/datasets/yusufsanni5/nairaland-news-headlines-dataset]
---

**Class Distribution (slightly imbalanced):**
- politics: 1218
- sports:	1085
- business: 1011
- tv-movies: 865
- music-radio: 856
- education: 704

---

## Data preprocessing and Modelling
- Dropped the link column
- Removed missing and duplicate headlines
- Remove noisy headlines below the length of 7
- Used CountVectorizer to for word freqency analysis
- Used TfidfVectorizer for feature extraction
- Tested sevaral models such as Logistic regression, KNN, SVC, LinearSVC, Naive Bayes,Tree-based models and boosting methods
- Final model (Naive Bayes) gave an accuracy and F1 score of 0.75


---

## Tech Stack
- Python
- Google Collab Jupiter Notebook
- Scikit-learn


---

## How to run Locally
- Clone repository : 
 ``` bash 
    []()
```
- Create and activate virtual environment: 
``bash
python -m venv .venv
```bash
.venv\Scripts\activate   # On Windows
source .venv/bin/activate # On Mac/Linux
```

- Install dependencies
```bash
pip install -r requirement.txt

```
