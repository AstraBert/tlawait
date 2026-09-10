import ast
import asyncio
import sys


def run_script_with_top_level_await(path: str) -> None:
    with open(path) as f:
        source = f.read()

    flags = ast.PyCF_ALLOW_TOP_LEVEL_AWAIT
    code = compile(source, path, "exec", flags=flags)

    async def runner():
        global_ns = {"__name__": "__main__"}
        result = eval(code, global_ns)
        if result is not None:
            # top-level await produces a coroutine to await
            await result

    asyncio.run(runner())


def main() -> None:
    run_script_with_top_level_await(sys.argv[1])
