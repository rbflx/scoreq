from setuptools import setup, find_packages

setup(
    name="scoreq",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "onnxruntime",
    ],
)
