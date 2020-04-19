# CSGO-Auto-Reconnect

This is a simple python script that automatically reconnects your CSGO client to an IP.

You have to enter this console command in CSGO beforehand: con_logfile console.log

The script reads the contents of the console.log periodically to detect any disconnect or timeout messages.
Once detected, the script clears the log file and reconnect your CSGO client by accessing an URL with Steam protocol - steam://connect/.

You can modify the sleep duration of the scan. The default sleep value is 10 seconds.
