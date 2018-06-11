# ELB-HC
Simulates 2 of the 3 Types of ELB HC 
1 - TCP HC - HC sends a SYN and must complete 3 WAY handshake to OK check, anything else == fail
2 - HTTP HC - HC sends HTTP GET method to configured path and must receive configured HTTP STATUS to OK HC

Modules used include: i) socket ii) time iii) http.client 

A] Running this in IDE ensure you have the right modules. 

B] Running in Linux do the below:

1) git clone: git clone git://github.com/senatoredu/ELB-HC/ 

OR just copy + past the .py into your editor and save

2) add the python shebang to the top of the .py using your text editor (nano, vim...): #!/usr/bin/env

3) Call python to run the .py: python ELB-HC.py 

Lots of bugs in this, lots of tweaks and conditionals statements to fix, but this is first iteration. 

Would also add HTTPS HC when less busy 

Have any ideas or quick fixes, hit me up!




