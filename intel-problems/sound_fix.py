import subprocess

# alsactl restore
subprocess.Popen(["alsactl", "restore"])

# the above sets the volume to 0, because of course it does...
# despite you know, not doing that when executing the same command from the terminal...

# amixer -D pulse sset Master 50%
subprocess.Popen(["amixer", "-D", "pulse", "sset", "Master", "50%"])
# which doesn't work either because it's muting the sound output...
# I knew that...why, why am I like this?



# bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
# import subprocess
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# output, error = process.communicate()