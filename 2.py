from django.conf import settings
from pathlib import Path

p = Path(__file__)
print(p)
print(p.joinpath('\data\apk\Read.apk'))