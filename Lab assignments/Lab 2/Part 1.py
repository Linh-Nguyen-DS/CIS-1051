weight = int(input("What is your weight?"))
height = int(input("How tall are you?"))
age = int(input("How old are you?"))
F_BMR = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
M_BMR = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
Amount_of_bars_F = F_BMR // 214
Amount_of_bars_M = M_BMR // 214
print(F_BMR, "F_BMR", Amount_of_bars_F, "Amount_of_bars_F", M_BMR, "M_BMR", Amount_of_bars_M, "Amount_of_bars_M")
