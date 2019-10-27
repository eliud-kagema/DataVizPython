from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool

def index(request):
    x = [1, 2, 3, 4, 5]
    y = [6, 10, 2, -4, 10]
    title = 'My Leaning Graph'

    plot = figure(title= title , 
        x_axis_label= 'High and Lows', 
        y_axis_label= 'Learning Topics', 
    
        plot_width =700,
        plot_height =700, tools="",
              toolbar_location=None,)
    
    #Formatting Graph
    cr = plot.circle(x, y, size=10, color= "blue", fill_color="grey", hover_fill_color="firebrick",
                fill_alpha=0.05, hover_alpha=0.3,
                line_color=None, hover_line_color="white")
    
    plot.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))            
    plot.title.text_font_size = '20pt'
    plot.line(x, y, legend= 'Leaning Line', line_width = 4, line_color = "brown", line_dash = 'dashed')
    plot.background_fill_color = "lightgrey"
    plot.border_fill_color = "whitesmoke"
    plot.min_border_left = 40
    plot.min_border_right = 40
    plot.outline_line_width = 7
    plot.outline_line_alpha = 0.2
    plot.outline_line_color = "purple"

    #Store components 
    script, div = components(plot)
   
    return render(request, 'index.html' , {'script': script, 'div':div})


def starter(request):
    plot = figure()
    plot.circle([1,2,3,4,5], [0,0,0,0,0], size=20, color="blue")

    script, div = components(plot)
    template_name = 'index.html'
    context = {
        'script': script,
        'div': div
    }

    return render(request, template_name, context)

