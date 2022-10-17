import re
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder as oneHot
from sklearn.preprocessing import MinMaxScaler as MMScaler


def get_first_cabin(row):
    """
    Extracts the first character of the passenger cabin ID

    Parameters
    ----------
    row : str
        The passenger cabin ID

    Returns
    -------
        The first character of the string

    """
    try:
        return row.split()[0]
    except AttributeError:
        return np.nan


def get_title(name):
    """
    Extracts the title from the passenger name

    Parameters
    ----------
    name : str
        The name of the passenger (includes the title)

    Returns
    -------
        The title of the passenger

    """
    if re.search("Mrs", name):
        return "Mrs"
    elif re.search("Mr", name):
        return "Mr"
    elif re.search("Miss", name):
        return "Miss"
    elif re.search("Master", name):
        return "Master"
    else:
        return "Other"


class CleaningTransformer(BaseEstimator, TransformerMixin):
    """Prepares the data for the training phase"""

    def __init__(self):
        self.feature_names_out = []

    def fit(self, df, y=None):
        """
        Fit method so that the class can be compatible with sklearn pipelines

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)
            The data to be preprocessed

        y : None
            Ignored

        Returns
        -------
        self : object
            The columns names are stored as property

        """
        self.feature_names_out = df.columns
        return self

    def transform(self, df, y=None):
        """
        It cleans the data set. More precisely, the "?" character is replaced
        by np.nan, the values in columns "age" and "fare" are converted to
        float, in the column "cabin" we apply the function "get_first_cabin",
        and in the column "title" we apply the funcion "get_title"

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        Xt : pandas data frame of shape (n_samples, n_features)
            Transformed data

        """
        df.replace("?", np.nan, inplace=True)
        df["age"] = df["age"].astype("float")
        df["fare"] = df["fare"].astype("float")
        df["cabin"] = df["cabin"].apply(get_first_cabin)
        df["title"] = df["name"].apply(get_title)
        return df


class RareLabelCategoricalEncoder(BaseEstimator, TransformerMixin):
    """
    Renames low frequency values in a categorical variable to 'Rare'

    Parameters
    ----------
    self : object

    tol : float
        Tolerance that determines which values are infrequent

    variables : list
        The list of categorical variables that will be used to replace
        infrequent categories.

    """

    def __init__(self, tol, variables):
        self.tol = tol
        self.variables = variables
        self.valid_labels_dict = {}
        self.feature_names_out = []

    def fit(self, df, y=None):
        """
        It determines, for each variable in the list "variables", the
        labels whose frequency is greather than the tolerance

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        self : object
            The frequent labels for each column in the list "variables" are
            stored as property

        """
        for var in self.variables:
            t = df[var].value_counts() / df.shape[0]
            self.valid_labels_dict[var] = t[t > self.tol].index.tolist()

        self.feature_names_out = df.columns
        return self

    def transform(self, df, y=None):
        """
        Renames the infrequent classes to "Rare"

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        df : pandas data frame of shape (n_samples, n_features)
            The transformed data frame

        """
        for var in self.variables:
            tmp = [
                col
                for col in df[var].unique()
                if col not in self.valid_labels_dict[var]
            ]
            df[var] = df[var].replace(
                to_replace=tmp, value=len(tmp) * ["Rare"]
            )

        return df


class CabinOnlyLetter(BaseEstimator, TransformerMixin):
    """
    Keeps only the letters in the column called "cabin"

    Parameters
    ----------
    column : str
        The column "cabin" in the titanic data set

    """

    def __init__(self, column):
        self.column = column
        self.feature_names_out = []

    def fit(self, df, y=None):
        """
        Fit method so that the class can be compatible with sklearn pipelines

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        self : object

        """
        self.feature_names_out = df.columns
        return self

    def transform(self, df, y=None):
        """
        Transform the selected column to one with only letters, i.e., it
        excludes digits and special characters

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        df : pandas data frame of shape (n_samples, n_features)
            Transformed data set

        """
        df[self.column] = [
            "".join(re.findall("[a-zA-Z]+", row)) if type(row) == str else row
            for row in df[self.column]
        ]

        return df


