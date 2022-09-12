# CSVQL
Query csv from current working directory using sql.

## dependencies
* pandas
* duckdb

## development

``` 
pip install poetry # install poetry 

git clone git@github.com:paulocesarcuneo/csvql.git

cd csvql

poetry install 

poetry run python csvql.py -h

```

## release standalone exec

To build a standalone executable:
``` 
poetry run pytinstaller csvql.py --onefile

ls dist  # exec will be generated dist folder
```

## License 

Inherited from dependencies. No warranties given.
