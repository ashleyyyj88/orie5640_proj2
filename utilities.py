
from sklearn import preprocessing


def normalize(series):
    min_max_scaler = preprocessing.MinMaxScaler()
    series = series.values.reshape(-1, 1)
    series_scaled = min_max_scaler.fit_transform(series)
    return series_scaled


def filterout(df, column, value):
    return df[df[column] != value]


def get_common_dates(df_list, filenames):
    benchmark = df_list[0]['DATE'].tolist()
    common_dates = {fn: [] for fn in filenames}
    i = 0
    for df in df_list:
        common_dates[filenames[i]] = df['DATE'].isin(benchmark)
        i += 1
    return common_dates
