import setuptools

setuptools.setup (
  include_package_data = True,
  name='mycalculator0001',
  version='1.0.0',
  description='oss-dev my calculator',
  author='sjchun',
  author_email='sjchun@donga.ac.kr',
  url = 'https://github.com/sejin-chun/mycalculator/',
  download_url = 'https://github.com/sejin-chun/mycalculator/archive/refs/tags/v1.0.0.zip',
  install_requires=['pytest'],
  long_description= 'oss-dev my calc',
  long_description_content_type = 'text/markdown',
  classifiers=[
      "Programming Language :: Python :: 3",
      "Operating System :: OS Independent",
  ],
)
