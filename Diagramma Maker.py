import matplotlib.pyplot as plt

form_of_diagram = input("Enter form of diagram (1 - Bar, 2 - Pie): ")
if form_of_diagram == "1":
 number_of_x_values = int(input("Enter number of x values: "))
 number_of_y_values = int(input("Enter number of y values: "))
 if number_of_x_values > 0 and number_of_y_values > 0:
   x_values = []
   for i in range(number_of_x_values):
    x_values.append(str(input(f"Enter x {i+1} value: ")))

   y_values = []
   for i in range(number_of_y_values):
    y_values.append(float(input(f"Enter y {i+1} value: ")))

   plt.title(input("Enter title: "))
   plt.bar(x_values, y_values)
   plt.show()
 if number_of_x_values < 1 or number_of_y_values < 1:
   print("Error")
elif form_of_diagram == "2":
   number_of_sections = int(input("Enter number of sections: "))
   if number_of_sections  != 1 or number_of_sections > 1:
    percents = []
    for i in range(number_of_sections):
      percents.append(float(input(f"Enter percent {i+1}: ")))
    z_values = []
    for i in range(number_of_sections):
      z_values.append(str(input(f"Enter z {i+1} value: ")))   
    plt.pie(percents, labels=z_values)
    plt.title(input("Enter title: "))
    plt.show()
   if number_of_sections == 1 or number_of_sections < 1:
    print("Error")
else:
   print("Error")