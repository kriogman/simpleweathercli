from setuptools import setup
from simpleweathercli import __version__


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='simpleweathercli',
      version=__version__,
      description='SimpleWeatherCLI is a simple command-line to find weather conditions in a city. It uses current and forecast data provided via API by https://openweathermap.org/. The purpose of this project is to create a simple example of a command-line interfaces using http://docopt.org/ and use Github Actions to build and upload the package to https://pypi.org/.',
      long_description=readme(),
      long_description_content_type="text/markdown",
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='weather app simpleweathercli',
      url='https://github.com/kriogman/weathercli',
      author='Javier Gonzalez',
      author_email='jgonzalezf@gmail.com',
      license='MIT',
      packages=['simpleweathercli'],
      install_requires=[
          'requests',
          'docopt',
      ],
      entry_points={
          'console_scripts': ['simpleweathercli=simpleweathercli.cli:main'],
      },
      )
