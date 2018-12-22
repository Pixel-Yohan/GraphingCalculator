import math
import random
from graphics import *

################################ FUNCTIONS ################################

#<return the function value at a given point x>#
def f0(x):
    return math.cos(x)
def f1(x):
    return math.sin(x**2)
def f2(x):
    return math.exp(x)
def f3(x):
    return (x**2)+1
def f4(x):
        1/x
        return 1/x
def f5(x):
    return (1/math.sqrt(2*math.pi))*math.exp(-(x**2)/2)
#<f evaluatesthe function s at the given point x>#
def f(x,s):
    if(s==0):
        return f0(x)
    if(s==1):
        return f1(x)
    if(s==2):
        return f2(x)
    if(s==3):
        return f3(x)
    if(s==4):
        return f4(x)
    if(s==5):
        return f5(x)
#<finds the minimum of a function on a given interval>#
def findMin(lowerbound,upperbound,functionSelect):
    diff=upperbound-lowerbound
    change=(upperbound-lowerbound)/600
    minimum=f(lowerbound,functionSelect)
    for i in range(0,600):
        if(f(lowerbound+(change*i),functionSelect)<minimum):
            minimum=f(lowerbound+(change*i),functionSelect)
    return minimum
#<finds the maximum of a function on a given interval>#
def findMax(lowerbound,upperbound,functionSelect):
    diff=upperbound-lowerbound
    change=(upperbound-lowerbound)/600
    maximum=f(lowerbound,functionSelect)
    for i in range(0,600):
        if(f(lowerbound+(change*i),functionSelect)>maximum):
            maximum=f(lowerbound+(change*i),functionSelect)
    return maximum

def checkBounds(lowerBound,upperBound):
    if(lowerBound==0 or upperBound==0):
        print("***********************")
        print("***********************")
        print("  INVALID BOUNDS ")
        print("  0 NOT ALLOWED ")
        print("     FOR THIS f(x)    ")
        print("")
        print("(╯ಠ ʖ̯ಠ）╯︵ ┻━┻")
        print("")
        print("   HELP RESTORE    ")
        print("       THE TABLE          ")
        print("     ┬─┬ ノ( ^_^ノ)    ")
        print("")
        print("***********************")
        print("***********************")
        main()
    elif((upperBound<0 and lowerBound>0) or (upperBound>0 and lowerBound<0)):
        print("***********************")
        print("***********************")
        print("  INVALID BOUNDS ")
        print("   NOT ALLOWED ")
        print("     FOR THIS f(x)    ")
        print("")
        print("(╯ಠ ʖ̯ಠ）╯︵ ┻━┻")
        print("")
        print("   HELP RESTORE    ")
        print("       THE TABLE          ")
        print("")
        print("     ┬─┬ ノ( ^_^ノ)    ")
        print("***********************")
        print("***********************")
        main()

############################ RIEMANN Σ ###########################

def leftRiemann(b_lower,b_upper,subintervals,fs):
    changeX=(b_upper-b_lower)/subintervals
    intlist=list()
    s=0
    for i in range(0,subintervals):
        s+=f(b_lower+(changeX*i),fs)*changeX
        intlist.append(b_lower+(changeX*i))
    graphCreate(b_lower,b_upper,"Left",intlist,subintervals,"riemann",fs)
    return s
def rightRiemann(b_lower,b_upper,subintervals,fs):
    changeX=(b_upper-b_lower)/subintervals
    intlist=list()
    s=0
    for i in range(1,subintervals+1):
        s+=f(b_lower+(changeX*i),fs)*changeX
        intlist.append(b_lower+(changeX*i))
    graphCreate(b_lower,b_upper,"Right",intlist,subintervals,"riemann",fs)
    return s
def midRiemann(b_lower,b_upper,subintervals,fs):
    changeX=(b_upper-b_lower)/subintervals
    intlist=list()
    s=0
    for i in range(0,subintervals):
        rightCoord=b_lower+(changeX*(i+1))
        leftCoord=b_lower+(changeX*i)
        val=(rightCoord+leftCoord)/2
        s+=f(val,fs)*changeX
        intlist.append(val)
    graphCreate(b_lower,b_upper,"Mid Point",intlist,subintervals,"riemann",fs)
    return s

