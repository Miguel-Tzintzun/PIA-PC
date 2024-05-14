"""
NOTA: El csv lo genera dentro de la carpeta que estamos buscando y el html en la carpeta de imagenes
"""
import os
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS
import gmplot
import csv
#Función que nos ayudara a hacer el html de las ubicaciones y el link individual
def google_maps(gps_coords,cc):
    dec_deg_lat = convert_decimal_degrees(float(gps_coords["lat"][0]),  float(gps_coords["lat"][1]), float(gps_coords["lat"][2]), gps_coords["lat_ref"])
    dec_deg_lon = convert_decimal_degrees(float(gps_coords["lon"][0]),  float(gps_coords["lon"][1]), float(gps_coords["lon"][2]), gps_coords["lon_ref"])
    cc.update({dec_deg_lat: dec_deg_lon})
    mapa = gmplot.GoogleMapPlotter(0, 0, 12)
    for  latitud, longitud in cc.items():
     mapa.marker(latitud, longitud, "#ff0000")
     mapa.draw("mapa.html")
    return f"https://maps.google.com/?q={dec_deg_lat},{dec_deg_lon}"

#Función que nos permite convertir a grados decimales  
def convert_decimal_degrees(degree, minutes, seconds, direction):
    decimal_degrees = degree + minutes / 60 + seconds / 3600
    if direction == "S" or direction == "W":
        decimal_degrees *= -1
    return decimal_degrees

def extract_metadata():
    cc = {}   
    ruta = input("Ingresa la ruta de la carpeta que deseas analizar: ")
    os.chdir(ruta)
    files = os.listdir() 
    if len(files) == 0:
        print('No tienes archivos en esta carpeta')
        return
    
    with open("../metadata_info.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        
        for file in files:
            try:
                image = Image.open(file)
                print(f"__{file}__ extracting metadata...")
                gps_coords = {}
                writer.writerow(("Filename", file))
                if image._getexif() == None:
                    writer.writerow((file, "Contains no exif data."))
                else:
                    for tag, value in image._getexif().items():
                        tag_name = TAGS.get(tag)
                        if tag_name == "GPSInfo":
                            for key, val in value.items():
                                writer.writerow((GPSTAGS.get(key), {val}))
                                if GPSTAGS.get(key) == "GPSLatitude":
                                    gps_coords["lat"] = val
                                elif GPSTAGS.get(key) == "GPSLongitude":
                                     gps_coords["lon"] = val
                                elif GPSTAGS.get(key) == "GPSLatitudeRef":
                                    gps_coords["lat_ref"] = val
                                elif GPSTAGS.get(key) == "GPSLongitudeRef":
                                    gps_coords["lon_ref"] = val 
                        else:
                            writer.writerow((tag_name, value))
                    if gps_coords:
                        writer.writerow(("Google Maps Link", google_maps(gps_coords, cc)))
            except IOError:
                print("File format not supported!")                    
    print("successful metadata extraction")


                    
                 

             
             

    
