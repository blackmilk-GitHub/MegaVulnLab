from setuptools import setup, find_packages

setup(
    name="vuln-python-app",
    version="1.0.0",
    description="A vulnerable Python application for security testing",
    author="MegaVulnLab",
    packages=find_packages(),
    install_requires=[
        "flask==0.12",
        "pyyaml==5.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
