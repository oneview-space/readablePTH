from setuptools import setup

setup(
    name='readablePTH',
    version='0.1',
    packages=['RPTH'],
    url='',
    license='',
    author='OneView',
    author_email='ophir@oneview.ai',
    description='Make pth readable ',
    entry_points={
        'console_scripts': [
            'rpth = RPTH:main',
        ],
    },
    install_requires=["torch~=1.8.1",
                      "json-tricks~=3.15.5"
                      ]
)
