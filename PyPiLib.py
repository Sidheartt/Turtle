from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Balbasaur", "Charlizad"])
table.add_column("Type",["Electric", "Plant", "Fire"])
table.align = "l"
print(table)

