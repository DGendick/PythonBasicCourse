#####===Life Guard Task===#####
#=============================#

import math     #Add math lib

#=======input function=======
def input_data():
    check = input('Вы хотите ввести значения вручную или использовать значения из примера? [y/n]')
    if check == 'y' or check == 'Y':
        d1 = int(input('Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды)'))
        print('d1 => ',d1)
        d2 = int(input('Введите кратчайшее расстояние от утопающего до берега, d2 (футы)'))
        print('d2 => ', d2)
        h = int(input('Введите боковое смещение между спасателем и утопающим, h (ярды)'))
        print('h => ', h)
        v_sand = int(input('Введите скорость движения спасателя по песку, v_sand (мили в час)'))
        print('v_sand => ', v_sand)
        n = int(input('Введите коэффициент замедления спасателя при движении в воде'))
        print('n => ', n)
        thetta1 = float(input('Введите направление движения спасателя по песку, theta1 (градусы)'))
        print('thetta1 => ', thetta1)
    elif check == 'n' or check == 'N':
    #Pre entered data for fast test
        d1 = 8
        d2 = 10
        h = 50
        v_sand = 5
        n = 2
        thetta1 = 39.413
    else:
        print('Введено некорректное значение, вам необходимо ввести [y] для ручного задания парамметров задачи или [n] для применения стандартного набора параметров из примера')

        return input_data()
    
    return d1, d2, h, v_sand, n, thetta1

#=======convertation function=======
def convertor(d2, v_sand, thetta1):
    d2 = d2/3                                       #convert feet 2 yard
    v_sand = v_sand*1760.0/3600.0                   #concert mph 2 yards per second
    thetta1 = math.radians(thetta1)                 #convert degrees 2 radians
    return d2, v_sand, thetta1

#=======counting function=======
def count(d1, d2, thetta1, h, v_sand, n):
    x = d1* math.tan(thetta1)       #Straight sand route length
    L1 = math.sqrt(x**2 + d1**2)        #Sand route length
    L2 = math.sqrt((h-x)**2 + d2**2)    #Water route length
    v_water = v_sand/n                  #On water speed count   
    print(f"скоорость на воде {v_water:.2f}")
    t = (1/v_sand)*(L1+n*L2)

    return t

#=======Call functions=======
d1, d2, h, v_sand, n, thetta1 = input_data()
    
d2, v_sand, thetta1 = convertor(d2, v_sand, thetta1)

t = count(d1, d2, thetta1, h, v_sand, n)

print(f"Если спасатель начнёт движение под углом theta1, равным {thetta1:.0f} градусам, он достигнет утопающего через {t:.1f} секунды")
