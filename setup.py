from setuptools import setup

setup(
    name='nebcli',
    version='1.0',
    py_modules=['nebcli'],
    include_package_data=True,
    install_requires=[
        'click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
          nebcli=nebcli:cli
    ''',
)

