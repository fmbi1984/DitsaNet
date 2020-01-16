#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QDebug>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_cmdCargar_clicked()
{
    Dialog2 *ventanaC = new Dialog2(this);
    ventanaC->setModal(true);
    ventanaC->show();
}
