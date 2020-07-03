from capture import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

output_file('Graph.html')

df['Start_string']=df['Start'].dt.strftime('%Y-%m-%D %H:%M:%S')
df['End_string']=df['Start'].dt.strftime('%Y-%m-%d %H:%M:%S')
cds=ColumnDataSource(df)
p=figure(x_axis_type='datetime', plot_height= 250, plot_width=800, title='Motion Graph')
p.yaxis.minor_tick_line_color=None
p.yaxis.ticker=[0,1]

hover=HoverTool(tooltips=[('Start','@Start_string'),('End','@End_string')])
p.add_tools(hover)

p.quad(top=1, bottom=0, right='End', left='Start', color='Green', source=cds)
show(p)
