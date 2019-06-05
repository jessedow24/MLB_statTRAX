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
                print('FIRST-TIME-USE INITIALIZE')
                print('processing... ', d)
                print("{}%".format(pct_complete))
                clear_output(wait=True)
                df_lst.append(tmp_df)
            except IndexError:
                continue
        return _pd.concat(df_lst, ignore_index=True), ct

def count_total_days_for_pct(seasons):
    lst = []
    for season in seasons:
        
        date_obj = get_mlb_dates(season)
        lst.append(date_obj.get_season_days_so_far())
    flat_lst = [item for sublist in lst for item in sublist]
    return len(flat_lst)