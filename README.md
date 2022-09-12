# CSVQL
Query csv from current working directory using sql.


https://user-images.githubusercontent.com/5214601/189738240-f2c385d7-bf42-4e53-870d-adf67d9248df.mp4


## dependencies
* poetry
* pandas
* duckdb

## development
This requires poetry for dependency management:
``` 
pip install poetry # install poetry 
```
If have poetry installed, clone repo, install deps.
```
git clone git@github.com:paulocesarcuneo/csvql.git

cd csvql

poetry install 
```

This is a silly script so no tests, try it out using poetry: 

```
poetry run python csvql.py -h
```

Or activate poetrys managed local venv

```
source .venv/bin/activate
./csvql.py
```

`

## release standalone exec

To build a standalone executable:
``` 
poetry run pyinstaller csvql.py --onefile

ls dist  # exec will be generated dist folder
```

## License 

Inherited from dependencies. No warranties given.
