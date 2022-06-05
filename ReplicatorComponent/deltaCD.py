import sys
sys.path.append('../')
import socket,pickle,time,random
from Model.DataModel import Data

class DeltaCD:
    def __init__(self):
        self.add = []
        self.update = []