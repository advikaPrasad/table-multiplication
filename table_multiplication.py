import turtle

window = turtle.Screen()
window.setup(800, 600)
window.title('Numbers')

t = turtle.Turtle()
t.speed("fastest")
t.pencolor("gold")
t.penup()
t.hideturtle()

myfont = ("Arial", "59", "bold")

n1 = window.numinput("N1", "Enter a number betwwen 1 and 10:",0 ,minval=1, maxval=10)
n2 = window.numinput("N2", "Enter a number betwwen 1 and 10:",0 ,minval=1, maxval=10)

n3 = n1+n2
n4 = n3*n1
n5 = n4/n2

print(n1)
print(n2)
print(n3)
print(n4)
print(n5)