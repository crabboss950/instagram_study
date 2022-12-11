# 사용법
# https://docs.python.org/ko/3/library/turtle.html
# https://blog.naver.com/python_math/221214856867
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=kkj6369&logNo=221248236812

import turtle

turtle.setup(width=600, height=600)
t=turtle.Turtle()
t.screen.bgcolor('black')
t.pensize(2)
t.color('green')
t.left(90)
t.backward(100)
t.speed(200)
t.shape("turtle")

def tree(i):
    if i < 10:
        return
    else:
        t.forward(i)
        t.color('orange')
        t.circle(2)
        t.color('brown')
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)
tree(100)
turtle.done()