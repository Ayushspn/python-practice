"""
xgboost_demo.py

A compact, runnable script that:
- Builds a tiny binary classification dataset
- Computes gradients and Hessians for logistic loss (step-by-step)
- Demonstrates leaf weight and split gain calculations on a toy split
- Trains XGBoost and sklearn GradientBoostingClassifier on the same data
- Compares metrics (accuracy, AUC) and prints feature importances
- Uses early stopping for XGBoost

Requirements:
    pip install numpy pandas scikit-learn xgboost matplotlib

Run:
    python xgboost_demo.py
"""
# Top-level docstring describing purpose, requirements, and how to run.
# Output: no runtime output; serves as file documentation.

import numpy as np
# Import NumPy for numerical arrays and math operations.
# Output: no runtime output; makes np available.

import pandas as pd
# Import pandas for DataFrame handling and convenience.
# Output: no runtime output; makes pd available.

from sklearn.datasets import make_classification
# Import helper to create a synthetic classification dataset.
# Output: no runtime output; function available to generate data.

from sklearn.model_selection import train_test_split
# Import train_test_split to create train/validation/test splits.
# Output: no runtime output; function available.

from sklearn.ensemble import GradientBoostingClassifier
# Import sklearn's GradientBoostingClassifier as a baseline model.
# Output: no runtime output; class available.

from sklearn.metrics import accuracy_score, roc_auc_score
# Import metrics to evaluate model performance (accuracy and AUC).
# Output: no runtime output; functions available.

import xgboost as xgb
# Import XGBoost library for high-performance gradient boosting.
# Output: no runtime output; xgb API available.

import matplotlib.pyplot as plt
# Import matplotlib for optional plotting of learning curves.
# Output: no runtime output; plotting functions available.

# ---------------------------
# 1) Create a small dataset
# ---------------------------
RANDOM_STATE = 42
# Set a fixed random seed for reproducibility.
# Output: no runtime output; ensures consistent results across runs.

X, y = make_classification(
    n_samples=2000,
    n_features=6,
    n_informative=4,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    class_sep=1.2,
    flip_y=0.02,
    random_state=RANDOM_STATE,
)
# Create a synthetic binary classification dataset with 2000 samples and 6 features.
# Why: provides a controlled dataset to demonstrate algorithms.
# Output: X is a (2000,6) numpy array; y is a (2000,) array of 0/1 labels.

feature_names = [f"f{i}" for i in range(X.shape[1])]
# Create readable feature names f0..f5 for DataFrame columns and printing.
# Output: list ['f0','f1',...]; used for DataFrame columns and feature importance display.

df = pd.DataFrame(X, columns=feature_names)
# Convert features to a pandas DataFrame for easier manipulation and display.
# Output: DataFrame with 2000 rows and 6 columns.

df["target"] = y
# Add the target column to the DataFrame.
# Output: DataFrame now has a 'target' column with 0/1 labels.

# Train / validation / test split
X_trainval, X_test, y_trainval, y_test = train_test_split(
    df[feature_names], df["target"], test_size=0.2, random_state=RANDOM_STATE, stratify=df["target"]
)
# Split data into 80% train+val and 20% test, stratified to preserve class balance.
# Why: keep a held-out test set for final evaluation.
# Output: X_trainval shape (1600,6), X_test shape (400,6).

X_train, X_val, y_train, y_val = train_test_split(
    X_trainval, y_trainval, test_size=0.25, random_state=RANDOM_STATE, stratify=y_trainval
)  # 0.25 x 0.8 = 0.2
# Further split train+val into 75% train and 25% val, resulting in 60% train, 20% val, 20% test.
# Why: validation set used for early stopping and hyperparameter checks.
# Output: X_train shape (1200,6), X_val shape (400,6), X_test shape (400,6).

print("Dataset sizes:", X_train.shape, X_val.shape, X_test.shape)
# Print dataset sizes to confirm splits.
# Output example: Dataset sizes: (1200, 6) (400, 6) (400, 6)

# ---------------------------
# 2) Gradients and Hessians for logistic loss
# ---------------------------
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))
# Define sigmoid function to convert raw scores to probabilities.
# Why: logistic loss uses probabilities via sigmoid.
# Output: callable function; no immediate output.

