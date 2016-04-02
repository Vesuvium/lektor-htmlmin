from setuptools import setup

setup(
    name='lektor-htmlmin',
    description='HTML minifier for Lektor. Based on htmlmin.',
     url='https://github.com/vesuvium/lektor-htmlmin',
    version='0.1',
    author=u'Jacopo Cascioli',
    author_email='jacopocascioli@gmail.com',
    license='MIT',
    py_modules=['lektor_htmlmin'],
    entry_points={
        'lektor.plugins': [
            'htmlmin = lektor_htmlmin:HTMLMinPlugin',
        ]
    },
    install_requires=['htmlmin']
)