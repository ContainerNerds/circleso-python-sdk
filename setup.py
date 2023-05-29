from setuptools import setup, find_packages

setup(
    name='circleso',
    version='0.1dev',
    author='Container Nerds LLC.',
    author_email='inquiries@containernerds.com',
    description=('A Python library for the Circle.so API.'),
    keywords='circle.so circle.so-api circle.so-api-client',
    long_description=open('README.md').read(),
    url='https://github.com/ContainerNerds/circleso-python-sdk',
    packages=find_packages(exclude=['tests*']),
    license='GPLv3',
    python_requires='>=3.7',
    project_urls={
        'Documentation': 'https://github.com/ContainerNerds/circleso-python-sdk',
        'Source': 'https://github.com/ContainerNerds/circleso-python-sdk',
    }
)
