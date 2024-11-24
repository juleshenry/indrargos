from surrealdb import Surreal
import datetime

async def delete_data():
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use((ns:="dev_v1"), (db_name:="headlines")) 
        await db.delete(db_name)

async def insert_data(hl_dict):
    # fmt: off
    hl_dict=[{oo.replace(r'\u',''):ooo for oo,ooo in o.items()}for o in hl_dict]
    # fmt: on
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use((ns:="dev_v1"), (db_name:="headlines"))  # namespace, database
        print(await db.query(make_bulk_insert_statement(hl_dict, db_name)))

async def query_data():
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use((ns:="dev_v1"), (db_name:="headlines"))  # namespace, database
        print("RESULT")
        print(
            await db.query(
                f"""
        select * from {db_name};
        """
            )
        )

def make_bulk_insert_statement(dl, db_name):
    assert type(dl) == list
    for d in dl:
        assert type(d) == dict

    q = f"""
            INSERT INTO {db_name} [
            {'\n'.join(map(lambda x:str(x)+',',dl))}
            ];
            """
    return q

async def test_main(hl_dict):
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use("test", "test_it")  # namespace, database
        await db.query(query_bulk_insert_dict_list(hl_dict))
        print(
            await db.query(
                """
        select * from test_it
        """
            )
        )

if __name__ == "__main__":
    import asyncio
    headlines = [f"Headline {i}" for i in range(10)]
    asyncio.run(
        delete_data()
    )
