#!/usr/bin/env python

import json, urllib2, sqlite3, sys

def main():
    key = None
    dbname = None
    query = None

    if len(sys.argv) != 2:
        print "Usage: %s configfile" % sys.argv[0]
        return

    with open(sys.argv[1], "r") as file:
        j = json.loads(file.read())
        key = j["key"]
        dbname = j["dbname"]
        query = j["query"]

    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS db (Id int, Hash varchar(128))")

    page = 0
    
    while True:
        url = "https://derpiboo.ru/search.json?key={0}&q={1}&page={2}".format(key, query, page)
        response = urllib2.urlopen(url)
        j = json.loads(response.read().decode("utf-8"))
        images = j["search"]
        if images:
            for image in images:
                id = image["id_number"]
                hash = image["sha512_hash"]
                cur.execute("SELECT Hash FROM db WHERE id=?", (id, ))
                if cur.fetchone() is None:
                    print "Inserting {0}".format(id)
                    cur.execute("INSERT INTO db(Id, hash) VALUES(?,?)", (id, hash))
                    con.commit()
        page += 1 

if __name__ == "__main__":
        main()