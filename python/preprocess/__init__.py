'''
Define and access a list of dates on which MLB games were played.
Use these dates to query raw stats for each batter for each game.
'''

from preprocess import service, model
'''
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

def get_batter_stats(year=None):
        read_obj = model.ReadData()
        read_obj.set_raw_stats_df()
        read_obj.update_raw_stats_df()
        save_obj = model.StoreData()
        save_obj.save(read_obj.get_raw_stats_df())
'''


read_obj = model.ReadData()
read_obj.set_raw_stats_df()
read_obj.update_raw_stats_df()
save_obj = model.StoreData()
save_obj.save(read_obj.get_raw_stats_df())

   




