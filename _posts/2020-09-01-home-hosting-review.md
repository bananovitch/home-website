---
title: Domowa hostownia - recenzja po kilku miesiącach
date: 2020-09-01 10:33:00 +0200
cover: /img/piServer.jpg
categories: code
#description: Przez kilka miesięcy moja strona była udostępniana światu z małego komputerka Raspberry Pi stojącego w moim salonie za pośrednictwem domowego łącza internetowego. Po jakimś czasie jednak zrezygnowałem z tego rozwiązania. Postanowiłem opisać proces uruchomienia tej strony i swoje dotychczasowe wrażenia, udostępnić materiały, z których korzystałem oraz podać powody dla których zdecydowałem się jednak zrezygnować z tego przedsięwzięcia. Przynajmniej na jakiś czas, gdyż dalej uważam sam koncept za bardzo ciekawy.
---



Przez kilka miesięcy moja strona była udostępniana światu z małego komputerka Raspberry Pi stojącego w moim salonie za pośrednictwem domowego łącza internetowego. Po jakimś czasie jednak zrezygnowałem z tego rozwiązania. Postanowiłem opisać proces uruchomienia tej strony i swoje dotychczasowe wrażenia, udostępnić materiały, z których korzystałem oraz podać powody dla których zdecydowałem się jednak zrezygnować z tego przedsięwzięcia. Przynajmniej na jakiś czas, gdyż dalej uważam sam koncept za bardzo ciekawy.

<!--more-->

## Po co, na co?

Głównym powodem, który mnie skłonił do wypróbowania opcji domowego hostingu była chęć sprawdzenia, jak daleko jestem w stanie uniezależnić się od zewnętrznych dostawców, a dalej mieć możliwość udostępniania treści. Co poniekąd się udało, byłem w pełni niezależny. Z tą niezależnością jednak wiązała się pewna cena. Musiałem sam zadbać o to, by serwer działał nieprzerwanie, by aktualizować oprogramowanie, oraz, co okazało się moim głównem bólem głowy - by wszystko było w miarę bezpieczne.  

Myśl, że korporacja ma na mój temat bardzo dużo informacji nie jest nowa, przynajmniej dla mnie. Być może teraz to mi jeszcze nie zaszkodziło w niczym, ale kiedyś jednak może. Jaka jest jednak dla tego alternatywa? Dzielenie się swoimi przemyśleniami i przeżyciami z innymi _jest fajne_, to chyba coś bardzo ludzkiego. Problematyczne jest _sprzedawanie_ tych informacji. Dodatkowo, decyzja tej korporacji może mięć *bardzo duży* wpływ na sposób, w jaki komunikuję się z innymi. Not cool.

Co ciekawe jednak, kiedyś już można było się dzielić i pisać bez takich silnych obaw - w starym internecie, sprzed powstania miediów społecznościowych. Wtedy, kiedy istniały blogi i ręcznie tworzone strony, z całą ich różnorodnością i nierzadko ohydnym wyglądem. Tak też widziałbym alternatywę dla mediów społecznościowych: zdecentralizowana, rozproszona sieć nieokiełznanych stron. Dzięki temu mógłbym tworzyć głównie dla bliskich mi odbiorców, nie zaś bliżej nieokreślonych reklamodawców.s

## Jak?

### Hardware

Pierwszym krokiem był oczywiście zakup Raspberry Pi, który chciałem mieć już od dłuższego czasu. W końcu miałem wreszcie wymówkę. Nie była to jednak najtańsza impreza - komputer, karta pamięci, zasilacz, obudowa kosztowały mnie ok. 250 zł. Sporo jak na początek. Hostowanie strony u komercyjnego dostawcy jest znacznie tańsze. Korzystanie ze społecznościówek jest darmowe - płacimy jednak zgadzając się na przekazanie danych dostawcom reklam. Opłacalność pozostawiam ocenie osobom czytającym. 

### Serwer

Uruchomienie serwera okazało się być bajecznie proste. Moim pierwszym wyborem był Apache - standard. wystarczyło go zainstalować, oraz umieścić stronę w odpowiednim katalogu, i bum, można ją oglądać (przynajmniej w lokalnej sieci wi-fi). Ostatecznie zdecydowałem się jednak na korzystanie z nginx - głównie ze względu na prostotę konfiguracji, oraz fakt, że jest on również uznawany za standard w hostowniach. Po uruchomieniu go, skonfigurowałem jeszcze możliwość łączenia się z komputerem poprzez SSH. Oprócz tego ustawiłem też prosty firewall, aby zablokować niechciane połączenia, jeśli takowe by były.

### Konfiguracja domeny

Zanim udostępniłem swoją stronę na zewnątrz musiałem zrobić kilka rzeczy. Po pierwsze, komputer w mojej lokalnej sieci powinien mieć stały adres IP, tak aby router mógł do niego przekierować ruch. Po drugie, musiałem w routerze ustawić port forwarding, tak, aby do serwera mógł trafić ruch z zewnątrz. Wszystko okazało się dość proste do wyklikania w interfejsie mojego routera. 

