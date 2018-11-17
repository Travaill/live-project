#ifndef RESULT_H
#define RESULT_H

#include <QWidget>
#include <QMainWindow>
#include <QString>
#include <string>
#include <vector>
using namespace std;
#include "data.h"

namespace Ui {
class Result;
}

class Result : public QWidget
{
    Q_OBJECT
    
public:
    explicit Result(QMainWindow *_parent, Data _data);
    ~Result();
    void updateResult();
    
private:
    inline int minval(int &a, int &b){
        return a<b?a:b;
    }
    Data data;
    QMainWindow *parent;
    Ui::Result *ui;
    void addLine(QString str);
    void readResult(const char *filePath);
    vector<string> result;
private slots:
    void onBtnBack();
    void onBtnExit();
};

#endif // RESULT_H
