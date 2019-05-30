'''
Define and access a list of dates on which MLB games were played
'''

from preprocess import dates

def get_mlb_dates(year=None):
        obj = dates.GetSchedule(year)
        obj.set_mlb_dates()
        obj.set_endpoints()
        obj.set_all_star_break_days()
        obj.set_season_days_so_far()
        return obj




