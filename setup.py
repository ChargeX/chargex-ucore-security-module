from setuptools import setup
setup(
    name='message signing module with botan',
    version='0.0.1',
    packages=['modules', 'thirdparty'],
    scripts=['bin/ucore-security-module'],

    package_data={
        # 'thirdparty': ['botan-windows-64.dll', 'libbotan-2-ubuntu-64.so']
    },
    include_package_data=True
)
