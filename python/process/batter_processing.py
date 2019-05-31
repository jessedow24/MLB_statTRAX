import pandas as _pd


class RawBatter():
    def __init__(self, raw_batter_df):
        self.raw_batter = raw_batter_df
        self.DATE  = self.raw_batter.DATE
        self.NAME  = self.raw_batter.Name
        self.AGE   = self.raw_batter.Age
        self.TEAM  = self.raw_batter.Tm
        self.G     = self.raw_batter.G
        self.PA    = self.raw_batter.PA
        self.AB    = self.raw_batter.AB
        self.R     = self.raw_batter.R
        self.H     = self.raw_batter.H
        self.doubl = self.raw_batter['2B']
        self.tripl = self.raw_batter['3B']
        self.HR    = self.raw_batter.HR
        self.RBI   = self.raw_batter.RBI
        self.BB    = self.raw_batter.BB
        self.IBB   = self.raw_batter.IBB
        self.K     = self.raw_batter.SO
        self.HBP   = self.raw_batter.HBP
        self.SH    = self.raw_batter.SH
        self.SF    = self.raw_batter.SF
        self.GDP   = self.raw_batter.GDP
        self.SB    = self.raw_batter.SB
        self.CS    = self.raw_batter.CS
        self.BA    = self.raw_batter.BA
        self.OBP   = self.raw_batter.OBP
        self.SLG   = self.raw_batter.SLG
        self.OPS   = self.raw_batter.OPS
        self.processed_batter = None
        self.processed_batter_short = None
        
    def process_batter(self):
        self.processed_batter = _pd.DataFrame({
            'DATE' : self.raw_batter.DATE
            , 'NAME' : self.NAME
            , 'AGE' : self.AGE
            , 'TEAM' : self.TEAM
            , 'G' : self.G
            , 'PA' : self.PA
            , 'AB' : self.AB
            , 'R' : self.R
            , 'H' : self.H
            , '2B' : self.doubl
            , '3B' : self.tripl
            , 'HR' : self.HR
            , 'RBI' : self.RBI
            , 'BB' : self.BB
            , 'IBB' : self.IBB
            , 'K' : self.K
            , 'HBP' : self.HBP
            , 'SH' : self.SH
            , 'SF' : self.SF
            , 'GDP' : self.GDP
            , 'SB' : self.SB
            , 'CS' : self.CS
            , 'BA_1GM' : self.BA
            , 'OPB_1GM' : self.OBP
            , 'SLG_1GM' : self.SLG
            , 'OPS_1GM' : self.OPS
        })
    def get_processed_batter(self):
        return self.processed_batter