#return a list [approximatedArea,listOfPointsInside,listOfPointsOutside]
#Area=(right-left)*(top-bottom)
def integralApproximationB(a,b,ttr,fs):
    pointsInside=list()
    pointsOutside=list()
    maxim=findMax(a,b,fs)
    minim=findMin(a,b,fs)
    lowY=0
    upperY=0
    height=0
    points=0
    if(maxim>0 and minim>0):
        height=findMax(a,b,fs)
        lowY=0
        upperY=maxim
    elif(maxim<0 and minim<0):
        height=0-findMin(a,b,fs)
        lowY=minim
        upperY=0
    else:
        height=findMax(a,b,fs)-findMin(a,b,fs)
        lowY=minim
        upperY=maxim
    area=(b-a)*height
    for i in range(ttr):
        coordinates=list()
        randomX=random.uniform(a,b)
        randomY=random.uniform(lowY,upperY)
        yVal=f(randomX,fs)
        coordinates.append(randomX)
        coordinates.append(randomY)
        if(yVal>0):
            if(randomY<=yVal and randomY>0):
                points+=1
                pointsInside.append(coordinates)
            else:
                pointsOutside.append(coordinates)
        elif(yVal<=0):
            if(randomY>=yVal and randomY<=0):
                points-=1
                pointsInside.append(coordinates)
            else:
                pointsOutside.append(coordinates)

    approximatedArea=area*(points/ttr)
    returnList=list()
    returnList.append(approximatedArea)
    returnList.append(pointsInside)
    returnList.append(pointsOutside)
    return returnList

############################ GRAPHING ###########################

#greaphCreate creates the graphing window and graphs the graph layout
def graphCreate(ib1,ib2,side,intlist,subintervals,decision,fs):
    #create graphing grid
    win= GraphWin("Graphing Window", 1000,800)
    win.setBackground("#000066")
    win.setCoords(-100,-100,900,700)
    if(decision=="riemann"):
        titleText=side+" Riemann Sum"
    elif(decision=="montecarlo"):
        titleText="Montecarlo"        
    graph_title=Text(Point(400,650),titleText)
    graph_title.setSize(20)
    graph_title.setFace("times roman")
    graph_title.setTextColor("#ffe066")
    graph_title.draw(win)
    horizontal_axis=Line(Point(0,300),Point(800,300))
    horizontal_axis.setFill("#ffe066")
    horizontal_axis.draw(win)
    horizontal_key=Text(Point(850,300), "x")
    horizontal_key.setFace("times roman")
    horizontal_key.setSize(20)
    horizontal_key.setFill("#ff00ff")
    horizontal_key.draw(win)
    vertical_axis=Line(Point(0,0),Point(0,600))
    vertical_axis.setFill("#ff00ff")
    vertical_axis.draw(win)
    ylinesize=600
    xlinesize=800
    for i in range(0,11):
        horizontal_line=Line(Point(0,60*i),Point(800,60*i))
        horizontal_line.setFill("#ff00ff")
        horizontal_line.draw(win)
    for i in range(1,11):
        vertical_line=Line(Point(i*80,0),Point(i*80,600))
        vertical_line.setFill("#ff00ff")
        vertical_line.draw(win)
    if(decision=="riemann"):
        graphPlot(win,ib1,ib2,side,intlist,subintervals,decision,fs)
    elif(decision=="montecarlo"):
        graphPlot(win,ib1,ib2,side,intlist,subintervals,decision,fs)
       
