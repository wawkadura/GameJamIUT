import QtQuick 2.0
import QtQuick.Window 2.2
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

Window {
    id: window
    visible: true
    width: 718
    height: 448
    color: "#000000"
    title: qsTr("LevelEdit")

    Column {
        id: column
        width: 200
        spacing: 0
        anchors.left: parent.left
        anchors.leftMargin: 0
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0
        anchors.top: parent.top
        anchors.topMargin: 0

        Row {
            id: row
            height: 40
            anchors.top: parent.top
            anchors.topMargin: 0
            anchors.right: parent.right
            anchors.rightMargin: 0
            anchors.left: parent.left
            anchors.leftMargin: 0
            spacing: 0
            layoutDirection: Qt.LeftToRight

            Button {
                id: save
                text: qsTr("Sauver")
            }

            Button {
                id: load
                text: qsTr("Charger")
            }
        }

        ComboBox {
            id: comboBox
            anchors.top: parent.top
            anchors.topMargin: 40
            anchors.right: parent.right
            anchors.rightMargin: 0
            anchors.left: parent.left
            anchors.leftMargin: 0
            model: ListModel {
                ListElement {
                    text: "Classic"
                }
                ListElement {
                    text: "Dark"
                }
                ListElement {
                    text: "Electric"
                }
            }
            onActivated: {
                switch(comboBox.currentText) {
                case "Classic":
                    map.tex = "./classic.png"
                    break;

                case "Dark":
                    map.tex = "./dark.png"
                    break;

                case "Electric":
                    map.tex = "./electric.png"
                    break;
                }
            }
        }

        TabBar {
            id: tabBar
            anchors.top: parent.top
            anchors.topMargin: 80
            anchors.right: parent.right
            anchors.rightMargin: 0
            anchors.left: parent.left
            anchors.leftMargin: 0

            TabButton {
                id: tabButton
                text: qsTr("Décor")
            }

            TabButton {
                id: tabButton1
                text: qsTr("Entité")
            }
        }

        SwipeView {
            id: swipeView
            width: 200
            anchors.right: parent.right
            anchors.rightMargin: 0
            anchors.left: parent.left
            anchors.leftMargin: 0
            currentIndex: tabBar.currentIndex
            anchors.top: parent.top
            anchors.topMargin: 120
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 0

            ScrollView {
                id: scrollView
                anchors.fill: parent

                Text {
                    id: element
                    color: "#ffffff"
                    text: qsTr("Page1")
                    font.pixelSize: 12
                }
            }

            ScrollView {
                id: scrollView1
                anchors.fill: parent

                Text {
                    id: element1
                    color: "#ffffff"
                    text: qsTr("Page2")
                    font.pixelSize: 12
                }
            }
        }
    }

    GridLayout {
        id: map
        flow: GridLayout.LeftToRight
        anchors.right: parent.right
        anchors.rightMargin: 0
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0
        anchors.top: parent.top
        anchors.topMargin: 0
        anchors.left: parent.left
        anchors.leftMargin: 206
        columnSpacing: 0
        rowSpacing: 0
        rows: 15
        columns: 16
        property var tex: './classic.png'
        property var spritex: 0
        property var spritey: 0
        Component.onCompleted: {
            for (var y = 0; y < 16; y++) {
                for (var x = 0; x < 16; x++) {
                    var newobj = Qt.createQmlObject('import QtQuick 2.0; Tile {id: tile' + x + '_' + y +  '; tex: map.tex;}', map, 'dynamicSnippet1')
                }
            }
        }


    }

}

/*##^##
Designer {
    D{i:2;anchors_width:200}D{i:5;anchors_y:40}D{i:10;anchors_width:240;anchors_y:80}
D{i:14;anchors_height:200;anchors_width:200}D{i:13;anchors_height:200}D{i:1;anchors_height:400;anchors_width:200}
D{i:18;anchors_height:100;anchors_width:100;anchors_x:206;anchors_y:0}
}
##^##*/
