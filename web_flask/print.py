import sys
sys.path.append("..")
import models
from models.state import State

dict1 = models.storage.all()
print(dict1)