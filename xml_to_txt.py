## Import Libraries

import os
import numpy as np
try:
    import xml.etree.cElementTree as ET 
except ImportError: 
    import xml.etree.ElementTree as ET 
import sys
import math


## Get element function

def rotate(angle, x, y):
    """
## Import Param from RoLabelImg
    :param angle:
    :param x:       x
    :param y:       y
    :return:
    """
    rotatex = math.cos(angle) * x - math.sin(angle) * y
    rotatey = math.cos(angle) * y + math.sin(angle) * x
    return rotatex, rotatey

## Def xy rotate

def xy_rorate(theta, x, y, centerx, centery):
    """
    :param theta:
    :param x:
    :param y:
    :param centerx:
    :param centery:
    :return:
    """
    r_x, r_y = rotate(theta, x - centerx, y - centery)
    return centerx+r_x, centery+r_y

## Def rec rotate 

def rec_rotate(x, y, width, height, theta):
    """
## Def Rotate Param of Oriented BBox
    :param x:
    :param y:
    :param width:
    :param height:
    :param theta:
    :return:
    """
    centerx = x + width / 2
    centery = y + height / 2
 
    x1, y1 = xy_rorate(theta, x, y, centerx, centery)
    x2, y2 = xy_rorate(theta, x+width, y, centerx, centery)
    x3, y3 = xy_rorate(theta, x, y+height, centerx, centery)
    x4, y4 = xy_rorate(theta, x+width, y+height, centerx, centery)
 
    return x1, y1, x2, y2, x4, y4,x3, y3

## Def test


def test(x,y,cx,cy,theta):
    x1_test = cx+(x-cx)*math.cos(theta)-(y-cy)*math.sin(theta)
    y1_test = cy+(y-cy)*math.cos(theta)+(x-cx)*math.sin(theta)
 ##   print('x1_testx1_testx1_testx1_testx1_test',x1_test)
 ##  print('y1_testy1_testy1_testy1_testy1_test',y1_test)

###########################################################################################################

## Import Your Path

PATH = '/home/af/Documents/Scripts/Tag-Tester/annotations/'

## Using for single file
## annotation_file = open("dahrankoli.xml")
None_List=[]
###########################################################################################################
for xml_folder in os.listdir(PATH):

    ### Take care inja esme file ra bar asase esme khode xml sakhtim va az esme toye xml estefade nakardim!!!! dar soorate niaz avaz konid.
    xml_folder2 = xml_folder.replace(".xml", "")
    tree = ET.parse(PATH+xml_folder)
    root = tree.getroot()
    filename = root.find('filename').text
  #  file_object = open(os.path.join("txt-out/"+filename+ ".txt"), 'w')
    file_object = open("/home/af/Documents/Scripts/txt-out/"+xml_folder2+ ".txt", "w")
    # file_object_log = open(filename + ".log", 'w')
    flag = False
    print(filename)
    for size in root.findall('size'):
        width = size.find('width').text
        height = size.find('height').text

    for object in root.findall('object'):
        name = object.find('name').text
        robndbox = object.find('robndbox')
        if robndbox==None:
            None_List.append(filename)


        else:

            cx = float(robndbox.find('cx').text)
            cy = float(robndbox.find('cy').text)
            w = float(robndbox.find('w').text)
            h = float(robndbox.find('h').text)
            angle = float(robndbox.find('angle').text)
            x = cx - w/2
            y = cy - h/2
            if angle<1.57:
                theta = round(angle, 6)
            else:
                theta = round(angle - np.pi, 6)
            x1, y1, x2, y2, x4, y4,x3, y3 = rec_rotate(x, y, w, h, theta)

            ## With integer output
        
        #    x1,y1,x2,y2,x4,y4,x3,y3 = int(x1),int(y1),int(x2),int(y2),int(x4),int(y4),int(x3),int(y3)

            ## With float output
            x1,y1,x2,y2,x4,y4,x3,y3 = round(x1,2),round(y1,2),round(x2,2),round(y2,2),round(x4,2),round(y4,2),round(x3,2),round(y3,2)
           ## print(filename, x1, y1, x2, y2, x4, y4,x3, y3)
            test(x,y,cx,cy,theta)


            ## With ' , ' delimited
        ##    file_object.write(str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+str(x4)+','+str(y4)+','+str(x3)+','+str(y3)+','+name+ str(0))

            ## With Yolo Space delimited
            file_object.write(str(x1)+' '+str(y1)+' '+str(x2)+' '+str(y2)+' '+str(x4)+' '+str(y4)+' '+str(x3)+' '+str(y3)+' '+name+ ' '+ str(0))
            file_object.write('\n')
    file_object.close()
