# Network Scanner


<pre>
$$\   $$\            $$\                                       $$\              $$$$$$\                                                             
$$$\  $$ |           $$ |                                      $$ |            $$  __$$\                                                            
$$$$\ $$ | $$$$$$\ $$$$$$\   $$\  $$\  $$\  $$$$$$\   $$$$$$\  $$ |  $$\       $$ /  \__| $$$$$$$\ $$$$$$\  $$$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$ $$\$$ |$$  __$$\\_$$  _|  $$ | $$ | $$ |$$  __$$\ $$  __$$\ $$ | $$  |      \$$$$$$\  $$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ \$$$$ |$$$$$$$$ | $$ |    $$ | $$ | $$ |$$ /  $$ |$$ |  \__|$$$$$$  /        \____$$\ $$ /      $$$$$$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |\$$$ |$$   ____| $$ |$$\ $$ | $$ | $$ |$$ |  $$ |$$ |      $$  _$$<        $$\   $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
$$ | \$$ |\$$$$$$$\  \$$$$  |\$$$$$\$$$$  |\$$$$$$  |$$ |      $$ | \$$\       \$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |$$ |  $$ |\$$$$$$$\ $$ |      
\__|  \__| \_______|  \____/  \_____\____/  \______/ \__|      \__|  \__|       \______/  \_______|\_______|\__|  \__|\__|  \__| \_______|\__|      
                                                                                                                                                    
~Cyber world University 
                                                                                                                                                    

</pre>
<br>


### This is a python based command line Network Scanner utility, which takes input as an argument for the exact IP address or the relative IP Address range you wish to do the Network Scan for and returns all the available IP addresses with their MAC addresses on your current Network.


<hr><br>


### NOTE: It will work with both, python2 and python3. You just need to install scapy module for both.
### Installation for scapy -->
<code>pip install scapy</code>

### OR

<code>pip3 install scapy-python3</code>

## How to use?

<code>USE --help for help menu (sudo python3 network_scanner.py --help)</code>



### Example -->

<code>sudo python3 network_scanner.py -t 192.168.137.2 </code><br>
<code>sudo python3 network_scanner.py --target 192.168.137.1/24</code>

### Output -->

<pre>
  IP                      MAC_Address
-----------------------------------------
192.168.1.1             00:1a:2b:3c:4d:5e
192.168.1.3             08:00:27:ab:cd:ef
192.168.1.5             dc:a6:32:11:22:33
192.168.1.10            3c:52:82:aa:bb:cc
</pre>
