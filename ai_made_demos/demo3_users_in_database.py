"""Demo 3: the '5 million users' problem with a real database (sqlite).
Average age of all users, done three ways. We measure peak Python memory for each."""
import os
import sqlite3
import tracemalloc

DB = "users_demo.db"
N = 500_000  # 500k here; scale the numbers by 10 to imagine 5M

if os.path.exists(DB):
    os.remove(DB)
conn = sqlite3.connect(DB)
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, city TEXT)")
conn.executemany(
    "INSERT INTO users (name, age, city) VALUES (?, ?, ?)",
    ((f"user{i}", 18 + i % 60, "bwn") for i in range(N)),
)
conn.commit()
print(f"database has {N:,} users, file size {os.path.getsize(DB) / 1e6:.1f} MB on DISK\n")


def measure(label, fn):
    tracemalloc.start()
    result = fn()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"{label:<34} average={result:.3f}   peak Python RAM={peak / 1e6:8.1f} MB")


def load_everything():
    """BAD at scale: every row becomes Python objects in one big list."""
    users = conn.execute("SELECT id, name, age, city FROM users").fetchall()
    return sum(u[2] for u in users) / len(users)


def batches():
    """GOOD: stream a small batch at a time, then throw it away."""
    total = count = 0
    cur = conn.execute("SELECT age FROM users")
    while True:
        batch = cur.fetchmany(10_000)
        if not batch:
            break
        total += sum(row[0] for row in batch)
        count += len(batch)
    return total / count


def let_database_do_it():
    """BEST here: the database computes it, Python receives ONE number."""
    return conn.execute("SELECT AVG(age) FROM users").fetchone()[0]


measure("1. fetchall() into a list", load_everything)
measure("2. batches of 10,000 (streaming)", batches)
measure("3. SELECT AVG(age) in the database", let_database_do_it)

conn.close()
os.remove(DB)
