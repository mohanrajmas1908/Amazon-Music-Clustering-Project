import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

# Centered, Large, Bold Title in Streamlit using custom HTML and Markdown.
st.image(r"D:\DS_Amazon_Music_Clustering\data_visualization\Amazon_logo.png", width=250)
st.markdown(
    """
    <h1 style='text-align: center; color: #9B59B6; font-size: 40px; font-weight: bold;'>
    🎶 Amazon Music Clustering  
    </h1>
    """,
    unsafe_allow_html=True
)

sb = st.selectbox(
    '## Amazon Music Clustering ',
    ["Scatter_Plots_Using_PCA/t-SNE", "Top_Tracks_Per_Cluster",
     "Heatmaps_on_Clusters", "Distribution_Plots","Average_feature_Bar_charts_per_cluster"],
    index=0
)

###########################
if sb == "Scatter_Plots_Using_PCA/t-SNE":
    # Load PCA and t-SNE data
    finaldf_PCA = pd.read_csv(r"D:\DS_Amazon_Music_Clustering\CSV\finaldf_PCA.csv")
    finaldf_TSNE = pd.read_csv(r"D:\DS_Amazon_Music_Clustering\CSV\X_tsne_finaldf.csv")

    # Create side-by-side plots
    fig, axes = plt.subplots(1, 2, figsize=(14,6))

    # PCA plot
    sns.scatterplot(data=finaldf_PCA,x='PC1', y='PC2',hue='clusters',palette='tab10',alpha=0.7,
        ax=axes[0]
    )
    axes[0].set_title("PCA Projection")

    # t-SNE plot
    sns.scatterplot(data=finaldf_TSNE,x='tsne1', y='tsne2',hue='clusters',palette='tab10',alpha=0.7,
        ax=axes[1]
    )
    axes[1].set_title("t-SNE Projection")
    st.pyplot(fig) 
########
if sb == "Top_Tracks_Per_Cluster":
    # Cluster DF's
    cluster0 = pd.read_csv(r"D:/DS_Amazon_Music_Clustering/CSV/top_tracks_cluster0.csv")
    cluster1 = pd.read_csv(r"D:/DS_Amazon_Music_Clustering/CSV/top_tracks_cluster1.csv")
    cluster2 = pd.read_csv(r"D:/DS_Amazon_Music_Clustering/CSV/top_tracks_cluster2.csv")

    # Create side-by-side plots
    fig, axes = plt.subplots(1, 3, figsize=(18,6))

    # cluster0
    sns.barplot(
        data=cluster0,
        x='song_mask',
        y='popularity_songs',
        hue='clusters',
        palette='tab10',
        ax=axes[0]
    )
    axes[0].set_title("Cluster 0 - Top 10 Tracks")
    axes[0].tick_params(axis='x', rotation=45)

    # cluster1
    sns.barplot(
        data=cluster1,
        x='song_mask',
        y='popularity_songs',
        hue='clusters',
        palette='tab10',
        ax=axes[1]
    )
    axes[1].set_title("Cluster 1 - Top 10 Tracks")
    axes[1].tick_params(axis='x', rotation=45)

    # cluster2
    sns.barplot(
        data=cluster2,
        x='song_mask',
        y='popularity_songs',
        hue='clusters',
        palette='tab10',
        ax=axes[2]
    )
    axes[2].set_title("Cluster 2 - Top 10 Tracks")
    axes[2].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    st.pyplot(fig)   # Streamlit rendering
    ##################
if sb == 'Heatmaps_on_Clusters':
    cluster_profiles = pd.read_csv(r"D:/DS_Amazon_Music_Clustering/CSV/cluster_profiles.csv")

    # Create figure
    fig, ax = plt.subplots(figsize=(12,6))
    sns.heatmap(
        cluster_profiles.T,
        cmap="Spectral",
        annot=True,
        fmt=".2f",
        linewidths=0.5,
        ax=ax
    )
    ax.set_title("Cluster Profiles Heatmap (Features vs Clusters)")
    ax.set_xlabel("Clusters")
    ax.set_ylabel("Features")

    plt.tight_layout()
    st.pyplot(fig)   # Streamlit rendering
##########################################################
if sb == 'Distribution_Plots':
    finaldf_PCA = pd.read_csv(r"D:\DS_Amazon_Music_Clustering\CSV\clusterdata.csv")

    # Create subplots grid
    fig, axes = plt.subplots(2, 4, figsize=(18,10), sharey=False)

    features_to_plot = [
        'danceability', 'energy', 'loudness', 'speechiness',
        'acousticness', 'instrumentalness', 'liveness', 'valence'
    ]

    # Flatten axes array for easy iteration
    axes = axes.flatten()

    for i, feature in enumerate(features_to_plot):
        sns.histplot(
            data=finaldf_PCA,
            x=feature,
            hue="cluster_label",
            palette='tab10',
            element='step',
            stat='density',
            common_norm=False,
            ax=axes[i]
        )
        axes[i].set_title(f"{feature.capitalize()} Distribution")
        axes[i].set_xlabel(feature.capitalize())
        axes[i].set_ylabel("Density")

    plt.tight_layout()
    st.pyplot(fig)   # ✅ Streamlit rendering
#################
if sb == 'Average_feature_Bar_charts_per_cluster':
    cluster_profiles = pd.read_csv(r"D:/DS_Amazon_Music_Clustering/CSV/cluster_profiles.csv")

    # Create figure
    fig, axis = plt.subplots(figsize=(14,6))
    cluster_profiles.plot(kind='bar', ax=axis)

    axis.set_title("Average Feature Values per Cluster")
    axis.set_ylabel("Mean Value")
    axis.set_xlabel("Features")
    axis.legend(title="Cluster")
    axis.set_xticklabels(cluster_profiles.index, rotation=45, ha='right')

    plt.tight_layout()
    st.pyplot(fig)   # ✅ Streamlit rendering