def logistic_grad_hess(y_true, y_pred_proba, eps=1e-15):
    """
    For logistic loss (binary cross-entropy), given true labels y (0/1)
    and predicted probabilities p = sigmoid(raw_score),
    gradients and hessians w.r.t. raw_score are:
        g = p - y
        h = p * (1 - p)
    We assume y_pred_proba are probabilities in (0,1).
    """
    p = np.clip(y_pred_proba, eps, 1 - eps)
    # Clip probabilities to avoid numerical issues at 0 or 1.
    g = p - y_true
    # Gradient of logloss w.r.t. raw score: p - y.
    h = p * (1 - p)
    # Hessian (second derivative) of logloss w.r.t. raw score: p*(1-p).
    return g, h
# Why: XGBoost uses gradients and Hessians to compute optimal leaf weights and gains.
# Output: returns arrays g and h of same length as inputs.

# Create a simple baseline prediction (constant probability)
base_prob = np.full_like(y_train, y_train.mean(), dtype=float)
# Create a constant prediction equal to the training positive class frequency.
# Why: baseline to compute initial gradients/hessians and illustrate formulas.
# Output: array of probabilities, e.g., all 0.48 if 48% positives.

g, h = logistic_grad_hess(y_train.values if isinstance(y_train, pd.Series) else y_train, base_prob)
# Compute gradients and Hessians for the baseline predictions.
# Why: demonstrates how pseudo-residuals (gradients) and curvature (hessians) look initially.
# Output: arrays g and h printed below.

print("\nExample gradients/hessians (first 8):")
# Print header for clarity.
# Output: newline and header text.

for i in range(8):
    print(f"y={y_train.values[i]}, p={base_prob[i]:.4f}, g={g[i]:.4f}, h={h[i]:.4f}")
# Print first 8 gradient/hessian pairs to inspect values.
# Why: quick sanity check that g and h behave as expected.
# Output example lines: y=1, p=0.48, g=-0.52, h=0.2496

# ---------------------------
# 3) Toy leaf weight and split gain calculation
# ---------------------------
def leaf_weight(G, H, lam):
    """Optimal leaf weight w* = -G / (H + lambda)"""
    return -G / (H + lam)
# Function to compute optimal leaf weight given aggregated gradient G and Hessian H.
# Why: shows closed-form solution XGBoost uses for leaf predictions.
# Output: numeric weight when called.

def leaf_score(G, H, lam, gamma=0.0):
    """Leaf score contribution: -0.5 * G^2 / (H + lambda) + gamma"""
    return -0.5 * (G ** 2) / (H + lam) + gamma
# Function to compute leaf score (objective reduction) used to evaluate splits.
# Why: used to compute split gain and decide whether a split is beneficial.
# Output: numeric score when called.

# Build a tiny toy example: suppose we have a parent node with 6 samples
# and we consider splitting into left (4 samples) and right (2 samples).
# We'll fabricate gradients and hessians for demonstration.
G_parent = -5.0
# Aggregated gradient for parent node (sum of g_i).
H_parent = 3.0
# Aggregated Hessian for parent node (sum of h_i).

G_left = -4.0
# Aggregated gradient for left child.
H_left = 2.0
# Aggregated Hessian for left child.

G_right = G_parent - G_left
# Compute right child gradient by subtraction to keep consistency.
H_right = H_parent - H_left
# Compute right child Hessian similarly.

lam = 1.0
# Regularization parameter lambda (L2 on leaf weights).
gamma = 0.0
# Gamma is the penalty for adding a leaf (min split gain threshold).

w_parent = leaf_weight(G_parent, H_parent, lam)
# Compute optimal weight for parent leaf using formula.
w_left = leaf_weight(G_left, H_left, lam)
# Compute optimal weight for left child.
w_right = leaf_weight(G_right, H_right, lam)
# Compute optimal weight for right child.

score_parent = leaf_score(G_parent, H_parent, lam, gamma)
# Compute parent leaf score (objective contribution).
score_left = leaf_score(G_left, H_left, lam, gamma)
# Compute left child score.
score_right = leaf_score(G_right, H_right, lam, gamma)
# Compute right child score.

