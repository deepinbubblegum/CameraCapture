from setuptools import setup
from Cython.Build import cythonize

setup(
    name='CaptureRTSP',
    ext_modules=cythonize("CaptureRTSP.pyx"),
    zip_safe=False,
)