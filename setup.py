from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

version = "0.1.1a0"

setup(
    name="ward",
    version=version,
    description="A Python 3 test framework.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/darrenburns/ward",
    author="Darren Burns",
    author_email="darrenb900@gmail.com",
    license="MIT",
    packages=["ward"],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'ward=ward.run:run'
        ]
    },
    install_requires = [
        "blessings==1.7",
        "colorama==0.4.1",
        "dataclasses==0.6",
    ]
)
