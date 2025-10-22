# News Headline Classifier
This is a supervised NLP classification project built on a scraped dataset from nairaland. The goal of the project is to train a classifier to identify the category news headlines belong to, whether it's politics, sports, education or business.

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

#### You can also download the dataset from [Kaggle](https://www.kaggle.com/datasets/yusufsanni5/nairaland-news-headlines-dataset)

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
- Cleaned and preprocessed headlines using the NLTK libary
- Remove noisy headlines below the length of 7
- Used CountVectorizer for word freqency analysis / text analysis
- Used TfidfVectorizer for feature extraction
- Tested sevaral models such as Logistic regression, SVC, LinearSVC and Naive Bayes
- Final model (Base Logistic Regression) gave an accuracy and F1 score of 0.80


---

## Tech Stack
- Python
- Google Collab Jupiter Notebook
- Scikit-learn


---

## How to run Locally
- Clone repository : 
 ``` bash 
    git clone https://github.com/Yusuf560-ui/News-Headline-Classifier
```

- Open folder
 ``` bash
cd News-Headline-Classifier-main
```

- Create and activate virtual environment: 
```bash
python -m venv .venv

```
```bash
.venv\Scripts\activate   # On Windows
source .venv/bin/activate # On Mac/Linux
```

- Install dependencies
```bash
pip install -r requirement.txt

```
- Better still, you can open the notebook in Google collab

---

# Testing the model 
I tested the model on news headlines across 5 categories and it performed very well. Check it out at the end of the notebook



