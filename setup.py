from os import path

from setuptools import find_namespace_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md")) as f:
    long_description = f.read()

setup(
    name="anagrammy",
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
    description="Creates anagrams from a bag of words.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/janjagusch/anagrammy",
    author="Jan-Benedikt Jagusch",
    author_email="jan.jagusch@gmail.com",
    classifiers=[  # Optional
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    package_dir={"": "src"},
    python_requires=">=3.7",
    packages=find_namespace_packages(where="src"),
    install_requires=[],
)
