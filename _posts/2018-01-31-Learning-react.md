---
title: A więc chcesz poznać React.js?
layout: post
excerpt: "Początek roku był bardzo pracowity. Ale nawet udalo mi się zaczać uczyć. To już coś!"
comments: true
categories: code
---

<p>No tak, minął miesiąc i już po postanowieniu noworocznym :)</p>

<p>Postanowiłem nauczyć się React.js. Co teraz? </p>

<p>Niby nic trudnego. Zacząłem od szybkiego wyszukiwania przy użyciu Google, jednak szybko okazało się że nie tędy droga. Przez ostatnie 1,5 roku w świecie front-endu wydarzyło się bardzo dużo. Przyznam się bez bicia, że troche nie trzymałem ręki na pulsie, przez co teraz nie za bardzo wiem jak to ugryźć.</p>

<p>Zacznijmy od tego, że zmienił się sam JavaScript. Nowa wersja zwie się ECMAScript 6 i jest najnowsza oficjalną specyfikacją. Środowisko React.js z moim obserwacji bardzo chętnie pisze w tej nowej specyfikacji. </p>

<p>Nie było by w tym nic nie zwykłego, lecz przeglądarki nie do końca radzą sobie z nowinkami składniowymi. Aby temu zaradzić potrzebny jest <em>transpiler	</em>, który tłumaczy ECMAScript 6 na zrozumiały dla większości przeglądarek ECMAScript 5. Z moich obserwacji wynika że standardem stał się tutaj Babel. Do jego funkcjonowania potrzebne jest node.js oraz npm, które również w jakiś sposób trzeba znać. </p>

<p>To już dwie rzeczy, które muszę nadrobić, a jeszcze nie przeszliśmy do właściwej nauki biblioteki!</p>

<p>Przejdźmy do samego React.js. Znajomość biblioteki to jedno, natomiast sam React korzysta również z czegoś, co zwie się JSX. Dzięki temu możemy operować w JavaScripcie znacznikami HTML i przekazywać je w sposób podobny do obiektu. Wszystko po to, by w łatwy sposób tworzyć podstawowe "klocki" aplikacji webowej, czyli tzw. komponenty.</p>

<p>Tyle o filozofii React.js, przejdźmy teraz do samej nauki. Otóż ekosystem JavaScriptowy zbudowany jest w oparciu o szereg narzędzi typu Open Source. Jedne narzędzia dobrze działają z innymi, inne gorzej. Każde z tych narzędzi rozwija się swoim tempem. Wersje zmieniają się bardzo szybko, co dla uczącego się oznacza mniej więcej tyle, że nawet kilkumiesięczny kurs może okazać się nieaktualny z powodu wyjścia nowej wersji np. node.js albo npm. To oznacza dużo kombinowania.</p>

<p>Mamy kilka narzędzi na raz do opanowania, składnia jest nieco inna, w dodatku ekosystem JavaScriptowy ciągle ewoluuje i nierzadko trzeba samemu dojść czemu kod z danego artykułu po prostu nie działa.</p>

<p>No i co mam począć ja, biedny klepacz HTML i CSS i prostych skryptów przeglądarkowych? </p>

<p>Na szczęście udało mi się znaleźć kurs, który zdaje się odpowiadać na wszystkie moje bolączki. Jest nim książka <a href="https://leanpub.com/the-road-to-learn-react" target="_blank">"The road to learn React" autorstwa Robina Wierucha.</a> Nie chcę żeby to wyglądało za bardzo na reklamę, ale jestem z niego jak na razie niesamowicie zadowolony. Jest na bieżąco uaktualniany (przez miesiąc od momentu mojego pierwszego z nim spotkania wyszła już nowa wersja), przedstawiając podstawy React.js powoli wprowadza w nową składnię JavaScript. Problemy instalacyjne rozwiązane są przez skorzystanie ze wspaniałego narzędzia create-react-app, czyli takiego gotowego projektu który możemy sobie samemu odpalić i pozmieniać. Miód malina. Jakby tego było mało - podręcznik można mieć za darmo! Płacimy tyle, ile chcemu. Polecam serdecznie.</p>

<p>W celu lepszego poznania tejże biblioteki tworzę obecnie aplikację będącą kopią popularnego wśród programistów i nie tylko <a href="https://news.ycombinator.com/">Hacker News</a>. Repozytorium znajduje się obecnie <a href="https://github.com/bananovitch/badger-news" target="_blank">tutaj</a>.</p>
