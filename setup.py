from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fastapi_versioning",
    version="0.4.0",
    author="Dean Way",
    description="api versioning for fastapi web applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DeanWay/fastapi-versioning",
    packages=['fastapi_versioning'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires='>=3.7',
)
