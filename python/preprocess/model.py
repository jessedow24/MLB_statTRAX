import preprocess
import pandas as _pd
import pybaseball as _pybaseball
import os as _os


class StoreData:
    def __init__(self, file_name='raw_batter_stats'):
        self.file_name = file_name
        self.path = None
        if _os.name == 'nt':
            self.data_dir = '..\\data\\csv\\'
        elif _os.name == 'posix':
            self.data_dir = '../data/csv/'
        else: 
            print('WARNING: If not using Windows or OSX, you must customize output path in Data class in preprocessing.data')
        self.path = self.data_dir+self.file_name+'.csv'
    def save(self, raw_stats_df):
        raw_stats_df.to_csv(self.path)

class ReadData:
    def __init__(self): 
        self.raw_stats_df = None

    def set_raw_stats_df(self):
        try:
            self.raw_stats_df = _pd.read_csv('../data/csv/raw_batter_stats.csv')
            #print('Pulling batter data from existing file...')
        except OSError:
            print('FIRST-TIME-USE INITIALIZE: pulling batter data from pybaseball api.  This will take several minutes...')
            self.raw_stats_df = preprocess.get_raw_batter_stats(year=preprocess.get_prior_years())

    def update_raw_stats_df(self):
        dates = preprocess.get_mlb_dates()
        season_days_so_far = dates.get_season_days_so_far()
        dates_we_got = list(self.raw_stats_df.DATE.unique())

        dates_we_dont_got = [d for d in season_days_so_far if d not in dates_we_got]
        weird_dates = ['2019-03-22', '2019-03-23', '2019-03-24', '2019-03-25'
            , '2019-03-26', '2019-03-27'] # Account for early Japanese series in '19
        dates_we_dont_got = [d for d in dates_we_dont_got if d not in weird_dates]


        if len(dates_we_dont_got) > 0:
            print('Updating batter data to most recent date...')
            print(dates_we_dont_got)
            new_df = _pd.DataFrame(preprocess.service.get_raw_stats(dates_we_dont_got))
            self.raw_stats_df = _pd.concat([self.raw_stats_df, new_df])
        else: 
            print('Batter data is current.')

        self.raw_stats_df.drop_duplicates(inplace=True)
        self.raw_stats_df.sort_values('DATE', inplace=True)

    def get_raw_stats_df(self):
        return self.raw_stats_df



    # pull new data for missing dates
    # pull existing raw_stats_df
    # Concat, drop duplicates, and sort