# 2. Gradient Descent Algorithms

## Types of Gradient Descent

### 1. Batch Gradient Descent
- **Description**: Uses the entire dataset to compute the gradient of the cost function.
- **Advantages**:
    - Converges to the global minimum for convex functions.
    - Stable updates.
- **Disadvantages**:
    - Computationally expensive for large datasets.
    - Requires a lot of memory.
- **Performence**:
    - with Zero Initialization Test Metrics: MSE: 66.6767, R2 Score: 0.8394
    - with Random Initialization Test Metrics: MSE: 66.4981, R2 Score: 0.8398
    - There is not much difference. Going with zero initialisation from now on

### 2. Stochastic Gradient Descent (SGD)
- **Description**: Uses one training example per iteration to compute the gradient.
- **Advantages**:
    - Faster convergence for large datasets.
    - Requires less memory.
- **Disadvantages**:
    - Updates can be noisy.
    - May not converge to the global minimum but rather oscillate around it.
- **Performance**:
    - MSE: 64.7104, R2 Score: 0.8441

### 3. Mini-Batch Gradient Descent
- **Description**: Uses a small random subset of the dataset to compute the gradient.
- **Advantages**:
    - Balances the efficiency of SGD and the stability of Batch Gradient Descent.
    - Reduces variance in the updates.
- **Disadvantages**:
    - Still requires tuning of batch size.
    - May require more iterations to converge compared to Batch Gradient Descent.
- **Performance**:
    - MSE: 64.6181, R2 Score: 0.8444
### Convergence
- stochastic gradient descent converges the fastest - reaching near convergence values by the 200th epoch. However - given the not too large size of the dataset, batch and mini batch models are not too far behind

## Lasso and Ridge Regularization

### Influence on the Model
- **Lasso Regularization**:
    - Adds a penalty equal to the absolute value of the magnitude of coefficients.
    - Can shrink some coefficients to zero, effectively performing feature selection.
    - MSE: 63.6213, R2 Score: 0.8468
- **Ridge Regularization**:
    - Adds a penalty equal to the square of the magnitude of coefficients.
    - Shrinks coefficients but does not set any to zero, retaining all features.
    - MSE: 113.3294, R2 Score: 0.7270  
    - I choose a lambda value of 0.5 for both ridge and lasso

## 4. Scaling of Features

### Effect on Model Performance
- **Improves Convergence**: Scaling features ensures that the gradient descent algorithms converge faster and more reliably.
- **Prevents Dominance**: Prevents features with larger scales from dominating the cost function, leading to better model performance..

## 5. Model Weights
-   The weightage of each feature strongly corresponds to the correlaion they share with delivery_time. Eg. Distance has the most weightage, the Prep time has slight +ve weightage while the the rest have neglidgible 

# 4. Decision Tree
1. Increasing max depth takes in more features for cnsideration which after a point begins to overfit the model
2. Both gini and entropy metrics are performing comparably same in terms of accuracy with validation/testing data

# 5. K means
## Hyperparametre
1. Increasing # clusters makes the superpixelss finer but increases computation
2. Increasing compactness makes the superpixels shapes uniform at the cost of color information
## RGB Space
1. RGB is not percetually uniform - the same delta in intensity can be more significant for some color channels. Also is more sensitive to brightnes
