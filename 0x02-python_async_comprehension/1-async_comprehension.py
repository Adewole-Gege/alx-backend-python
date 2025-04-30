#!/usr/bin/env python3
"""Coroutine that collects 10 random numbers from an async generator."""

from typing import List
from 0-async_generator import async_generator  # Import the coroutine

async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from async_generator using async comprehension."""
    return [i async for i in async_generator()]
