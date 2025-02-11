from setuptools import setup, find_packages

setup(
    name="yrs_commons",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'requests>=2.25.1',
    ],
    author="Yogesh Sharma",
    author_email="yogeshsharma1994hotmail.com",
    description="DSA oriented helper funcs",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/yrs_commons",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'my-command=yrs_commons.main:main',
        ],
    },

    test_suite='tests',
    tests_require=[
        'pytest>=6.0',
        'pytest-cov>=2.0',
        'pytest-xdist>=2.0',
    ],
)
