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
    thetta1_rad = math.radians(thetta1)             #convert degrees 2 radians
    return d2, v_sand, thetta1_rad

#=======counting function=======
def count(d1, d2, thetta1_rad, h, v_sand, n):
    x = d1* math.tan(thetta1_rad)           #Straight sand route length
    L1 = math.sqrt(x**2 + d1**2)        #Sand route length
    L2 = math.sqrt((h-x)**2 + d2**2)    #Water route length
    v_water = v_sand/n                  #On water speed count   
    print(f"скоорость на воде {v_water:.2f}")
    t = (1/v_sand)*(L1+n*L2)

    return t

#=======optimal thetta value counting function=======
def count_optimal(d1, d2, h, v_sand, n):
    for thetta_2 in range(360):             #cycle for check all angles
        thetta2_rad = math.radians(thetta_2)#convert degrees 2 radians 
        x = d1* math.tan(thetta2_rad)       #Straight sand route length
        L1 = math.sqrt(x**2 + d1**2)        #Sand route length
        L2 = math.sqrt((h-x)**2 + d2**2)    #Water route length
        v_water = v_sand/n                  #On water speed count   
        t2 = (1/v_sand)*(L1+n*L2)           #Time count
        if thetta_2 == 0:                   #First iteration condition 
            t2_prev = t2                    #Saving start value of time
        elif t2 < t2_prev:                  #Condition of comparing time of prev and curr iteration(angle)
            thetta_opt = thetta_2
            t2_prev = t2
            t2_opt = t2            
        else:                               #pass to next iteration
            pass

    return t2_opt, thetta_opt

#=======call functions in main function=======
def main():
    d1, d2, h, v_sand, n, thetta1 = input_data()
    
    d2, v_sand, thetta1_rad = convertor(d2, v_sand, thetta1)

    t = count(d1, d2, thetta1_rad, h, v_sand, n)

    t2_opt, thetta_opt = count_optimal(d1, d2, h, v_sand, n)
    
    print("=====================ИТОГ=====================")
    print(f"Если спасатель начнёт движение под углом thetta1, равным {thetta1:.0f} градусам, он достигнет утопающего через {t:.1f} секунды")
    print(f"Оптимальный угол для введеных исходных данных {thetta_opt:.0f} градусов, время достижения утопающего спасателем составит {t2_opt:.1f}")

main()                                      #Call main functions

