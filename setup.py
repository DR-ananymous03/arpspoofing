from setuptools import setup

setup(
    name="arpspoofing",
    version="1.0.0",
    py_modules=["main"],
    install_requires=[
        "scapy",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "arpspoofing=main:main",
        ],
    },
)