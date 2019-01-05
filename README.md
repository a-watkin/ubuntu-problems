# My solutions to some problems I had with Ubuntu 18.04

# Ethernet Connection I217-V disabled on boot

The Intel I217-V NIC would be disabled on boot all the time. From what I've read on forums this seems to be a common problem for a failry uncommon NIC.

Solution can be found in nic_fix.py run with:

`sudo python nic_fix.py`

## Notes

This NIC seems to work just fine on Fedora, has always worked ok with Windows 7 it seems to be some specific thing with Ubuntu maybe it's a Debian thing in general but I don't know.

It doesn't seem to be the driver that's used, I compiled the driver from Intel and it was exactly the same.

After restarting from windows this NIC will not work no matter what. It will only work from a cold boot. Why? No idea.

# Line out selected as the output port

I use headphones most of the time so this is quite annoying. At the moment the script also mutes output for some reason and attempts to change the volume and unmute from the terminal have failed.

But at least I don't have to go through the sound mixed to enable sound anymore.

Run with:

`sudo python sound_fix.py`
