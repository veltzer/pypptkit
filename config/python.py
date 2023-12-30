from typing import List


console_scripts: List[str] = [
    "pypptkit=pypptkit.main:main",
]
config_requires: List[str] = []
dev_requires: List[str] = [
    "pypitools",
]
install_requires: List[str] = [
    "pytconf",
    "pylogconf",
    "python-pptx",
    "pyvardump",
]
make_requires: List[str] = [
    "pymakehelper",
    "pyclassifiers",
    "pydmt",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires
