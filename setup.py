import os
from setuptools import (
    setup,
    find_packages,
)


version = '1.0dev'
shortdesc = 'Simple Report View for PloneFormGen Data Adapters'
longdesc =  open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()  
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()  
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()  


setup(name='collective.pfg.report',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python', 
          'Topic :: Software Development',
          'Framework :: Plone',
      ],
      keywords='',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      license='GPLv2',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'Products.PloneFormGen',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
