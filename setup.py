from setuptools import setup, find_packages

setup(
    name='CryptoTradingBot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'aiogram==2.25.1',
        'pandas==2.0.3',
        'matplotlib==3.7.2',
        'mypy==1.5.1',
        'pytest==7.4.0',
        'pytest-asyncio==0.21.1',
        'python-decouple==3.8',
    ],
    entry_points={
        'console_scripts': [
            'cryptobot=cryptobot.main:run',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple cryptocurrency trading bot for interview task.',
    license='MIT',
    keywords='crypto trading bot',
    url='https://github.com/1nikitas/testCryptoTradingBot',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

