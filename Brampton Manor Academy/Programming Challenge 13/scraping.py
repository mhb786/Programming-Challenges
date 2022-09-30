import urllib.request
import html

def read_website(url):
    mybytes = url.read()
    mystr = mybytes.decode("utf-8")
    mystr = html.unescape(mystr)
    return mystr

def get_singles(mystr):
    position = mystr.find('<div class="title">')
    count = 1
    pos2 = mystr.find('<div class="artist">')
    while position != -1 and pos2 != -1 and count <= 10:
        start = mystr.find('>', position + len('<div class="title">'))+1
        stop = mystr.find('<', start)
        begin = mystr.find('>', pos2 +len('<div class="artist">')) + 1
        end = mystr.find('<', begin)
        print(f'{count}. {mystr[start:stop]} - {mystr[begin:end]}')
        position = mystr.find('<div class="title">', stop)
        pos2 = mystr.find('<div class="artist">', end)
        count +=1


if __name__ == "__main__":
    fp = urllib.request.urlopen('https://www.officialcharts.com/charts/singles-chart/')
    web_str = read_website(fp)
    get_singles(web_str)
