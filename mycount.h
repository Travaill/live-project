#ifndef MYCOUNT_H
#define MYCOUNT_H

#include <QWidget>
#include <QTimer>
#include "result.h"
#include <QMainWindow>
#include "data.h"

namespace Ui {
class MyCount;
}

class MyCount : public QWidget
{
    Q_OBJECT
public:
    explicit MyCount(QMainWindow *_parent, Data _data);
    ~MyCount();
    void startCount(int time = 3);
    
private:
    Data data;
    Ui::MyCount *ui;
    QMainWindow *parent;
    virtual void timerEvent(QTimerEvent *event);
    int timerId;
    int timeLeft;
    Result *result;
};

#endif // MYCOUNT_H
