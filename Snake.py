import turtle
import random
import time

# Demora
delay = 0.1

# Contadores para los marcadores
marcador = 0
marcador_alto = 0

s = turtle.Screen()
s.setup(650, 650) #Marca la dimension de la pantalla.
s.bgcolor("gray")
s.title("Snake")


# Caracteristicas de la serpiente.
snake = turtle.Turtle()
snake.speed(1)
snake.shape("square")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"
snake.color("green")

#Comida
comida = turtle.Turtle()
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)
comida.speed(0)

#Lista para el cuerpo
cuerpo = []

# Forma de los contadores:
texto = turtle.Turtle()
texto.speed(0)
texto.color("blue")
texto.penup()
texto.hideturtle()
texto.goto(0, -200)
texto.write("Marcador: 0\tMarcador mas alto: 0", align="center", font=("verdana",24 , "normal"))


#Funciones que definen la direccion 
def arriba():
    snake.direction = "up"

def abajo():
    snake.direction = "down"

def derecha():
    snake.direction = "right"

def izquierda():
    snake.direction = "left"


def movimiento():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

s.listen() #Prepara a la pantalla para escuchar una accion.
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")


#Es es el loop de movimiento
while True:
    s.update()

    if snake.xcor() > 300 or snake.xcor() < -300 or snake.ycor() > 300 or snake.ycor() < -300:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        snake.home()
        snake.direction = "stop"
        cuerpo.clear()

        marcador = 0
        texto.clear()
        texto.write("Marcador:{}\tMarcador mas alto: {}".format(marcador, marcador_alto),align="center", font=("verdana", 24, "normal"))


    if snake.distance(comida)<20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        comida.goto(x,y)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("green")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo) # Agrega al cuerpo un elemento nuevo.

        marcador += 10
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write("Marcador:{}\tMarcador mas alto: {}".format(marcador, marcador_alto),align="center", font=("verdana", 24, "normal"))

    total = len(cuerpo)
    for index in range(total -1, 0, -1):
        x = cuerpo[index - 1].xcor()
        y = cuerpo[index - 1].ycor()
        cuerpo[index].goto(x,y)

    if total > 0:
        x = snake.xcor()
        y = snake.ycor()
        cuerpo[0].goto(x, y)

    movimiento() 
    for i in cuerpo:
        if i.distance(snake) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            snake.home()
            cuerpo.clear()    
            snake.direction = "stop"

    time.sleep(delay)

turtle.done()