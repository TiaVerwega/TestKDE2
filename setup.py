import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TestKDE2", # Replace with your own username
    version="0.0.1",
    author="Maria-Theresia Verwega",
    author_email="mtv@informatik.uni-kiel.de",
    description="A small KDE example package", # one sentence
    long_description=long_description, # loaded from the README.md
    long_description_content_type="text/markdown", # README is markdown
    url="https://github.com/TiaVerwega/TestKDE2",
    packages=setuptools.find_packages(), # list of all Python import packages that should be in the Distribution Package; you can use find_packages() to get them
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], # licenses and ...
    python_requires='>=3.6',
)
