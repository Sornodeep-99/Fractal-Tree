import turtle as tur


trr = tur.Turtle() #Turtle object
wn = tur.Screen() #Screen Object
wn.bgcolor("#c3e7b9") #Screen Bg color
wn.title("Tree Pattern")
trr.left(90) #moving the turtle 90 degrees towards left
trr.speed("fastest")#setting the speed of the turtle

def  draw(l,color,div1,div2,pen): #recursive function taking length l(forward move)
#color,div1,div2(configures the fact tree) and pen (pensize) as argument'''
    if(l<10):
        return
    else:
        trr.pensize(pen) #Setting Pensize
        trr.pencolor(color) #Setting Pencolor as yellow
        trr.forward(l) #moving turtle forward by 'l'
        trr.left(30) #moving the turtle 30 degrees towards left
        draw(div1*l/div2,color,div1,div2,pen) #drawing a fractal on the left of the turtle object 'trr' with 3/4th of its length
        trr.right(60) #moving the turtle 60 degrees towards right
        draw(div1*l/div2,color,div1,div2,pen) #drawing a fractal on the right of the turtle object 'trr' with 3/4th of its length
        trr.left(30) #moving the turtle 30 degrees towards left
        trr.pensize(pen)
        trr.backward(l) #returning the turtle back to its original psition


#inner fractal trees(white)
draw(25,"#FFF8DC",3,4,4)
trr.right(90)
draw(25,"#FFF8DC",3,4,4)
trr.right(90)
draw(25,"#FFF8DC",3,4,4)
trr.right(90)
draw(25,"#FFF8DC",3,4,4)

#middle fractal trees(red)
draw(40,"#AA1428",4,5,3)
trr.right(90)
draw(40,"#AA1428",4,5,3)
trr.right(90)
draw(40,"#AA1428",4,5,3)
trr.right(90)
draw(40,"#AA1428",4,5,3)


#outer fractal tree(blue)
draw(80,"#000042",6,8,2)
trr.right(90)
draw(80,"#000042",6,8,2)
trr.right(90)
draw(80,"#000042",6,8,2)
trr.right(90)
draw(80,"#000042",6,8,2)
trr.right(90)

trr.hideturtle()#hides the turtle pointer
wn.exitonclick()#exits the screen upon click



