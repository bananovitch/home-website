---
title: Bardzo trudne "Hello World"
layout: post
excerpt: "Na tym etapie zaczynam poważnie wątpić w sens całego przedsięwzięcia i rozważam porzucenie. A to dopiero pierwszy dzień!"
comments: true
categories: code
#cover: "/img/posts/2017/code-cover.jpg"
#alt: "code"
---




<p>Aby móc cokolwiek napisać musiałem zaoznać się z podstawami tworzenia pluginów VST. Zacząłem oczywiście standardowo od wyszukiwarki google. Tam też wpisałem nurtujące mnie pytanie, czyli "how to write VST plugins".</p>

<p>W ten sposób trafiłem na pierwszą z brzegu instrukcję jak zrobić to krok po kroku. To już coś!</p>

<p>Zanim jednak cokolwiek zacznę pisać, musze mieć jak to robić, a więc musimy sobie stworzyć środowisko programistyczne. W pierwszej kolejności zdecydowałem się na Visual Studio Code (nigdy nie używałem, a słyszałem pochlebne opinie). Nie mam zielonego pojęcia czy cokolwiek uda się odpalić. Szybko jednak przekonuję się, że to kompletnie nie to, o co mi chodzi i konieczna będzie instalacja Visual Studio Community Edition.</p>

<p>W dalszej kolejności będziemy potrzebować biblioteki WDL-OL. Zgodnie z tym co jest napisane na wyżej wymienionej stronie jest to narzędzie który pozwoli mi tworzyć plugin, a następnie skompilować go do różnych formatów. Czyli, jeżeli dobrze to rozumiem, dzięki tej biblioteki że piszę raz, a nastepnie mogę swój plugin odpalić na Macu i Windowsie, oraz nie muszę przejmować się niskopoziomowymi rzeczami. Brzmi jak dokładnie to, czego potrzebuję. Klonuję zatem repozytorium do folderu z syntezatorem.</p>

<p>Uh oh. Gdzie są te wszystkie pliki o których mowa w tutorialu?</p>

<p>Pobieram brakujące paczki ASIO SDK oraz VST3 SDK. Hm. czemu lista plików nie zgadza się z tym co jest w tutorialu? Zapewne dlatego, że tutorial był pisany kilka lat temu, a od tego czasu wiele mogło się zmienić. No nic, próbujemy dalej pomimo tego. Ponadto na oficjalnej stronie nie ma paczki z SDK VST2.. zapewne dlatego że ten standard również wyszedł z użycia. OK. </p>



<p>Korzystając z magicznego skryptu w Pythonie tworzę swój pierwszy plugin, co działa mniej więcej jak zaawansowana wersja "kopiuj wklej".</p>

<p>Jak na razie idę jak burza. Kolejnym krokiem będzie otworzenie pliku MyFirstPlugin.slp, który powinien załadować projekt do Visual Studio. Oczywiście nic takiego się nie dzieje. Pojawia się jednak informacja, żebym zainstalował rozszerzenie C# do mojego edytora, co też czynię. Oj, wygląda na to że nie mogę skompilować i odpalić projektu tak ja w tutorialu, który korzysta z normalnej werjsi Visual Studio.</p>

<p>No tak, nie zainstalowałem Visual C++, co było napisane w dziale "What you'll need". :) Pobieram zatem darmowe Visual Studio Community Edition oraz je instaluję.</p>

<h2>"Trochę" później</h2>

![My helpful screenshot]({{ site.url }}/img/posts/fail.png)

<p>Przekonałem się na własnej skórze, że to co inni mówią o instalacji Visual Studio to prawda. Zajęła mi ona dobre 6 godzin.</p>

<p>W bólach porodowych zainstalowałem VS, uruchomiłem projekt, zgodnie z instrukcją powinien odpalić się sam bez żadnej mojej ingerencji..</p>


<p>Ależ oczywiście, nie odpalił się. Na tym etapie zaczynam poważnie wątpić w sens całego przedsięwzięcia i rozważam porzucenie. A to dopiero pierwszy dzień!</p>

<p>Bez paniki, Visual Studio proponuje abym wykonał "retarget solution", co też czynię. O dziwo operacja wykonuje się bez błędu. Hmm, tym razem build wysypuje się, twierdząc brakuje jakichś plików. Skąd ja znam taką sytuację. Naprawiam jeden błąd żeby przejść do drugiego. Wygląda na to, że to co próbuję teraz zrobić jest dość skomplikowanym pluginem działającym na wielu platformach, więc może poszukać czegoś naprawdę prostego?</p>

<p>Okej, poszukajmy czegoś innego. Może sam WDL? Wszystko pięknie, ale wygląda na to, że jest to robione pod VST w wersji 2.x, która już przestała być rozwijana przez Steinberg. MAMY PROBLEM.</p>

<p>Szybkie googlanie wskazuje jednak, że wszystkie pliki potrzebne du zbudowania pluginu znajdują się w nowej wersji biblioteki. OK, przenoszę ję zgodnie z instrukcją, kopiuję, klikam "Build" i.... DZIAŁA!</p>

![My helpful screenshot]({{ site.url }}/img/posts/HelloWorld.png)

<p>Odpalam Abletona. Oto moim oczom ukazuje się przykładowy plugin. Hello World. COŚ WIDAĆ. Nareszcie. Po tych wszystkich zmaganiach, udało mi się stworzyć plugin. Widać pokrętełko, jakieś mierniki. Wszystko piękne i oldschoolowe. Odetchnąłem z ulgą. Nie jest to szczyt marzeń, właściwie nic nie napisałem samemu, ale skonfigurowałem środowisko i uruchomiłem cokolwiek. Całkiem sporo jak na jeden dzień!</p>

<p>A teraz jak sprawić, żeby plugin wydał z siebie dźwięk?</p>



