import pandas as pd
from ten import data, labels

def repl_nan(data, labels):
    '''
    :param data: dict
    :param labels: list[str]
    :return: pandas.core.frame.DataFrame
    '''
    return pd.DataFrame(data, labels).groupby('animal', group_keys=False).apply(lambda x: x.fillna(x.mean())).sort_index()


print(repl_nan(data, labels))
