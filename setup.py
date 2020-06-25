from setuptools import setup
setup(
    name='pygame-demo',
    version='0.0.1',
    packages=['modules'],
    #packages=['modules', 'thirdparty'],
    scripts=['bin/pygame'],

    # install_requires=["pygame"],

    package_data={
        '': ['*.gif'],
        # 'thirdparty': ['botan-windows-64.dll', 'libbotan-2-ubuntu-64.so']
    },
    include_package_data=True
)
