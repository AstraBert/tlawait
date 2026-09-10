# tlawait

Python scripts executor that allows for top-level awaits.

## Installation

```bash
uv tool install tlawait
# or, from source
git clone https://github.com/AstraBert/tlawait
cd tlawait
uv tool install .
```

## Usage

Run a script with `tlawait`:

```bash
tlawait script.py
```

`tlawait` is designed to run standalone scripts that do not require passing CLI options (specifically tutorials translated from notebooks).

## License

`tlawait` is provided under [Apache 2.0](./LICENSE).
