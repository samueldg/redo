try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="redo",
    version="2.0",
    description="Utilities to retry Python callables.",
    author="Ben Hearsum",
    author_email="ben@hearsum.ca",
    packages=["redo"],
    entry_points={
        "console_scripts": ["retry = redo.cmd:main"],
    },
    url="https://github.com/bhearsum/redo",
)
