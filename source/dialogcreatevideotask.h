#ifndef DIALOGCREATEVIDEOTASK_H
#define DIALOGCREATEVIDEOTASK_H

#include <QDialog>

namespace Ui {
class DialogCreateVideoTask;
}

class DialogCreateVideoTask : public QDialog
{
    Q_OBJECT

public:
    explicit DialogCreateVideoTask(QWidget *parent = nullptr);
    ~DialogCreateVideoTask();

private:
    Ui::DialogCreateVideoTask *ui;
};

#endif // DIALOGCREATEVIDEOTASK_H
