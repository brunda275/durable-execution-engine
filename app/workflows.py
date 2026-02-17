import asyncio
from app.engine import execute_step

async def step1():
    await asyncio.sleep(1)
    print("Step1 complete")
    return "ok1"

async def step2():
    await asyncio.sleep(2)
    print("Step2 complete")
    return "ok2"

async def step3():
    await asyncio.sleep(2)
    print("Step3 complete")
    return "ok3"

async def run_workflow():
    await execute_step("step1", step1)

    # parallel steps
    await asyncio.gather(
        execute_step("step2", step2),
        execute_step("step3", step3)
    )
