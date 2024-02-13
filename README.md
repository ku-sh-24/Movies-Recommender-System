<h1>Movie Recommender System</h1>

<p>This project is an end-to-end implementation of a movie recommender system, from building the machine learning model to deploying it as a website. The recommender system is based on content-based filtering, using features such as movie genres, keywords, directors, actors, and actresses to recommend similar movies to users.</p>

<h2>Theory</h2>

<h3>What is a Recommender System?</h3>
<p>A recommender system is a technology that provides personalized recommendations to users for items they may be interested in, such as movies, products, or articles.</p>

<h3>Why do we need it?</h3>
<p>Recommender systems help users discover new items of interest based on their past preferences and behavior, enhancing user experience and engagement on platforms.</p>

<h3>Types of Recommender Systems</h3>
<ul>
  <li><strong>Content-based:</strong> Recommends items similar to those the user has liked in the past, based on item attributes (e.g., movie genres, keywords).</li>
  <li><strong>Collaborative Filtering:</strong> Recommends items based on the preferences of similar users or items.</li>
</ul>
<p>This project focuses on a content-based recommender system.</p>

<h2>Project Flow</h2>

<ol>
  <li><strong>Data Collection and Preprocessing:</strong> Utilizes the TMDB 5000 movie dataset, which consists of two datasets - one containing movie data and the other containing credits. Preprocessing involves feature selection, merging datasets, handling null values and duplicates, and transforming columns for better text analysis.</li>
  <li><strong>Model Building:</strong> Builds a content-based recommender model using vectorization techniques such as bag of words and cosine similarity. Text data is converted into numerical vectors to calculate similarity between movies.</li>
  <li><strong>Website Conversion:</strong> Converts the model into a website using Streamlit. The model is deployed on the website to provide movie recommendations to users.</li>
  <li><strong>API Integration:</strong> Integrates with TMDB API to retrieve movie posters for display on the website. Users can interact with the recommender system by entering a movie title, and the system will recommend similar movies based on the entered title.</li>
</ol>

<h2>Libraries Used</h2>
<ul>
  <li>Numpy</li>
  <li>Pandas</li>
  <li>Scikit-learn</li>
  <li>NLTK</li>
  <li>Streamlit</li>
  <li>Pickle</li>
  <li>Requests</li>
</ul>

<h2>Challenges and Solutions</h2>
<ul>
  <li><strong>Data Transformation:</strong> Ensured consistent formatting of text data to improve model performance and accuracy.</li>
  <li><strong>Vectorization:</strong> Utilized techniques such as bag of words and cosine similarity for text vectorization to calculate movie similarity.</li>
  <li><strong>Website Deployment:</strong> Deployed the model as a user-friendly website using Streamlit, overcoming challenges related to data transfer and integration with external APIs.</li>
</ul>

<h2>Conclusion</h2>
<p>This project demonstrates the end-to-end implementation of a content-based movie recommender system, from data preprocessing and model building to website deployment. By leveraging machine learning techniques and web development tools, users can receive personalized movie recommendations based on their preferences and interests. Additionally, API integration enhances the user experience by providing movie posters and enriching the recommendation interface.</p>
