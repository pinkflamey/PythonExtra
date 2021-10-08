import turtle

turtle.speed(1000)
colors = ["#C81FDE", "#DE1FDC", "#DE1FCD", "#DE1FBE", "#DE1FAE", "#DE1FBE", "#DE1FCD", "#DE1FDC"]
turtle.width(2)

for x in range(50):
    turtle.color("black")
    turtle.forward(x / 10)
    turtle.left(x - 100)
    turtle.right(x)
    turtle.forward(x)
    turtle.left(x / 200)
    turtle.pencolor(colors[x % 6])
    turtle.forward(x)

    

turtle.done()
