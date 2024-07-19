#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times with the specified max_delay
    and returns the list of all the delays (float values)."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