#graphPlot plots x-axis and y-axis values. It then proceeds to plot function values
#difference between x intervals (upperbound-lowerbound)
#changex= xdiff/10 to fit in the 10 interval lines
#maxim=function maximum
#minim=function minimum
#changey=ydiff/10 to fit a range of 10 values between the maximum and minimum
#first for-loop plots x-axis values for the interval
#second for-loop plots y-axis values for the interval
#while loop calculates f(x) values for values in between the given intervals of ib1 and ib2
#third for-loop plots the points in the graph
#fourth for-loop draws the riemann sum rectangles
def graphPlot(window,ib1,ib2,side,intlist,subintervals,decision,fs):
    xdiff=ib2-ib1
    changex=xdiff/10
    maxim=0
    minim=0
    if(fs==0 or fs==1):
        maxim=1
        minim=-1
    else:
        maxim=findMax(ib1,ib2,fs)
        minim=findMin(ib1,ib2,fs)

    ydiff=0
    changey=0
    #if the graph exists above the x-axis
    if(maxim>0 and minim>0):
        ydiff=maxim
        changey=ydiff/10
        #graphs the y-values on the y axis
        for i in range(0,11):
            if(i==10):
                y_val=str(maxim)
            y_val=str((changey*i))
            funValT=Text(Point(-30,i*60),y_val[0:5])
            funValT.setTextColor("#ff00ff")
            funValT.draw(window)
    #if the graph exists below the x-axis
    elif(maxim<0 and minim<0):
        ydiff=minim
        changey=abs(ydiff/10)
        #graphs the y-values on the y axis
        for i in range(0,11):
            if(i==10):
                y_val="0"
            y_val=str((changey*i+ydiff))
            funValT=Text(Point(-30,i*60),y_val[0:5])
            funValT.setTextColor("#ff00ff")
            funValT.draw(window)
    #if the graph crosses the x-axis
    else:
        ydiff=maxim-minim
        changey=ydiff/10
        #graphs the y-values on the y axis
        for i in range(0,11):
            y_val=str((changey*i)+minim)
            funValT=Text(Point(-30,i*60),y_val[0:5])
            funValT.setTextColor("#ff00ff")
            funValT.draw(window)
    #graphs the x-values on the x axis
    for i in range(0,11):
        x_val=str((ib1+changex*i))
        funValT=Text(Point(i*80,-50),x_val[0:5])
        funValT.setTextColor("#ff00ff")
        funValT.draw(window)
    fxvals=list()
    x=ib1
    changex=(ib2-ib1)/600
    for i in range(0,600):
        coords=list()
        coords.append(ib1+(changex*i))
        coords.append(f(ib1+(changex*i),fs))
        fxvals.append(coords)
    x_scale=800/(ib2-ib1)
    y_scale=0
    #workable vertical distance
    workableVD=600
    val=(600-maxim*y_scale)
    #if the graph exists above the x-axis
    if(maxim>0 and minim>0):
        #we have to scale it so that it fits the area that we can actually use
        #above the x-axis
        workableVD-=minim
        y_scale= workableVD/abs(maxim)
        #val=minim*y_scale
        val=0
    #if the graph exists below the x-axis
    elif(maxim<0 and minim<0):
        workableVD-=abs(maxim)
        y_scale=workableVD/(-minim)
    #if the graph crosses the x-axis
    else:
        y_scale=(600/(maxim-minim))
        val=(600-maxim*y_scale)
    #graphs the graph by making lines
    for i in range(0,len(fxvals)-1):
        x0=(fxvals[i][0]*x_scale)-fxvals[0][0]*x_scale
        y0=(fxvals[i][1]*y_scale)+val
        x1=(fxvals[i+1][0]*x_scale)-fxvals[0][0]*x_scale
        y1=(fxvals[i+1][1]*y_scale)+val
        connectLine=Line(Point(x0,y0),Point(x1,y1))
        connectLine.setFill("#ffe066")
        connectLine.setOutline("#ffe066")
        connectLine.setWidth(8)
        connectLine.draw(window)
    #proceeds to graph blocks for the Riemann Sum or points for the MonteCarlo Method
    if(decision=="riemann"):
        graphRiemann(window,ib1,ib2,side,fxvals,intlist,subintervals,x_scale,fs,val,y_scale,maxim)
    elif(decision=="montecarlo"):
        graphMonteCarlo(window,ib1,ib2,side,fxvals,intlist,subintervals,x_scale,val,y_scale)

