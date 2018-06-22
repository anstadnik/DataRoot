import pandas as pd
from ten import data, labels


def sorted_df(data, labels):
    '''
    :param data: dict
    :param labels: list[str]
    :return: pandas.core.frame.DataFrame
    '''
    return pd.DataFrame(data, labels).sort_values(by=['age', 'weight'], ascending=[True, False])


print(sorted_df(data, labels))
