import pandas as pd

def split_csv(file_name, parts):
    '''
    Parameters
    ----------
    file_name : string
        name of the csv file without the '.csv' ending
    parts : integer
        into how many parts to split the file?

    Returns
    -------
    None
    '''
    _df = pd.read_csv(f'{file_name}.csv') # import csv into df
    _chunk = _df.shape[0] // parts # number of rows in each subfile
    
    for x in range(parts):
        _start = x*_chunk
        _end = (x+1)*_chunk
        if x == parts-1: # when last chunk take the remainder of df
            _temp = _df[_start:]
        else:
            _temp = _df[_start:_end]
        _temp.to_csv(f'{file_name}_part{x:02}.csv', index=False) # export

### example
#split_csv('202212-divvy-tripdata', 2)
split_csv('data_clean', 30)