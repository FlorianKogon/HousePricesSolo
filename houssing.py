import pandas as pd


class Houssing(object):
    """docstring for Houssing"""
    def __init__(self, arg):
        super(Houssing, self).__init__()
        self.arg = arg

    def data_base(self, path):
        self.data_base = pd.read_csv(path)

    def get_features(self, dataframe, columns):
        self.get_features = dataframe.drop(columns=columns, inplace=True)

    def get_target(self, dataframe, column):
        self.get_target = dataframe[[column]]
