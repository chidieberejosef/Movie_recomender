from setuptools  import setup, find_packages

with open ("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


AUTHOR_NAME = "CHIDIEBERE PAUL-JOSEPH"
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email = 'chidieberejosef@gmail.com',
    description = 'A package for movies recommendation',
    long_description = long_description,
    long_description_content_type= 'text/markdown',
    packages = find_packages(where=SRC_REPO),
    python_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS,
)
