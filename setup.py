from setuptools import setup, find_packages

setup(
    name='mkweather',
    version='0.0.1',
    python_requires='>=3.8.5,<3.9.0',
    install_requires=[
        'requests>=2.24.0,<2.25.0',
        'click>=7.1.2<7.2.0',
    ],
    entry_points={"console_scripts": [
        "mkweather=mkweather.main:display_weather"]
    },
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    license='MIT'
)
