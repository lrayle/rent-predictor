from setuptools import setup

setup(
    name='rent_predictor',
    packages=['rent_predictor'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)

# When using setuptools, it is also necessary to specify any special files that should be included in your package (in the MANIFEST.in). 
#In this case, the static and templates directories need to be included, as well as any table schema and data files.
# put these in MANIFEST.in