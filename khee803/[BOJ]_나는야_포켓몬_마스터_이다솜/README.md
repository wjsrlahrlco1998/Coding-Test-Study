# [BOJ] 나는야 포켓몬 마스터 이다솜 - 1620 (Silver IV)

[문제링크](https://www.acmicpc.net/problem/1620)

## 1. 문제 설명
### 1.1 문제요약

- 첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N과 맞춰야 하는 문제의 개수 M이 주어진다. N과 M은 1보다 크거나 같고, 100,000 보다 작거나 같은 자연수이다.
- 둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한줄에 하나씩 입력으로 들어온다. 포켓몬의 이름은 모두 영어로만 이루어져있고 이름의 최대 길이는 20, 최소 길이는 2다.
- 그 다음 줄부터 총 M개의 줄에 맞춰야 하는 문제가 입력으로 들어온다. 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 숫자로만 들어오면 포켓몬 번호에 해당하는 문자를 출력한다. 입력으로 들어오는 숫자는 반드시 1보다 크거나 같고, N보다 작거나 같고, 입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름으로만 주어진다.

### 1.2 입출력 예시

- 입력

  ```python
  26 5
  Bulbasaur
  Ivysaur
  Venusaur
  Charmander
  Charmeleon
  Charizard
  Squirtle
  Wartortle
  Blastoise
  Caterpie
  Metapod
  Butterfree
  Weedle
  Kakuna
  Beedrill
  Pidgey
  Pidgeotto
  Pidgeot
  Rattata
  Raticate
  Spearow
  Fearow
  Ekans
  Arbok
  Pikachu
  Raichu
  25
  Raichu
  3
  Pidgey
  Kakuna
  ```

- 출력

  ```python
  Pikachu
  26
  Venusaur
  16
  14
  ```

## 2. 문제해결 아이디어
- 딕셔너리에서 value를 이용해 key를 찾아내고싶어서 `{v:k for k,v in dic.items()}` 로 딕셔너리의 key, value를 뒤집은 딕셔너리를 추가로 만들어 사용했다.
- isdigit() : 어떤 문자열이 숫자의 형태면 True를 반환