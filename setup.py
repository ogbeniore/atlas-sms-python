import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="atlas-sms-test",
    version="0.0.1",
    author="Oreoluwa Ojo ",
    author_email="oreeboy@gmail.com",
    description="A simple wrapper for the Atlas SMS Gateway",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ogbeniore/atlas-sms-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
