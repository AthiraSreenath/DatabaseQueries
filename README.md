# DatabaseQueries

# Query a database using a natural language query

Most of us have been querying the databases using a query language, mostly SQL. 

In this project we see how the `large language models` and the `langchain` agents can provide a completely new, natural language based interface to the database.

## Setup

We will need the following:

* A relational database server, such as mysql https://www.mysql.com/

* Create a schema named `foodmart` in the database server.

* Uncompress and untar the script: `footmart_mysql.tar.gz` and use it to import the data into your `foodmart` schema.

```
mysql> use foodmart;
mysql> source foodmart_mysql.sql;
```

* Get the necessary libraries
```
pip install -r requirements.txt
```


## Getting started

We use the `sql-agent` from the `langchain`, and the `SqlDatabaseToolkit`.
"""