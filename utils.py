def convert_to_min(df, lst):
    for col in lst:
        df[f'{col}_min'] = (df[col] / 60).round(0)
        df.drop(col, axis=1,  inplace=True)


