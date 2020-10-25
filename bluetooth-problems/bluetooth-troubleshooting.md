# bluetooth command line tool

## how to connect - solution

```
bluetoothctl
select 5C:F3:70:9C:CA:D3
connect 38:18:4C:17:DA:4E
```

onboard bluetooth seems to work following this procedure:

```
bluetoothctl
power off
power on
connect 38:18:4C:17:DA:4E
```


## bluetooth management

btmgmt

## bluetooth control

bluetoothctl

## MAC address of headphones 
```
38:18:4C:17:DA:4E
```

## list bluetooth adapters

```
hciconfig -a
```

or

```
bluetoothctl
list
```

## intel controllor that doesn't seem to work at times

80:32:53:71:12:03

## Good controllor

5C:F3:70:9C:CA:D3

## Select a controllor

select 5C:F3:70:9C:CA:D3


# every time I try to connect
```
Failed to connect: org.bluez.Error.Failed
```


# when trying to connect it cycles like this

```
[NEW] Device 38:18:4C:17:DA:4E WH-CH700N
[CHG] Device 38:18:4C:17:DA:4E Connected: no
[DEL] Device 38:18:4C:17:DA:4E WH-CH700N
```

And does not establish a connection.


## before and after removing new adapter

[bluetooth]# list
Controller 80:32:53:71:12:03 smol #1 [default]
Controller 5C:F3:70:9C:CA:D3 smol #2 
[CHG] Controller 5C:F3:70:9C:CA:D3 Class: 0x00000000
[CHG] Controller 5C:F3:70:9C:CA:D3 Powered: no
[CHG] Controller 5C:F3:70:9C:CA:D3 Discovering: no
[DEL] Controller 5C:F3:70:9C:CA:D3 smol #2 
[bluetooth]# list
Controller 80:32:53:71:12:03 smol #1 [default]






# This did nothing

sudo subl /etc/init.d/disable_builtin_bluetooth


#!/bin/bash
echo "Disabling hci0 bluetooth adapter"
/usr/sbin/hciconfig hci0 down &

echo "Disabling hci0 bluetooth adapter"
/usr/sbin/hciconfig hci0 down &


update-rc.d disable_builtin_bluetooth start 26 2 3 4 5  .


sudo rfcomm connect hci1 '38:18:4C:17:DA:4E' 1


# This didn't do anything
---

## list usb devices

lsusb

Bus 001 Device 008: ID 0a5c:21e8 Broadcom Corp. BCM20702A0 Bluetooth 4.0

https://askubuntu.com/questions/898881/deactivate-internal-bluetooth-adapter-while-leaving-usb-dongle-online

sudo -H subl /etc/udev/rules.d/81-bluetooth-hci.rules

