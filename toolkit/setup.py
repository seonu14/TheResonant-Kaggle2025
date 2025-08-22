from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="resonant_repro",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.8",
    author="The Resonant",
    license="MIT",
    description="Reproduction toolkit for red-teaming scenarios (gpt-oss-20b)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="gpt-oss-20b, red-teaming, AI safety, reproducibility, alignment",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    project_urls={
        "GitHub": "https://github.com/yourusername/TheResonant-Kaggle2025",
        "Kaggle Submission": "https://www.kaggle.com/competitions/red-teaming-challenge-2025/your-submission",
    }
)
