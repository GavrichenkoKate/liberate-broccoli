import pygame as pg
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pandas
from Build_Graph.py import *
from Excel_Read.py import *
from Transform_to_Latex import *



print('what will we build?')
print('graphics = a, tables = b, histograms = c')
desired = input()

if desired == 'a':
    print('Число графиков:')
    plot_num = int(input())  #Ввод числа графиков (опционально)
    print('Путь сохранения:')
    path = input()  # Ввод пути папки сохранения
    # path = '/home/fima/Documents/uni/labs/' + lab_num + '/figs/graph_' + graph_num + '.png'
    data = pd.read_excel("name" + ".xlsx")
    
    Questions()
    
    for i in range(plot_num):
        print('XY-координаты' + str(i) + '-го графика')
        x, y = input()   # Ввод x,y координат i-го графика
        plotfile(data, x, y)
        # tablefile(data)
        PlotBuild()
    PlotShow(path)
    
elif desired == 'b':
    
elif desired == 'c':  
      
    read_csv(file_name)
    make_latex_table_with_borders(data)
    make_latex_table_without_borders(data)
    make_latex_table_with_separator_between_columns(data)
    
    print('Введите фиксированную длину столбца')
    len_array = int(input())
    
    make_latex_table_with_length_columns(data, len_array)
    '''
    :param data:
    :param len_array: ширина столбца в сантиметрах
    :return:
    '''
    len_array = [2, 3, 4]
    A = read_csv(r"C:\Users\user\Downloads\23.csv")
    for i in make_latex_table_with_length_columns(A, len_array):
        print(i)         

