## converts Rotating Rectangular BBox.

This project is aimed at converting between two representations of text detection bounding box labels (rotated rectangle bounding boxes): txt and xml.

Commonly used annotation forms for text detection include horizontal rectangular boxes, rotated rectangular boxes, arbitrary quadrilateral boxes, arbitrary polygonal boxes, and other forms (such as text snakes), etc., as shown in the figure below.

This project reads, writes and converts the rotating rectangular box representation that is most commonly used for text detection. The rotating rectangular box is different from the conventional target detection bounding box. On its basis, a rotation angle is added to rotate the conventional horizontal detection frame.

Rotated rectangular boxes usually have two representations:
1. Center point coordinates, width, height, and rotation angle are often saved in xml files.
2. The coordinates of the four corner points of the rectangle are usually simply saved directly using a txt file (such as the ICDAR2015 Dataset)
## Center-rotation angle representation

​
Take the following detection frame as an example:

```bash
<object>
    <type>robndbox</type>
    <name>wenben</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <robndbox>
      <cx>860.5666</cx>
      <cy>734.5734</cy>
      <w>644.8657</w>
      <h>52.3775</h>
      <angle>3.031593</angle>
    </robndbox>
  </object>
```

## Rectangular corner point coordinate representation.
Take the following detection frame as an example:

```bash
x1,y1,x2,y2,x3,y3,x4,y4,labelname
```

Each line in the txt file is as shown above. x1, y1, x2, y2, x3, y3, x4, y4 are the horizontal and vertical coordinates of the four corner points respectively, and labelname is the category of the detection frame.
## Conversion between two representations
The specific calculation formula is as follows:

```bash
x1 = cx-w/2*cos(theta)+h/2*sin(theta)
y1 = cy-h/2*cos(theta)-w/2*sin(theta)
x2 = cx-w/2*cos(theta)+h/2*sin(theta)
y2 = cy-h/2*cos(theta)+w/2*sin(theta)
x3 = cx+w/2*cos(theta)-h/2*sin(theta)
y3 = cy+h/2*cos(theta)-w/2*sin(theta)
x4 = cx+w/2*cos(theta)+h/2*sin(theta)
y4 = cy+h/2*cos(theta)+w/2*sin(theta)
```











