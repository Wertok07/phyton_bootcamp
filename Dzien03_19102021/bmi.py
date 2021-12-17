"""

Skrypt obliczający BMI

BMI = Waga (kg) / wzrost (m^2)
Wzrost w cm
"""

weight = input("Podaj wagę w kg:")
height = input("Podaj wzrost w cm:")

# print(weight, height)

weight = int(weight)
height = int(height)

# bmi = weight / pow( height/100, 2)
# print("1", bmi)

bmi = weight / ((height * 0.01) ** 2)
print("Twoje BMI =", f"{bmi:.2f}")
# print("Twoje BMI =", round(bmi, 2))
# print("Twoje BMI = " + str(round(bmi, 2)))
# print(f"Twoje BMI = {bmi:.2f}")
# print(f"Twoje BMI = {bmi:.2f}")

# if bmi >= 25:
#     print("ogranicz kebaby")
#     print("ogranicz monsterki")
# elif bmi < 18.5:
#     print("zjedz cos")
# else:
#     print("wszystko ok")

if bmi >= 18.5 and bmi < 52:
    print("wszystko ok")
elif bmi >= 25:
    print("ogranicz kebaby")
    print("ogranicz monsterki")
    if bmi > 35:
        print("Do lekarza")
elif bmi < 25:
    print("zjedz cos")
else:
    pass

# import math
# bmi = weight / math.pow(height/100, 2)
# print("3", bmi)
