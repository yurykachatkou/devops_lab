from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="snapshot",
    scripts=[],
    packages=find_packages(),
    version="1.1",
    author="Yury Kachatkou",
    author_email="author@example.com",
    description="Snapshot app",
)

