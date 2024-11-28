# Machine Learing 

# .gitignore
```
# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv
uv.lock


# rust fmt
.ruff_cache

# General
.DS_Store
dir/otherdir/.DS_Store

```

<br>

<hr>


# How to leave/exit/deactivate a Python virtualenv

- https://stackoverflow.com/questions/990754/how-to-leave-exit-deactivate-a-python-virtualenv

- https://matplotlib.org/3.5.0/devel/development_setup.html#installing-for-devs



<hr>

# Next-gen Python tooling

https://astral.sh/

# matplotlib

- https://matplotlib.org/stable/tutorials/pyplot.html 

# ruff(python fmt, check)

- https://github.com/astral-sh/ruff

# conda대체 - GN⁺: Uv - 러스트로 구현한 초고속 파이썬 패키징 도구 (astral.sh)

- https://news.hada.io/topic?id=13388

  - https://astral.sh/blog/uv

- uv(conda보다 가벼운 패키지)

  - https://pypi.org/project/uv/

# 가상환경 만들기

```bash
 uv pip
```


- `uv pip install "numpy"` 필요한 패키지 설치하기


```bash
$ uv pip install "numpy"
Resolved 1 package in 34ms
Downloaded 1 package in 337ms
Installed 1 package in 8ms
 + numpy==1.26.4

my_project/Python_Lang/finance via 🐍 v3.9.6 (finance) 
$ uv pip install "pandas"
Resolved 6 packages in 80ms
Downloaded 5 packages in 345ms
Installed 5 packages in 23ms
 + pandas==2.2.1
 + python-dateutil==2.9.0.post0
 + pytz==2024.1
 + six==1.16.0
 + tzdata==2024.1


$ uv pip install "matplotlib"
Resolved 13 packages in 345ms
Downloaded 10 packages in 243ms
Installed 10 packages in 14ms
 + contourpy==1.2.0
 + cycler==0.12.1
 + fonttools==4.50.0
 + importlib-resources==6.3.2
 + kiwisolver==1.4.5
 + matplotlib==3.8.3
 + packaging==24.0
 + pillow==10.2.0
 + pyparsing==3.1.2
 + zipp==3.18.1

$ uv pip install "scipy"
Resolved 2 packages in 67ms
Downloaded 1 package in 635ms
Installed 1 package in 10ms
 + scipy==1.12.0
```



- `uv pip sync requirements.txt`

안에 패키지 버젼이랑 같이 넣어서 싱크해주기




```bash
$ uv pip sync requirements.txt 
Audited 17 packages in 4ms  

예시 requirements.txt



numpy==1.26.4
pandas==2.2.1
python-dateutil==2.9.0.post0
pytz==2024.1
six==1.16.0
tzdata==2024.1
contourpy==1.2.0
cycler==0.12.1
fonttools==4.50.0
importlib-resources==6.3.2
kiwisolver==1.4.5
matplotlib==3.8.3
packaging==24.0
pillow==10.2.0
pyparsing==3.1.2
zipp==3.18.1
scipy==1.12.0
```


# 개인용 ChatGPT만들기 100% private

- Private Q&A and summarization of documents+images or chat with local GPT, 100% private, Apache 2.0. Supports LLaMa2, llama.cpp, and more. Demo: https://gpt.h2o.ai/

https://github.com/h2oai/h2ogpt


<hr>

<hr>

<br>


# tensorflow_deep

<br>

# StableLM: Stability AI Language Models(LM)

https://github.com/stability-AI/stableLM/

# C언어로 신경망구현하기-Building a neural network FROM SCRATCH (no Tensorflow/Pytorch, just numpy & math)

https://youtu.be/w8yWXqWQYmU

<hr>

# 머신러닝+딥러닝 책 보는 순서-총 정리!!(Book-RoadMap)

https://economiceco.tistory.com/11818

![KakaoTalk_20230305_143811173](https://user-images.githubusercontent.com/67513038/225540880-d4d870d2-1221-4a46-b09c-b5d9aa63b3af.png)
![img](https://user-images.githubusercontent.com/67513038/225540886-69f18b72-aade-440f-a929-2bfc2fd5cd82.jpg)

# 무료로 머신러닝 배우기(코딩야학)

https://coding.yah.ac/

https://opentutorials.org/course/4547

# NLP 101: 딥러닝과 자연어 처리 학습을 위한 자료 저장소

https://github.com/Huffon/NLP101/blob/master/README_KR.md

<hr>

<br>

# ♥︎Anaconda주로 사용하는 명령어 총 정리

https://economiceco.tistory.com/11830

<br>

<hr>

<hr>

# 파이썬의 정석(파이썬 기초의 모든것 ) - 프로그램 동산 

- 1강에서 4강까지 파이썬의 정석, 딕셔너리 한방에 끝내기

https://youtu.be/g320D427-cY

<br>

- 시리즈 모아 보기

https://youtube.com/playlist?list=PLDtzZPtOGenaG_LeSAHpr4opgz0HebcwJ

<br>

<hr>


<br>

# Python for Beginners – Full Course [Programming Tutorial]

https://youtu.be/eWRfhZUzrAc


<br>

<hr>

# python Debugging

- 한글파이썬Python강의_001⭐️Python개발환경_디버깅기초_AstroVim세팅Debugging_Vim_macOS_M1_pro #debugging #Astrovim


macOS만 가능한듯요 ㅠㅠ

<br>

https://youtu.be/waPzGgZAyZU

<br>

<hr>

<br>

# 파이썬 텐서플로우 & 머신러닝 기초 강좌 (TensorFlow Machine

https://youtube.com/playlist?list=PLRx0vPvlEmdAbnmLH9yh03cw9UQU_o7PO

<br>

<hr>

# CNN영상에 주로 사용 / RNN 글씨 문자에 사용

https://ebbnflow.tistory.com/119

# Tensorflow.blog 텐서플로우 블로그

https://tensorflow.blog/

# 딥러닝 기초를 위한 선형대수학

https://ko.khanacademy.org/math/linear-algebra

# 딥러닝 기초eBook& 행렬기초

https://atcold.github.io/pytorch-Deep-Learning/ko/
