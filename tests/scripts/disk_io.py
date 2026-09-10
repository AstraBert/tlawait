# ruff: noqa

import tempfile

import aiofiles

async with aiofiles.open("pyproject.toml", "r") as f:  # pyright: ignore
    content = await f.read()  # pyright: ignore

async with aiofiles.open(tempfile.NamedTemporaryFile(suffix=",txt").name, "w") as f:  # pyright: ignore
    await f.write("hello")  # pyright: ignore
