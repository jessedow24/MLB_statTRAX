from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot, grid
from bokeh.models import NumeralTickFormatter, BasicTickFormatter, ColumnDataSource
import bokeh.io
bokeh.io.reset_output()
bokeh.io.output_notebook()

def show_ratio_graph(df, stat, name, year):
    stat_ref = {'AVG':{'day7':'ROLLING_BAVG', 'seas':'CUMSUM_BAVG', 'ticks':None}
                , 'SLG':{'day7': 'ROLLING_SLG', 'seas':'CUMSUM_SLG', 'ticks':None}
                , 'OBP':{'day7': 'ROLLING_OBP', 'seas':'CUMSUM_OBP', 'ticks':None}
                , 'OPS':{'day7': 'ROLLING_OPS', 'seas':'CUMSUM_OPS', 'ticks':None}}
    # define graph vectors
    df = df[(df.NAME == name) & (df.YEAR == year)]
    print(df.shape)
    col_day7 = stat_ref[stat]['day7']
    col_seas = stat_ref[stat]['seas']
    day7     = df[col_day7]
    seas     = df[col_seas]
    y_ticks  = stat_ref[stat]['ticks']
    x = df.DATE
    # create a plot
    p = figure(title=name+' '+str(year)
               , x_axis_label='DATE'
               , y_axis_label=stat
               , x_axis_type='datetime'
               , y_axis_type='linear'
               , y_minor_ticks = 5
               , plot_width = 900
               , plot_height = 600
              )
    # format the y axis
    p.yaxis.formatter=NumeralTickFormatter(format='0.000')
    # add a line renderer with legend and line thickness
    p.line(x, day7, legend=stat+": 7-day", line_width=2, color="teal", alpha=.4)
    p.line(x, seas, legend=stat+": season", line_width=3, color="coral")
    show(p)

def show_stat_graph(df, stat, name, year):
    stat_ref = {'HR':{'day7':'HR_7DAYROLL', 'seas':'HR_CUMSUM', 'ticks':None}
            , 'SB':{'day7': 'SB_7DAYROLL', 'seas':'SB_CUMSUM', 'ticks':None}}
    # define graph vectors
    df = df[(df.NAME == name) & (df.YEAR == year)]
    print(df.shape)
    col_day7 = stat_ref[stat]['day7']
    col_seas = stat_ref[stat]['seas']
    seas     = df[col_seas]
    day7     = df[col_day7]
    y_ticks  = stat_ref[stat]['ticks']
    print(y_ticks)
    x = df.DATE
    
    p = figure(title=name+' '+str(year)
           , x_axis_label='DATE'
           , y_axis_label=stat
           , x_axis_type='datetime'
           , y_axis_type='linear'
           , y_minor_ticks = None
           , y_range=(0, 8)
           , plot_width = 900
           , plot_height = 600
          )
    
    p.line(x, day7, legend=stat+": 7-day total.", line_width=3, color="coral")
    #p.line(x, seas, legend=stat+": season", line_width=2, color="teal", alpha=.4)
    
    show(p)
    