---
title: Aplikacja do przeglądania przemówień sejmowych
layout: post
excerpt_separator: 
excerpt: "Tworzę aplikację do przeglądania danych o pracy sejmu."
comments: true
categories: code
---

<h2>Sejmowe API - aplikacja do przeglądania przemówień sejmowych.</h2>

<a href="/sejmator">Demo aplikacji</a> <br>
<a href="https://github.com/bananovitch/sejmator">Kod na Github</a>

<p>Postanowiłem po raz kolejny ruszyć z miejsca z nauką React.js. Przeczytałem do końca książkę, jednak projektu nie kontynuowałem - stwierdziłem, że zamiast tego spróbuję samemu napisać aplikację, korzystając z książki jako źródła wiedzy, a z fragmentów kodu jako inspiracji do tego by stworzyć coś samemu.</p>

<p>Odkryłem niedawno (nie pamiętam już jak), że na stronie mojepanstwo.pl znajduje się API umożliwiające przeglądanie treści przemówień sejmowych oraz danych na temat posłów i ich pracy. Od razu zaświeciła mi się w głowie lampka: to jest doskonały pomysł na stworzenie aplikacji. Tym bardziej że API jest darmowe oraz dostępne dla wszystkich. W dodatku wygląda na ładnie udokumentowane.</p>

<h2>It's alive!</h2>

<p>Zacząłem pisać aplikację. Co tam zatem ciekawego się dzieje? Na razie udało mi się połaczyć z serwerem i pobrać dane oraz wyświetlić je na stronie. Poczatkowo była pierwsze 50 osób na liście posłów sejmu 8 kadencji. Skorzystałem tutaj z metody <code>fetch</code>. </p>

{% highlight javascript %}

fetchSpeeches( page = 0 ) {
    fetch(`${pathBase}?${requestType}&${paramPage}${page}`)
    .then(response => response.json())
    .then(response => this.setState({ 
      result:response.Dataobject,
      page
     }));
}

{% endhighlight %}

<p>Korzystam tutaj z kilku rzeczy których się nauczyłem. Po pierwsze, cała metoda jest wpisana bezpośrednio w klasę <code>App</code>. Następnie podaję metodzie argument page - którą stronę chce wyświetlić, oraz przypisuję mu wartość domyślną. </p>

{% highlight javascript %}

fetchSpeeches( page = 0 ) {
	...
}

{% endhighlight %}

<p>Wywołuję następnie metodę <code>fetch</code>. argumentem funkcji jest adres, którego wywołanie zwraca listę posłów w formacie JSON. Adres buduję przy użyciu kilku zmiennych, które łączę stosując <code>template string</code>.</p>

{% highlight javascript %}
fetch(`${pathBase}?${requestType}&${paramPage}${page}`)
    ...
    );
{% endhighlight %}

<p><code>Fetch</code> po wykonaniu zwraca tzw. <code>promise</code>, który dysponuje kolejną fajną metodą: <code>then</code>. W metodzie tej podajemy funkcję którą chcemy wykonać po otrzymaniu odpowiedzi z danymi. Jak widać można je łączyć. We fragmencie poniżej najpierw formatujemy odpowiedź do JSON po czym ustalamy stan aplikacji. Zmiana stanu aplikacji komponentu <code>App</code> powoduje jego ponowne renderowanie. </p>

{% highlight javascript %}

.then(response => response.json())
.then(response => this.setState({ 
	result:response.Dataobject,
	page
}));

{% endhighlight %}

<p>W ten sposób mam metode przyjmującą numer strony jako parametr, czytającą odpowiedź zapisującą dane z odpowiedzi w stanie aplikajci. Not bad!</p>

<p>OK, pobraliśmy dane, dodajmy je sobie do dokumentu. Mamy zatem metodę <code>render</code>.Aby dodać pobrane z API dane do dokumentu mapujemy je do elementu JSX. Zmiana strony wywoływana jest po kliknięciu na przycisk.</p>

{% highlight html %}

render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Przemówienia sejmowe.</h1>
        </header>
        <h2>Sejmator</h2>
        <button 
        	onClick={() => this.fetchSpeeches(this.state.page) }
        >Pobierz dane</button>
        <button 
        	onClick={() => this.fetchSpeeches(this.state.page - 1) }
        >Poprzednia strona</button>
        <button 
        	onClick={() => this.fetchSpeeches(this.state.page + 1) }
        	>Następna strona strona
        </button>
        <ol>
        {this.state.result.map( (item, index) => 
          <li key={index}>{item.slug}</li> 
          )}
        </ol>
        
      </div>
    );
  }
}

{% endhighlight %}

<p>Jest tu oczywiście dużo do poprawy. Mógłbym np. pobierać dane już po zamontowaniu komponentu zaplikacją, dodać testy oraz wyświetlić więcej danych. Ale o tym już w następnych postach :)</p>
