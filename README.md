# pytichy
Tichy API and command line tool

## Usage:
```
$ ./tichy-cli.py CMD [OPTIONS] ...
  CMD:
    course - course commands
    exercise - exercise commands
    send - send submission
  OPTIONS:
    --course/-c   - course index
    --list/-l     - list items
    --exercise/-e - exercise index
```

### Get course list
`$ ./tichy-cli.py course -l`
```
$ ./tichy-cli.py course -l
[0] Egzamin z ASD2 2018/2019
[1] Algorytmy i Struktury Danych II - 2018/2019
[2] Egzamin z ASD1 2018/2019
[3] Algorytmy i Struktury Danych I - 2018/2019
[4] Koło Algorytmiczne
```

### Get exercise list
`$ ./tichy-cli.py exercise --list --course=<course>`
```
$ ./tichy-cli.py exercise -l -c 1
[ 1] Janusz biznesu
[ 2] Janusz biznesu II
[ 3] Organizacja zakupów
[ 4] Fachowcy
[ 5] Poważny gracz
[ 6] Klienci
[ 7] Optymalizacja
[ 8] Lista przebojów
[ 9] Wyszukiwarka piosenek
[10] Biblioteka
[11] Kolizje
[12] Ukryta sekwencja
[13] Gdzie jest Grażyna
[14] Ale upał
[15] Kto ma gorzej?
```

### Send submission
`$ ./tichy-cli.py send --course=<course> -exercise=<exercise> <file>`
```
$ ./tichy-cli.py s -c 4 -e 0 test.cc
Waiting for results...
Date: None
Result: None
Points: 0.00

Id | Result         | Time (s)    | Memory (kB)
 0 | Zła odpowiedź  | 0.00 / 0.2  | 1036 / 16384
 1 | Zła odpowiedź  | 0.00 / 0.2  | 1036 / 16384
 2 | Zła odpowiedź  | 0.00 / 0.2  | 1036 / 16384
 3 | Zła odpowiedź  | 0.00 / 0.2  | 1036 / 16384
 4 | Zła odpowiedź  | 0.00 / 0.2  | 1036 / 16384
 5 | Zła odpowiedź  | 0.00 / 0.2  | 1036 / 16384
 6 | Zła odpowiedź  | 0.00 / 0.3  | 1036 / 16384
 7 | Zła odpowiedź  | 0.00 / 0.2  | 1036 / 16384
 8 | Zła odpowiedź  | 0.00 / 0.2  | 1036 / 16384
 9 | Zła odpowiedź  | 0.00 / 0.2  | 1036 / 16384
10 | Zła odpowiedź  | 0.00 / 0.2  | 1036 / 16384
```
