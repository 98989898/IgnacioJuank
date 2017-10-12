from bs4 import BeautifulSoup
import requests
import lxml
import time
import csv

class post:
    titulo = ''
    link = ''
    precio = ''
    area = ''
    ubicacion = []
    def __init__(self):
        self.titulo = ''
        self.link = ''
        self.precio = ''
        self.area = ''
        self.ubicacion = []
    def __str__(self):
        return('\n'.join([self.titulo, self.link, self.precio, self.area, str(self.ubicacion)] ) )

def main(thehtml):
    posts = []
    soup = BeautifulSoup(thehtml, 'lxml')
    listaPosts = soup.find_all('div', class_="detail_wrap")
    arr = list(map(lambda x: buildPost(x), listaPosts))
    return arr

def buildPost(pPost):
    try:
        new_post = post()
        new_post.__init__()
        new_post.titulo = pPost.find('h2').string.encode('utf-8')
        new_post.link = pPost.find('a', itemprop='url')['href'].encode('utf-8')
        new_post.precio = pPost.find('span', itemprop='price').string.encode('utf-8')
        new_post.area = pPost.find('div', class_='m2').find('span').string.encode('utf-8')
        # print(new_post.link)
        recursive_html = requests.get(new_post.link).text
        noodles = BeautifulSoup(recursive_html, 'lxml')
        try:
            a = noodles.find('div', id='ubicacion_y_valorizacion')
            new_post.ubicacion.append( a.find('input', id='longitude')['value'].encode('utf-8') )
            new_post.ubicacion.append( a.find('input', id='latitude')['value'].encode('utf-8') )
        except:
            pass
        # print('post created: ', new_post.__str__())
        return new_post
    except:
        print(pPost)
        print('something went wrong')
        pass

url = "http://www.metrocuadrado.com/search/list/ajax"

querystring = {"":"","mnrogarajes":"","mnrobanos":"","mnrocuartos":"","mtiempoconstruido":"","marea":"","mvalorarriendo":"","mvalorventa":"","mciudad":"pereira","mubicacion":"","mtiponegocio":"arriendo","mtipoinmueble":"apartamento","mzona":"","msector":"","mbarrio":"","selectedLocationCategory":"1","selectedLocationFilter":"mciudad","mestadoinmueble":"","madicionales":"","orderBy":"","sortType":"","companyType":"","companyName":"","midempresa":"","currentPage":1,"totalPropertiesCount":"19211","totalUsedPropertiesCount":"19211","totalNewPropertiesCount":"0","sfh":"1"}

