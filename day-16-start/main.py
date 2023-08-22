# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import turtle
# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.color('DarkViolet')
# timmy.shape("turtle")
# turtle.forward(100)
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'
print(table.align)
print(table)