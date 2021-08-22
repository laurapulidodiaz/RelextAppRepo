from controller import local_to_dataframes as ltd

def min_max_scale(x):
    x_max = x.max()
    x_min = x.min()
    if x_max == x_min:
        return x.apply(lambda z: 0)
    return x.apply(lambda z: (z-x_min)/(x_max-x_min))


def min_max_scaled(data, how='all'):
    min_max_scaled_df = data.copy()
    if how == 'row':
        return min_max_scaled(min_max_scaled_df.T, how='col').T
    elif how == 'all':
        x_max = min_max_scaled_df.max().max()
        x_min = min_max_scaled_df.min().min()
        return (min_max_scaled_df-x_min)/(x_max-x_min)
    else:
        for col in min_max_scaled_df.columns:
            min_max_scaled_df[col] = min_max_scale(min_max_scaled_df[col])
        return min_max_scaled_df






    