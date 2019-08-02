import os
from typing import cast

from PyQt5.QtCore import QObject

from UM.Extension import Extension
from UM.Logger import Logger
from UM.PluginRegistry import PluginRegistry
from UM.i18n import i18nCatalog
from cura.CuraApplication import CuraApplication

i18n_catalog = i18nCatalog("cura")


# This extension allows the user to load some primitive 3D model into the build plate in Cura.
class CameraPositionExtension(QObject, Extension):

    def __init__(self, parent = None) -> None:
        QObject.__init__(self, parent)
        Extension.__init__(self)

        self.setMenuName("Camera Position")
        self.addMenuItem("Set camera position", self.showPopup)

        self._view = None

    def showPopup(self) -> None:
        if self._view is None:
            self._createView()
            if self._view is None:
                Logger.log("e", "Not creating Camera Position window since the QML component failed to be created.")
                return
        self._view.show()

    def _createView(self) -> None:
        Logger.log("d", "Creating Camera Position plugin view.")

        # Create the plugin dialog component
        plugin_path = PluginRegistry.getInstance().getPluginPath("CameraPosition")
        path = os.path.join(plugin_path, "resources", "qml", "CameraPositionPanel.qml")
        self._view = CuraApplication.getInstance().createQmlComponent(path, {"manager": self})
