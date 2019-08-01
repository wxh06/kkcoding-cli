import setuptools

from kkcoding import __version__


setuptools.setup(
    name='kkcoding',
    version=__version__,
    author='汪心禾',
    author_email='wangxinhe06@gmail.com',
    description='Command-line Interface for KKCoding.net',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/wangxinhe2006/kkcoding-cli',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests<3,>=2.4.2'
    ],
    entry_points={
        'console_scripts': ['kkcoding=kkcoding:console'],
    },
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: '
        'GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
    ],
)
