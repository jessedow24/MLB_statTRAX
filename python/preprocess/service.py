from preprocess import dates, service
import pandas as _pd
import pybaseball as _pybaseball

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
def get_raw_batter_stats(year=None):
        obj = service.RawBatterStats(year)
        obj.set_raw_stats()
        return obj.get_stats()
def get_raw_stats(season_days_so_far, len_days):
        df_lst = []
        for i in range(len(season_days_so_far)):
            d = season_days_so_far[i]
            try:
                pct_complete = int(round(i/len_days * 100, 0))
                tmp_df = _pybaseball.batting_stats_range(str(d), )
                tmp_df['DATE'] = d
                print(' Collecting date: ', d, '%d%%\r'%pct_complete,  end="")
                df_lst.append(tmp_df)
            except:
                continue
        return _pd.concat(df_lst, ignore_index=True)
def count_total_days_for_pct(seasons):
    lst = []
    for season in seasons:
        dates = get_mlb_dates(season)
        lst.append(dates.get_season_days_so_far())
    flat_lst = [item for sublist in lst for item in sublist]
    return len(flat_lst)

class RawBatterStats:
    def __init__(self, seasons=None):
        self.seasons = seasons
        self.raw_stats = _pd.DataFrame()
        self.len_days = count_total_days_for_pct(self.seasons)
    def set_raw_stats(self):
        if self.seasons:
            df_lst2 = []
            for season in self.seasons:
                dates = get_mlb_dates(season)
                season_days_so_far = dates.get_season_days_so_far()
                df_lst2.append(get_raw_stats(season_days_so_far, self.len_days))
            df_lst2 = [df for sublist in df_lst2 for df in sublist]
            self.raw_stats = _pd.concat(df_lst2, ignore_index=True)
        else: 
            dates = get_mlb_dates()
            season_days_so_far = dates.get_season_days_so_far()
            self.raw_stats = _pd.concat(get_raw_stats(season_days_so_far, len(season_days_so_far)), ignore_index=True)
    def get_stats(self):
        return self.raw_stats 






        