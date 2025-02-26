# Unsupervised Learning: Gaussian Mixture Models (GMM)

## Overview
Gaussian Mixture Models (GMM) are a probabilistic clustering method used in unsupervised learning. Unlike k-means, which assumes clusters are spherical, GMM assumes each cluster follows a multivariate Gaussian distribution, allowing for more flexible and ellipsoidal cluster shapes.

## Resources
Here are some useful resources that provide an in-depth understanding of Gaussian Mixture Models that i covered in my study:

1. **[In Depth: Gaussian Mixture Models](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.12-Gaussian-Mixtures.ipynb)**  
   - An in-depth look at Gaussian Mixture Models as discussed in the Python Data Science Handbook.  

2. **[A GAUSSIAN MIXTURE MODEL LAYER JOINTLY OPTIMIZED WITH DISCRIMINATIVE FEATURES WITHIN A DEEP NEURAL NETWORK ARCHITECTURE](https://research.google/pubs/a-gaussian-mixture-model-layer-jointly-optimized-with-discriminative-features-within-a-deep-neural-network-architecture/)**

    - A study on integrating GMM as the last layer of a Deep Neural Network (DNN) and optimizing it using ASGD. It explores the impact of joint optimization, depth, and generative modeling compared to standard DNNs.
    - **[PDF Material](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43912.pdf)** 

3. **[Deep Gaussian mixture model for unsupervised image segmentation](https://arxiv.org/pdf/2404.12252)**
    - A study by Matthias Schwab, Agnes Mayr, and Markus Haltmeier on combining GMM with deep learning for image segmentation.

4. **[Gaussian Mixture Models Explained](https://www.youtube.com/watch?v=JNlEIEwe-Cg)**  
   - Follow along as Siraj Raval predicts customer churn using a clustering technique called the Gaussian Mixture Model.  

5. **[Training Gaussian Mixture Models at Scale via Coresets](https://research.google/pubs/training-gaussian-mixture-models-at-scale-via-coresets/)**

    - How can we train a statistical mixture model on a massive data set? In this work we show how to construct \emph{coresets} for mixtures of Gaussians. A coreset is a weighted subset of the data, which guarantees that models fitting the coreset also provide a good fit for the original data set. We show that, perhaps surprisingly, Gaussian mixtures admit coresets of size polynomial in dimension and the number of mixture components, while being \emph{independent} of the data set size. Hence, one can harness computationally intensive algorithms to compute a good approximation on a significantly smaller data set. More importantly, such coresets can be efficiently constructed both in distributed and streaming settings and do not impose restrictions on the data generating process. Our results rely on a novel reduction of statistical estimation to problems in computational geometry and new combinatorial complexity results for mixtures of Gaussians. Empirical evaluation on several real- world data sets suggests that our coreset-based approach enables significant reduction in training-time with negligible approximation error.

These resources will help reinforce the concepts and provide practical insights into applying GMM in real-world scenarios.

