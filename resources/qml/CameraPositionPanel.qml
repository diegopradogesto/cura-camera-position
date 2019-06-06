import QtQuick 2.7
import QtQuick.Controls 2.3

import UM 1.2 as UM
import Cura 1.0 as Cura


UM.Dialog
{
    id: dialog

    title: "Camera Position"

    Cura.PrimaryButton
    {
        text: "Set camera position"
        onClicked: print("Setting camera position")
    }
}