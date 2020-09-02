---
title: Organizacji kodu - "głupie" i "mądre" komponenty oraz ich testowanie.
layout: post
comments: true
categories: code
#cover: "/img/posts/2018/08/test-tubes.jpg"
#alt: "test tubes"
excerpt: "Dzielę komponenty na kontenery i komponenty prezentacyjne oraz piszę kilka testów automatycznych"
---

<p>Postanowiłem zmierzyć się wreszcie z TDD. Jako że moja aplikacja została stworzona przy użyciu <code>create-react-app</code> mam od razu do dyspozycji bibliotekę proponową przez twórców Reacta, tj. Enzyme.</p>

<p>Zanim do tego przejdziemy, powiem jeszcze o ciekawym wzorcu projektowym, który moim zdaniem jest świetnym rozwiązaniem ułatwiającym testowanie aplikacji. Jest nim podział komponentów na prezentacyjne i kontenery - lub komponenty "mądre" oraz "głupie". Na czym to polega? Każdy komponent rozdzielamy na dwie warstwy.</p>

<p>Zgodnie z tym założeniem komponenty prezentacyjne składają się wyłącznie z markupu JSX i odpowiadają tylko za wygląd. Komponenty-kontenery zajmują się wyłącznie logiką aplikacji - robią to przekazując niżej odpowiednie funkcje.</p>

<p>Przełóżmy to na moją aplikację. Właściwie wymagało to niezbyt wielu przeróbek. Np, komponent tabelki początkowo wyglądał tak:</p>

{% highlight jsx %}

export class AppHeader extends Component {
  render(){
    const { currentPage, clickHandler } = this.props  
    return <header className="App-header">
      <h1 className="App-title">Posłowie</h1>
       	<button 
      	onClick={ () => {clickHandler(currentPage - 1)} }
      	>
  		Poprzednia strona
  		</button>
      	<button 
      	onClick={ () => {clickHandler(currentPage + 1)} }
      	>
  		Następna strona
  		</button>
     </header>
  }

}

{% endhighlight %}

<p>Nienajgorzej, ale może być lepiej. Zmienić można tutaj jedną rzecz - zamienić klasę na funkcję - "głupi" komponent będzie jedynie zwracał element JSX, nie potrzebuje żadnych metod. Funkcja odpowiedzialna za zmienianie strony zostaje przekazana z komponentu - kontenera.</p>

{% highlight jsx %}

export const Pagination = ({ currentPage, changePage }) => (
	<header className="App-header">
      <button 
      	onClick={ () => changePage( currentPage - 1 ) }
      	>Poprzednia strona
      </button>
      <button 
      	onClick={ () => changePage( currentPage + 1 ) }
      >Następna strona</button>
     </header>
)


{% endhighlight %}

<p>Jak się to ma do testów? Otóż taki podział pozwala nam oddzielnie przetestować warstwę prezentacyjną i logiczną komponentów - nice. <code>Create-react-app</code>, na którym buduję aplikację ma od razu wbudowany silnik do testów - Enzyme. Składnia testów sprawia że można je niemal czytać jak zdania. Na przykład jeśli chcemy sprawdzić czy nasz nowy komponent przy renderowaniu zwraca dwa przyciski, możemy napisać taki test:</p>

{% highlight javascript %}

describe("When rendering", ()=> {
	it("contains two buttons", () => {
		expect(wrapper.find('button')).toHaveLength(2);
	})
})

{% endhighlight %}

<p>Mało tego, Enzyme jest na tyle sprytny, że przy jego uruchomieniu sprawdza, które pliki zmieniły się od ostatniego commitu i uruchamia tylko te testy, których dotyczą zmiany. Wygląd jednak to nie wszystko - można oczywiście przetestować też przekazywanie handlerów:</p>

{% highlight javascript %}

it("passes click handler properly", () => {
	wrapper.find('button').first().simulate('click');
	wrapper.find('button').last().simulate('click');
	expect(changePageMock.mock.calls.length).toEqual(2);
})

{% endhighlight %}

<p>Podczas testowania lepiej jest sprawdzać daną funkcjonalność, zamiast szczegółów implementacji. Ma to zaletę przy refaktorowaniu. Załóżmy że chciałem przy tabelce zastosować ten sam zabieg co przy paginacji - zamienić komponent na "głupi", składający się jedynie z funkcji zwracającej element JSX. Napisałem więc test sprawdzający tylko czy został wygenerowany prawidłowy HTML. Przy refaktorowaniu Enzyme sam sprawdzał, czy dostałem dokładnie ten sam wynik, bez sprawdzania w jaki sposób go osiągnąłem - magia.</p>

<p>Na razie testujemy tylko komponenty prezentacyjna ("głupie"). W następnym odcinku mojego nieregularnego cyklu projektowego zmierzymy się z testowaniem komponentów "mądrych".</p>