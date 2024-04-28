import web_scraping

def menuwebs():
    url = input("Ingrese la URL: ")
    url_nueva = web_scraping.verificador_nav(url)
    html = web_scraping.conexion_request(url_nueva)
    
    print(html)


if __name__=='__main__':
    menuwebs()