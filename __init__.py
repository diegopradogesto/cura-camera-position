from .src import CameraPosition


def getMetaData():
    return {}


def register(app):
    return { "extension": CameraPosition.CameraPositionExtension()}