Małe schody zaczęły się w momencie, w którym okazało się, że moje łącze, jak wiele przyłączy konsumenckich ma dynamiczny adres IP. Aby strona działała, do serwerów DNS na całym świecie musi zostać rozpropagowana informacja w której do mojego adresu strony (bananovitch.pl) przypisany jest adres IP. Dzięki temu po wpisaniu adresu w przeglądarkę widać moją stronę. Co w sytuacji, gdy adres ten ulega zmianie co jakiś czas? Wówczas rozwiązaniem jest DDNS - dynamiczny DNS. Dla mnie oznaczało to przede wszystkim konfiurację skryptu, który przy zmianie adresu IP wyśle o tym informację do dostawcy. Dostawcą DNS, na którego się zdecydowałem, to Cloudflare. Cloudflare posiada darmowy plan, w którym oprócz obsługi DDNS ma jeszcze kilka innych usług, głównie związanych z bezpieczeństwem. Całkiem nieźle. Narzędzie, które ostatecznie udało mi się skonfigurować to DDClient.

Po tych wszystkich przygodach, chciałem jeszcze dodać certyfikat SSL. Tak, aby w przeglądarce obok mojego adresu nie pojawiał się złowróżbny napis "Niezabezpieczona" tylko ładna kłódeczka. Pamiętam, że było z tym trochę zabawy, jednak ostatecznie udało mi się skonfigurować darmowy certyfikat od Let's Encrypt przy użyciu narzędzia zwanego Certbot. 

## Ruszyła Maszyna

Wszystko to kosztowało mnie _całkiem sporo_ pracy. Nie jest to zdecydowanie rozwiązanie dla każdego. Nie uważam to jednak za czas stracony. Nauczyłem się całkiem sporo na temat serwerów oraz czułem się już dość pewnie korzystając z terminalu Linuxa. Całkiem nieźle! 

Na swojej stronie nie dodałem (i nie zamierzam dodawać) skryptów śledzących w stylu Google Analytics. Dlatego też nie ma na niej ostrzeżenia o Cookies - nie korzystam z cookies w ogóle. Miałem jednak wgląd do logów serwerowych, więc miałem z grubsza pojęcie o ilości odwiedzin na swojej stronie, krajach z których pochodza odwiedzający, z jakich systemów i przeglądarek korzystają. Znalazłem bardzo fajne, darmowe narzędzie do przeglądania logów w terminalu - nazywa się GoAccess. Korzystając z niego, okazało się, że ...

### Bot jest u bram

... *znaczna* część ruchu na mojej stronie to boty. Było ich naprawdę dużo. Od kilkuset do kilku tysięcy w ciągu dnia, wszystkie robiące zautomatyzowane zapytania do nieistniejących stron. Szukały oczywistych dziur w moich zabezpieczeniach. Z racji tego, że moja strona to tylko statyczny html, nic złego się nie stało, jednak to przeświadczenie o tym, że te boty ciągle tam są nie dawało mi spokoju. Zainstalowałem więc na serwerze rozwiązanie o wdzięcznej nazwie Fail2Ban, które na podstawie logów systemowych blokuje dostęp do strony botom robiącym zapytania o nieistniejące strony. Dzięki temu udało mi się odsiać ich troche, ale jednak nie dość dużo. W dodatku, w trakcie tego konfigurowania musiałem tak ustalić limity zapytań, żeby prawdziwy użytkownik nie został zbanowany przez ten skrypt. Wtedy też zadałem sobie dość istotne pytanie:

## Czy to jest tego warte?

Nie jestem ekspertem od bezpieczeństwa serwerów internetowych (jeszcze :wink:). Brak pewności co do tego czy moja strona jest dostatecznie zabezpieczona (czy jakakolwiek jest?) oraz myśl, że _nie wiem, czego nie wiem_, sprawiła, że zdecydowałem się chwilę obecną skorzystać z komercyjnej hostowni. Nie oznacza to jednak, że nie wrócę do tematu - wręcz przeciwnie, zmotywowało mnie to do zgłębienia się w tematykę internetowego bezpieczeństwa. Póki jednak nie będę się czuł pewnie - dla świętego spokoju zostawię ochrone przed intruzami profesjonalistom. 

## Dalej chcesz mieć domową hostownię?

Jeśli tak, poniżej zostawiam kilka linków do materiałów, z których korzystałem przy ustawianiu swojego serwera. 
* [Manifest Homebrew Server Club - inspiracja](https://homebrewserver.club/)
* [Konfiguracja SSH w Raspberry Pi](https://www.raspberrypi.org/documentation/remote-access/ssh/README.md)
* [Ustawienia NGINX](https://medium.com/l0rd/how-to-host-a-nginx-website-with-raspberry-pi-ddos-protected-1a166e36cce)
* [Konfiguracja ddclient i Cloudflare](https://letswp.io/cloudflare-as-dynamic-dns-raspberry-pi/)
* [Konfiguracja certyfikatu SSL](https://pimylifeup.com/raspberry-pi-ssl-lets-encrypt/)
* [Fail2Ban](https://pimylifeup.com/raspberry-pi-fail2ban/)
* [GoAccess - program do przeglądania logów](https://goaccess.io/get-started)
