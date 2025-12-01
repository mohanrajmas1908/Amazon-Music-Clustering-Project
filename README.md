🎯 Project Objectives

This project builds a complete unsupervised learning pipeline to group songs based on their audio characteristics. The goal is to extract meaningful musical segments that support:

	Personalized playlist curation

	Improved song discovery and recommendations

	Artist and competitor analysis

	Market segmentation for streaming platforms

	By leveraging clustering techniques, we transform raw musical attributes into actionable insights.

📈 Project Scope

This repository demonstrates how clustering can enhance the music ecosystem:

✔ Personalized Playlist Curation

Automatically group similar-sounding tracks for seamless listening experiences.

✔ Song Discovery

Recommend new music that aligns with user taste.

✔ Artist Analysis

Identify songs that compete within the same acoustic space.

✔ Market Segmentation

Analyze patterns across genres to inform marketing and promotional strategies.

🛠️ Approach

The workflow is broken into clear, modular phases:

1️⃣ Data Exploration & Preprocessing

	Load the dataset → single_genre_artists.csv

	Inspect schema, data types, missing values

	Drop non-informative columns: track_name, artist_name, track_id


Normalize features using StandardScaler

2️⃣ Feature Selection

Selected audio features used for clustering:

	energy

	loudness

	speechiness

	acousticness

	instrumentalness

	liveness

	valence

These features capture both musical composition and production style.

3️⃣ Dimensionality Reduction (Optional)

	Used to simplify visualization and reduce noise:

	PCA → Preserve variance

	t-SNE → Capture non-linear relationships for 2D visualization


4️⃣ Clustering Techniques

We evaluate multiple clustering algorithms:

✔ K-Means

Use Elbow Method + Silhouette Score to find optimal k

✔ DBSCAN

Automatically identifies noise/outliers

Useful for datasets with irregular cluster shapes

✔ Hierarchical Clustering

Dendrogram visualization for cluster merging history

5️⃣ Cluster Evaluation & Interpretation

Metrics used:

	Silhouette Score

	Davies–Bouldin Index

	Inertia (for K-Means)


Interpretation steps:

Compute mean feature values for each cluster

Translate numeric patterns into human-readable musical insights, e.g.


	Party / Club tracks
	Acoustic / Mellow tracks
	Rap / spoken word tracks

6️⃣ Visualizations

Multiple plots help interpret the audio landscape:

PCA & t-SNE scatter plots

Heatmaps comparing cluster-level features

Bar charts of average feature values

Distribution plots (tempo, loudness, valence, etc.)

⚙️ Tech Stack
Category:	Tools
Language:	Python 3.x
Data Handling:	pandas, numpy
Machine Learning:	scikit-learn
Visualization:	matplotlib, seaborn
Environment:	Jupyter Notebook / VS Code

📊 Example Outputs

Cluster Distribution Pie Chart

Bar Charts → Feature comparison across clusters

Heatmaps → High-level cluster differences

PCA / t-SNE Scatter Plots → Visual cluster separation

Final dataset with cluster labels
