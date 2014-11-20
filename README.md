# DerpibooruHashCollector

Runs a query on Derpibooru and stores all IDs and SHA512 hashs of all images in a SQL database.

## Requirements

* Python 2.7
* SQLite 3

## Usage

> DerpibooruHashCollector.py configfile

## Configuration

Example configuration:


```
{
    "key": "yourDerpibooruAPIKey",
    "dbname": "cuteImagesDB.db",
    "query": "cute"  
}
```