from setuptools import setup, find_packages
setup(
    name='rw_modbus',
    sdk_version='2.1.3',
    version='0.0.1',
    author='thomas',
    author_email='thomas.philip@roamworks.com',
    description='The application is built for Roamworks to read modbus data',
    license='MIT',
    packages = find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    install_requires=[
    ],
    entry_points = """
        [console_scripts]
        rw_modbus = Application:main
        """
)
