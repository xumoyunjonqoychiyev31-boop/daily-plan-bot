import aiosqlite

DB_NAME = "database.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            full_name TEXT,
            username TEXT,
            joined_at TEXT
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS plans(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            plan_date TEXT,
            plan_time TEXT,
            status TEXT DEFAULT 'pending'
        )
        """)

        await db.commit()
        from datetime import datetime

async def add_user(user_id, full_name, username):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        INSERT OR IGNORE INTO users(user_id, full_name, username, joined_at)
        VALUES (?, ?, ?, ?)
        """, (
            user_id,
            full_name,
            username,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))
        await db.commit()


async def user_exists(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT user_id FROM users WHERE user_id=?",
            (user_id,)
        )
        return await cursor.fetchone()
