#include "result.h"
#include "ui_result.h"
#include <QMainWindow>
#include <QString>
#include <fstream>
using namespace std;
#include <string.h>
#include <qDebug>
#include <QPropertyAnimation>
#include "mainwindow.h"

Result::Result(QMainWindow *_parent, Data _data) :
    parent(_parent),
    QWidget(0),
    ui(new Ui::Result),
    data(_data)
{
    ui->setupUi(this);
    connect(ui->btn_back,SIGNAL(clicked(bool)),this,SLOT(onBtnBack()));
    connect(ui->btn_exit,SIGNAL(clicked(bool)),this,SLOT(onBtnExit()));
    
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

Result::~Result()
{
    delete ui;
}

void Result::addLine(QString str)
{
    QListWidgetItem *item = new QListWidgetItem();
    item->setText(str);
    item->setTextAlignment(Qt::AlignCenter);
    ui->listWidget->addItem(item);
    
}

void Result::readResult(const char *filePath)
{
    result.clear();
    ifstream ifs(filePath);
    char buf[1024] = {0};
    
    while(ifs.is_open() && !ifs.eof() && result.size() < data.presentNum)
    {
        ifs.getline(buf,1024);
        if(strlen(buf)>0)
            result.push_back(string(buf));
    }
    ifs.close();
}

void Result::onBtnBack()
{
    ((MainWindow*)parent)->resetUI();
    parent->show();
    
    QLabel *label = new QLabel(parent);
    label->resize(parent->size());
    label->setPixmap(this->grab());
    label->show();
    
    QPropertyAnimation *animation= new QPropertyAnimation(label,"geometry");
    animation->setDuration(500);
    animation->setStartValue(label->geometry());
    animation->setEndValue(QRect(-label->width(), 0, label->width(), label->height()));
    animation->start();
    
    this->hide();
    
}

void Result::onBtnExit()
{
    qApp->exit(0);
}

void Result::updateResult()
{
    ui->listWidget->clear();
    readResult("..\\LuckDraw\\python\\result.txt");

    for(int i=0;i<result.size();i++)
    {
        addLine(result[i].c_str());
    }
    
}
