from setuptools import setup, find_packages

setup(
    name='degree_days',
    version='0.1.0',
    author='Ryan Kmetz',
    author_email='kmetzrm@gmail.com,
    description='A library for calculating Heating and Cooling Degree Days for energy analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/degree_days',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.1',
        'numpy>=1.19',
        'scikit-learn>=0.24',
        'matplotlib>=3.3',
        'meteostat>=1.5'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
