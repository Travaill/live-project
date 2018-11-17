#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "mycount.h"
#include <QString>
#include <String>
using namespace std;
#include "data.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT
    
public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
    void resetUI();
private:
    Data data;
    Ui::MainWindow *ui;
    void setupCSS();
    MyCount *countdown;
private slots:
    void onBtnStart();
};

#endif // MAINWINDOW_H
