from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='readablePTH',
    version='0.1.4',
    packages=['RPTH'],
    url="https://github.com/oneview-space/readablePTH",
    license='',
    author='OneView',
    author_email='ophir@oneview.ai',
    description='This project can write json file from pth and can write the pth again from the json.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'rpth = RPTH:main',
        ],
    },
    install_requires=["torch>=1.6",
                      "json-tricks~=3.15.5",
                      "numpy>=1.18.1"
                      ]
)
