from setuptools import setup, find_packages


setup(
    name='sentry-patrol',
    version='0.0.1',
    description='Command Line program to interact with sentry API',
    url='https://github.com/daneoshiga/sentry-patrol',
    author='Danilo Shiga',
    author_email='daniloshiga@gmail.com',
    license='MIT',
    zip_safe=False,
    packages=find_packages(exclude=['docs', 'tests', 'tests.*', 'Pipfile*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Distributed Computing',
    ],
    keywords='sentry cli patrol',
    entry_points='''
        [console_scripts]
        patrol=patrol.cli:cli
    ''',
)
