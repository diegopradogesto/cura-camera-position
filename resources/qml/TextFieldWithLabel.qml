import QtQuick 2.10
import QtQuick.Controls 2.3

import UM 1.4 as UM
import Cura 1.0 as Cura

Item
{
    property alias value: textField.text
    property alias text: label.text
    property alias validator: textField.validator
    height: childrenRect.height

    Label
    {
        id: label
        text: "Sample text"
        anchors
        {
            right: textField.left
            left: parent.left
            verticalCenter: textField.verticalCenter
        }
    }

    Cura.TextField
    {
        id: textField
        width: (parent.width / 2) | 0
        anchors
        {
            right: parent.right
        }
        text: "0"
        validator: IntValidator
        {
            bottom: -5000
            top: 5000
        }
    }
}