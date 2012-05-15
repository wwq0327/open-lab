安装说明
======================================

环境需求
--------------------------------------

- python 2.7
- django 1.3
- virtualenv

环境搭建
--------------------------------------
- 虚拟环境
::

  $ vitrualenv class
  $ cd class
  $ source bin/activate

所需模块安装
--------------------------------------

clone 代码到 ``class`` 目录，然后：

::
  $ pip install -r requirements/prj.xtx

这步会安装应用所需的python模块。

初始化数据库
--------------------------------------
::
  $ ./dev_manage.py syncdb
  $ ./dev_manage.py migrate

提示是否需要创建 管理员 帐号时，选择 ``no`` 。

启动服务器
--------------------------------------

::

  $ ./dev_manage.py runserver
  (class)[wyatt@localhost openclass]$ ./dev_manage.py runserver
  Validating models...

  0 errors found
  Django version 1.3, using settings 'openclass.settings_local'
  Development server is running at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.

在浏览器中打开上面的网址即可进行使用了。
