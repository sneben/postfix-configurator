postfix-configurator (pfc)
==========================

Configure postfix **main.cf** and **master.cf** from different file sources.

Why?
====
Do you use a package management like **apt** or **rpm** for configuration management? Then you will have the problem that a file only can be owned by one package. The main configuration files from postfix are owned by the postfix package itself. Because of this you have no possibility to inject your own configuration by another package.

The idea
========
By using the directories **/etc/postfix/main.cf.d** and **/etc/postfix/master.cf.d** for configuration snippets like this:

    /etc/postfix
       |-main.cf.d/
       |   |---- 00-basic.cf
       |   |---- 10-restrictions.cf
       |   |---- ...
       |
       |-master.cf.d/
       |   |---- 00-default.cf
       |   |---- 10-restrictions.cf
       |   |---- ...

An init-script will take this snippets, compose and write the **main.cf** and **master.cf** and tide over the given action to the original postfix init-script:

    service postfix-configurator start
    
So every time you make an action like *restart*, a possibly new configuration (deployed from your package management) will adapt to the main configuration files of postfix before the action is really executed.

Installation
============
Libraries
---------

    python setup.py install
    
Init-Script
-----------

    cp init.d/postfix-configurator /etc/init.d/

Usage
=====
To wrap the original init-script you can remove the old one from the runlevels. Then add pfc to the runlevels at the same point.

For manually usage:

    service postfix-configurator [start|stop|status|restart|reload|force-reload]
    
