from setuptools import setup, find_packages

setup(
    name="arpspoofing",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "scapy",
    ],
    entry_points={
        "console_scripts": [
            "arpspoofing=main:main",  # هنا حددنا أن اسم الأمر سيكون arpspoofing وينفذ الدالة الرئيسية في main.py
        ],
    },
)