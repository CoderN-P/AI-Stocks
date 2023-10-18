def generate_lag(DF, columns_to_lag):

    # Create lag features for selected columns
    for column in columns_to_lag:
        DF[f'{column}_lag'] = DF[column].shift(1)

    DF = DF.drop(0)
    return DF