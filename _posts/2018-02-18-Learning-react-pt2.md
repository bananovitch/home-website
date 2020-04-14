---
title: Ciąg dalszy nauki React.js oraz pierwsza aplikacja. 
layout: post
excerpt: "Zepsułem blog. I napisałem prostą aplikacji w React.js"
comments: true
categories: code
cover: "/img/posts/2018/02/react-2.jpg"
alt: "code"
---

<p>Krok po kroku kontynuuję nieocenioną książkę Robina Wierucha. Miałem pewien moment zwątpienia związany pewnie z dużą ilością nowej wiedzy do przyswojenia, ale po nim nastąpiło pewnego rodzaju przejaśnienie. Mam wrażenie, że zaczynam trochę rozumieć, o co chodzi w tej bibliotece, i powoli elementy układanki zaczynają się układać w całość.</p>

<p>A zatem o co chodzi w Reakcie? U podłoża biblioteki leży założenie, żeby aplikację webową podzielić na małe kawałeczki, nazywane komponentami. Z takich kawałeczków możemy następnie budować inne komponenty oraz całą aplikację. Działa to w ten sposób, że deklarujemy sobie taki komponent, oraz jego <i>stan</i> (słowo - klucz). Określamy jakie elementy HTML będą się na niego składać. Do zbudowania aplikacji korzystamy z naszych komponentów pisząc je tak, jakby były one elementami HTML (mniej więcej do tego właśnie używana jest składnia JSX, chociaz nie do końca.) Wygląda to mniej więcej tak:</p>


{% highlight html %}
const Search = ({value, onChange, children}) => 
<form>
	{children}
	<input type="text" 
	onChange={onChange}
	value={value}
	/>
</form>
{% endhighlight %}

<p>Następnie możemy tak zadeklarowany komponent wykorzystać w naszej aplikacji, w ten sposób:</p>

{% highlight html %}
<div class="app">
	<Search/>
</div>
{% endhighlight %}

<p>W przypadku, gdy chcemy zmienić coś w naszym komponencie, robimy to w miejscu jego deklaracji, co powoduje zmiany w całej aplikacji. Całkiem fajnie. Ponadto, jak już napisałem, każdy komponent ma swój stan. Jeśli w aplikacji coś zmodyfikuje stan komponentu, wówczas React odświeży ten komponent w aplikacji, i nic więcej, bez przeładowywania przeglądarki. Dzięki temu możemy wybudować tzw. SPA, czyli <i>Single Page Application</i>.</p>

<p>To, co cały czas jest dla mnie nieco niejasne, jest sposób w jaki obsługiwane są wydarzenia, co być może spowodowane jest tym, że za nic nie mogę przyzwyczaić się do nowej notacji funkcji w ES6. Przykładowa deklaracja funkcji "strzałkowej" wygląda tak:</p>

{% highlight javascript %}
const sum = (a, b) => a + b
{% endhighlight %}

<p>Mógłbym tak jeszcze długo zanudzać o tym, co mi się spodobało bądź nie. Zamiast tego, zaprezentują może po prostu swoje dotychczasowe dokonania, czyli prostą aplikację. Na razie nic się w niej specjalnego nie dzieje. Mamy listę bibliotek JavaScriptowych, z wyszukiwarką oraz przycisk który książkę usuwa z listy. Jest to jednak kawałek kodu napisany własnie przy użyciu React.js. W kolejnym rozdziale kursu zaczynają się dziać rzeczy ciekawe, gdyż listę tą zapełnimy danymi udostępnianymi przez API serwisu HackerNews. A to zaczyna już coś przypominać. </p>

<p><a href="http://bananovitch.github.io/badgernews" target="_blank">Projekt można obejrzeć i przetestować tutaj.</a></p>

<p>Na marginesie tego dodam jeszcze czemu tak długo z tym postem zeszło. Wynika to z tego, że "zepsułem" w międzyczasie swój blog, i spędziłem dosłownie kilka dni na jego naprawianiu. Przyczyna tego jest prosta, jak to mówią niektyrzy: "lepiej jest wrogiem dobrego".</p>

<p>Zamiast standardowego WordPressa zdecydowałem się na silnik oferowany przez serwis Github, czyli Jekyll. Podstawowa różnica pomiędzy tymi dwoma silnikami jest taka, że Jekyll to narzędzie do budowania stron <i>statycznych</i>. W przeciwieństwie do WordPressa nie korzysta z bazy danych, a pisanie w nim polega na dodaniu nowego pliku z postem i w granie go na serwer.</p>

<p>Dotychczas korzystanie z niego było bardzo przyjemne. Jekyll napisany jest w Ruby, a składnia jest na tyle czysta i przejrzysta, że nawet bez jego znajomości mogłem stworzyć blog od zera. Wszystko co dotychczas mi się zamarzyło w blogu można było najczęściej osiągnąć jedną linijką kodu (no, nie do końca, ale na pewno zdecydowanie prościej niż w WordPressie. Do momentu, gdy stwierdziłem że trzeba przygotować blog na większą ilość postów, i dodać paginację.</p>

<p>Wtedy okazało się, że Jekyll sam z siebie nie obługuje tego, i konieczna jest instalacja pluginu "jekyll-paginate". Jednak próba instalacji tego pluginu lokalnie na moim komputerze nie powiodła się. Wyglądało na to, że jest konflikt w zainstalowanych bibliotekach. Usunięcie problematycznej paczki spowodowało że serwer przestał się w ogóle uruchamiać lokalnie. Prosta instalacja też się nie powiodła, więc stwierdziłem że przeinstaluję po prostu Ruby.</p>

<p>Wtedy okazało się że najnowsza wersja Ruby korzysta z inneg devkitu. Który niespecjalnie chciał mi się zainstalować pod Windowsem. 3 dni zajęło mi znalezienie problemu który uniemożliwiał mi instalację devkitu. W końcu, gdy to się powiodło, mogłem zainstalować paginację oraz wreszcie dodać ją na blog. No i mogłem w spokoju kontynuować naukę.</p>

<p>A wszystko zaczęło się tego, że chciałem zrobić sobie paginację na stronie.</p>
