#Импорт модуля json
import json

file = 'dump.json'  
#Ввод номера квалификации
qualification_code = str(input("Введите код квалификации: "))
#Если квалификация найдена - true
found_skills = False

#Открываем файл и загружаем в content
with open(file, 'r', encoding = 'utf-8') as file:  
    content = json.load(file) 
    
    #Проходимся по каждому элементу в content
    for skill in content:
        #Проверка
        if skill.get("model") == "data.skill":
            #Проверка на совпадение кода квалификации
            if skill["fields"].get("code") == qualification_code: 
                #Сохраняем код квалификации
                code_of_qualification = skill["fields"].get("code")
                #Сохраняем название квалификации
                title_of_qualification = skill["fields"].get("title")
                #Сохраняем специальность
                special = skill["fields"].get("specialty")
                #Переменная found_skills - true
                found_skills = True
            
                #Перебор данных для нахождения нужной квалификации
                for profession in content:
                    #Проверка модели элемента на совпадение с "data.specialty"
                    if profession.get("model") == "data.specialty":
                        #Сохраняем код специальности
                        code_of_special = profession["fields"].get("code")
                        #Сохраняем первичный ключ квалификации
                        pk_of_special = profession["pk"]
                        #Проверка на совпадение идентификатора и первичного ключа
                        if special == pk_of_special:  
                            #Сохраняем информацию
                            title_of_special = profession["fields"].get("title")
                            special_educational = profession["fields"].get("c_type")
                            break
                break  

#Проверяем, была ли найдена квалификация
if not found_skills:
   #Вывод
   print("=============== Не Найдено ===============") 
else:
   print("=============== Найдено ===============") 
   print(f"{code_of_special} >> Специальность: {title_of_special} , {special_educational}")
   print(f"{code_of_qualification} >> Квалификация: {title_of_qualification}")