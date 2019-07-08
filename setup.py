import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="saki709",
    version="0.0.1",
    author="Ivan Sakal",
    author_email="sakalivan4@gmail.com",
    description="Package for initializing a flask project structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/isakal/flask_creator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    'Click>=7'
    ]
)
