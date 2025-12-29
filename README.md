# Movie Recommender System

Content-Based Movie Recommendation using Python, Machine Learning, and Streamlit

---

## Project Summary

This project is a **Content-Based Movie Recommender System** that suggests movies similar to a user-selected title based on textual features such as genres, keywords, overview, cast, and crew.  
The system uses **Natural Language Processing (NLP)** techniques and **cosine similarity** to compute similarity scores between movies.

An interactive **Streamlit web application** is built to allow users to select a movie and instantly receive recommendations along with movie posters fetched via the **TMDB API**.

---

## Table of Contents

1. Project Overview  
2. Dataset Description  
3. Project Architecture  
4. Data Preparation & Feature Engineering  
5. Similarity Model (Machine Learning Logic)  
6. Application Workflow  
7. Streamlit Application Features  
8. How to Run the Project  
9. Project Structure  
10. Future Enhancements  
11. Project Outcome  

---

## 1. Project Overview

The Movie Recommender System analyzes movie metadata to recommend similar movies based on content similarity.

### Business Objectives
- Provide personalized movie recommendations  
- Reduce content discovery time for users  
- Demonstrate practical use of NLP in recommendation systems  
- Build an end-to-end ML-powered web application  

### Target Audience
- Movie streaming platforms  
- Data science learners  
- Recruiters and hiring managers  
- Recommendation system enthusiasts  

---

## 2. Dataset Description

The dataset is derived from **TMDB (The Movie Database)** and contains metadata for thousands of movies.

### Key Columns
- `movie_id`
- `title`
- `overview`
- `genres`
- `keywords`
- `cast`
- `crew`
- `vote_average`
- `vote_count`
- `release_date`

The processed dataset is stored as serialized pickle files for fast loading.

---

## 3. Project Architecture

User Input (Movie Selection)
↓
Text Vectorization (CountVectorizer)
↓
Cosine Similarity Matrix
↓
Top-N Similar Movies
↓
TMDB API (Poster Fetching)
↓
Streamlit UI Display


---

## 4. Data Preparation & Feature Engineering

Performed using **Python (Pandas & NLP techniques)**:

1. Loaded raw movie and credit datasets  
2. Merged datasets on `movie_id`  
3. Extracted relevant features:
   - Genres
   - Keywords
   - Cast (Top 3 actors)
   - Director (from crew)
4. Cleaned text data:
   - Removed spaces
   - Converted text to lowercase
5. Created a combined feature column called `tags`
6. Removed null values and duplicates
7. Saved processed data using `pickle`

---

## 5. Similarity Model (Machine Learning Logic)

### Feature Vectorization

```python
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
```

Similarity Calculation
```python
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)
```
The similarity matrix is used to identify the most similar movies.

---

## 6. Application Workflow

  1. User selects a movie from the dropdown
  2. Selected movie index is identified
  3. Similarity scores are retrieved
  4. Top 5 similar movies are selected
  5. Movie posters are fetched via TMDB API
  6. Recommendations are displayed on the Streamlit UI

---

## 7. Streamlit Application Features
  
  - Movie selection dropdown
  - Recommendation button
  - Movie poster display
  - Responsive UI
  - Fast similarity-based results

### Poster Fetch Function
```python
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=API_KEY&language=en-US"
    data = requests.get(url).json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
```

---

## 8. How to Run the Project

#### Step 1: Clone the Repository
```python
git clone https://github.com/your-username/movie-recommender-system.git
```

```python

```

```python

```

```python

```

```python

```

```python

```




















