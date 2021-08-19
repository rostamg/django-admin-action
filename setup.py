import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

    tests_require = [
        "pytest>=3.6.3",
        "pytest-django>=3.3.2",
    ]


dev_requires = ["black==20.8b1", "isort"] + tests_require

setuptools.setup(
    name="django-admin-action",
    version="0.1.0",
    description="Django Admin Action",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["tests*"]),
    classifiers=[
        "Development Status :: 3 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["django>=1.11"],
    setup_requires=["pytest-runner"],
    tests_require=tests_require,
    extras_require={
        "test": tests_require,
        "dev": dev_requires,
    },
)
