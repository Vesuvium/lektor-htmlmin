import io
from setuptools import setup

readme = io.open('README.rst', 'r', encoding='utf-8').read()


setup(
    name='lektor-htmlmin',
    description='HTML minifier for Lektor. Based on htmlmin.',
    long_description=readme,
     url='https://github.com/vesuvium/lektor-htmlmin',
    version='1.0.3',
    author=u'Jacopo Cascioli',
    author_email='jacopocascioli@gmail.com',
    license='MIT',
    py_modules=['lektor_htmlmin'],
    entry_points={
        'lektor.plugins': [
            'htmlmin = lektor_htmlmin:HTMLMinPlugin',
        ]
    },
    classifiers=[
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=['htmlmin', 'chardet']
)
