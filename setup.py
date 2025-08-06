from setuptools import setup, find_packages

setup(
    name='secret-comment-hunter',
    version='1.0',
    description='Secret Comment Hunter: JS comment and secret scanner with GitHub dorking and path bruteforce',
    author='Al-Amin',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'tqdm',
    ],
    entry_points={
        'console_scripts': [
            'secret-comment-hunter=secret-comment-hunter:main',
        ],
    },
)
