from preprocess import dates, service
import pandas as _pd
import pybaseball as _pybaseball
import os as _os

def get_mlb_dates(year=None):
        obj = dates.GetSchedule(year)
        obj.set_prior_years()
        obj.set_mlb_dates()
        obj.set_endpoints()
        obj.set_all_star_break_days()
        obj.set_season_days_so_far()
        return obj
def get_prior_years():
        obj = dates.GetSchedule()
        obj.set_prior_years()
        return obj.prior_years

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
        raw_stats_df.to_csv(self.path, index=False)
    def get_path(self):
        return self.path

class ReadData:
    def __init__(self, path): 
        self.raw_stats_df = None
        self.dates_we_dont_got = None
        #self.season_days_so_far = dates.get_season_days_so_far()
        self.path = path
    def set_raw_stats_df(self):
        try:
            self.raw_stats_df = _pd.read_csv(self.path)
            #self.raw_stats_df = _pd.read_csv('../data/csv/raw_batter_stats.csv')
        except OSError:
            print('FIRST-TIME-USE INITIALIZE: compiling batter data using pybaseball.')
            obj = service.RawBatterStats(seasons=get_prior_years())
            obj.set_raw_stats()
            self.raw_stats_df = obj.get_stats()
    def set_dates(self):
        dates = get_mlb_dates()
        season_days_so_far = dates.get_season_days_so_far()
        weird_dates = ['2019-03-22', '2019-03-23', '2019-03-24', '2019-03-25'
        , '2019-03-26', '2019-03-27'] # Account for early Japanese series in '19
        self.dates_we_got = list(self.raw_stats_df.DATE.unique())
        self.dates_we_dont_got = [d for d in season_days_so_far if d not in self.dates_we_got]
        self.dates_we_dont_got = [d for d in self.dates_we_dont_got if d not in weird_dates]
    def update_raw_stats_df(self):
        dates = get_mlb_dates()
        season_days_so_far = dates.get_season_days_so_far()
        dates_we_got = list(self.raw_stats_df.DATE.unique())
        self.dates_we_dont_got = [d for d in season_days_so_far if d not in dates_we_got]
        weird_dates = ['2019-03-22', '2019-03-23', '2019-03-24', '2019-03-25'
            , '2019-03-26', '2019-03-27'] # Account for early Japanese series in '19
        self.dates_we_dont_got = [d for d in self.dates_we_dont_got if d not in weird_dates]
        if len(self.dates_we_dont_got) > 0:
            print('UPDATING...')
            print('Adding stats from dates: ', self.dates_we_dont_got)
            df_lst, ct = service.get_raw_stats(self.dates_we_dont_got, len(self.dates_we_dont_got), ct=0)
            new_df = _pd.concat(df_lst, ignore_index=True)
            self.raw_stats_df = _pd.concat([self.raw_stats_df, new_df], ignore_index=True)
            self.raw_stats_df.update(new_df, overwrite=False)
        else: 
            print('Batter data is current.')
        self.raw_stats_df.drop_duplicates(inplace=True)
        self.raw_stats_df.sort_values('DATE', ascending=False, inplace=True)
    def get_raw_stats_df(self):
        return self.raw_stats_df
