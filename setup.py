import setuptools


def get_readme():
    with open("README.rst") as f:
        return f.read()


setuptools.setup(
    # the first three fields are a must according to the documentation
    name="pypptkit",
    version="0.0.5",
    packages=[
        "pypptkit",
    ],
    # from here all is optional
    description="pypptkit helps doing things with ppt files",
    long_description=get_readme(),
    long_description_content_type="text/x-rst",
    author="Mark Veltzer",
    author_email="mark.veltzer@gmail.com",
    maintainer="Mark Veltzer",
    maintainer_email="mark.veltzer@gmail.com",
    keywords=[
        "ppt",
        "download",
        "convert-to-text",
    ],
    url="https://veltzer.github.io/pypptkit",
    download_url="https://github.com/veltzer/pypptkit",
    license="MIT",
    platforms=[
        "python3",
    ],
    install_requires=[
        "pytconf",
        "pylogconf",
        "python-pptx",
        "pyvardump",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
    ],
    entry_points={"console_scripts": [
        "pypptkit=pypptkit.main:main",
    ]},
)
