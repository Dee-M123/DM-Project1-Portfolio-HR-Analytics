import pandas as pd
import numpy as np
from typing import Dict

class HREDA:
    """
    A helper class for performing exploratory data analysis (EDA) on the dataset.
    
    This class takes into account numeric and categorical columns and provides
    utilities for generating descriptive statistics, distribution summaries, and
    categorical value summaries.
    """
    

    def __init__(self, df: pd.DataFrame):
        """
        Initialize the HREDA object with a dataframe.
        
        """
        
        
        self.df = df
        self.numeric_col = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
        self.categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    def numeric_summary(self) -> pd.DataFrame:
        """
        Generate summary statistics for all numeric columns.

        Returns
        -------
        
            Transposed dataframe containing count, mean, std, min, quartiles, and max
            for each numeric column.
        """
        
        return self.df[self.numeric_col].describe().T

    def numeric_distribution_stats(self, col: str) -> Dict[str, float]:
        """
        Compute detailed distribution statistics for a single numeric column.

        Parameters
        ----------
            Name of the numeric column to summarize.

        Returns
        -------
            A dictionary containing mode, min, max, and specific quantiles.
        """
        
        numeric_data = self.df[col].dropna()

        return {
            "mode": numeric_data.mode()[0] if not numeric_data.mode().empty else None,
            "min": numeric_data.min(),
            "max": numeric_data.max(),
            "q25 (lower)": numeric_data.quantile(0.25),
            "q50 (median)": numeric_data.quantile(0.50),
            "q75 (upper)": numeric_data.quantile(0.75),
            "q90 (top 10%)": numeric_data.quantile(0.90),
            "q99": numeric_data.quantile(0.99),
        }

    def summarise_cat(self, col: str) -> pd.DataFrame:
        """
        Generate count and percentage distributions for a single categorical column.

        Returns
        -------
            DataFrame showing counts and percentage share of each category.
        """
        
        counts = self.df[col].value_counts(dropna=False)
        perc = self.df[col].value_counts(normalize=True, dropna=False) * 100

        return pd.DataFrame({"count": counts, "percentage": perc})

    def cat_summary(self) -> Dict[str, pd.DataFrame]:
        """
        Generate summary distributions for all categorical columns.

        Returns
        -------
            A dictionary where each key is a column name and each value is a 
            summary dataframe containing category counts and percentages.
        """
        
        return {col: self.summarise_cat(col) for col in self.categorical_cols}
