import os
from setuptools import setup
from sirtrevor import __version__


README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-sirtrevor',
    version=__version__,
    packages=['sirtrevor'],
    include_package_data=True,
    license='MIT License',
    description='A simple Django app that provides a model field and corresponding widget based on the fantastic Sir Trevor project',
    long_description=README,
    url='https://github.com/philippbosch/django-sirtrevor/',
    author='Philipp Bosch',
    author_email='hello@pb.io',
    install_requires=['markdown2', 'django-appconf'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
