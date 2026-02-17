from app.db import get_conn
import asyncio

def log_step(step, status, result=""):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO workflow_runs(step_name,status,result) VALUES(?,?,?)",
        (step, status, result),
    )
    conn.commit()
    conn.close()

def is_completed(step):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM workflow_runs WHERE step_name=? AND status='done'",
        (step,),
    )
    data = cur.fetchone()
    conn.close()
    return data is not None

async def execute_step(name, func):
    if is_completed(name):
        print(f"Skipping {name}, already done")
        return

    try:
        log_step(name, "running")
        result = await func()
        log_step(name, "done", str(result))
    except Exception as e:
        log_step(name, "failed", str(e))
        raise
