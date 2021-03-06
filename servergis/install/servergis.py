# -*- coding: utf-8 -*-
#! /bin/sh
#
# Copyright (c) 2011 Anjan Bhowmik
# All rights reserved.

# Author: Anjan Bhowmik, 2011
#
# /etc/init.d/nodejs
#   and its symbolic link
# /usr/sbin/rcnodejs
##Asegurarse que sea ejecutable
#sudo chmod 755 /etc/init.d/servergis
#sudo chown root:root /etc/init.d/servergis


### BEGIN INIT INFO
# Provides:          nodejs
# Required-Start:    $network
# Required-Stop:
# Default-Start:     3 5
# Default-Stop:      0 1 2 6
# Short-Description: Node.js daemon
# Description:       NOde.js server that listens to port 8088
### END INIT INFO

#$NODEJS_BIN = $(which node)
$NODEJS_BIN = python
#$NODEJS_JS_FILE = /home/anjan/server.js
$NODEJS_JS_FILE = /opt/api3/ServerGis/servergis/servergis.py

# Load the rc.status script for this service.
. /etc/rc.status

# Reset status of this service
rc_reset

case "$1" in
    start)
        echo -n "Starting servergis "
        ## Start daemon with startproc(8). If this fails
        ## the return value is set appropriately by startproc.
        startproc $NODEJS_BIN $NODEJS_JS_FILE

        # Remember status and be verbose
        rc_status -v
        ;;
    stop)
        echo -n "Shutting down servergis "
        ## Stop daemon with killproc(8) and if this fails
        ## killproc sets the return value according to LSB.

        killproc -TERM $NODEJS_BIN

        # Remember status and be verbose
        rc_status -v
        ;;
    restart)
        ## Stop the service and regardless of whether it was
        ## running or not, start it again.
        $0 stop
        $0 start

        # Remember status and be quiet
        rc_status
        ;;
    reload)
        # If it supports signaling:
        echo -n "Reload service servergis "
        killproc -HUP $NODEJS_BIN
        #touch /var/run/BAR.pid
        rc_status -v

        ## Otherwise if it does not support reload:
        #rc_failed 3
        #rc_status -v
        ;;
    status)
        echo -n "Checking for service servergis "
        ## Check status with checkproc(8), if process is running
        ## checkproc will return with exit status 0.

        # Return value is slightly different for the status command:
        # 0 - service up and running
        # 1 - service dead, but /var/run/  pid  file exists
        # 2 - service dead, but /var/lock/ lock file exists
        # 3 - service not running (unused)
        # 4 - service status unknown :-(
        # 5--199 reserved (5--99 LSB, 100--149 distro, 150--199 appl.)

        # NOTE: checkproc returns LSB compliant status values.
        checkproc $NODEJS_BIN
        # NOTE: rc_status knows that we called this init script with
        # "status" option and adapts its messages accordingly.
        rc_status -v
        ;;
    *)
        ## If no parameters are given, print which are avaiable.
        echo "Usage: $0 {start|stop|status|restart|reload}"
        exit 1
        ;;
esac

rc_exit