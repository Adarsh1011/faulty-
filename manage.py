#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import math
import pandas as pd

class Custom_transform(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X_, y=None):
        return self
    def transform(self, X_, y=None):
        X = X_.copy().astype(float)
        train_median = dict(X.median())
        X = X.fillna(train_median)
        for column in X.columns:
            X[column] = X[column].map(lambda i: np.log(i) if i > 0 else 0)
        return X

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_start.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    Custom_transform()
