ping1=$(/usr/bin/wget -q -O /dev/stdout --no-cache --timeout=5 --no-check-certificate https://127.0.0.1/ping)
#echo $ping1
if [ "pong" != "$ping1" ]; then
    echo "`date`: Restarting nginx"
    /usr/bin/sudo /etc/init.d/nginx restart
    sleep 10
    ping2=$(/usr/bin/wget -q -O /dev/stdout --no-cache --timeout=5 --no-check-certificate https://127.0.0.1/ping)
    if [ "pong" != "$ping2" ]; then
        echo "`date`: Rebooting after nginx bad restart"
        /usr/bin/sudo /sbin/reboot
    else
        echo "`date`: Nginx OK at second ping"
    fi
else
    echo "`date`: Nginx OK at first ping"
fi

shell1=$(/usr/bin/wget -q -O /dev/stdout --no-cache --timeout=5 --no-check-certificate http://127.0.0.1:4200)
#echo $shell1
if [ -z "$shell1" ]; then
    echo "`date`: Restarting ShellInABox"
    /usr/bin/sudo /etc/init.d/shellinabox restart
    sleep 10
    shell2=$(/usr/bin/wget -q -O /dev/stdout --no-cache --timeout=5 --no-check-certificate http://127.0.0.1:4200)
    if [ -z "$shell2" ]; then
        echo "`date`: Rebooting after ShellInABox bad restart"
        /usr/bin/sudo /sbin/reboot
    else
        echo "`date`: ShellInABox OK at second check"
    fi
else
    echo "`date`: ShellInABox OK at first check"
fi

