import numpy as np
import torch
from scipy.linalg import eigh
from sklearn.cluster import KMeans

def random_matrix_theory_filter(correlation_matrix, q):
    """
    Filters the correlation matrix using Random Matrix Theory (RMT).
    This removes noise and retains significant eigenvalues and eigenvectors.
    
    Args:
        correlation_matrix (np.ndarray): Empirical correlation matrix.
        q (float): Ratio of time series length (T) to the number of assets (N).
    
    Returns:
        np.ndarray: Filtered correlation matrix.
    """
    # Eigen decomposition
    eigenvalues, eigenvectors = eigh(correlation_matrix)
    
    # Theoretical maximum eigenvalue for random matrix
    lambda_plus = (1 + (1 / q) ** 0.5) ** 2
    
    # Filter eigenvalues
    significant_eigenvalues = eigenvalues[eigenvalues > lambda_plus]
    significant_eigenvectors = eigenvectors[:, eigenvalues > lambda_plus]
    
    # Reconstruct filtered correlation matrix
    filtered_correlation_matrix = significant_eigenvectors @ np.diag(significant_eigenvalues) @ significant_eigenvectors.T
    
    return filtered_correlation_matrix

def detect_communities(filtered_correlation_matrix, n_clusters):
    """
    Detects communities in the filtered correlation matrix using KMeans clustering.
    
    Args:
        filtered_correlation_matrix (np.ndarray): Filtered correlation matrix.
        n_clusters (int): Number of clusters to detect.
    
    Returns:
        np.ndarray: Cluster labels for each asset.
    """
    # Perform KMeans clustering on the rows of the filtered correlation matrix
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(filtered_correlation_matrix)
    
    return cluster_labels

def portfolio_risk_model(returns, cluster_labels):
    """
    Computes portfolio risk based on the identified clusters.
    
    Args:
        returns (np.ndarray): Matrix of asset returns (T x N).
        cluster_labels (np.ndarray): Cluster labels for each asset.
    
    Returns:
        float: Portfolio risk.
    """
    n_clusters = np.unique(cluster_labels).size
    cluster_risks = []
    
    for cluster in range(n_clusters):
        cluster_indices = np.where(cluster_labels == cluster)[0]
        cluster_returns = returns[:, cluster_indices]
        cluster_covariance = np.cov(cluster_returns, rowvar=False)
        cluster_risk = np.trace(cluster_covariance)
        cluster_risks.append(cluster_risk)
    
    total_risk = sum(cluster_risks)
    return total_risk

if __name__ == '__main__':
    # Generate dummy data
    np.random.seed(42)
    torch.manual_seed(42)
    
    # Number of assets (N) and time series length (T)
    N = 50
    T = 200
    q = T / N
    
    # Generate random returns matrix (T x N)
    returns = np.random.randn(T, N)
    
    # Compute empirical correlation matrix
    correlation_matrix = np.corrcoef(returns, rowvar=False)
    
    # Filter correlation matrix using RMT
    filtered_correlation_matrix = random_matrix_theory_filter(correlation_matrix, q)
    
    # Detect communities (e.g., 5 clusters)
    n_clusters = 5
    cluster_labels = detect_communities(filtered_correlation_matrix, n_clusters)
    
    # Compute portfolio risk
    risk = portfolio_risk_model(returns, cluster_labels)
    
    print("Cluster labels:", cluster_labels)
    print("Portfolio risk:", risk)