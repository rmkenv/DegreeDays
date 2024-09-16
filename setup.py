from setuptools import setup, find_packages

setup(
    name='degree_days',
    version='0.1.0',
    author='Ryan Kmetz',
    author_email='kmetzrm@gmail.com',  # Fixed missing closing quote
    description='A library for calculating Heating and Cooling Degree Days for energy analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rmkenv/degree_days',  # You might want to update this URL
    packages=find_packages(),
    install_requires=[
        'pandas>=1.1',
        'numpy>=1.19',
        'scikit-learn>=0.24',
        'matplotlib>=3.3',
        'meteostat>=1.6.5'
    ],
    extras_require={
        'dev': [  # Added a 'dev' extra for development dependencies
            'pytest',
            'flake8',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',  # Added specific Python version classifiers
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    include_package_data=True,  # Added to include non-Python files if any
    entry_points={  # Added in case you want to provide command-line scripts
        'console_scripts': [
            'degree_days=degree_days.cli:main',  # Adjust as needed
        ],
    },
)

# Created/Modified files during execution:
print("setup.py")
