import setuptools

setuptools.setup(
    name="bushk",
    version="0.0.1b",
    author="MaxPython110331",
    description="取得香港巴士的數據!",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://replit.com/@MAX110331/discohooker",                                         
    packages=["discohooker"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "datetime", "pytz"],
    python_requires=">=3.6"
)