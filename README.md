# thinpad-pre-commit
Pre-commit check scripts for Thinpad templates

## Installation

Copy the files into your thinpad_top project directory.

After that, run the following command in the root directory of your project.

```bash
pip install pre-commit
pre-commit install
```

## Usage

After installation, it will automatically check your synthesis log before committing changes.

If the script found latches / multiple driven nets in log, it will cancel the commit process.

If you want to use this pre-commit hook, make sure to run synthesis before commit. It will check the modification time of the changed verilog files and synthesis log.

Use `--no-verify` option when commit to skip the pre-commit hook.

```bash
git commit -m"Skip pre-commit hook` --no-verify
```
