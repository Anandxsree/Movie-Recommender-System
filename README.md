# 🎬 Movie Recommender System 🎥

A simple **Movie Recommendation System** built with **Streamlit**, **Pandas**, and **TMDb API**. It suggests movies based on similarity using machine learning techniques. Great for learning how recommendation systems work and for building beginner-friendly ML projects.

---

## 📌 Features

* ✅ Search for a movie and get **5 similar movie recommendations**
* ✅ Displays **movie posters** using TMDb API
* ✅ Interactive UI built with **Streamlit**
* ✅ Real-time search experience
* ✅ Lightweight and fast performance

---

## 🧠 How It Works

* The system uses **cosine similarity** on a vectorized dataset of movies.
* Pre-processed movie metadata (title, genre, cast, keywords) is combined and converted to vectors.
* When a movie is selected, it calculates similarity with other movies and suggests the top 5.

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Anandxsree/movie-recommender.git
cd movie-recommender
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

> ℹ️ The first run may take a few seconds to load the model and fetch posters.

---

## 🛠️ Technologies Used

* **Python** 🐍 – Core logic and data manipulation
* **Streamlit** 🎭 – Frontend web app interface
* **Pandas** 🏆 – Data wrangling and manipulation
* **Scikit-learn** 📘 – Cosine similarity model
* **TMDb API** 🎞️ – Poster and movie data

---

## 📁 Repository Structure

```bash
movie-recommender/
├── app.py                   # Main Streamlit app
├── movies.csv               # Preprocessed movie metadata
├── similarity.pkl           # Precomputed cosine similarity matrix
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 📸 Sample UI

> Add a screenshot here:

```
📍 User selects "Inception"
🎥 System recommends: Interstellar, The Prestige, The Matrix, Shutter Island, Tenet
🖼️ Posters loaded via TMDb API
```

---

## 🌐 Deployment (Optional)

Deploy easily to [Streamlit Cloud](https://streamlit.io/cloud):

* Push your code to a public GitHub repo
* Sign in to Streamlit Cloud and connect your repo
* Configure `app.py` as the entry point
* Your app goes live!

---

## 📬 Contact

**Anand Sreekumar**
🔗 [LinkedIn](https://www.linkedin.com/in/anand-sreekumar-09188b291/)
📧 [anandsreekuamr025@gmail.com](mailto:anandsreekuamr025@gmail.com)

---

## 💡 Additional Tips

* 📸 Add **screenshots or a demo video** to the repository
* 🌐 Include **a link to the deployed app** if hosted on Streamlit Cloud
* 🧠 Consider using **TF-IDF or deep learning embeddings** for advanced results
* ✨ Keep the UI clean and the code modular for scalability

---

## 📢 Credits

* Dataset inspired by [Kaggle TMDB Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* Poster retrieval powered by [TMDb API](https://www.themoviedb.org/documentation/api)

---
