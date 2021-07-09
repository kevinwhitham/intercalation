import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "intercalation",
    version = "0.0.6",
    author = "Kevin Whitham",
    author_email = "kevin.whitham@gmail.com",
    description = "Routines to create intercalated crystals",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "",
    install_requires=[""],
    classifiers = [
            "Programming Language :: Python :: 3",
            "License :: OSI Approvied :: GNU General PUblic License v3 or later (GPLv3+)",
            "Operating System :: OS Independent",
    ],

    packages = setuptools.find_packages(),
    python_requires = ">=3",
)

