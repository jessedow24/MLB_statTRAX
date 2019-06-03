import preprocess 
import pandas as _pd
import pybaseball as _pybaseball

def get_raw_stats(season_days_so_far):
        df_lst = []
        for i in range(len(season_days_so_far)):
            d = season_days_so_far[i]
            try:
                tmp_df = _pybaseball.batting_stats_range(str(d), )
                print('%d%%\r'%i, end="")
                tmp_df['DATE'] = d
                df_lst.append(tmp_df)
            except:
                continue
        return _pd.concat(df_lst, ignore_index=True)

class RawBatterStats:
    def __init__(self, seasons=None):
        self.seasons = seasons
        self.raw_stats = _pd.DataFrame()
        
    def set_raw_stats(self):
        if self.seasons:
            df_lst2 = []
            for season in self.seasons:
                dates = preprocess.get_mlb_dates(season)
                season_days_so_far = dates.get_season_days_so_far()
                df_lst2.append(get_raw_stats(season_days_so_far))
            df_lst2 = [df for sublist in df_lst2 for df in sublist]
            self.raw_stats = _pd.concat(df_lst2, ignore_index=True)
        else: 
            dates = preprocess.get_mlb_dates()
            season_days_so_far = dates.get_season_days_so_far()
            self.raw_stats = _pd.concat(get_raw_stats(season_days_so_far), ignore_index=True)

    def get_stats(self):
        return self.raw_stats 






        