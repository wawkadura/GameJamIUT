import QtQuick 2.0
import QtQuick.Layouts 1.3

Rectangle {
    id: main
    Layout.fillHeight: true
    Layout.fillWidth: true
    transform: Scale{origin.x: 0; origin.y: 0; xScale: 2; yScale: 2}
    property var spritex: 0
    property var spritey: 0
    property var tex: ''

    Rectangle {
        width: 16
        height: 16
        clip: true

        Image {
            x: 0
            y: 0
            width: 256
            height: 256
            source: main.tex
            sourceSize.height: 256
            sourceSize.width: 256
            fillMode: Image.PreserveAspectFit
        }
    }
}


/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
