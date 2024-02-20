def test_add_record(cursor):
    data = [('Monty Python and the Holy Grail', 1975, 8.2), ('And Now for Something Completely Different', 1971, 7.5)]

    cursor.execute("""
        INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
        """)

    res = cursor.execute("SELECT * FROM movie")
    assert res.fetchall() == data


def test_delete_record(cursor):
    data = [('And Now for Something Completely Different', 1971, 7.5)]

    cursor.execute("""
        INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
        """)

    cursor.execute("DELETE FROM movie WHERE year=1975")
    res = cursor.execute("SELECT * FROM movie")
    assert res.fetchall() == data


