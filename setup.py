from setuptools import setup, find_packages

setup(
    name="tokenomics",
    version="0.1.0",
    description="Taming the 'linguistic tax' in global AI.",
    author="AI Architecture Dragon",
    packages=find_packages(),
    install_requires=[
        "tokenizers>=0.19.0",
        "transformers>=4.40.0",
        "openai>=1.20.0",
        "numpy>=1.26.0",
        "qdrant-client>=1.9.0",
        "networkx>=3.3",
        "pydantic>=2.7.0",
        "rich>=13.7.0",
    ],
    python_requires=">=3.10",
)
# Placeholder for core architectural component
