#!/usr/bin/env python
# vim: set et ts=4 sw=4 tw=0 fdm=syntax fileencoding=iso-8859-1:

import sqlite

def printall(db, table='test'):
    """Funcion que imprime todos los elementos de una tabla de sqlite.
    """
    dbh = sqlite.connect(db)
    dbr = dbh.cursor()
    dbr.execute('SELECT * FROM ' + table)
    for row in dbr.fetchall():
        for k, v in row: print k, '=', v

