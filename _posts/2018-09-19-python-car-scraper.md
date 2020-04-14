---
title: Jak pobrać w kilka minut wszystkie oferty z otomoto.pl?
layout: post
excerpt_separator: 
excerpt: czyli o tym jak pokochałem Pythona
comments: true
categories: code
cover: "/img/posts/2018/09/python.jpg"
alt: "a green snake"
---

<p>Stanąłem niedawno przed problemem, na ile mogę wycenić swoje auto. Ponieważ gdzieś w międzyczasie czytałem sobię podręcznik Pythona <a href="http://automatetheboringstuff.com/">Automate the Boring Stuff with Python</a> (którą gorąco polecam, jest za darmo!) stwierdziłem, że jest to idealny moment by użyć świeżo zdobytą wiedzę i napisać sobie skrypt który pobierze mi dane na temat wszystkich dostępnych ofert.</p>

<p><a href="https://www.reddit.com/r/programming/comments/fqtqk/if_programming_languages_were_essays/">W wielu hermetycznych programistycznych memach</a> Python przedstawiany jest jako język w którym wszystko importujesz i właściwie niewiele później robisz. Co ciekawe, właśnie tak wyglądało moje doświadczenie z pisaniem skryptu. Poniżej znajduje się cały kod, który wykorzystałem.</p>

{% highlight python %}

import requests, bs4, io

path = 'https://www.otomoto.pl/osobowe/opel/vectra/'

res = requests.get(path)
res.raise_for_status()

#prepare the file
carFile = io.open('carData.txt', 'w', encoding="utf-8")


#check how many pages are there
carSoup = bs4.BeautifulSoup(res.text, features="lxml")
lastPage = int(carSoup.select('.page')[-1].text)

for i in range(1, lastPage):
    res = requests.get(path + '?page=' + str(i))
    res.raise_for_status()
    currentPage = bs4.BeautifulSoup(res.text, features='lxml')
    carList = currentPage.select('article.offer-item')
    print("parsing page " + str(i))
    for car in carList:
        #get the interesting data and write to file
        price = car.find('span',class_='offer-price__number').text.strip()
        carFile.write(price + ',' )
        title = car.find('a',class_='offer-title__link').text.strip()
        carFile.write(title + ',' )
        params = car.find_all("li", class_='offer-item__params-item')
        for param in params:
            carFile.write(param.text.strip()+ ',')
        carFile.write('\n')
    
carFile.close()

{% endhighlight %}

<p>I to wszystko. Importuje bibliotekę <code>requests</code> żeby pobrać strony. Pobieram pierwszą stronę. Przy pomocy biblioteki <code>Beautiful Soup</code> szukam w niej interesującej mnie informacji - liczby stron. Gdy ją znam, dla każdej z niej wykonuję te samą operację - pobieram, szukam informacji. Na sam koniec zapisuje je do pliku. W rezultacie otrzymuję plik <code>.txt</code> z interesującymi mnie danymi. W tym wypadku mamy to co widać na głównej stronie - model, rocznik, cenę, rodzaj paliwa. Magia.</p>

<p>Można oczywiście ten skrypt usprawnić. Nie wszystkie oferty mają podane wszystkie parametry. Podobnie wynikowe dane mogłyby zostac zapisane od razu w pliku Excela.</p>

<p>Muszę przyznać, że pomimo tego, że skrypt jest dość "łopatologiczny" mogłem szybko zautomatyzować zadanie nad którym samemu spędziłbym dużo więcej czasu. Python okazał się być bardzo przyjazny i prosty w zrozumieniu. Z pewnością będę używał go częściej.</p>