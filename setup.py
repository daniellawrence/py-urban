from setuptools import setup

setup(
    name='urbandict',
    version='0.4',
    py_modules=['urbandict'],
    scripts=['urbandicli'],
    author='Daniel Lawrence',
    author_email='dannyla@linux.com',
    description='CLI client and a library for urbandictionary.com',
    url='https://github.com/daniellawrence/py-urbandict',
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)
