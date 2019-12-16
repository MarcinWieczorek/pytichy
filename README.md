# pytichy
Tichy API and command line tool

## Usage:
`$ ./tichy-cli.py <c|e|s> ...`

### Get course list
`$ ./tichy-cli.py c`
```
$ ./tichy-cli.py c
[0] Egzamin z ASD2 2018/2019                    (1dc03ecca13b40d8b732c218c74b1e5a)
[1] Algorytmy i Struktury Danych II - 2018/2019 (c809c8875a3b4661af251c9ee4c6470e)
[2] Egzamin z ASD1 2018/2019                    (663c794743e74b308da883fd87c448ae)
[3] Algorytmy i Struktury Danych I - 2018/2019  (6d04fea06d8849dca56e223e158c980c)
[4] Koło Algorytmiczne                          (c625db077a1445e78b34c9c39de4db0d)
```

### Get exercise list
`$ ./tichy-cli.py e <course>`
```
$ ./tichy-cli.py e 1
[ 1] Janusz biznesu                 (cbd1cd913d8846b5b3c81fd02233d3f5)
[ 2] Janusz biznesu II              (1faa0ad0857343faaaf99ec724b4b7cb)
[ 3] Organizacja zakupów            (4d6854e024d14cbf8ceedde3f0281fe1)
[ 4] Fachowcy                       (d958cb2b7c88428ab920e824296806e2)
[ 5] Poważny gracz                  (4c621835a3964d3d86af7144f9540f41)
[ 6] Klienci                        (b4e960baf2ea4f46859697f6bf1e72ec)
[ 7] Optymalizacja                  (7158cb68eebc46f49d17241abcbb1829)
[ 8] Lista przebojów                (eab1293a45ff4c20b6c610955be55681)
[ 9] Wyszukiwarka piosenek          (1b48518bd3af4a75b6418854eef1a860)
[10] Biblioteka                     (3cdb8e06ddac45d8b88e175881ac98a2)
[11] Kolizje                        (4b05b2402e3648a89982600abf2ee9a8)
[12] Ukryta sekwencja               (204a46a106b843c09a387cce5b2df34d)
[13] Gdzie jest Grażyna             (7780ccd7e760435c8e99c0a3c2c16d27)
[14] Ale upał                       (9f5948ae99d147c88ebdb5e2a8600a60)
[15] Kto ma gorzej?                 (6351fa7127b44e708569ddcbbda3e2ac)

```

### Send file
`$ ./tichy-cli.py s <course> <exercise> <file>`
```
$ ./tichy-cli.py s 4 0 test.cc
[1] Niesprawdzone Time: /0.2s,  Memory: /16384KB (94ec915df14f45ac861c56d2c5c6122a)
[2] Niesprawdzone Time: /0.2s,  Memory: /16384KB (b9dd8062c9a34564a547994ab5b95d90)
[3] Niesprawdzone Time: /0.2s,  Memory: /16384KB (f1b2858256be48dc98e4090bc271f112)
[4] Niesprawdzone Time: /0.2s,  Memory: /16384KB (30b1878b07434703a699e6acc5f7a131)
[5] Niesprawdzone Time: /0.2s,  Memory: /16384KB (0edd5270505f4bcb8bc6a2bef88113a3)
[6] Niesprawdzone Time: /0.2s,  Memory: /16384KB (aed4b2c331554272847831d9bf97f0b9)
[7] Niesprawdzone Time: /0.3s,  Memory: /16384KB (00f5088b53384964b78ec1f9dcb3ed7d)
[8] Niesprawdzone Time: /0.2s,  Memory: /16384KB (87c89b14423340b8948e3dae28228dc7)
[9] Niesprawdzone Time: /0.2s,  Memory: /16384KB (df89cf3168f84a6f9029fb2645b607cd)
[10] Niesprawdzone Time: /0.2s, Memory: /16384KB (475ba076abc74147ab2f5f9e79304276)
[11] Niesprawdzone Time: /0.2s, Memory: /16384KB (c4f0aeca3f3c439a9fad1a5d0dc47492)

```
