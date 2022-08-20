using System;
using Qml.Net;
using Qml.Net.Runtimes;

namespace LevelEdit
{
    class Program
    {
        static int Main(string[] args)
        {
            RuntimeManager.DiscoverOrDownloadSuitableQtRuntime();

            using (var qapp = new QGuiApplication(args))
            {
                using (var qengine = new QQmlApplicationEngine())
                {

                    qengine.Load("ui.qml");
                    return qapp.Exec();
                }
            }
        }
    }
}
