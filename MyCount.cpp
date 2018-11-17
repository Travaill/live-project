#include "mycount.h"
#include "ui_MyCount.h"
#include <QFont>
#include <QString>
#include <QTimer>
#include "result.h"
#include <QPropertyAnimation>
#include <QRect>

MyCount::MyCount(QMainWindow *_parent, Data _data) :
    QWidget(0),
    parent(_parent),
    ui(new Ui::MyCount),
    data(_data)
{
    ui->setupUi(this);
    
    QLabel *label = new QLabel(this);
    label->resize(parent->size());
    label->setPixmap(parent->grab());
    label->show();
    QPropertyAnimation *animation= new QPropertyAnimation(label,"geometry");
    animation->setDuration(500);
    animation->setStartValue(this->geometry());
    animation->setEndValue(QRect(-this->width(), 0, this->width(), this->height()));
    animation->start();
    
}

MyCount::~MyCount()
{
    delete ui;
}

void MyCount::startCount(int time)
{
    timeLeft = time;
    timerId = startTimer(1000);
}

void MyCount::timerEvent(QTimerEvent *event)
{
    if(event->timerId() == timerId){
        ui->label->setText(QString::number(timeLeft--));
        if(timeLeft<0){
            killTimer(timerId);
            //parent->show();
            result = new Result(parent,data);
            result->setWindowTitle(("抽奖结果"));
            result->setWindowIcon(QIcon("..\\LuckDraw\\AppIcon\\icon.png"));
            result->show();
            result->updateResult();
            this->hide();
        }
    }
}
