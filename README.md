# JWT秘钥爆破脚本

## 用法

```python
python3 -m pip install requirements.txt

usage: CrackJWT.py [-h] [-s JWT_STR] [-p KEYS] [-a ALGORITHM]

optional arguments:
  -h, --help            show this help message and exit
  -s JWT_STR, --str JWT_STR
                        input jwt code
  -p KEYS               input key's dir
  -a ALGORITHM          input encryption algorithm
```

## 示例

```
python3 -s eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJhdWQiOiJ3ZWJnb2F0Lm9yZyIsImlhdCI6MTY0OTU4NjA2NCwiZXhwIjoxNjQ5NTg2MTI0LCJzdWIiOiJ0b21Ad2ViZ29hdC5vcmciLCJ1c2VybmFtZSI6IlRvbSIsIkVtYWlsIjoidG9tQHdlYmdvYXQub3JnIiwiUm9sZSI6WyJNYW5hZ2VyIiwiUHJvamVjdCBBZG1pbmlzdHJhdG9yIl19.TTZNCltG31wMCmNB90dbdNF88G4Fr1EnCxrFbIQmih0 -p passwd.txt -a HS256
```
