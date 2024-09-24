from setuptools import setup, find_packages


setup(
    name='llmtradingbot',
    version='0.0.1',
    author="Kanwal Arora",
    author_email="kanwalarora029@gmail.com",
    packages=find_packages(),
    install_requires=["langchain","langchain-openai","langchain-astradb","datasets","pypdf","python-dotenv","flask"]
)