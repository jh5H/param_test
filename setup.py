from setuptools import setup
import os
from glob import glob

package_name = 'param_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.py*'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.yaml'))),        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='per',
    maintainer_email='per@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f'logger_1 = {package_name}.logger_1:main',
        ],
    },
)
