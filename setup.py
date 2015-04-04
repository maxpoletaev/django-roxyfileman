from setuptools import setup, find_packages

setup(
    name='django-roxyfileman',
    version='1.4.2.3',
    packages=find_packages(),
    include_package_data=True,
    description='Integrate Django with Roxy Fileman',
    author='Maxim Poletaev',
    author_email='zenwalker2@gmail.com',
    url='https://github.com/zenwalker/django-roxyfileman',
    keywords=['filemanager'],
    license='GPLv3',
    install_requires=['pillow'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
