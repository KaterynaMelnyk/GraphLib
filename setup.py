from setuptools import setup, Extension
from setuptools.command.build_py import build_py as _build_py


class BuildPy(_build_py):
    def run(self):
        self.run_command("build_ext")
        return super().run()


GraphLib_c_ext = Extension(name='_GraphLib_c',
                           swig_opts=['-c++'],
                           extra_compile_args=['-O2'],
                           sources=['graph_lib/graph/GraphLib_c.i'])

setup(name='graph_lib',
      version='0.1',
      description='Library for the analysis of graph-structured and tree-structured data',
      url='https://github.com/KaterynaMelnyk/graphKKE.git',
      author='Kateryna Melnyk',
      author_email='kateryna.melnyk96@gmail.com',
      cmdclass={'build_py': BuildPy},
      ext_modules=[GraphLib_c_ext],
      packages=['graph_lib'],
      install_requires=['numpy',
                        'itertools',
                        'seaborn',
                        'matplotlib',
                        'scipy',
                        'sklearn',
                        'pandas',
                        'mpl_toolkits'],
      classifiers=['Development Status :: 3 - Alpha',
                   'License :: MIT License',
                   'Programming Language :: Python :: 3.7'])
