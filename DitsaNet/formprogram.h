#ifndef FORMPROGRAM_H
#define FORMPROGRAM_H

#include <QWidget>

namespace Ui {
class FormProgram;
}

class FormProgram : public QWidget
{
    Q_OBJECT

public:
    explicit FormProgram(QWidget *parent = nullptr);
    ~FormProgram();

private:
    Ui::FormProgram *ui;
};

#endif // FORMPROGRAM_H
