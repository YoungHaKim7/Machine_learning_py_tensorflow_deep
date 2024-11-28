# 자동 정렬(ruff) - 러스트로 만든 python formatter 굿

```
$ ruff format hello.py
1 file reformatted
  
```

# Result

```bash
# uv run hello.py

/home/g/pandas_py01/.venv/lib/python3
.10/site-packages/numpy/_core/getlimits.py:548: UserWarning: Signature b'\x00\xd0\xcc\xcc\xcc\xcc\xcc\xcc\xfb\xbf\x00\x00\x00\x00\x00\x00' for <class 'numpy.longdouble'> does not match any known type: falling back to type probe function.
This warnings indicates broken support for the dtype!

  machar = _get_machar(dtype)
    Name  Age    Country
0   John   28        USA
1   Anna   24         UK
2  Peter   35  Australia
3  Linda   32    Germany
    Name  Age    Country      City
0   John   28        USA  New York
1   Anna   24         UK    London
2  Peter   35  Australia    Sydney
3  Linda   32    Germany    Berlin
    Name  Age    Country    City
2  Peter   35  Australia  Sydney
3  Linda   32    Germany  Berlin
Country
Australia    35.0
Germany      32.0
UK           24.0
USA          28.0
Name: Age, dtype: float64
```



```
$ uv tree
Resolved 7 packages in 1ms
pandas-py01 v0.1.0
├── numpy v2.1.3
├── pandas v2.2.3
│   ├── numpy v2.1.3
│   ├── python-dateutil v2.9.0.post0
│   │   └── six v1.16.0
│   ├── pytz v2024.2
│   └── tzdata v2024.2
├── python-dateutil v2.9.0.post0 (*)
├── pytz v2024.2
├── six v1.16.0
└── tzdata v2024.2
(*) Package tree already displayed
```
