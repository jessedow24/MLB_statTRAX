import preprocess 
import pandas as _pd
import pybaseball as _pybaseball


def get_one_season_raw_stats(season_days_so_far):
        df_lst = []
        for d in season_days_so_far:
            try:
                tmp_df = _pybaseball.batting_stats_range(str(d), )
                print(' processing ', d)
                tmp_df['DATE'] = d
                df_lst.append(tmp_df)
            except:
                continue
        return df_lst


class RawBatterStats:
    def __init__(self, seasons=None):
        self.seasons = seasons
        self.raw_stats = _pd.DataFrame()
    def set_raw_stats(self):
        if self.seasons:
            for season in self.seasons:
                dates = preprocess.get_mlb_dates(season)
                season_days_so_far = dates.get_season_days_so_far()
                self.raw_stats = _pd.concat(get_one_season_raw_stats(season_days_so_far))       
        else: 
            dates = preprocess.get_mlb_dates()
            season_days_so_far = dates.get_season_days_so_far()
            self.raw_stats = _pd.concat(get_one_season_raw_stats(season_days_so_far))
    def get_stats(self):
        return self.raw_stats 