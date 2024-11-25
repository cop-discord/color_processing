from setuptools import setup, find_packages
with open("requirements.txt", "r") as file:
    requirements = file.readlines()
setup(
    name='color_processing',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,  # This will include non-code files specified in MANIFEST.in
    package_data={
        'color_processing': ['data/*.pkl'],  # Include all pickle files in the data directory
    },
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
    install_requires=[],  # List your package dependencies here
    author='cop-discord',
    author_email='cop@catgir.ls',
    description='a package for fetching detailed color information',
    long_description=open('README.md').read(),  # Long description from README file
    long_description_content_type='text/markdown',  # Specify the format of the long description
    url='https://github.com/cop-discord/color_processing',  # URL to your package's repository
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Adjust according to your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python version required
)