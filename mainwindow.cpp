#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <qDebug>
#include <QFile>
#include <QString>
#include "mycount.h"
#include <QPlainTextEdit>
#include <QTextBlock>
#include <QTextDocument>
#include <QPropertyAnimation>
#include <QParallelAnimationGroup>
#include <QMessageBox>
#include <stdio.h>
#include <stdlib.h>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setupCSS();
    connect(ui->btn_start,SIGNAL(clicked(bool)),this,SLOT(onBtnStart()));
    
    
    QPropertyAnimation *animation = new QPropertyAnimation(this,"windowOpacity");
    animation->setDuration(1000);
    animation->setStartValue(0);
    animation->setEndValue(1);
    animation->start();
    
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::resetUI()
{
    ui->lineEdit_name->setText("");
    ui->lineEdit_present->setText("");
    ui->lineEdit_peopleNum->setText("");
    ui->lineEdit_keyWord->setText("");
    ui->comboBox_rule->setCurrentIndex(0);
}

void MainWindow::setupCSS()
{
    int index =3;
    QString paths[] = {
        "",
        "..\\LuckDraw\\Styles\\blue.qss",
        "..\\LuckDraw\\Styles\\darkorange.css",    
        "..\\LuckDraw\\Styles\\golden.qss",
        };
    if(index == 0)
    {
        qApp->setStyleSheet("");
        return;
    }
    else
    {
        QFile file(paths[index]);
        if(file.open(QIODevice::ReadOnly|QIODevice::Text))
        {
            QTextStream in(&file);
            QString style = in.readAll();
            file.close();
            qApp->setStyleSheet(style);
        }
    }
}

void MainWindow::onBtnStart()
{
    data.name = ui->lineEdit_name->text();
    data.presentName = ui->lineEdit_present->text();
    data.presentNum = ui->lineEdit_peopleNum->text().toInt();
    data.keyWord = ui->lineEdit_keyWord->text();
    data.filterRule = ui->comboBox_rule->currentIndex();
    
    if(data.name=="" || data.presentName=="" || data.presentNum<=0 || data.keyWord==""){
        QMessageBox::warning(NULL, QString::fromLocal8Bit("信息不完整或错误"), QString::fromLocal8Bit("请正确填写抽奖信息"));
        return;
    }
    
    countdown = new MyCount(this,data);
    countdown->setWindowTitle(QString::fromLocal8Bit("抽奖倒计时"));
    countdown->setWindowIcon(QIcon("..\\LuckDraw\\AppIcon\\icon.png"));
    
    FILE *fp = fopen("..\\LuckDraw\\python\\search.txt","w");
    fprintf(fp,"%d\n",data.filterRule);
    fprintf(fp,"#%s#",data.keyWord.toStdString().c_str());
    fclose(fp);
    system("cd ..\\LuckDraw\\python\\ & python luckdraw.py");
    
    countdown->startCount(3);
    countdown->show();
    this->hide();
    
}

