from setuptools import setup, Extension


from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name='mizpel',
  version='0.1',
  scripts=['mizpel'],
  author="Doug Marsola",
  author_email="douglasmarsola@gmail.com",
  description="Spell checker, word suggestion and dictionary",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/dmarsola/mizpel",
  packages=Extension.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ]
)
