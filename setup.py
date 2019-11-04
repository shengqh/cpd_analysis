import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cpd_analysis",
    version="0.0.1",
    author="Quanhu Sheng",
    author_email="quanhu.sheng.1@vumc.org",
    description="CPDseq analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shengqh/cpd_analysis",
    entry_points = {
        'console_scripts': ['cpd_analysis=cpd_analysis.__main__:main'],
    },
    packages=['cpd_analysis'],
    package_dir={'cpd_analysis': 'src/cpd_analysis'},
    install_requires=['argparse' ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
)

