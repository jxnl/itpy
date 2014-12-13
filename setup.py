from setuptools import setup, find_packages

version = '0.2'

setup(name='itpy',
      version=version,
      description='A wrapper for iterators to allow for expressive chained transformations',
      long_description=open("readme.md").read(),
      author='Jason Liu',
      author_email='jason@jxnl.co',
      url='https://github.com/jxnl/itpy',
      license='MIT',
      packages=['itpy'],
      include_package_data=True,
      install_requires=[
          ['pybloom']
      ],
      )
