#Steven Cisneros
#Professor Nguyen
#CIS 103-20324-LEC
#20 February 2020


hString = input("Enter the height (feet):")
height = float(hString)

wString = input("Enter the width(feet):")
width = float(wString)

area = height * width

ONE_GALLON_PER_150_SQUAREFEET = 150

gallons = area/ONE_GALLON_PER_150_SQUAREFEET

print("The amount paint is ", gallons, "gallons")
