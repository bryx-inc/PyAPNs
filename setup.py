from setuptools import setup, find_packages


setup(
    name = 'apns',
    description = 'A python library for interacting with the Apple Push Notification Service',
    author = 'David Jacobs',
    author_email = 'david@29.io',
    download_url = 'https://github.com/djacobs/PyAPNs',
    license = 'unlicense.org',
    url = 'http://29.io/',
    version = '2.0.2',
    setup_requires=[
        'setuptools_scm'
    ],
    install_requires=[
        'setuptools >= 0.7',
    ],
    zip_safe=False,

)
