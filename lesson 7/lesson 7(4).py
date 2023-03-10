# -*- coding: utf-8 -*-
import speedtest
import platform


def get_name_os():
    name_os = platform.platform()
    print('Тип системы: ', name_os)


def get_name_processor():
    processor = platform.processor()
    print('Установленный процессор: ', processor)


def get_name_compil():
    compil = platform.python_compiler()
    print('Текущая версия компилятора: ', compil)


def get_name_version():
    version = platform.python_version()
    print('Текущая версия python', version)


def get_speed():
    wifi = speedtest.Speedtest()
    print('Скорость загрузки:', round(wifi.download() / 1000000, 2), 'МБит/сек')
    print('Скорость отдачи:', round(wifi.upload() / 1000000, 2), 'МБит/сек')


get_name_os()
get_name_processor()
get_name_compil()
get_name_version()
get_speed()
