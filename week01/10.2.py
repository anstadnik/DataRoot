import pandas as pd
from ten import data, labels


def weight_to_type(data, labels):
    '''
    :param data: dict
    :param labels: list[str]
    :return: dict
    '''
    # print(pd.DataFrame(data, labels))
    return pd.DataFrame(data, labels).groupby('animal', group_keys=False)['weight'].mean().to_dict()


print(weight_to_type(data, labels))