def graphRiemann(window,ib1,ib2,side,fxvals,intlist,subintervals,x_scale,fs,val,y_scale,maxim):
    for i in range(0,subintervals):
        changeX=(ib2-ib1)/subintervals
        start=val
        minimum=findMin(ib1,ib2,fs)
        riemannSum=Rectangle(Point(changeX*i*x_scale,start),Point(changeX*(i+1)*x_scale,f(intlist[i],fs)*y_scale+val))
        riemannSum.setOutline("#cce6ff")
        riemannSum.setWidth(4)
        riemannSum.draw(window)

def graphMonteCarlo(window,ib1,ib2,side,fxvals,intlist,subintervals,x_scale,val,y_scale):
    pointsInside=intlist[1]
    pointsOutside=intlist[2]
    for i in range(len(pointsInside)):
        x=(pointsInside[i][0]*x_scale)-fxvals[0][0]*x_scale
        y=(pointsInside[i][1]*y_scale)+val
        insidePoint=Circle(Point(x,y),4)
        insidePoint.setFill("#99ff99")
        if(pointsInside[i][1]<0):
            insidePoint.setFill("#6699ff")
        insidePoint.draw(window)
    for i in range(len(pointsOutside)):
        x=(pointsOutside[i][0]*x_scale)-fxvals[0][0]*x_scale
        y=(pointsOutside[i][1]*y_scale)+val
        outsidePoint=Circle(Point(x,y),4)
        outsidePoint.setFill("#ffff99")
        outsidePoint.draw(window)

###################### FUNCTION CALLS & USER INTERACTIONS ######################
function0="cos(x)"
function1="sin(x^2)"
function2="e^x"
function3="(x^2)+1"
function4="1/x"
function5="(1/(√2x)) * e^((-x^2)/2)"
def main():
    l_b=0
    u_b=0
    sints=0
    ptp=-1
    fSelect=-1
    decision="0"
    while decision!="1":
        while(fSelect<=-1):
            print("0| "+function0)
            print("1| "+function1)
            print("2| "+function2)
            print("3| "+function3)
            print("4| "+function4)
            print("5| "+function5)
            print("")
            fSelect=int(input("| Please enter the function you want to use: "))
        l_b=float(input("| Please enter lower bound: "))
        u_b=float(input("| Please enter upper bound: "))
        while(l_b>u_b):
            u_b=float((input("| Please enter a value greater than the previous value: ")))
        if(fSelect==4):
            checkBounds(l_b,u_b)
        while True:
            try:
                sints=int(input("| Please enter how many subintervals: "))
                while(sints<0):
                    sints=int(input("| Please enter a positive integer: "))
                break
            except TypeError:
                print("| Please enter an integer value!")
        if(ptp==-1):
            while True:
                try:
                    ptp=int((input("| Please enter the # of points you would like to use to approximate the function's integral:")))
                    break
                except TypeError:
                    print("| Please enter a positive integer value!")          
        print("Midpoint Riemann:",midRiemann(l_b,u_b,sints,fSelect))
        print("Right Riemann:",rightRiemann(l_b,u_b,sints,fSelect))
        print("Left Riemann:",leftRiemann(l_b,u_b,sints,fSelect))
        returnedList=integralApproximationB(l_b,u_b,ptp,fSelect)
        print("Montecarlo Approximation for =",returnedList[0])
        graphCreate(l_b,u_b,"Integral Approximation",returnedList,"","montecarlo",fSelect)
        fSelect=-1
        print("********************************************************")
        print("[◕෴◕] Would you like to run another simulation? [◕෴◕]")
        decision=input("Enter 1 if not, enter any other key to proceed: ")
        if(decision==1):
            print("See you!(づ◔ ³◔)づ")
            break
        print("********************************************************")
        main()
main()
