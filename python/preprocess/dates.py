import mlbgame 
import pandas as _pd
from datetime import datetime, timedelta

class GetSchedule:
    def __init__(self, season=None):

        self.season             = season
        self.current_season     = datetime.today().year
        self.mlb_dates          = None
        self.first_half_start   = None
        self.first_half_end     = None
        self.second_half_start  = None
        self.second_half_end    = None
        self.allstar_break_days = None
        self.season_days_so_far = None

    def set_mlb_dates(self):
        if self.season:
            self.mlb_dates = mlbgame.important_dates(self.season)
        else:
            self.mlb_dates = mlbgame.important_dates(self.current_season)

    def set_endpoints(self):
        self.first_half_start = self.mlb_dates.first_date_seas[:10]
        self.first_half_end = self.mlb_dates.last_date_1sth[:10]
        self.second_half_start = self.mlb_dates.first_date_2ndh[:10]
        self.second_half_end = self.mlb_dates.last_date_seas[:10]

    def set_all_star_break_days(self):
        start = datetime.strptime(self.first_half_end, '%Y-%m-%d') + timedelta(days=1)
        stop = datetime.strptime(self.second_half_start, '%Y-%m-%d') - timedelta(days=1)
        self.allstar_break_days = list(_pd.date_range(start=start, end=stop).astype(str))
 
    def set_season_days_so_far(self):
        today = datetime.today()
        start = datetime.strptime(self.first_half_start, '%Y-%m-%d')
        season_days = list(_pd.date_range(start=start, end=today).astype(str))
        self.season_days_so_far = [d for d in season_days if d not in self.allstar_break_days]
  
    #@abstractmethod
    def get_season_days_so_far(self):
        return self.season_days_so_far
