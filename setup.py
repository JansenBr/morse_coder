from setuptools import setup


with open("README", 'r') as f:
    long_description = f.read()


setup(
  name="morse_coder",
  version="0.1.0",
  description="A simple CLI tool for encoding text to morse and morse to text.",
  long_description=long_description,
  author="JansenBr",
  packages=['morse_coder'],
  install_requires=['bidict', 'numpy', 'sounddevice']
)
