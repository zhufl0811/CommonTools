#include "dialogcreatevideotask.h"
#include "ui_dialogcreatevideotask.h"
#include <QFile>

DialogCreateVideoTask::DialogCreateVideoTask(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DialogCreateVideoTask)
{
    QFile file(":/QSS/ConsoleStyle.qss");
    file.open(QFile::ReadOnly);
    if (file.isOpen())
    {
        QString styleSheet = this->styleSheet();
        styleSheet += QLatin1String(file.readAll());
        this->setStyleSheet(styleSheet);
    }
    ui->setupUi(this);
}

DialogCreateVideoTask::~DialogCreateVideoTask()
{
    delete ui;
}
