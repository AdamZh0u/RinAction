#coding:utf-8
import arcpy,sys
from arcpy import env as env

'''Workspace = sys.argv[1]
old = sys.argv[2]
new = sys.argv[3]
mydistance = sys.argv[4]'''

Workspace = 'F:/ECO/2'
old = '1990study_built.shp'
new = '19901995new.shp'
mydistance = 30

env.workspace = Workspace
env.overwriteOutput = True
arcpy.MakeFeatureLayer_management(new,'new')
arcpy.MakeFeatureLayer_management(old,'old')

with arcpy.da.SearchCursor(new,("FID")) as cursor:
    count = 0
    for row in sorted(cursor):
        count += 1

PEI = []
LEI = []
nns = []
for i in range(count):
    print 'processing:patch of %s'%(str(i))
    buffer_areas = []
    n = 0
    buffer_dist = float(mydistance)
    whereclause='%s=%i' %("FID",i)
    select=arcpy.SelectLayerByAttribute_management("new","NEW_SELECTION",whereclause)
    intersect_area = 0.0
    while intersect_area == 0.0 and n<21:
        mybuffer = arcpy.Buffer_analysis(select,'buffer',buffer_dist,"OUTSIDE_ONLY")
        arcpy.CalculateField_management(mybuffer, 'area', 'float(!SHAPE.area!)',"PYTHON_9.3")
        buffer_cursor = arcpy.da.SearchCursor(mybuffer,("area"))
        buffer_area = 0.0
        for cursor in buffer_cursor:
            buffer_area = buffer_area + cursor[0]
        buffer_areas.append(buffer_area)
        myintersect = arcpy.Intersect_analysis([mybuffer,"old"],'intersect')
        arcpy.CalculateField_management(myintersect, 'area', 'float(!SHAPE.area!)',"PYTHON_9.3")
        cursors = arcpy.da.SearchCursor(myintersect,('area'))
        for cursor in cursors:
            intersect_area = intersect_area + cursor[0]
        buffer_dist = buffer_dist + 30
        n = n+1
        print n
    nns.append(n)
    if n != 1 and n!=21:
        a = intersect_area / (buffer_areas[n-1]-buffer_areas[n-2])
        PEI.append(1.0/((1-a)+n))
        LEI.append(0)
    elif n==21:
        PEI.append(1.0/21)
        LEI.append(0)
    else:
        a = intersect_area / buffer_areas[n-1]
        if a > 1.0:
            PEI.append(1.0)
        else:
            PEI.append(1.0/((1-a)+n))
        LEI.append(a)
    
arcpy.AddField_management(new,"PEI","DOUBLE")
arcpy.AddField_management(new,"LEI","DOUBLE")
arcpy.AddField_management(new,"nn","DOUBLE")
cursor = arcpy.da.UpdateCursor(new,("PEI","nn","LEI"))
m = 0
for row in cursor:
    row[0] = PEI[m]
    row[1] = nns[m]
    row[2] = LEI[m]
    cursor.updateRow(row)
    m = m+1
del cursor        
