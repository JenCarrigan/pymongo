from setuptools import setup, find_packages

with open("requirements.txt", "r") as requirements_file:
  requirements = requirements_file.read()

setup(
  name="crudapp",
  version="0.0.1",
  author="Jen Carrigan",
  description="simple crud app",
  packages=find_packages(),
  install_requires=requirements
)