# CSGO-Auto-Reconnect

This is a simple python script that automatically reconnects your CSGO client to an IP.

Enter this command into CSGO console before running the script: `con_logfile console.log`

The script reads the content of `console.log` periodically to detect any disconnect or timeout messages.
Once detected, the script clears the log file and reconnect your CSGO client by accessing an URL with Steam protocol `steam://connect/`.

You can modify the sleep duration of the scan which defaults to 10 seconds.
