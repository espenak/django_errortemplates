from os.path import join, dirname
from setuptools import setup, find_packages

this_dir = dirname(__file__)

setup(name = 'django_errortemplates',
      description = 'Django error page templates (404.html and 500.html).',
      version = '1.0.1',
      license='BSD',
      url = 'https://github.com/espenak/django_errortemplates',
      author = 'Espen Angell Kristiansen',
      packages=find_packages(exclude=['ez_setup']),
      install_requires = ['setuptools', 'Django'],
      include_package_data=True,
      long_description=open(join(this_dir, 'README.rst')).read(),
      zip_safe=False,
      classifiers=[
                   'Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'
                  ]
)
