import sqlite3 as sl


def insertsignup(name, email, phone, password):
    sulist = [name, email, phone, password]

    con = sl.connect('slugs.db')
    c = con.cursor()

    # get the count of tables with the name
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='SUINFO' ''')

    # if the count is 1, then table exists
    if c.fetchone()[0] == 1:
        print('Table exists.')
    else:
        print('Table does not exist.')

        with con:  # table with all the different columns that will be used, and type of data
            con.execute("""               
                    CREATE TABLE SUINFO (
                        name TEXT,
                        email TEXT,
                        phone TEXT,
                        password TEXT,
                        );
                """)
    sql = 'INSERT INTO SUINFO (name, email, phone, password) values(?, ?, ?, ?)'
    with con:
        con.execute(sql, sulist)
    with con:
        data = con.execute("SELECT * FROM SUINFO")
    for row in data:
        print(row)

    return


def logincheck(name, email, phone, password):
    paramlst = []
    paramlst.append(name)
    con = sl.connect('slugs.db')
    c = con.cursor()

    sql = 'SELECT password FROM SUINFO WHERE mail_address=?'

    c.execute(sql, paramlst)
    stpw = c.fetchone()[0]
    if password == stpw:
        return ("yes")
    else:
        return ("no")
    return