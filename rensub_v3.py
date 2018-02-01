'''
Created on 9 ene. 2018

@author: The Pope
'''
from os import system, listdir, chdir, rename
from pathlib import Path
from pip._vendor.distlib.compat import raw_input
import kivy
from kivy import app

def print_header():
    print("+---------------------------------------+")
    print("         R E N O M B R A D O R")
    print("                 D E")
    print("          S U B T I T U L O S")
    print("+---------------------------------------+")
    print("          Formato SXXEXX - v3")
    print("+---------------------------------------+\n")
    

def print_header_log():
    print("\n+---------------------------------------+")    
    print("        L O G  D E  P R O C E S O")    
    print("+---------------------------------------+")    
    print("El valet cosmico ha empezado - - - - - ")
    
def get_arc_list():
    print ( "Ingrese ruta de archivos")
    path = raw_input()
    if path == "":
        get_arc_list()
    else:
        try:
            list = listdir(path)
            #Modifico directorio al de los subtitulos
            chdir(path)
            return list
        except:
            print ("Directorio invalido")
            system("pause")    
            quit()

def search_ep(temp,string):
    id_temp = 'S' + temp + 'E' #Remplazar por logica de armado de busqueda
    pos_temp = string.find(id_temp)
    
    if pos_temp >= 0:
        pos_d = pos_temp + 4
        pos_h = pos_temp + 6
        try:
            ep = int(string[pos_d:pos_h])
        except:
            return 0
        return ep


def add_file_list(temp,archivo,videos,subtitulos):
    nombre = Path(archivo).stem
    nombre = nombre.upper()
    episodio = search_ep(temp,nombre)
    if episodio > 0:
        ext = Path(archivo).suffix
        if ext == ".srt":
            subtitulos[episodio] = [archivo]
        else:
            videos[episodio] = [archivo]
    else:
        print("Archivo %s - No se pudo determinar nro. de episodio." % archivo)
        
        
def rename_arc(nro_temp,videos,subtitulos):
    
    for video in videos:
        
        episodio_vid = str(video)
        find = False
        
        for sub in subtitulos:
            
            episodio_sub = str(sub)
            if episodio_vid == episodio_sub:
                ext = Path(subtitulos[sub][0]).suffix
                new = Path(videos[video][0]).stem + ext
                rename(subtitulos[sub][0],new)
                print("Episodio %s - Renombrado: %s" % (episodio_sub,new))
                del subtitulos[sub]
                find = True
                break
            
        if find == False:
            print("Episodio %s no encontrado" % episodio_vid)
        
         
print_header()    

print("Ingrese nro de temporada")
nro_temp = raw_input()

videos = {}
subtitulos = {}

lista_arc = get_arc_list()

print_header_log()

for archivo in lista_arc:
    add_file_list(nro_temp,archivo,videos,subtitulos)

rename_arc(nro_temp,videos,subtitulos)

system("pause")
