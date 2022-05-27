---
title: Posprzątajmy trochę swój kod.
layout: post
comments: true
categories: code
excerpt: ".. czyli o tym jak podzielić swój kod na moduły."
---

<a href="/sejmator">Demo aplikacji</a> <br>
<a href="https://github.com/bananovitch/sejmator">Kod na Github</a>

<p>Dodałem kilka nowych rzeczy w mojej aplikacji. Po pierwsze, nie trzeba już klikać "pobierz dane". Dzięki metodzie <code>componentDidMount()</code> aplikacja pobiera dane tuż po jej wyrenderowaniu. Dzięki temu już na samym początku coś widać. Dodałem też 3 nowe pola do tabelki: skrót klubu, frekwencję posła oraz liczbę jego wypowiedzi.</p>

<p>Może i aplikacja działa, ale trochę puchnie już jej kod. Myślę, że jest do dobry moment by zacząć pracę z modułami a potem testami automatycznymi.</p>

<p>Zacznijmy od modułów. Dotychczas wszystko było zbudowane w jednej klasie <code>App</code> która zawierała co najmniej kilka komponentów. Postanowiłem przenieść nagłówek do osobnego komponentu. Jest tu jeden problem - w nagłówku znajdują się przyciski odpowiedzialne za przechodzenie na kolejną stronę z wynikami. Każdy z nich ma przypisaną funkcję odpowiedzialną za pobieranie danych z serwera, która to znajduje się w komponencie <code>App</code>. Dlatego też, trzeba będzie ją przekazać z komponentu stojącego wyżej w hierarchii.</p>

<p>Przeniosłem więc nagłówek do osobnego komponentu. Już na tym etapie miałem nieco problemów z prawidłowym przekazaniem funkcji obsługującej pobieranie danych. Była ona zapisana w komponencie-rodzicu, podczas gdy musiałem go wywoływać z komponentu-dziecka. Było to o tyle problematyczne, że funkcja ta zawiera odwołanie do stanu rodzica. Na szczęscie jest ES6 i jej funkcje strzałkowe (teraz doceniam ich przydatność!). Ot, specyfika JavaScriptu.</p>

{% highlight jsx %}
class AppHeader extends Component {
  render(){
    const { currentPage, clickHandler } = this.props  
    return <header className="App-header">
      <h1 className="App-title">Posłowie</h1>
      <button 
        onClick={ () => {clickHandler(currentPage - 1)} }
      >Poprzednia strona</button>
      <button 
        onClick={ () => {clickHandler(currentPage + 1)} }
      >Następna strona</button>
     </header>
  }

}
{% endhighlight %}

<p>Widziałem w wielu przykładach że ludzie idą krok dalej wyodrębniając przyciski do odzielnych komponentów, ale mówiąc szczerze nie widzę zbytniego sensu tworzenia komponentu do pojedynczego elementu HTML. Jedyna róznica pomiędzy jednym a drugim podejściem jest, że w naszym kodzie zamiast wpisywać przykładowo <code>&lt;button&gt;</code> będziemy wpisywać jakąś inną nazwę, np. <code>&lt;SomeButtonComponent&gt;</code>. Może jest w tym faktycznie jakiś sens, jednak ja osobiście nie widzę go na razie.</p>

<p>Tak stworzony komponent możemy przenieść do osobnego pliku i następnie go zaimportować. Dzięki temu można rozbić jeden wielki plik na kilka mniejszych. Pozwoli to zachować porządek i z pewnością ułatwi utrzymanie aplikacji później. Aby tak zrobić przenosimy go do osobnego pliku, dodajemy deklarację <code>export</code> oraz importujemy go w pliku z aplikacją.</p>

{% highlight jsx %}

import React, { Component } from 'react';

class ResultsTable extends React.Component {
  ...
}

export default ResultsTable;

{% endhighlight %}
definicja importu:
{% highlight jsx %}

import ResultsTable from './Components/ResultsTable.js'

<ResultsTable 
  dataArray={this.state.result}
/>

{% endhighlight %}

<p>Not bad! Dzięki temu rozmiar kodu całej aplikacji zmniejszył się dość znacznie. Metoda <code>render</code> wygląda teraz znacznie ładniej.</p>

{% highlight jsx %}
render() {
    return (
      <div className="App">
        <AppHeader 
          currentPage={this.state.page} 
          clickHandler={this.fetchSpeeches}
        />
        <ResultsTable 
          dataArray={this.state.result}
        />
      </div>
    );
  }
{% endhighlight %}

<p>Na marginesie dodam że zaczynam rozumieć cały ten <i>hype</i> dookoła Reacta. Przy bardzo małym nakładzie pracy stworzyłem aplikację pobierająca dane z serwera, podzieloną na strony, z modułowym kodem. Zmiana widoku dzieje się "sama" po zaktualizowaniu stanu aplikacji. Magia.</p>
