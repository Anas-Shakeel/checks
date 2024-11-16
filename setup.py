import codecs
from os.path import join, abspath, dirname
from setuptools import setup, find_packages


def readme():
    return codecs.open(join(abspath(dirname(__file__)), "README.md")).read()


setup(
    name="checks-cli",  # Because checks is reserved on PyPI.
    version="0.1",
    description="Command-line tool to manage tasks list.",
    long_description=readme(),
    long_description_content_type='text/markdown',
    author="Anas Shakeel",
    url="https://github.com/anas-shakeel/checks",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # "pinsy", # This is currently not needed but will! in near future.
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
        "License :: OSI Approved :: MIT License",  # Update the license if needed
        "Operating System :: OS Independent",
    ],
)
