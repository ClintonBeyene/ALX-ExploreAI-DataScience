# Machine Learning Classifiers: k-Nearest Neighbors (KNN) and Naive Bayes

This README offers an overview of two fundamental machine learning classifiers I explored during my learning journey: k-Nearest Neighbors (KNN) and Naïve Bayes. It covers their core concepts, implementation guidelines, and a curated list of resources to enhance your understanding.

---

## 1. k-Nearest Neighbors (KNN)

### Overview
KNN is a simple, distance-based supervised learning algorithm used for classification and regression. It predicts the class of a data point by examining the classes of its `k` closest neighbors in the feature space.

### Key Concepts
- **Distance Metrics**: Euclidean, Manhattan, or Minkowski distances are commonly used to measure similarity.
- **Choice of `k`**: A smaller `k` increases sensitivity to noise, while a larger `k` smooths decision boundaries.
- **Curse of Dimensionality**: High-dimensional data can reduce KNN's effectiveness due to sparse distance metrics.

### Implementation Resources
- **Scikit-Learn Documentation**:  
  [KNeighborsClassifier Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)  
  *Official guide for implementing KNN using Scikit-Learn.*
- **Step-by-Step Tutorial**:  
  [KNN in Python and Scikit-Learn](https://realpython.com/knn-python/)  
  *Hands-on tutorial covering data preprocessing, model training, and evaluation.*
- **IBM Article on KNN:**
  [What is the k-nearest neighbors (KNN) algorithm?](https://www.ibm.com/think/topics/knn)
  *A detailed explanation of KNN's working principles, use cases, and tradeoffs.*

---

## 2. Naive Bayes

### Overview
Naive Bayes is a probabilistic classifier based on Bayes' theorem, with the "naive" assumption that features are conditionally independent. It is fast, scalable, and effective for high-dimensional datasets.

### Key Concepts
- **Bayes' Theorem**: Calculates the probability of a class given observed features:  
  \( P(y | X) = \frac{P(X | y) P(y)}{P(X)} \)
- **Feature Independence**: Assumes no correlation between features (simplifies computation).
- **Variants**:  
  - **Gaussian**: For continuous data.  
  - **Multinomial**: For discrete counts (e.g., text classification).  
  - **Bernoulli**: For binary features.

### Implementation Resources
- **Bayes' Theorem Video Explanation**:  
  [Understanding Bayes Theorem](https://youtu.be/HZGCoVF3YvM)  
  *Visual primer on the fundamentals of Bayesian probability.*
- **Scikit-Learn Documentation**:  
  [Naive Bayes Documentation](https://scikit-learn.org/stable/modules/naive_bayes.html)  
  *Comprehensive guide to Gaussian, Multinomial, and Bernoulli Naive Bayes in Scikit-Learn.*
- **Python Tutorial**:  
  [Naive Bayes Classifier Tutorial](https://hands-on.cloud/naive-bayes-classifier-python-tutorial/)  
  *End-to-end walkthrough for building a Naive Bayes model from scratch.*
- **IBM Article on Naive Bayes:**:
  [What are Naïve Bayes classifiers?](https://www.ibm.com/think/topics/naive-bayes)
  *Overview of the algorithm, its applications, and limitations.*

---

## 3. General Workflow for Both Algorithms
1. **Data Preparation**: Split data into training and testing sets. Normalize features for KNN.
2. **Model Training**: Use `fit()` in Scikit-Learn.
3. **Prediction**: Generate class labels with `predict()`.
4. **Evaluation**: Assess accuracy, precision, recall, or F1-score.

---

## 4. When to Use Each Algorithm?
- **KNN**:  
  - Small to medium datasets.  
  - Interpretability of decision boundaries matters.  
  - Non-linear relationships exist.  
- **Naive Bayes**:  
  - Text classification (e.g., spam detection).  
  - Real-time predictions due to speed.  
  - High-dimensional data (e.g., NLP tasks).

---

## 5. Further Reading
- Explore hyperparameter tuning (e.g., `k` in KNN, Laplace smoothing in Naive Bayes).
- Compare with other classifiers like Decision Trees or SVMs.

---

**Happy Learning!** 