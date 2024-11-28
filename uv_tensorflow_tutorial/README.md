# uv(Conda보다 압도적으로 빠름) rust로 만듬
- https://github.com/astral-sh/uv

- python fomatter(러스트로 만든 파이썬 formatter 겁나 빠름)
  - An extremely fast Python linter and code formatter, written in Rust. 
  - https://github.com/astral-sh/ruff

# install

- 1. Rust 를 Install한다.

- 2. Rust 를 이용한 Install

```
cargo install --git https://github.com/astral-sh/uv uv  
```

- 3. Path확인

- `.cargo/bin` 에 잘 설치 되었는지 확인 `.cargo/bin`이 path가 잘 되었는지 확인

```
echo $PATH  
```

- 4. update

```
uv self update  
```

# tutorial(uv)

- https://docs.astral.sh/uv/getting-started/

- uv help

```bash
uv --help
```

# .gitignore
```
# A collection of useful .gitignore templates 
# https://github.com/github/gitignore
# General
.DS_Store
dir/otherdir/.DS_Store
.venv/

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
