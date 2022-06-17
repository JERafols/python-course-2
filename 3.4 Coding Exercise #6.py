class customers :
    greeting = 'welcome to coffee place!'

c_1 = customers()
c_1.name = "samirah"
c_1.beverage = "ice coffee latte"
c_1.food = "cinnamon roll"
c_1.total = 225

c_2 = customers()
c_2.name = "jerry"
c_2.beverage = "caramel macciato"
c_2.food = "glaze doughnut"
c_2.total = 230

print(customers.greeting)
print(c_1.beverage)
print(c_2.food)
