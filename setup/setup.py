import setuptools


with open("README.md", "r") as fhandle:
    long_description = fhandle.read() 

setuptools.setup(
    name="pjer", # Put your username here!
    version="0.0.1", # The version of your package!
    author="lucasammer", # Your name here!
    author_email="me@lucasammer.com", # Your e-mail here!
    description="A python game engin", # A short description here!
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucasammer/pjer", # Link your package website here! (most commonly a GitHub repo)
    packages=setuptools.find_packages(), # A list of all packages for Python to distribute!
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], # Enter meta data into the classifiers list!
    python_requires='>=3.6', # The version requirement for Python to run your package!
)