headers = {
    'accept': "*/*",
    'origin': "http://www.metrocuadrado.com",
    'x-devtools-emulate-network-conditions-client-id': "f0ac5f33-47cd-443c-b031-713436e7a8a6",
    'x-requested-with': "XMLHttpRequest",
    'x-devtools-request-id': "1233.1663",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'referer': "http://www.metrocuadrado.com/apartamentos/arriendo/pereira/",
    'accept-encoding': "gzip, deflate",
    'accept-language': "en-US,en;q=0.8",
    'cookie': "__utmz=other; G_ENABLED_IDPS=google; s_vnum=1502667903479%26vn%3D2; s_cm=Natural%20Searchwww.google.com.co; s_v10=%5B%5B%27Natural%2520Search%27%2C%271500075903485%27%5D%2C%5B%27Natural%2520Search%27%2C%271500075922378%27%5D%2C%5B%27Natural%2520Search%27%2C%271500075922398%27%5D%2C%5B%27Natural%2520Search%27%2C%271500095118948%27%5D%5D; s_v8=%5B%5B%27natural%2520search%253A%2520google%253A%2520keyword%2520unavailable%27%2C%271500075903485%27%5D%2C%5B%27natural%2520search%253A%2520google%253A%2520keyword%2520unavailable%27%2C%271500075922378%27%5D%2C%5B%27natural%2520search%253A%2520google%253A%2520keyword%2520unavailable%27%2C%271500075922400%27%5D%2C%5B%27natural%2520search%253A%2520google%253A%2520keyword%2520unavailable%27%2C%271500095118954%27%5D%5D; visid_incap_434661=akoiu2XJRm+7GkSxV1/kF3xXaVkAAAAAQUIPAAAAAABaNioHzJQs0Z4wNrX36k8o; incap_ses_223_434661=efa5OXb/7TuiN3Ozp0EYA4+iaVkAAAAAdDQ29qP7kuiFQo4uRNo3Lg==; resultListOriginURL=/search/list/non-ajax/?&mnrogarajes=&mnrobanos=&mnrocuartos=&mtiempoconstruido=&marea=&mvalorarriendo=&mvalorventa=&mciudad=pereira&mubicacion=&mtiponegocio=arriendo&mtipoinmueble=apartamento&mzona=&msector=&mbarrio=&selectedLocationCategory=1&selectedLocationFilter=mciudad&mestadoinmueble=&madicionales=&orderBy=&sortType=&companyType=&companyName=&midempresa=&currentPage=1&totalPropertiesCount=19210&totalUsedPropertiesCount=19210&totalNewPropertiesCount=0&sfh=1#4042-208; cookieInterestedProperty=4042-208%3A1; s_cc=true; _ga=GA1.2.1512535764.1500075905; _gid=GA1.2.1111954021.1500075905; _ceg.s=ot4aaw; _ceg.u=ot4aaw; madicionales=; mbarrio=; mciudad=Bogot%C3%A1; mnrobanos=; mnrocuartos=; mnrogarajes=; msector=; mubicacion=; mvalorventa=; mzona=; orderBy=; selectedLocationCategory=1; selectedLocationFilter=mciudad; sortType=; writtenFilters=mnrogarajes%3Bmnrobanos%3Bmnrocuartos%3Bmtiempoconstruido%3Bmarea%3Bmvalorarriendo%3Bmvalorventa%3Bmciudad%3Bmubicacion%3Bmtiponegocio%3Bmtipoinmueble%3Bmzona%3Bmsector%3Bmbarrio%3BselectedLocationCategory%3BselectedLocationFilter%3Bmestadoinmueble%3Bmadicionales%3BorderBy%3BsortType%3Bmestadoinmueble%3BcompanyType%3BcompanyName%3Bmidempresa%3B; m2-srv=ffffffff0975c82e45525d5f4f58455e445a4a4229a2; mtiponegocio=arriendo; mtipoinmueble=apartamento; mvalorarriendo=; marea=; mtiempoconstruido=; companyType=; companyName=; midempresa=; mestadoinmueble=; gpv_pn=metrocuadrado%3A%20buscar%3A%20resultados%20inmuebles%3A%20usado; s_invisit=true; s_nr=1500098877115-Repeat; s_lv=1500098877118; s_lv_s=Less%20than%201%20day; s_sq=%5B%5BB%5D%5D",
    'cache-control': "no-cache",
    'postman-token': "a911fa52-08b6-7c4a-3d74-802fd0439ad0"
    }

lista = []

for i in range(1):
    print(str(i) + '/15')
    querystring['currentPage'] = i
    response = requests.request("POST", url, headers=headers, params=querystring)
    lista.extend( main(response.text) )
    # time.sleep(2)
print('finished Scraping', lista)

with open('pereira.csv', 'w') as csvfile:
    print('started writing in csv')
    fieldnames = ['titulo', 'link', 'precio' , 'area', 'ubicacionX', 'ubicacionY']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for pub in lista:
        print(pub)
        try:
            writer.writerow({'titulo': pub.titulo, 'link': pub.link, 'precio': pub.precio, 'area': pub.area, 'ubicacionX': pub.ubicacion[0], 'ubicacionY': pub.ubicacion[1] })
        except:
            writer.writerow({'titulo': pub.titulo, 'link': pub.link, 'precio': pub.precio, 'area': pub.area, 'ubicacionX': '', 'ubicacionY': '' })
