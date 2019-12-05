import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="createflaskapp",
    version="0.1",
    license="MIT",
    author="Ivan Sakal",
    author_email="sakalivan4@gmail.com",
    description="Package for initializing a flask project structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/isakal/create-flask-app",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    pymodules=["create-flask-app"],
    install_requires=[
        "Click>=7",
        "animation>=0.0.6",
        "termcolor>=1.1.0"
    ],
    entry_points={
        "console_scripts": ["create-flask-app=create_flask_app:create_project"]
    }
)
