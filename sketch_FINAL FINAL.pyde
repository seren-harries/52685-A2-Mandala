import math
from processing import *

# previous mouse position variables based on x and y coordinates
px = 0.0
py = 0.0

# Number of lines to draw in a radial pattern
count = 10

# The angle offset between each line
offset = 1

# Set up the canvas 
def setup():
    # Set canvas size and background colour
    size(800, 800)
    background(0)
    
    # Set initial stroke colour and weight for the lines 
    stroke(10)
    # Set line thickness 
    strokeWeight(0.5)  
    
    # Calculate angle between each line
    global offset
    offset = (2 * math.pi) / count
    
    # Draw initial radial pattern at the centre of the canvas
    for i in range(count):
        # Draw a line from the centre of the canvas to a point on the circumference
        line(width / 2, height / 2, 
             width / 2 + math.cos(i * offset) * width, 
             height / 2 + math.sin(i * offset) * height)
    
    # Set color mode to HSB for dynamic colour control
    colorMode(HSB)
    # Set line thickness
    strokeWeight(0.5)  
    
#  enable user to draw pattern 
def draw():
    pass

# When the mouse is pressed, store  position for later use
# function found on processing website tutorial 
def mousePressed():
    global px, py
    px = mouseX  # Store the current X position of the mouse
    py = mouseY  # Store the current Y position of the mouse

# When the mouse is dragged, calculate angles and distances to draw lines with shapes at the ends
# function found on processing wesbite tutorial
def mouseDragged():
    global px, py
    
    # Calculate the angle between the mouse and the centre of the canvas
    ang = math.atan2(mouseY - height / 2, mouseX - width / 2)
    
    # Calculate the distance between the mouse and the centre of the canvas
    dist = math.sqrt((mouseY - height / 2) ** 2 + (mouseX - width / 2) ** 2)

    # Use the distance to map the stroke colour for a gradient effect
    stroke(map(dist, 0, math.sqrt((width / 2) ** 2 * 2), 0, 255), 255, 255)

    # Calculate the angle and distance for the previous mouse position
    pang = math.atan2(py - height / 2, px - width / 2)
    pdist = math.sqrt((py - height / 2) ** 2 + (px - width / 2) ** 2)

# lines 56 - 65 modified sequences, used YouTube tutorial (Bro Codes, Math Methods)

    # Recalculate the angle offset for each line
    offset = (2 * math.pi) / count

    # Draw multiple lines from the center of the canvas to the mouse position
    # Used equations from YouTube Tutorial by BarneyCodes 
    for i in range(count):
        # Calculate the x and y coordinates for the end of the current line
        y1 = math.sin(ang + i * offset) * dist + height / 2
        y2 = math.sin(pang + i * offset) * pdist + height / 2
        x1 = math.cos(ang + i * offset) * dist + width / 2
        x2 = math.cos(pang + i * offset) * pdist + width / 2
       

        # Draw the line 
        line(x1, y1, x2, y2)

        # Draw a circle at the end of each line with a fixed diameter
        ellipse(x2, y2, 10, 10)  
    
    # Update the previous mouse position to the current mouse position for the next drag event
    px = mouseX
    py = mouseY
