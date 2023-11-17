# from turtle import Turtle, Screen
#
# timmy = Turtle()
# screen = Screen()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# screen.exitonclick()
from prettytable import from_csv
from prettytable import PrettyTable, from_csv

table = PrettyTable()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)
print(table)
table1 = PrettyTable()
table1.add_column("City name",
                  ["Adelaide", "Brisbane", "Darwin", "Hobart", "Sydney", "Melbourne", "Perth"])
table1.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
                                1554769])
table1.add_column("Annual Rainfall", [600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
                                      869.4])
table1.add_column("Humidity", [1, 34, 78, 98.67, 34, 12, 23])
print("========================table=============================")
table1.align = "l"
print(table1.get_string())

file = open("currency.csv", encoding="utf-8")
