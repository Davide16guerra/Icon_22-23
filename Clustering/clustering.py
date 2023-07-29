import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import silhouette_score


def categorical_feature_encoding(dataset):
    # applicazione del one-hot encoding sulle feature di tipo stringa
    categorical_features = ['experience_level', 'job_title', 'employee_residence', 'company_location', 'company_size']

    onehot_encoder = OneHotEncoder(sparse_output=False)
    encoded_dataset = onehot_encoder.fit_transform(dataset[categorical_features])

    # combinazione delle feature encodate con il resto del dataset
    return pd.concat([dataset.drop(columns=categorical_features), pd.DataFrame(encoded_dataset)], axis=1)


def elbow_method(dataset):
    # esecuzione K-means per un range di K cluster
    dataset = np.array(dataset)
    wcss = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
        kmeans.fit(dataset)
        wcss.append(kmeans.inertia_)    # inseriamo le somme degli errori al quadrato

    # tracciamento del grafico
    plt.plot(range(1, 11), wcss, 'bx-')
    plt.title('elbow method')
    plt.xlabel('Numero di cluster (K)')
    plt.ylabel('WCSS')
    plt.show()


def clustering(dataset, k_cluster):
    dataset = np.array(dataset)
    kmeans = KMeans(n_clusters=k_cluster, n_init=10, random_state=42)
    kmeans.fit(dataset)
    validation(kmeans, dataset)
    return kmeans.labels_


def validation(k_means, dataset):
    # Calcolo della somma dei quadrati intra-cluster (WCSS)
    wcss = k_means.inertia_
    print("WCSS:", wcss)

    # Calcolo dello Silhouette Score
    silhouette_avg = silhouette_score(dataset, k_means.labels_)
    print("Silhouette Score:", silhouette_avg)


dataset = pd.read_csv('..\Datasets\ds_salaries_usd.csv')
encoded_dataset = categorical_feature_encoding(dataset)
elbow_method(encoded_dataset)
cluster_result = clustering(encoded_dataset, 3)

dataset['cluster'] = cluster_result
dataset.to_csv('..\Datasets\ds_salaries_usd+clusters.csv', index=False)