from distutils.core import setup
from Cython.Build import cythonize

setup(
      ext_modules = cythonize('rbf_cython_2.pyx')
      )