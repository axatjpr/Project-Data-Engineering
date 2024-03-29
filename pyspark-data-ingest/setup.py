from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyspark==3.2.1"
    ],
    entry_points={
        'console_scripts': [
            'my_project = src.main:main'
        ]
    }
)