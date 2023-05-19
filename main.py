import os
packages = ['rich','instagrapi']

for package in packages:
  os.system(f'pip install -U {package}')
