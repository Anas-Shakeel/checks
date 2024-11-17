import codecs
from os.path import join, abspath, dirname
from setuptools import setup, find_packages


def readme():
    with codecs.open(join(abspath(dirname(__file__)), "README.md"), encoding="utf-8") as f:
        return f.read()


setup(
    name="checks-cli",
    version="1.1.0",
    description="Command-line tool to manage tasks list.",
    long_description=readme(),
    long_description_content_type='text/markdown',
    author="Anas Shakeel",
    url="https://github.com/anas-shakeel/checks",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pinsy",
        "tabulate"
    ],
    keywords=[
        "todo",
        "task",
        "task-manager",
        "tasklist",
        "todo-list",
        "cli",
        "command-line",
        "productivity",
        "organizer",
    ],
    entry_points={
        'console_scripts': [
            "checks=checks.cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
