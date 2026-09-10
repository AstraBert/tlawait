# ruff: noqa

import httpx

async with httpx.AsyncClient() as client:  # pyright: ignore
    await client.get("https://example.com/")  # pyright: ignore
