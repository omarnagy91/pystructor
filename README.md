# pystructor

This is a simple Python console tool that creates a directory structure and files from a json file.

## Usage

```commandline
python src/main.py <json_file> <output_dir>
```

Where:
- `json_file` is the path to the json file containing the directory structure
- `output_dir` is the path to the output directory where the structure will be created

## Example

```json
{
    "my_project": {
        "README.md": "",
        "LICENSE": "",
        "src": {
            "main.py": ""
        },
        "tests": {
            "test_main.py": ""
        },
        "requirements.txt": "",
        ".gitignore": ""
    }
}
```

The above json file will create a directory structure like this:

```
my_project/
    README.md
    LICENSE
    src/
        main.py
    tests/
        test_main.py
    requirements.txt
    .gitignore
```

## Requirements

- Python 3.x

## Contributing

If you find a bug or have an idea for a new feature, please open an issue or pull request on the [GitHub repository](https://github.com/vorniches/pystructor).

## License

The `pystructor` is released under the [MIT License](https://opensource.org/licenses/MIT).