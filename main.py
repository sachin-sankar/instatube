import os
import insta
from rich.pretty import pprint as print
def updateSystem():
  packages = ['rich','instagrapi','loguru','pillow']
  for package in packages:
    os.system(f'pip install -U {package}')


print(insta.getCreators())