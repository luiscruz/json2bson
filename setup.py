import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json2bson",
    version="0.0.2",
    author="Luis Cruz",
    author_email="luismirandacruz@gmail.com",
    description="CLI tool to convert JSON files to BSON.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luiscruz/json2bson",
    packages=setuptools.find_packages(),
    install_requires=[
        "Click",
        "bson",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['json2bson=json2bson.json2bson:tool'],
    },
)