class OneHotEncoder(BaseEstimator, TransformerMixin):
    """
    Replaces the categorical variables by its dummy variables

    Parameters
    ----------
    self : object

    variables : list
        The list of categorical variables that will be used to create the
        dummy variables

    """

    def __init__(self, variables):
        self.encoder = oneHot(handle_unknown="ignore", drop="first")
        self.variables = variables
        self.feature_names_out = []

    def fit(self, df, y=None):
        """
        Trains the encoder. It stores the original column names of the data
        frame as property feature_names_out, and stores the dummy variables
        names as property variables_out.

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        self : object

        """
        self.feature_names_out = df.columns
        self.encoder.fit(df[self.variables])
        self.variables_out = self.encoder.get_feature_names_out(self.variables)
        return self

    def transform(self, df, y=None):
        """
        Replaces the categorical variables specified in "variables" by its
        dummy variables

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        df : pandas data frame
            The transformed data frame

        """
        df[self.encoder.get_feature_names_out(self.variables)] = \
            self.encoder.transform(df[self.variables]).toarray()
        df.drop(self.variables, axis=1, inplace=True)
        return df


class MissingIndicator(BaseEstimator, TransformerMixin):
    """
    For each variable in "columnsList" it creates a new column that indicates
    whether there is a missing value in a row

    Parameters
    ----------
    columnsList : list
        Columns that contain missing values

    """

    def __init__(self, columnsList):
        self.columnsList = columnsList
        self.feature_names_out = []

    def fit(self, df, y=None):
        """
        Fit method so that the class can be compatible with sklearn pipelines

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        self : object

        """
        self.feature_names_out = df.columns
        return self

    def transform(self, df, y=None):
        """
        Creates missing indicator columns

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        df : pandas data frame
            The transformed data frame

        """
        for column in self.columnsList:
            df[f"{column}_nan"] = df[column].isnull().astype(int)
        return df


class MinMaxScaler(BaseEstimator, TransformerMixin):
    """Scales the values of numerical columns between 0 and 1"""

    def __init__(self):
        self.scaler = MMScaler()
        self.feature_names_out = []

    def fit(self, df, y=None):
        """
        Trains the scaler

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------

        """
        self.scaler.fit(df)
        self.feature_names_out = df.columns
        return self

    def transform(self, df, y=None):
        """
        Scales the numerical variables

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        df : pandas data frame
            Transformed data set

        """
        return self.scaler.transform(df)


class NumericalImputesEncoder(BaseEstimator, TransformerMixin):
    """
    Imputes the missing values in numerical variables by the median

    Parameters
    ----------
    variables : list
        List of numerical variables with missing values

    """

    def __init__(self, variables):
        self.variables = variables
        self.feature_names_out = []
        self.valid_labels_dict = {}

    def fit(self, df, y=None):
        """
        Learns the median for each variable and keeps this information as
        property valid_labels_dict

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        self : object

        """
        for var in self.variables:
            t = df[var].median()
            self.valid_labels_dict[var] = t
        self.feature_names_out = df.columns

        return self

    def transform(self, df, y=None):
        """
        Imputation by the median

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        df : pandas data frame
            Transformed data frame

        """
        for var in self.variables:
            df[var] = df[var].fillna(self.valid_labels_dict[var])
        return df


class CategoricalImputerEncoder(BaseEstimator, TransformerMixin):
    """
    Imputes missing values of categorical variables by the class "missing"

    Parameters
    ----------
    variables : list
        List of categorical variables with missing values

    """

    def __init__(self, variables):
        self.variables = variables
        self.feature_names_out = []

    def fit(self, df, y=None):
        """
        Fit method so that the class can be compatible with sklearn pipelines

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        self : object

        """
        self.feature_names_out = df.columns
        return self

    def transform(self, df, y=None):
        """
        Imputation of missing values

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        df : pandas data frame
            Transformed data frame

        """
        df[self.variables] = df[self.variables].fillna("missing")
        return df


class DropTransformer(BaseEstimator, TransformerMixin):
    """
    Drop columns that are not needed for the training

    Parameter
    ---------
    drop_columns : list
        List of column names that will be removed

    """

    def __init__(self, drop_columns):
        self.drop_columns = drop_columns
        self.feature_columns = []
        self.feature_names_out = []

    def fit(self, df, y=None):
        """
        Fit method so that the class can be compatible with sklearn pipelines

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        self : object

        """
        self.feature_columns = df.drop(columns=self.drop_columns).columns
        return self

    def transform(self, df, y=None):
        """
        Remove unnecessary columns

        Parameters
        ----------
        df : pandas data frame of shape (n_samples, n_features)

        y : None
            Ignored

        Returns
        -------
        df : pandas data frame
            Transformed data frame

        """
        return df.drop(columns=self.drop_columns)
