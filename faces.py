import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk() #создание окна
root.geometry("600x500") #изменение размеров окна
root.title("Распознавание лиц")  #заголовок окна

scaleFactor = tk.DoubleVar(value='') #создаем переменную под параметр scaleFactor
minNei = tk.IntVar(value='') #создаем переменную под параметр minNeihbors

label1 = tk.Label(root, text="Введите параметр scaleFactor:") # текстовое поле
label1.config(font=("Arial", 16))
label1.pack()
entry1 = tk.Entry(root, textvariable=scaleFactor) #поле ввода параметра scaleFactor
entry1.config(font=("Arial", 16))
entry1.pack(pady = 30)

label2 = tk.Label(root, text="Введите параметр minNeighbors:") # текстовое поле
label2.pack()
label2.config(font=("Arial", 16))
entry2 = tk.Entry(root, textvariable=minNei) #поле ввода параметра minNeighbors
entry2.config(font=("Arial", 16))
entry2.pack(pady = 30)

def find_faces(scaleFactor, minNei):
    file_path = filedialog.askopenfilename() #загружаем фото
    img = cv2.imread(file_path) # переменная с фото, с которую обрабатываем
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #изменяем цветовую гамму с цветной на серую
    faces = cv2.CascadeClassifier('faces.xml') # загружаем натренированную xml-модель
    results = faces.detectMultiScale(gray, scaleFactor, minNei) #поиск лиц на фото с параметрами scaleFactor и minNei

    for (x, y, w, h) in results:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3) #обводим лица в красный прямоугольник

    cv2.imshow("result", img) #вывод изображения
    cv2.waitKey(0)
    root.destroy()


label = tk.Label(root)
label.pack(padx=10, pady=10)

button = tk.Button(root, text="Загрузить фото", command=lambda: find_faces(scaleFactor.get(), minNei.get()))
button.pack(pady=10)
button.config(font=("Arial", 16))

root.mainloop()