#include "formprogram.h"
#include "ui_formprogram.h"

FormProgram::FormProgram(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::FormProgram)
{
    ui->setupUi(this);
}

FormProgram::~FormProgram()
{
    delete ui;
}
