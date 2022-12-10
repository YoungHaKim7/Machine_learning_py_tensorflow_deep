# Machine_Learning tutorial

-  TensorFow 2.0 Beginner Tutorials

https://youtube.com/playlist?list=PLhhyoLH6IjfxVOdVC1P1L5z5azs0XjMsb

- TensorFlow Tutorial 1 - Installation and Setup Deep Learning Environment (Anaconda and PyCharm)

https://youtu.be/5Ym-dOS9ssA

<hr>

- TensorFlow 2.0 전체 과정 - 초보자를 위한 Python 신경망 튜토리얼

https://youtu.be/tPYj3fFJGjk

<br>

<hr>

<br>

<hr>

#  Anaconada 기초 


https://www.anaconda.com/products/distribution#Links


#  Anaconda 주로 사용하는 명령어 정리 

- miniforge3설치가 끝나고 가상환경을 만든다.
이름은 tf25로 함

```
conda create --name tf25 python=3.8
```

- 가상 환경이 생성되고 activate로 환경 전환

```
conda activate tf25
```

- abc Project라는 이름의 env를 생성 파이썬 버전 3.8로 설정합니다.

```
conda env create -n abcProject python=3.8
```



- abcProject라는 이름의 Env를 삭제합니다

```
conda env remove -n abcProject
```


- Env 목록 확인

```
conda env list



# 또는 

conda info --envs




# 현재 가상환경을 더 자세히 알고 싶으면


conda info


```





- conda 활성화, 비활성화

```
conda activate base


비활성화
conda deactivate

```




- Anaconda 패키지 검색

```
conda search tensorflow

```

- Anaconda 패키지 설치

```
conda install tensorflow-gpu

```


- 가상환경 abcProject들어가서 가상환경에 설치된 패키지 확인하기

```
conda activate abcProject

들어가서 

conda list


하면 설치된 패키지가 쭉 나옴.



conda deactivate


하면 가상환경 빠져나옴.
```


- conda 터미널에서 자동 활동화 되는거 false로 만들기

```
(base) conda config --set auto_activate_base false

```


- anaconda 최신버젼으로 업그레이드 하기

https://docs.anaconda.com/anaconda/install/update-version/

<br>

https://economiceco.tistory.com/11830

<br>

<hr>


# Matplotlib Crash Course

https://youtu.be/3Xc3CA655Y4



