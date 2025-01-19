from setuptools import setup, find_packages

setup(
    name="bincat",
    version="1.0.0",
    description="Secure token management library.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Edu Olivares",
    author_email="youremail@example.com",
    url="https://github.com/eduolihez/BinCat",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "cryptography>=39.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
