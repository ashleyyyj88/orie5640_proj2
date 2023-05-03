
from sklearn import preprocessing


def normalize(series):
    min_max_scaler = preprocessing.MinMaxScaler()
    series = series.values.reshape(-1, 1)
    series_scaled = min_max_scaler.fit_transform(series)
    return series_scaled


def filterout(df, column, value):
    return df[df[column] != value]


def get_common_dates(df_list, filenames):

    common_dates = {fn: [] for fn in filenames}
    common_dates['IG'] = df_list['IG']['Date'].isin(
        df_list['HY']['Date']) & df_list['IG']['Date'].isin(df_list['SPX']['Date'])
    common_dates['HY'] = df_list['HY']['Date'].isin(
        df_list['IG']['Date']) & df_list['HY']['Date'].isin(df_list['SPX']['Date'])
    common_dates['SPX'] = df_list['SPX']['Date'].isin(
        df_list['HY']['Date']) & df_list['SPX']['Date'].isin(df_list['IG']['Date'])

    return common_dates
