from setuptools import setup, find_packages

setup(
    name='django-roxyfileman',
    version='1.3',
    packages=find_packages(),
    include_package_data=True,
    description='Integrate Django with Roxy Fileman',
    author='Maxim Poletaev',
    author_email='max.poletaev@gmail.com',
    url='https://github.com/zenwalker/django-roxyfileman',
    keywords=['filemanager'],
    license='GPLv3',
    install_requires=['pillow'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
    ]
)
