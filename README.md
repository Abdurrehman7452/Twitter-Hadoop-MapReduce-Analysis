# X (Twitter) Data Analysis with Hadoop MapReduce

This project demonstrates how to use **Hadoop MapReduce** for analyzing social media data from Platform X (formerly Twitter), focusing on two major tasks: **Hashtag Popularity** and **User Influence**.

## 📁 Dataset

The dataset is a collection of COVID-19 tweets and includes fields such as user metadata, tweet content, hashtags, and more.

- Source: [Kaggle - COVID19 Tweets Dataset](https://www.kaggle.com/datasets/gpreda/covid19-tweets)

## 🧰 Technologies Used

- Python (Preprocessing & MapReduce scripts)
- Hadoop (Single-node)
- Pandas, Matplotlib, numPy (for visualization)
- Linux/Unix CLI (for running Hadoop jobs)

## ✅ Tasks Performed

### 1. Hashtag Popularity (MapReduce)
- Parsed and cleaned hashtags from tweet text.
- Implemented a MapReduce job to count hashtag frequencies.
- Output: `hashtagpopularity.txt`
- Visualized as bar chart and pie chart.

### 2. User Influence Score (MapReduce)
- Combined metrics: followers, favourites, and verification status.
- Calculated weighted influence score per user.
- Output: Top 25 influential users printed to console.


## 🖥️ How to Run

### Preprocessing
Run in Jupyter Notebook 

### MapReduce (Hadoop Streaming)
##### Hashtag Popularity
```bash
hadoop jar /path/to/hadoop-streaming.jar \
-input cleaned_hashtags.txt \
-output output/hashtags \
-mapper mapper_hs.py \
-reducer reducer_hs.py
```

##### User Influence
```bash
hadoop jar /path/to/hadoop-streaming.jar \
-input user_influence_data.json \
-output output/influence \
-mapper mapper_inf.py \
-reducer reducer_inf.py
```

## 📊 Results

  Top 15 hashtags ranked by usage.

  Top 25 users scored by influence metrics (followers, likes, verification).

  Visuals using bar and pie charts (with log scale for count analysis).

## 📌 Notes

  Uses simple Python logic to ensure readability.

  Focus is on clarity and learning Hadoop MapReduce concepts, not data scale.

  Dataset was cleaned and reduced for local experimentation.

## 🧠 Author

Abdur Rehman
Bachelors in Data Science | Passionate about clean, explainable code & scalable systems.
