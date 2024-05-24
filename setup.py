from io import open
from setuptools import find_namespace_packages, setup

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name="qurator-sbb-topic-modelling",
    version="0.0.3",
    author="Kai Labusch, The Qurator Team",
    author_email="Kai.Labusch@sbb.spk-berlin.de",
    description="Qurator",
    long_description=open("README.md", "r", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    keywords='Qurator',
    license='Apache',
    url="https://github.com/qurator-spk/sbb_topic-modelling",
    packages=find_namespace_packages(include=['qurator']),
    install_requires=install_requires,
    entry_points={
      'console_scripts': [
        "extract-corpus=qurator.topic_modeling.cli:extract_corpus",
        "extract-docs=qurator.topic_modeling.cli:extract_docs",
        "lda-grid-search=qurator.topic_modeling.cli:lda_grid_search",
        "run-lda=qurator.topic_modeling.cli:run_lda",
        "make-topicm-config=qurator.topic_modeling.cli:make_config"
      ]
    },
    python_requires='>=3.6.0',
    tests_require=['pytest'],
    classifiers=[
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
