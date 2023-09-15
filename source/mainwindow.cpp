#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFile>
#include <QDebug>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    QFile file(":/QSS/ManjaroMix.qss");
    file.open(QFile::ReadOnly);
    if (file.isOpen())
    {
        QString styleSheet = this->styleSheet();
        styleSheet += QLatin1String(file.readAll());
        this->setStyleSheet(styleSheet);
    }
    ui->setupUi(this);
    connect(ui->btnVideoResizeCreateTask, SIGNAL(clicked()), this, SLOT(onVideoResizeCreateClicked()));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::onVideoResizeCreateClicked(){
    createVideoTaskWindow = new DialogCreateVideoTask(this);
    createVideoTaskWindow->setModal(false);
    createVideoTaskWindow->show();
}
