from distutils.core import setup
import py2exe

# use python(34) setup.py py2exe

setup(
    name='trophy-generator',
    version=1.0,
    description='a trophy generator',
    long_description='Generator for the school trophies, sans the crests',
    url='https://github.com/Jackywathy/school-trophies',
    author='Jack Jiang, Shourov Quazi, Archie Fox',
    author_email='jackywathy24@gmail.com',
    console=['trophy.py'],
    options={'py2exe': {'bundle_files': 1, 'compressed': True}},
    zipfile=None

)