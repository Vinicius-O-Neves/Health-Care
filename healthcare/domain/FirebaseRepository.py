import abc
from abc import ABC


class FirebaseRepository(ABC):

    @abc.abstractmethod
    def sendToFirebase(self):
        pass

    @abc.abstractmethod
    def getFromFirebase(self):
        pass
