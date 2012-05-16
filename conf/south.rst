South数据库变更工具
============================================

在Django中，当 ``models.py`` 中的字段内容变更后，数据库内容不会发生变化，使用 ``south`` 可以让Model中的变化与数据库同步。

::

    python manage.py schemamigration youappname --initial  # youappname目录下面创建一个migrations的子目录（注意！！就算有多个app，也只要initial一个就可以）

    python manage.py syncdb                                #初始化数据表等


    #以后每次对models更改后，可以运行以下两条命令同步到数据库

    python manage.py schemamigration youappname --auto     #检测对models的更改

    python manage.py migrate youappnam  #将更改反应到数据库（如果出现表已存在的错误，后面加 --fake）
