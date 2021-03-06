from setuptools import setup

with open("README.md", "r") as f:
  long_description = f.read()

setup(
  name='JSONifier',
  version='0.0.7',
  description="A package for reading, writing, and editing of JSON files, Python dictionaries, and such.",
  py_modules=["jsonify"],
  package_dir={"": "src"},
  long_description=long_description,
  long_description_content_type="text/markdown",
  author="minecraftpr03",
  url="https://github.com/MasterCoder21/JSONifier",
  author_email=None,
  classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
  ]
)