Common active reconnaissance tools and methods include the following:

- Host enumeration
- Network enumeration
- User enumeration
- Group enumeration
- Network share enumeration
- Web page enumeration
- Application enumeration
- Service enumeration
- Packet crafting

Common passive reconnaissance tools and methods include the following:

- Domain enumeration
- Packet inspection
- Open-source intelligence (OSINT)
- Recon-ng
- Eavesdropping

- Use **nslookup** to obtain domain and IP address information.
- Use the **whois** command to find additional registration information.
- Dig tools.
There are also several CT monitoring tools available, such as CertSpotter and Censys, which can help automate the process of monitoring CT logs for specific domains or SSL/TLS certificates

**[https://crt.sh](https://crt.sh/)**. - to debug ssl certification details

The following are additional tools that allow you to search for breach data dumps:

- **WhatBreach:** _[https://github.com/Ekultek/WhatBreach](https://github.com/Ekultek/WhatBreach)_
- **LeakLooker:** _[https://github.com/woj-ciech/LeakLooker](https://github.com/woj-ciech/LeakLooker)_
- **Buster:** _[https://github.com/sham00n/buster](https://github.com/sham00n/buster)_
- **Scavenger:** _[https://github.com/rndinfosecguy/Scavenger](https://github.com/rndinfosecguy/Scavenger)_
- **PwnDB:** _[https://github.com/davidtavarez/pwndb](https://github.com/davidtavarez/pwndb)_

Tools like h8mail and WhatBreach take advantage of breached data repositories of websites such as haveibeenpwned.com and snusbase.com. Historically, websites such as weleakinfo.com (seized by the FBI) have been used by criminals to dump information from past security breaches.

By using basic search techniques combined with advanced operators, both you and attackers can use Google as a powerful vulnerability search tool. The following are some advanced operators:

- **Filetype:** Directs Google to search only within the text of a particular type of file (for example, filetype:xls)
- **Inurl:** Directs Google to search only within the specified URL of a document (for example, inurl:search-text)
- **Link:** Directs Google to search within hyperlinks for a specific term (for example, link:www.domain.com)
- **Intitle:** Directs Google to search for a term within the title of a document (for example, intitle: “Index of /etc”)

By using these advanced operators in combination with key terms, both you and attackers can get Google to uncover many pieces of sensitive information that shouldn’t be revealed. These search strings are often called _Google dorks_.

To see how Google dorking works, enter the following phrase into Google:

**intext:JSESSIONID OR intext:PHPSESSID inurl:access.log ext:log**

You can use advanced operators to search for many types of data. The following is another example of a Google search string (or Google dork) that can reveal passwords of web applications:

**"public $user =" | "public $password = " | "public $secret =" | "public $db =" ext:txt | ext:log -git**

Now that we have discussed some basic Google search techniques, let’s look at advanced Google hacking. We recommend that you visit the Google Hacking Database (GHDB) repositories at _[https://www.exploit-db.com/google-hacking-database/](https://www.exploit-db.com/google-hacking-database/)_. GHDB has the following search categories:

- Footholds
- Files containing usernames
- Sensitive directories
- Web server detection
- Vulnerable files
- Vulnerable servers
- Error messages
- Files containing juicy info
- Files containing passwords
- Sensitive online shopping info
- Network or vulnerability data
- Pages containing login portals
- Various online devices
- Advisories and vulnerabilities

GHDB is a community effort. Anyone can upload a new Google dork to perform these types of searches. Once you start playing with the dorks in GHDB, you will be surprised by the unbelievable things found through Google hacking. GHDB has made using Google dorks very easy, and there are other options as well. Later in this module, you will learn about additional tools that can be used to perform similar searches (such as Recon-ng).

It is possible to learn more about a person or organization by searching on a known email address. It is useful to determine if employees of a company have had their work email addresses compromised. Several online services provide the ability to search on individual email addresses and entire domains to reveal breaches. Some of those sites are:

- haveibeenpwned.com
- f-secure.com
- hacknotice.com
- breachdirectory.com
- keepersecurity.com
You will use a tool called `EmailHarvester` to find information about a domain, including email addresses of personnel.

wouldn’t it be great if there were a tool that could pull together all these different functions? This is where Recon-ng comes in. It is a framework developed by Tim Tomes of Black Hills Information Security. This tool was developed in Python with Metasploit **msfconsole** in mind. If you have used the Metasploit console before, Recon-ng should be familiar and easy to understand.

Shodan is a search engine for IoT devices that was developed by John Matherly in 2009. Shodan can discover all types of internet-connected “things", from mobile phones to smart appliances, to power plants. It is a powerful tool to determine what devices are currently connected to the network and how they are connected.  [https://www.shodan.io/](https://www.shodan.io/).


**Port Scans**

A **_port scan_** is an active scan in which the scanning tool sends various types of probes to the target IP address and then examines the responses to determine whether the service is actually listening. For instance, with an Nmap SYN scan, the tool sends a TCP SYN packet to the TCP port it is probing. This process is also referred to as half-open scanning because it does not open a full TCP connection. If the response is a SYN/ACK, this would indicate that the port is actually in a listening state. If the response to the SYN packet is an RST (reset), this would indicate that the port is closed or is not in a listening state. If the SYN probe does not receive any response, Nmap marks it as filtered because it cannot determine if the port is open or closed. 

**Nmap scan types**
- TCP Connect Scan (**-sT**)
- UDP Scan (**-sU**)
- TCP FIN Scan (**-sF**)
- Host Discovery Scan (**-sn**)
- Timing Options (**-T 0-5**)

The Nmap scanner provides six timing templates that can be specified with the -T option and the template number (0 through 5) or name:

- -T0 (Paranoid): Very slow, used for IDS evasion
- -T1 (Sneaky): Quite slow, used for IDS evasion
- -T2 (Polite): Slows down to consume less bandwidth and runs about ten times slower than the default
- -T3 (Normal): Default, a dynamic timing model based on target responsiveness
- -T4 (Aggressive): Assumes a fast and reliable network and may overwhelm targets
- -T5 (Insane): Very aggressive; will likely overwhelm targets or miss open ports

**TCP Connect Scan ( -sT )**

A TCP connect scan actually makes use of the underlying operating system’s networking mechanism to establish a full TCP connection with the target device being scanned. Because it creates a full connection, it creates more traffic (and thus takes more time to run). This is the default scan type that is used if no scan type is specified with the **nmap** command. However, it should typically be used only when a SYN scan is not an option, such as when a user who is running the **nmap** command does not have raw packet privileges on the operating system because many of the Nmap scan types rely on writing raw packets

**UDP Scan ( -sU )**

The majority of the time, you will be scanning for TCP ports, as this is how you connect to most services running on target systems. However, you might encounter some instances in which you need to scan for UDP ports – for example, if you are trying to enumerate a DNS, SNMP, or DHCP server. These services all use UDP for communication between client and server. To scan UDP ports, Nmap sends a UDP packet to all ports specified in the command-line configuration. It waits to hear back from the target. If it receives an ICMP port unreachable message back from a target, that port is marked as closed. If it receives no response from the target UDP port, Nmap marks the port as open/filtered. Table 3-4 shows the UDP scan responses.

**TCP FIN Scan ( -sF )**

There are times when a SYN scan might be picked up by a network filter or firewall. In such a case, you need to employ a different type of packet in a port scan. With the TCP FIN scan, a FIN packet is sent to a target port. If the port is actually closed, the target system sends back an RST packet. If nothing is received from the target port, you can consider the port open because the normal behavior would be to ignore the FIN packet

**Host Discovery Scan ( -sn )**

A host discovery scan is one of the most common types of scans used to enumerate hosts on a network because it can use different types of ICMP messages to determine whether a host is online and responding on a network.

**Timing Options ( -T 0-5 )**

The Nmap scanner provides six timing templates that can be specified with the **-T** option and the template number (0 through 5) or name. Nmap timing templates enable you to dictate how aggressive a scan will be, while leaving Nmap to pick the exact timing values. These are the timing options:

- **-T0 (Paranoid)** : Very slow, used for IDS evasion
- **-T1 (Sneaky)** : Quite slow, used for IDS evasion
- **-T2 (Polite)** : Slows down to consume less bandwidth, runs about 10 times slower than the default
- **-T3 (Normal)** : Default, a dynamic timing model based on target responsiveness
- **-T4 (Aggressive)** : Assumes a fast and reliable network and may overwhelm targets
- **-T5 (Insane)** : Very aggressive; will likely overwhelm targets or miss open ports



## Types of Enumeration

- Host Enumeration
- User Enumeration
- Group Enumeration
- Network Share Enumeration
- Additional SMB Enumeration Examples
- Web Page Enumeration/Web Application Enumeration
- Service Enumeration
- Exploring Enumeration via Packet Crafting

**User Enumeration**

Gathering a valid list of users is the first step in cracking a set of credentials. When you have the username, you can then begin brute-force attempts to get the account password. You perform **_user enumeration_** when you have gained access to the internal network. On a Windows network, you can do this by manipulating the Server Message Block (SMB) protocol, which uses TCP port 445. Figure 3-12 illustrates how a typical SMB implementation works.

The information contained in the responses to these messages enables you to reveal information about the server:

- **SMB_COM_NEGOTIATE:** This message allows the client to tell the server what protocols, flags, and options it would like to use. The response from the server is also an SMB_COM_NEGOTIATE message. This response is relayed to the client about which protocols, flags, and options it prefers. This information can be configured on the server itself. A misconfiguration sometimes reveals information that you can use in penetration testing. For instance, the server might be configured to allow messages without signatures. You can determine if the server is using share- or user-level authentication mechanisms and whether the server allows plaintext passwords. The response from the server also provides additional information, such as the time and time zone the server is using. This is necessary information for many penetration testing tasks.
- **SMB_COM_SESSION_SETUP_ANDX** : After the client and server have negotiated the protocols, flags, and options they will use for communication, the authentication process begins. Authentication is the primary function of the SMB_COM_SESSION_SETUP_ANDX message. The information sent in this message includes the client username, password, and domain. If this information is not encrypted, it is easy to sniff it right off the network. Even if it is encrypted, if the mechanism being used is not sufficient, the information can be revealed using tools such as Lanman and NTLM in the case of Microsoft Windows implementations. The following example shows this message being used with the smb-enum-users.nse script:
    ```sh
    #**nmap  --script smb-enum-users.nse 192.168.88.251**
    nmap --script smb-enum-users.nse** _<host>
    ```
**Group Enumeration**

For a penetration tester, **_group enumeration_** is helpful in determining the authorization roles that are being used in the target environment. The Nmap NSE script for enumerating SMB groups is **smb-enum-groups**. This script attempts to pull a list of groups from a remote Windows machine. You can also reveal the list of users who are members of those groups. The syntax of the command is as follows:

```sh
nmap --script smb-enum-groups.nse --script-args smbusername=vagrant,smbpass=vagrant 192.168.56.3

nmap --script smb-enum-groups.nse -p445** _<host>
```

Example 3-25 shows sample output of this command run against the Windows server at 192.168.56.3. This example uses known credentials to gather information.

**Network Share Enumeration**

Identifying systems on a network that are sharing files, folders, and printers is helpful in building out an attack surface of an internal network. The Nmap **smb-enum-shares** NSE script uses Microsoft Remote Procedure Call (MSRPC) for **_network share enumeration_**. The syntax of the Nmap **smb-enum-shares.nse** script is as follows:

```sh
nmap --script smb-enum-shares.nse -p 445 <host>
nmap --script smb-enum-shares.nse -p 445 192.168.88.251
```

You can also use tools such as enum4linux to enumerate Samba shares, including user accounts, shares, and other configurations. 

There is a Python-based enum4linux implementation called enum4linux-ng that can be downloaded from _[https://github.com/cddmp/enum4linux-ng](https://github.com/cddmp/enum4linux-ng)_.
```sh
enum4linux-ng.py -As 192.168.88.251
```

**Web Page Enumeration/Web Application Enumeration**

Once you have identified that a web server is running on a target host, the next step is to take a look at the web application and begin to map out the attack surface performing **_web page enumeration_** or often referred to as **_web application enumeration_**. You can map out the attack surface of a web application in a few different ways. The handy Nmap tool actually has an NSE script available for brute forcing the directory and file paths of web applications. Armed with a list of known files and directories used by common web applications, it probes the server for each of the items on the list. Based on the response from the server, it can determine whether those paths exist. This is handy for identifying things like the Apache or Tomcat default manager page that are commonly left on web servers and can be potential paths for exploitation. The syntax of the http-enum NSE script is as follows:

```sh
nmap -sV --script=http-enum <target>
nmap -sV --script=http-enum -p 80 192.168.88.251
```
**Nikto** is an open-source web vulnerability scanner that has been around for many years. It’s not as robust as the commercial web vulnerability scanners; however, it is very handy for running a quick script to enumerate information about a web server and the applications it is hosting. 
Because of the speed at which Nikto works to scan a web server, it is very noisy. It provides a number of options for scanning, including the capability to authenticate to a web application that requires a username and password
```sh
nikto -h 192.168.88.251
```
**Service Enumeration**

**_Service enumeration_** is the process of identifying the services running on a remote system, and it is a primary focus of what Nmap does as a port scanner. Earlier discussion in this module highlights the various scan types and how they can be used to bypass filters. When you are connected to a system that is on a directly connected network segment, you can run some additional scripts to enumerate further. A port scan takes the perspective of a credentialed remote user. The Nmap **smb-enum-processes** NSE script enumerates services on a Windows system, and it does so by using credentials of a user who has access to read the status of services that are running. This is a handy tool for remotely querying a Windows system to determine the exact list of services running. The syntax of the command is as follows:

```sh
nmap --script smb-enum-processes.nse --script-args smbusername= <username>, smbpass=<password> -p445 <host>
```
**Exploring Enumeration via Packet Crafting**

When it comes to enumeration via packet crafting and generation, Scapy is one of pentesters' favorite tools and frameworks. Scapy is a very comprehensive Python-based framework or ecosystem for packet generation. This section looks at some of the simple ways you can use this tool to perform basic network reconnaissance.
```sh
send(IP(dst="192.168.88.251")/ICMP()/"malicious_payload")
```
shows the ICMP packet received by the target system (192.168.88.225/vulnhost-1). The tshark packet capture tool is used to capture the crafted ICMP packet.
```sh
sudo tshark host 192.168.78.142
```

The Server Message Block (SMB) protocol is a network file sharing protocol supported on Windows computers and by SAMBA on Linux. SMB enables applications to read and write files or request services over a network. Open public shares or shared devices such as print servers on a network, can be accessed through SMB.

### Packet Inspection and Eavesdropping

As a penetration tester, you can use tools like Wireshark, tshark, and tcpdump to collect packet captures for packet inspection and eavesdropping. Anyone who has been involved with networking or security has at some point used these tools to capture and analyze traffic on a network. For a penetration tester, such tools can be convenient for performing passive reconnaissance. Of course, this type of reconnaissance requires either a physical or a wireless connection to the target. If you are concerned about being detected, you are probably better off attempting a wireless connection because it would not require you to be inside the building. Many times, a company’s wireless footprint bleeds outside its physical walls.

![[Pasted image 20251108201517.png]]

TODO
- Part 1: Investigate the Scapy Tool.
- Part 2: Use Scapy to Sniff Network Traffic.
- Part 3: Create and Send an ICMP Packet.
- Part 4: Create and Send TCP SYN Packets.


```sh
sudo tcpdump -i eth0 -s 0 -w packetdump.pcap
```

## Types of vulnerability scans

- Unauthenticated Scans
- Authenticated Scans
- Discovery Scans
- Full Scans
- Stealth Scans
- Compliance Scans


 _Elicitation_ is the act of gaining knowledge or information from people. In most cases, an attacker gets information from a victim without directly asking for that particular information.
 
_Malvertising_ involves incorporating malicious ads on trusted websites. Users who click these ads are inadvertently redirected to sites hosting malware.

_Pretexting_, or impersonation, is an attack where an attacker presents as someone else to gain access to information. Sometimes, it can be very simple, such as quickly pretending to be someone else within an organization; in other cases, it can involve creating a whole new identity and then using that identity to request sensitive information.


Pharming is a type of impersonation attack in which a threat actor redirects a victim from a valid website or resource to a malicious one that is a clone of the valid site. This can occur due to an altered hosts file or some sort of DNS manipulation. From there, an attempt is made to extract confidential information from the user or install the malware in the victim's system.

**_Vishing_** (which is short for _voice phishing_) is a social engineering attack carried out in a phone conversation. The attacker persuades the user to reveal private personal and financial information or information about another person or a company.

**_Universal Serial Bus (USB) drop key_** attacks to successfully compromise victim systems

A **_watering hole attack_** is a targeted attack that occurs when an attacker profiles websites that the intended victim accesses. The attacker then scans those websites for possible vulnerabilities.

A watering hole, or pivot attack, is targeted when an attacker profiles websites the intended victim accesses. The attacker then scans those websites for possible vulnerabilities. Suppose the attacker locates a website that can be compromised. In that case, the website is then injected with a JavaScript or similar code injection designed to redirect the user when the user returns to that site. 

**_Dumpster diving_**, a person scavenges for private information in garbage and recycling containers. To protect sensitive documents, an organization should store them in a safe place as long as possible.

**_shoulder surfing_**, someone obtains information such as personally identifiable information (PII), passwords, and other confidential data by looking over a victim’s shoulder.

The **_Social-Engineer Toolkit (SET)_** is a tool developed by David Kennedy. This tool can be used to launch numerous social engineering attacks and can be integrated with third-party tools and frameworks such as Metasploit.

“Exploiting Application-Based Vulnerabilities,” you will learn about web application vulnerabilities, such as cross-site scripting (XSS) and cross-site request forgery (CSRF). XSS vulnerabilities leverage input validation weaknesses on a web application. These vulnerabilities are often used to redirect users to malicious websites to steal cookies (session tokens) and other sensitive information. **_Browser Exploitation Framework (BeEF)_** is a tool that can be used to manipulate users by leveraging XSS vulnerabilities. You can download BeEF from [_https://beefproject.com_](https://beefproject.com/) or [_https://github.com/beefproject/beef_](https://github.com/beefproject/beef).

The following are a few examples of **_call spoofing tools_**:

- **SpoofApp**: This is an Apple iOS and Android app that can be used to easily spoof a phone number.
- **SpoofCard**: This is an Apple iOS and Android app that can spoof a number and change your voice, record calls, generate different background noises, and send calls straight to voicemail.
- **Asterisk**: Asterisk is a legitimate voice over IP (VoIP) management tool that can also be used to impersonate caller ID.
