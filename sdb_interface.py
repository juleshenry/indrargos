from surrealdb import Surreal
import datetime


async def main(hl_dict):
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use("dev_v1", "headlines")  # namespace, database
        await db.query(query_bulk_insert_dict_list(hl_dict))
        print("RESULT")
        print(
            await db.query(
                """
        select * from headlines
        """
            )
        )


def query_bulk_insert_dict_list(dl):
    q = f"""
            INSERT INTO test_it [
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
        test_main(
            [
                {
                    "headline": hl,
                    "country": "Nigeria",
                    "date_time": str(datetime.datetime.now(datetime.timezone.utc)),
                }
                for hl in headlines
            ]
        )
    )
