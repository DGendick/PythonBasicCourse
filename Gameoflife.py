####Игра "Жизнь"####

from PIL import Image

field = []
new_field = []
history = []
CELL_SIZE = 50  ##размер одной клетки в пикселях
gen_counter = 0 ##счетчик поколений
stop = False
max_age = 10
def read_file():
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()

            if line:
                row = []
                for c in line:
                    if c == 'X':
                        row.append(1)
                    else:
                        row.append(0)
                field.append(row)

    width = len(field[0])

    for row in field:
        if len(row) != width:
            raise ValueError("Все строки поля должны иметь одинаковую длину")

    height = len(field)
    return field

def save_image(field, filename, base_color):
    height = len(field)
    width = len(field[0])

    img = Image.new("RGB", (width * CELL_SIZE, height * CELL_SIZE), "white")
    pixels = img.load() ##работа с отдельными пикселями

    for i in range(height):
        for j in range(width):

            age = field[i][j]
            color = age_to_color(base_color,age,max_age)
           
            ##закрашиваем квадрат CELL_SIZE x CELL_SIZE
            for di in range(CELL_SIZE):
                for dj in range(CELL_SIZE):
                    pixels[j * CELL_SIZE + dj, i * CELL_SIZE + di] = color

    img.save(filename)

##расчет соседних клеток
def count_neighbors(field, i, j):
    height = len(field)
    width = len(field[0])

    count = 0

##проверяем соседей
    for di in (-1,0,1):     
        for dj in (-1,0,1):

            if di == 0 and dj == 0:
                continue

            ni = i + di
            nj = j + dj

            if 0 <= ni < height and 0 <= nj < width:
                #count += field[ni][nj]
                if field[ni][nj] > 0:
                    count += 1

    return count

##расчет следующего поколения
def next_gen(field):
    height = len(field)
    width = len(field[0])
    new_field = []
    
    ##создаем новое поле
    for _ in range(height):
        new_field.append([0]*width)
        
    #считаем соседей
    for i in range(height):
        for j in range(width):
    
            neighbors = count_neighbors(field, i, j)
            cell = field[i][j]

            if cell > 0:
                if neighbors == 2 or neighbors == 3:
                    new_field[i][j] = cell + 1
                else:
                    new_field[i][j] = 0
            else:
                if neighbors == 3:
                    new_field[i][j] = 1

    return new_field

def age_to_color(base_color, age, max_age):
    if age <=0:
        return (255,255,255)

    t = min(age / max_age,1.0)

    r,g,b = base_color

    new_color = 1.0 - 0.7 * t

    return (int(r * new_color), int(g * new_color), int(b * new_color))

##Проверка не пустое ли поле
def all_dead_check(field):
    for row in field:
        for cell in row:
            if cell > 0:
                return False
    return True

##Подготовка данных для истории
def history_prep(field):
    hist_field = []
    for row in field:
        new_row = []
        for cell in row:
            if cell > 0:
               new_row.append(1)
            else:
                new_row.append(0)
        hist_field.append(new_row)
        
    return hist_field

            
##Проверка истории
def history_check(field,history):
    if field in history:
        return True
    return False

##Проверка есть ли изменения
def no_field_changes(field,new_field):
    if field == new_field:
        return True
    return False

def saving_output2(f, field, gencounter):
    for row in field:
        row2 =[]
        for cell in row:
            if cell != 0:
                row2.append('X')
            else:
                row2.append('.')
        
        print(''.join(row2), file=f)

#############################
####Запуск и чтение файла####
#############################

print(f"Введите кол-во поколений")
gen_ammount = int(input())
print(f"Введите цвет живых клеток: \nr - красный\ng - зеленый\nb - синий")
color = str(input())
if color == "r":
    base_color = (255,0,0)
elif color == "g":
    base_color = (0,255,0)   
elif color == "b":
    base_color = (0,0,255)
    
field = read_file()
print("Нулевое поколение")
for i in range(len(field)):
    print(field[i])
         
filename = "gen0.png"
save_image(field, filename, base_color) ##сохранили изображение поколения 0

##history.append(field)   ##сохранили поколение в историю

while gen_counter <= gen_ammount - 1:

    
    hist_field = history_prep(field)
    
######    if history_check(hist_field, history):
######        print("История пошла по кругу")
######        with open("output.txt", "a") as f:
######            print("История пошла по кругу",file = f)
######        break
    
    history.append(hist_field)   ##сохранили поколение в историю
    
    new_field = next_gen(field)
    gen_counter += 1

    
    if all_dead_check(field):
        print("Все мертвы")
        filename2 = f"gen{gen_counter}input.txt"
        break
    
######  функция проверки отсутствия изменений
######    if no_field_changes(hist_field, history_prep(new_field)):
######        print("Нет изменений")
######        with open("output.txt", "a") as f:
######            saving_output(f, field, gen_counter)
######            print("Больше изменений нет",file = f)
######            field = new_field
######            filename = f"gen{gen_counter}.png"
######            save_image(field, filename,base_color)
######        break
    
    field = new_field
    filename = f"gen{gen_counter}.png"

    print(f"Поколение {gen_counter}")
    for i in range(len(field)):
        print(field[i])
    filename2 = f"gen{gen_counter}input.txt"
    with open(filename2, "w") as f:
        saving_output2(f, field, gen_counter)
    
    save_image(field, filename,base_color)
