# R in Action

## Graphs

### Working with Graphs

```R
pdf("mygraph.pdf")# set a destination
attach(mtcars)
plot(wt, mpg)
abline(lm(mpg~wt))
title("Regression of MPG on Weight")
detach(mtcars)
dev.off()# close 

# dev
dev.new()
dev.next()
dev.prev()
dev.set()
dev.off()
```

### Plot a graph

```R
dose  <- c(20, 30, 40, 45, 60)
drugA <- c(16, 20, 27, 40, 60)
drugB <- c(15, 18, 25, 31, 40)
plot(dose, drugA, type="b")# both points and lines

# Custom：
# One way
opar <- par(no.readonly=TRUE) # get default options
par(lty=2, pch=17)# change options  
plot(dose, drugA, type="b")   
par(opar) # recover options

# other way
plot(dose, drugA, type="b", lty=2, pch=17)


```

### Symbols  and lines

```R
pch# point style 0-25
cex# point size
lty# line style  1-6
lwd# line width
col# border color
bg# fill color
```

### Colors

```R
col # default color
col.axis # axis text
col.lab # axis label
col.main # titles
col.sub # subtitles
fg # foreground
bg # background
colors()# return all color
# define color
col=1
col="white"
col="#FFFFFF"
col=rgb(1,1,1)
col=hsv(0,0,1)
#generate color
rainbow()
heat.colors()
terrain.colors()
topo.colors()
cm.colors()
```

* RColorBrewer: package for creating attractive color palettes

```R
library(RColorBrewer)
n <- 7
mycolors <- brewer.pal(n, "Set1")
barplot(rep(1,n), col=mycolors)

brewer.pal.info
display.brewer.all()

n <- 10
mycolors <- rainbow(n)
pie(rep(1, n), labels=mycolors, col=mycolors)
mygrays <- gray(0:n/n)
pie(rep(1, n), labels=mygrays, col=mygrays)
```

### Text characteristics

```R
cex # scaled size
cex.axis # scaled axis text
cex.lab # scaled axis labels
cex.main # titles
cex.sub # subtitles
# 
font # style integer
ps # ps*cex =size inch
family # drawing text font family
# "serif" "sans" "mono"

windowsFonts(
  A=windowsFont("Arial Black"),
  B=windowsFont("Bookman Old Style"),
  C=windowsFont("Comic Sans MS")
)
par(family = "A")

# PDF
names(pdfFonts())#get all fonts
pdf(file = "myplot.pdf", family="fontname")

#PS
names(postscriptFonts())
postscript(file="myplot.ps", family="fontname")
```

### Graph and margin diemensions

```R
pin # plot dimensions in inches
mai # numerical vector c(bottom, left, top, right) in inches
mar # in lines 
par(pin=c(4,3), mai=c(1,.5, 1, .2))

opar <- par(no.readonly=TRUE)                  
par(pin=c(2, 3))                              
par(lwd=2, cex=1.5)                           
par(cex.axis=.75, font.axis=3)                
plot(dose, drugA, type="b", pch=19, lty=2, col="red")            
plot(dose, drugB, type="b", pch=23, lty=6, col="blue", bg="green")    
par(opar)
```

### Text, customized axes, legends, titles

```R
plot(dose, drugA, type="b",  
     col="red", lty=2, pch=2, lwd=2,
     main="Clinical Trials for Drug A", 
     sub="This is hypothetical data", 
     xlab="Dosage", ylab="Drug Response",
     xlim=c(0, 60), ylim=c(0, 70))
title(main="main title", sub="subtitle", 
      xlab="x-axis label", ylab="y-axis label")
title(main="My Title", col.main="red", 
      sub="My Subtitle", col.sub="blue", 
      xlab="My X label", ylab="My Y label",
      col.lab="green", cex.lab=0.75)

# axes
axis(side, at=, labels=, pos=, lty=, col=, las=, tck=)
axes = FALSE # suppresses all axes
frame.plot=TRUE # 
xaxt = "n" # suppress x axis 
yaxt = "n"
mtext() # add text to the margin

# Minor tick marks
library(Hmisc)
minor.tick(nx=n, ny=n, tick.ratio=n)
minor.tick(nx=2, ny=3, tick.ratio=0.5) 

# Reference Lines
abline(h=yvalues, v=xvalues)
abline(v=seq(1, 10, 2), lty=2, col="blue")

# legend
legend(location, title, legend, ...)

# text annotations
text(location, "text to place", pos, ...)
mtext("text to place", side, line=n, ...)
pos # 1 bottom 2 left 3 up 4 right
offset
side # side to put text

# math annotations
plotmath()
```

```R
x <- c(1:10)                          
y <- x                                   
z <- 10/x                             
opar <- par(no.readonly=TRUE)
par(mar=c(5, 4, 4, 8) + 0.1)        
plot(x, y, type="b",
     pch=21, col="red",    
     yaxt="n", lty=3, ann=FALSE)    
lines(x, z, type="b", pch=22, col="blue", lty=2) 
axis(2, at=x, labels=x, col.axis="red", las=2)
axis(4, at=z, labels=round(z, digits=2),
     col.axis="blue", las=2, cex.axis=0.7, 	tck=-.01)
mtext("y=1/x", side=4, line=3, cex.lab=1, las=2, col="blue") 
title("An Example of Creative Axes",
      xlab="X values",
      ylab="Y=X")

par(opar)
```

### Combining graphs

```R
par(mfrow = c(nrows,ncols))# fill by rows
hist(ann=FALSE) # suppress all titles and labels

layout(mat)# matrix specifying the location

attach(mtcars)
layout(matrix(c(1,1,2,3), 2, 2, byrow = TRUE),# vector nrow ncol
       widths=c(3, 1), heights=c(1, 2))
hist(wt)
hist(mpg)
hist(disp)
detach(mtcars)
```

```R
#Fine control
fig =c(x1,x2,y1,y2)

# example
opar <- par(no.readonly=TRUE)
par(fig=c(0, 0.8, 0, 0.8))   # 0-0.8 0-0.8
plot(mtcars$wt, mtcars$mpg,                      
     xlab="Miles Per Gallon",                               
     ylab="Car Weight")

par(fig=c(0, 0.8, 0.55, 1), new=TRUE)        # 0-0.8 0.55-1                           
boxplot(mtcars$wt, horizontal=TRUE, axes=FALSE) 

par(fig=c(0.65, 1, 0, 0.8), new=TRUE)          
boxplot(mtcars$mpg, axes=FALSE)   

mtext("Enhanced Scatterplot", side=3, outer=TRUE, line=-3)
par(opar)
```

