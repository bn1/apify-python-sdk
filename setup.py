from distutils.core import setup
__version__ = '0.1.0'

setup(
    name='apify',
    packages=['apify'],
    version=__version__,
    description='Python client for Apify API',
    author='bn1',
    author_email='me@bn1.cz',
    url='https://github.com/bn1/python-apify',
    download_url='https://github.com/bn1/python-apify/tarball/{}'.format(
        __version__),
    keywords='api parser table data html',
    classifiers=[
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        'Topic :: Internet',
        'Topic :: Utilities',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    install_requires=[
        'requests',
    ],
    tests_require=[
        'pytest',
        'httmock',
        'pytest-cov'
    ]
)
