from setuptools import setup

setup(
    name="cosmocloud",
    version="0.0.1",
    py_modules=["cosmocloud"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "cosmocloud = cosmocloud:cli",
        ],
    },
)
