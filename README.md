<div align="center">

# Algorithm practice

<p> with BOJ </p>

<br>

<h2> What language I used 📓 </h2>

<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/>

<p> but in BOJ, there is no JavaScript. Instead, I used Node.js </p>

<br>

[![Solved.ac프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=chaevivin)](https://solved.ac/chaevivin)

<br>
<br>
<br>

<h2> 파이썬 입력 </h2>

</div>

1. 숫자 한줄씩 입력받기

```py
import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
```

<br>

2. 한 줄에 여러 개 숫자 입력받기
```py
import sys

a,b,c = map(int,sys.stdin.readline().split())
```
- map() : map(f, iterable)은 반복 가능한(iterable) 데이터에 함수(f)를 적용해 결과를 리턴한다.
- split() : 문자열을 나눠주는 함수. 괄호 안에 특정 값을 넣어주면 그 값을 기준으로 나눈다. 빈 괄호이면 공백을 기준으로 나눈다.

<br>

3. 임의의 개수 숫자 한 줄에 입력받아 리스트에 저장하기
```py
import sys

a = list(map(int,sys.stdin.readline().split()))
```
- list() : 자료형을 리스트로 바꿔준다.

<br>

4. 문자열 n줄을 입력받아 리스트에 저장하기
```py
import sys

n = int(sys.stdin.readline())
a = [sys.stdin.readline().strip() for i in range(n)]
```
- strip() : 문자열 맨 앞과 맨 끝 공백을 제거한다.
