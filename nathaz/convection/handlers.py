## This file is where you write your event handlers in Python.
## Define functions named like element_id__event(dom) e.g.
#   btn_mybutton__click(dom):
#       dom['txt_textbox']['value'] = "Button clicked."
#   return dom
#
## You can delete this comment once you've read it.

import re
import io 
import ashiba
#import matplotlib.pylab as plt
import ashiba.plot
from ashiba.plot import plt 
#Probably going to have to have a 'this' as well as dom.
def checkvalue(value):
    # Everything is a string, gotta validate.
    value_str = value.strip()
    rex = re.match('([+-]?\d+\.?\d*)', value_str)
    if not rex:
        print "ERROR: INVALID Input"
        raise ValueError("Invalid Input")
    else:
        value = float(rex.group(1))
    return value 
def calc(dom):
    g= 9.8 #m/s**2
    beta = checkvalue(dom['t_exp']['value'])
    v = checkvalue(dom['visc']['value'])
    alpha = checkvalue(dom['t_diff']['value'])
    delT = checkvalue(dom['delT']['value'])
    x = checkvalue(dom['delX']['value'])
    ra = (g*beta*delT*(x**3))/(v*alpha)
    return ra 
def btn_calculate__click(dom):
    ra = calc(dom)
    dom['Ra']['value'] = ra
    return dom
def plotNumber(ra,label):
    # set up the figure
    
    # draw lines
    xmin = 0
    xmax = 10000
    y = 1
    height = 5
    
    plt.hlines(y, xmin, xmax)
    plt.vlines(xmin, y - height / 2., y + height / 2.)
    plt.vlines(xmax, y - height / 2., y + height / 2.)
    
    # draw a point on the line
    px = ra
    plt.plot(px,y, 'ro', ms = 10, mfc = 'r')
    
    # add an arrow
    plt.annotate(label, (px,y), xytext = (px - 1, y + 2), 
                  arrowprops=dict(facecolor='black', shrink=0.1), 
                  horizontalalignment='right')
    
    # add numbers
    #plt.text(xmin - 0.1, y, '80', horizontalalignment='right')
    #plt.text(xmax + 0.1, y, '10000', horizontalalignment='left')
    

    plt.yticks([])
    return 
import io



    
def btn_plot__click(dom):
    ra = calc(dom)
    plotNumber(ra,dom['label']['value'])
    #plt.plot([1,2,3],[1,2,3])
    #plt.savefig('image.jpg')
    dom['img_plot'].set_image(plt.get_svg(), 'svg')
    return dom 