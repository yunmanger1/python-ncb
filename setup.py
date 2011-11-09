
from setuptools import setup

setup(
    name='python-ncbrates',
    version=__import__('ncbrates').__version__,
    description='NCB rates (nationalbank.kz)',
    author='German Ilyin',
    author_email='germanilyin@gmail.com',
    url='https://github.com/yunmanger1/python-ncb/',
    packages=['ncbrates',],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
