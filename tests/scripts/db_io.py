# ruff: noqa

import aiosqlite

async with aiosqlite.connect(":memory:") as db:  # pyright: ignore
    await db.execute("CREATE TABLE test (id INT, name TEXT)")  # pyright: ignore
    await db.execute("INSERT INTO test VALUES (1, 'Alice')")  # pyright: ignore
    await db.commit()  # pyright: ignore

    async with db.execute("SELECT * FROM test") as cursor:  # pyright: ignore
        async for row in cursor:  # pyright: ignore
            print(row)
