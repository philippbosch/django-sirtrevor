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
    description='',
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
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
