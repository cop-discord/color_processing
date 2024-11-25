from setuptools import setup, find_packages
with open("requirements.txt", "r") as file:
    requirements = file.readlines()

setup(
    name='color_processing',
    version='0.1',
    packages=find_packages(),
    include_package_data=True, 
    package_data={
        'color_processing': ['data/*.pkl'], 
    },
    install_requires=requirements,
    author='cop-discord',
    author_email='cop@catgir.ls',
    description='a package for fetching detailed color information',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown', 
    url='https://github.com/cop-discord/color_processing', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)