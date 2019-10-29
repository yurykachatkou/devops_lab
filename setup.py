from setuptools import setup, find_packages

setup(
    name="snapshot",
    scripts=["snapshot/snapshot.py"],
    packages=find_packages(),
    version="1.1",
    author="Yury Kachatkou",
    author_email="yury_kachatkou@emap.com",
    description="Snapshot app",
)
