from os.path import dirname, join

from setuptools import setup, find_packages



version = '0.4'

setup(
    name = 'django-ipauth',
    version = version,
    description = "IP Authentication for Django",
    long_description = open(join(dirname(__file__), 'README.rst')).read() + "\n" +
                       open(join(dirname(__file__), 'HISTORY.rst')).read(),
    classifiers = [
        "Framework :: Django",
        "Development Status :: 3 - Alpha",
        #"Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"],
    keywords = 'django auth backend',
    author = 'TAMU COA ITS',
    author_email = 'webadmin@arch.tamu.edu',
    url = 'http://www.arch.tamu.edu',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = ['setuptools'],
)
