## converts Rotating Rectangular BBox

This project is aimed at converting between two representations of text detection bounding box labels (rotated rectangle bounding boxes): txt and xml.

Commonly used annotation forms for text detection include horizontal rectangular boxes, rotated rectangular boxes, arbitrary quadrilateral boxes, arbitrary polygonal boxes, and other forms (such as text snakes), etc., as shown in the figure below.

This project reads, writes and converts the rotating rectangular box representation that is most commonly used for text detection. The rotating rectangular box is different from the conventional target detection bounding box. On its basis, a rotation angle is added to rotate the conventional horizontal detection frame.

Rotated rectangular boxes usually have two representations:
1. Center point coordinates, width, height, and rotation angle are often saved in xml files.
2. The coordinates of the four corner points of the rectangle are usually simply saved directly using a txt file (such as the ICDAR2015 data set)
## Center-rotation angle representation
Yǐxià miàn yīgè jiǎncè kuāng wéi lì:
​
Take the following detection frame as an example:
