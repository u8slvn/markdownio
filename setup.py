import re

from setuptools import setup

with open('markdownio/__init__.py', 'r') as f:
    regex_version = r"^__version__\s*=\s*['\"]([\d\.]*)['\"]"
    version = re.search(regex_version, f.read(), re.MULTILINE).group(1)

with open('README.md', 'rb') as file:
    readme = file.read().decode('utf-8')

setup(
    name='markdownio',
    version=version,
    description="Python tool to write Markdown easily.",
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/u8slvn/markdownio',
    author='u8slvn',
    author_email='u8slvn@gmail.com',
    license='MIT',
    download_url=f"https://github.com/u8slvn/markdownio/archive/"
                 f"{version}.tar.gz",
    packages=['markdownio'],
    platforms='all',
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: English',
        'Programming Language :: Python',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        'Operating System :: OS Independent',
    ],
    keywords=[
        'markdown',
        'domain-specific-language'
        'markup-language',
    ],
    include_package_data=True,
    extras_require={
        'dev': [
            'pytest>=5.4.1',
            'pytest-cov>=2.10.0',
            'coverage>=5.1',
            'flake8>=3.8.3',
            'bandit>=1.6.2',
        ]
    },
    python_requires='>=3.6',
)
