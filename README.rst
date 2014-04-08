===== 
About
===== 

============
Installation
============
Flash your Spark Core
---------------------

Flash your core with the firmware provided. It all goes in one file.

Environment variables required for the Python script
---------------------
- LIBRATO_USER
- LIBRATO_AUTH
- SPARK_CORE_ID
- SPARK_CORE_TOKEN

=====
Usage
=====

1. Wire your Spark Core with the DS18B20 sensor wired to D1. 
2. Verify correct temperature output with the serial output of your Spark Core.
3. Run the Python script using something like nohup so that it continues to run after your session has closed:

nohup python relay.py &