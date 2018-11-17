#include "mainwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.setWindowTitle("幸运抽奖");
    QIcon icon("..\\LuckDraw\\AppIcon\\icon.png");
    w.setWindowIcon(icon);
    w.show();
    
    return a.exec();
}
