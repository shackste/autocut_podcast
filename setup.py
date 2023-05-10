from setuptools import setup, find_packages

setup(
    name='autocut_podcast',
    version='0.1',
    description='Python package for auto-cutting and combining podcast episodes',
    author='Stefan Hackstein',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cut = autocut_podcast.cut:main',
            'combine = autocut_podcast.combine:main',
            'episodes = autocut_podcast.episodes:main'
        ]
    }
)
