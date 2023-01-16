#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2023  Eduardo Valenzuela

import requests
import argparse

parser = argparse.ArgumentParser(description="Muestra información sobre Cloudfare y DNS")
parser.add_argument("-t", "--target", type=str, default="https://www.google.com", help="sitio web para revisar header", required=True)
parser.add_argument("-m", "--method", type=int, default=1, help="Metodo para comprobar opciones = 1 (header), 2 (dns)", required=True)

parser = parser.parse_args()

def validateStatusCode(resp): 
    if(resp.status_code != 404) :
        print("Status Code:", resp.status_code)
        return True
    else :
        print("Status Code can not working:", resp.status_code)
        return False

def obtenerHeaders(url):
    resp = requests.get(url)
    
    match = (resp.headers["Server"])

    if(validateStatusCode(resp)) :
        if match == 'cloudflare':
            print("EL sitio tiene cloudflare !!!")
        else:
            print("El sitio web no tiene cloudflare !!!")
            
        for k,v in resp.headers.items():
            print("K : {} + V :{}".format(k, v))
    

if __name__ == "__main__":
    if parser.target and parser.method == 1:
        obtenerHeaders(parser.target)
    elif parser.target and parser.method == 2:
        print("method 2!!!")
    else :
        print("opciones de los argumentos incorrectas !!!")
else :
    print("error __main__")