from preprocess import dates, service
import pandas as _pd
import pybaseball as _pybaseball
from IPython.display import clear_output

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
def get_raw_stats(season_days_so_far, len_days, ct):
        df_lst = []
        for i in range(len(season_days_so_far)):
            ct += 1
            #print(ct, len_days)
            d = season_days_so_far[i]
            try:
                tmp_df = _pybaseball.batting_stats_range(str(d), )
                tmp_df['DATE'] = d
                pct_complete = int(round(ct/len_days * 100, 0))
                print('FIRST-TIME-USE INITIALIZATION')
                print('Compiling... ', d)
                print("{}%".format(pct_complete))
                clear_output(wait=True)
                df_lst.append(tmp_df)
            except IndexError:
                continue
        return df_lst, ct

def count_total_days_for_pct(seasons):
    lst = []
    for season in seasons:
        
        date_obj = get_mlb_dates(season)
        lst.append(date_obj.get_season_days_so_far())
    flat_lst = [item for sublist in lst for item in sublist]
    return len(flat_lst)

class RawBatterStats:
    def __init__(self, seasons=None):
        self.seasons = seasons
        self.raw_stats = None#_pd.DataFrame()
        self.len_days = count_total_days_for_pct(self.seasons)


    def set_raw_stats(self):
        if self.seasons:
            df_lst2 = []
            ct = 0
            for season in self.seasons:
                date_obj = get_mlb_dates(season)
                season_days_so_far = date_obj.get_season_days_so_far()
                lst, ct = get_raw_stats(season_days_so_far, self.len_days, ct)
                df_lst2.append(lst)
            df_lst2 = [df for sublist in df_lst2 for df in sublist]
            self.raw_stats = _pd.concat(df_lst2, ignore_index=True)
        else: 
            ct = 0
            date_obj = get_mlb_dates()
            season_days_so_far = date_obj.get_season_days_so_far()
            lst, ct = get_raw_stats(season_days_so_far, len(season_days_so_far), ct)
            self.raw_stats, ct = _pd.concat(lst, ignore_index=True)



    def get_stats(self):
        return self.raw_stats 






        