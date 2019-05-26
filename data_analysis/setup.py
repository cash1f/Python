from setuptools import setup, find_packages

setup(
    name='data_analysis',
    version='0.0.1',
    # url='www.github.com/cash1f/data_analysis',
    license='BSD',
    author='S. Kashif Haider',
    packages=find_packages(),
    install_requires=['PyQt5',
                      'pandas',
                      'sqlalchemy',
                      'nltk',
                      'numpy',
                      # 'jupyter',
                      'python-twitter',
                      'tweepy'],
    entry_points={},
    extras_require={'dev': ['flake8', ]},

)