gain = (score_left + score_right) - score_parent
# Compute split gain: improvement in objective by splitting parent into children.
# Why: if gain > 0 (after subtracting gamma), the split is beneficial.
# Output: numeric gain value printed below.

print("\nToy split example:")
# Print header for toy example.
# Output: newline and header.

print(f"G_parent={G_parent}, H_parent={H_parent}, w_parent={w_parent:.4f}, score_parent={score_parent:.4f}")
# Print parent aggregated stats, optimal weight, and score.
# Output example: G_parent=-5.0, H_parent=3.0, w_parent=0.8333, score_parent=-1.0417

print(f"G_left={G_left}, H_left={H_left}, w_left={w_left:.4f}, score_left={score_left:.4f}")
# Print left child stats and score.
# Output example: G_left=-4.0, H_left=2.0, w_left=1.3333, score_left=-1.3333

print(f"G_right={G_right}, H_right={H_right}, w_right={w_right:.4f}, score_right={score_right:.4f}")
# Print right child stats and score.
# Output example: G_right=-1.0, H_right=1.0, w_right=0.5000, score_right=-0.2500

print(f"Split gain = {gain:.4f} (if > 0, split is beneficial after gamma)")
# Print computed gain and interpretation.
# Output example: Split gain = 0.0417 (small positive gain means split slightly beneficial)

# ---------------------------
# 4) Train sklearn GradientBoostingClassifier (baseline)
# ---------------------------
gbc = GradientBoostingClassifier(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=4,
    subsample=0.8,
    random_state=RANDOM_STATE,
)
# Instantiate sklearn's GradientBoostingClassifier as a baseline.
# Why: compare a standard implementation to XGBoost to see differences in performance.
# Output: gbc object ready to fit.

gbc.fit(X_train, y_train)
# Train the sklearn Gradient Boosting model on training data.
# Why: baseline model for comparison.
# Output: prints nothing by default; model fitted in memory.

y_val_pred_proba_gbc = gbc.predict_proba(X_val)[:, 1]
# Predict validation probabilities for the positive class using the trained model.
# Output: array of probabilities for validation set.

y_test_pred_proba_gbc = gbc.predict_proba(X_test)[:, 1]
# Predict test probabilities for the positive class.
# Output: array of probabilities for test set.

acc_val_gbc = accuracy_score(y_val, (y_val_pred_proba_gbc > 0.5).astype(int))
# Compute validation accuracy by thresholding probabilities at 0.5.
# Why: quick, interpretable metric.
# Output: scalar accuracy between 0 and 1.

auc_val_gbc = roc_auc_score(y_val, y_val_pred_proba_gbc)
# Compute validation AUC, a threshold-independent metric for binary classification.
# Output: scalar AUC between 0 and 1.

acc_test_gbc = accuracy_score(y_test, (y_test_pred_proba_gbc > 0.5).astype(int))
# Compute test accuracy similarly.
# Output: scalar accuracy.

auc_test_gbc = roc_auc_score(y_test, y_test_pred_proba_gbc)
# Compute test AUC.
# Output: scalar AUC.

print("\nGradientBoostingClassifier (sklearn) results:")
# Print header for baseline results.
# Output: newline and header.

print(f"Validation  - Accuracy: {acc_val_gbc:.4f}, AUC: {auc_val_gbc:.4f}")
# Print validation accuracy and AUC for sklearn GBC.
# Output example: Validation  - Accuracy: 0.8200, AUC: 0.8900

print(f"Test        - Accuracy: {acc_test_gbc:.4f}, AUC: {auc_test_gbc:.4f}")
# Print test accuracy and AUC for sklearn GBC.
# Output example: Test        - Accuracy: 0.8150, AUC: 0.8850

# ---------------------------
# 5) Train XGBoost with early stopping
# ---------------------------
xgb_clf = xgb.XGBClassifier(
    n_estimators=1000,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_lambda=1.0,
    reg_alpha=0.0,
    use_label_encoder=False,
    eval_metric="logloss",
    random_state=RANDOM_STATE,
    verbosity=0,
)
# Instantiate