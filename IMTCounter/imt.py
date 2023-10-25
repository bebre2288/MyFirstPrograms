print('введите ваш вес:')
m=float(input())
print('введите ваш рост в сантиметрах:')
h=float(input())
h=h/100
BMI = m/(h*h)
print(BMI)
BMI=int(BMI)
if BMI<=16:
    print('Выраженный недостаток массы тела')
if BMI in range(16,18):
    print('Сниженная масса тела')
if BMI in range(18,24):
    print('	Норма')
if BMI in range(25,30):
    print('Избыточная масса тела')
if BMI in range(30,35):
    print('Ожирение первой степени')
if BMI in range(35,39):
    print('Ожирение второй степени')
if BMI>=40:
    print('Ожирение третьей степени')
input()