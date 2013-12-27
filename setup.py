from setuptools import setup, find_packages

import tasty_social_pie as app

setup(name="tasty-social-pie",
      version=app.__version__,
      description="Django application that ties together django-tastypie and python-social-auth.",
      author="Zenobius Jiricek",
      author_email="airtonix@gmail.com",
      packages=find_packages(),
      include_package_data=True
      )
