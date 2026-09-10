# tlawait

Python scripts executor that allows for top-level awaits.

## Installation

```bash
# add it as a dependency in your virtual environment
uv pip install tlawait
uv add --dev tlawait
# or, from source
git clone https://github.com/AstraBert/tlawait
cd tlawait
uv tool install .
```

## Usage

Run a script with `tlawait`:

```bash
uv run tlawait script.py
```

`tlawait` is designed to run standalone scripts that do not require passing CLI options (specifically tutorials translated from notebooks).

## License

`tlawait` is provided under [Apache 2.0](./LICENSE).
