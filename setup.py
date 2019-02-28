from setuptools import setup

exec(open("version.py").read())

setup(
    name='chunks',
    version=__version__,
    description='Yield successive n-sized chunks from list.',
    author='Fachrul Kurniansyah',
    maintainer='Fachrul Kurniansyah',
    maintainer_email='fchrulk@outlook.com',
    url='https://github.com/fchrulk/chunks'
)
