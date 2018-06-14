import pandas as pd
from ten import data, labels


def kittens(data, labels):
    '''
    :param data: dict
    :param labels: list[str]
    :return: pandas.core.frame.DataFrame
    '''
    df = pd.DataFrame(data, labels)
    return df[(df.animal == 'cat') & (df.age < 3)]


print(kittens(data, labels))
