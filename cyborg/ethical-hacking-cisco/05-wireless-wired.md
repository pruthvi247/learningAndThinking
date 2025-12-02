The following are some examples of network-based attacks and exploits:

- Windows name resolution-based attacks and exploits
- DNS cache poisoning attacks
- Attacks and exploits against Server Message Block (SMB) implementations
- Simple Network Management Protocol (SNMP) vulnerabilities and exploits
- Simple Mail Transfer Protocol (SMTP) vulnerabilities and exploits
- File Transfer Protocol (FTP) vulnerabilities and exploits
- Pass-the-hash attacks
- On-path attacks (previously known as man-in-the-middle [MITM] attacks)
- SSL stripping attacks
- Denial-of-service (DoS) and distributed denial-of-service (DDoS) attacks
- Network access control (NAC) bypass
- Virtual local area network (VLAN) hopping attacks

An attacker can cause legitimate wireless clients to deauthenticate from legitimate wireless APs or wireless routers to either perform a DoS condition or to make those clients connect to an evil twin. This type of attack is also known as a **_disassociation attack_** because the attacker disassociates (tries to disconnect) the user from the authenticating wireless AP and then carries out another attack to obtain the user’s valid credentials.

A service set identifier (SSID) is the name or identifier associated with an 802.11 wireless local area network (WLAN). SSID names are included in plaintext in many wireless packets and beacons. A wireless client needs to know the SSID in order to associate with a wireless AP. It is possible to configure wireless passive tools like Kismet or KisMAC to listen to and capture SSIDs and any other wireless network traffic. In addition, tools such as _Airmon-ng_ (which is part of the _Aircrack-ng suite_) can perform this reconnaissance. The Aircrack-ng suite of tools can be downloaded from [_https://www.aircrack-ng.org_](https://www.aircrack-ng.org/). Example 5-14 shows the Airmon-ng tool. The system in this example has five different wireless network adapters, and the adapter wlan1 is used for monitoring.

**_Example 5-14_** _-_ _Starting Airmon-ng_

The 802.11w standard defines the Management Frame Protection (MFP) feature. MFP protects wireless devices against spoofed management frames from other wireless devices that might otherwise deauthenticate a valid user session.

 A popular site among war drivers is WiGLE ([_https://wigle.net_](https://wigle.net/)). The site allows users to detect Wi-Fi networks and upload information about the networks by using a mobile app.
 [_https://www.krackattacks.com_](https://www.krackattacks.com/).
Wi-Fi Protected Setup (WPS) is a protocol that simplifies the deployment of wireless networks.

A tool called Reaver makes WPS attacks very simple and easy to execute. You can download Reaver from [_https://github.com/t6x/reaver-wps-fork-t6x_](https://github.com/t6x/reaver-wps-fork-t6x).

You can find a paper describing and demonstrating fragmentation attacks at [_http://download.aircrack-ng.org/wiki-files/doc/Fragmentation-Attack-in-Practice.pdf_](http://download.aircrack-ng.org/wiki-files/doc/Fragmentation-Attack-in-Practice.pdf)

Credential harvesting is an attack that involves obtaining or compromising user credentials

**_Bluejacking_** is an attack that can be performed using Bluetooth with vulnerable devices in range.This is done using the Object Exchange (OBEX) protocol. A vCard can contain name, address, telephone numbers, email addresses, and related web URLs. This type of attack has been mostly performed as a form of spam over Bluetooth connections.

You can find an excellent paper describing Bluejacking at [_http://acadpubl.eu/jsi/2017-116-8/articles/9/72.pdf_](http://acadpubl.eu/jsi/2017-116-8/articles/9/72.pdf).

 **_Bluesnarfing_** attacks are performed to obtain unauthorized access to information from a Bluetooth-enabled device. An attacker can launch Bluesnarfing attacks to access calendars, contact lists, emails and text messages, pictures, or videos from the victim
 Bluesnarfing attacks can also be used to obtain the International Mobile Equipment Identity (IMEI) number for a device. Attackers can then divert incoming calls and messages to another device without the user’s knowledge.

Numerous IoT devices use Bluetooth Low Energy (BLE) for communication. BLE communications can be susceptible to on-path attacks, and an attacker could modify the BLE messages between systems that would think that they are communicating with legitimate systems. DoS attacks can also be problematic for BLE implementations. Several research efforts have demonstrated different BLE attacks. For instance, Ohio State University researchers have discovered different fingerprinting attacks that can allow an attacker to reveal design flaws and misconfigurations of BLE devices. Details about this research can be found at [_https://dl.acm.org/doi/pdf/10.1145/3319535.3354240_](https://dl.acm.org/doi/pdf/10.1145/3319535.3354240).

Radio-frequency identification (RFID) is a technology that uses electromagnetic fields to identify and track tags that hold electronically stored information.

- Attackers can silently steal RFID information (such as a badge or a tag) with an RFID reader such as the Proxmark3 ([_https://proxmark.com_](https://proxmark.com/)) by just walking near an individual or a tag.
  
  **_Password spraying_** is a type of credential attack in which an attacker brute-forces logins (that is, attempts to authenticate numerous times) based on a list of usernames with default passwords of common systems or applications. For example, an attacker could try to log in with the word password1 using numerous usernames in a wordlist.

A similar attack is credential stuffing. In this type of attack, the attacker performs automated injection of usernames and passwords that have been exposed in previous breaches. You can learn more about credential stuffing attacks at [_https://owasp.org/www-community/attacks/Credential_stuffing_](https://owasp.org/www-community/attacks/Credential_stuffing).

Most sophisticated attacks leverage multiple vulnerabilities to compromise systems. An attacker may “chain” (that is, use multiple) exploits against known or zero-day vulnerabilities to compromise systems, steal, modify, or corrupt data.

![[Pasted image 20251109215941.png]]

NetBIOS provides three different services:

- NetBIOS Name Service (NetBIOS-NS) for name registration and resolution
- Datagram Service (NetBIOS-DGM) for connectionless communication
- Session Service (NetBIOS-SSN) for connection-oriented communication

NetBIOS-related operations use the following ports and protocols:

- **TCP port 135:** Microsoft Remote Procedure Call (MS-RPC) endpoint mapper, used for client-to-client and server-to-client communication
- **UDP port 137:** NetBIOS Name Service
- **UDP port 138:** NetBIOS Datagram Service
- **TCP port 139:** NetBIOS Session Service
- **TCP port 445:** SMB protocol, used for sharing files between different operating systems, including Windows and Unix-based systems

open-source tool that is very popular and has even been used by malware is Pupy, which is available on GitHub. Pupy is a Python-based cross-platform remote administration and post-exploitation tool that works on Windows, Linux, macOS and even Android.

Simple Network Management Protocol (SNMP) is a protocol that many individuals and organizations use to manage network devices. SNMP uses UDP port 161. In SNMP implementations, every network device contains an SNMP agent that connects with an independent SNMP server (also known as the SNMP manager)

Mimikatz is a tool used by many penetration testers, attackers, and even malware that can be useful for retrieving password hashes from memory; it is a very useful post-exploitation tool. You can download the Mimikatz tool from [_https://github.com/gentilkiwi/mimikatz_](https://github.com/gentilkiwi/mimikatz). Metasploit also includes Mimikatz as a Meterpreter script to facilitate exploitation without the need to upload any files to the disk of the compromised host. You can find more information about Mimikatz/Metasploit integration at [_https://www.offensive-security.com/metasploit-unleashed/mimikatz/_](https://www.offensive-security.com/metasploit-unleashed/mimikatz/).

Empire is a popular tool that can be used to perform golden ticket and many other types of attacks. Empire is basically a post-exploitation framework that includes a pure-PowerShell Windows agent and a Python agent. You will learn more about post-exploitation methodologies later in this module. With Empire, you can run PowerShell agents without needing to use powershell.exe. You can download Empire and access demonstrations, presentations, and documentation at [_https://github.com/BC-SECURITY/Empire_](https://github.com/BC-SECURITY/Empire)

**_Kerberoasting_** is a post-exploitation activity that is used by an attacker to extract service account credential hashes from Active Directory for offline cracking.

In an **_on-path attack_** (previously known as a man-in-the-middle [MITM] attack), an attacker places himself or herself in-line between two devices or individuals that are communicating in order to eavesdrop (that is, steal sensitive data) or manipulate the data being transferred (such as by performing data corruption or data modification).

**_ARP cache poisoning_** (also known as ARP spoofing) is an example of an attack that leads to an on-path attack scenario. An ARP spoofing attack can target hosts, switches, and routers connected to a Layer 2 network by poisoning the ARP caches of systems connected to the subnet and intercepting traffic intended for other hosts on the subnet.

**_Media Access Control (MAC) spoofing_** is an attack in which a threat actor impersonates the MAC address of another device (typically an infrastructure device such as a router). The MAC address is typically a hard-coded address on a network interface controller. In virtual environments, the MAC address could be a virtual address (that is, not assigned to a physical adapter). An attacker could spoof the MAC address of physical or virtual systems to either circumvent access control measures or perform an on-path attack.

 An attack tool called SSLStrip uses on-path functionality to transparently look at HTTPS traffic, hijack it, and return non-encrypted HTTP links to the user in response. This tool was created by a security researcher called Moxie Marlinspike. You can download the tool from [_https://github.com/moxie0/sslstrip_](https://github.com/moxie0/sslstrip).


The following are some additional Layer 2 security best practices for securing your infrastructure:

- Select an unused VLAN (other than VLAN 1) and use it as the native VLAN for all your trunks. Do not use this native VLAN for any of your enabled access ports. Avoid using VLAN 1 anywhere because it is the default.
- Administratively configure switch ports as access ports so that users cannot negotiate a trunk; also disable the negotiation of trunking (that is, do not allow Dynamic Trunking Protocol [DTP]).
- Limit the number of MAC addresses learned on a given port by using the port security feature.
- Control Spanning Tree to stop users or unknown devices from manipulating it. You can do so by using the BPDU Guard and Root Guard features.
- Turn off Cisco Discovery Protocol (CDP) on ports facing untrusted or unknown networks that do not require CDP for anything positive. (CDP operates at Layer 2 and might provide attackers information you would rather not disclose.)
- On a new switch, shut down all ports and assign them to a VLAN that is not used for anything other than a parking lot. Then bring up the ports and assign correct VLANs as the ports are allocated and needed.
- Use Root Guard to control which ports are not allowed to become root ports to remote switches.
- Use DAI.
- Use IP Source Guard to prevent spoofing of Layer 3 information by hosts.
- Implement 802.1X when possible to authenticate and authorize users before allowing them to communicate to the rest of the network.
- Use Dynamic Host Configuration Protocol (DHCP) snooping to prevent rogue DHCP servers from impacting the network.
- Use storm control to limit the amount of broadcast or multicast traffic flowing through a switch. An attacker could perform a **_packet storm_** (or broadcast storm) attack to cause a DoS condition. The attacker does this by sending excessive transmissions of IP packets (often broadcast traffic) in a network.
- Deploy access control lists (ACLs), such as Layer 3 and Layer 2 ACLs, for traffic control and policy enforcement.

![[Pasted image 20251109230804.png]]
Once we have gained access to a client’s LAN, we often will use a tool like Ettercap to conduct an on-path attack.

Border Gateway Protocol (BGP) is a dynamic routing protocol used to route Internet traffic. An attacker can launch a BGP hijacking attack by configuring or compromising an edge router to announce prefixes that have not been assigned to his or her organization.

Denial-of-service (DoS) and distributed DoS (DDoS) attacks have been around for quite some time, but there has been heightened awareness of them over the past few years. DoS attacks can generally be divided into three categories, described in the following sections:

- Direct
- Botnet
- Reflected
- Amplification
NAC is a technology that is designed to interrogate endpoints before joining a wired or wireless network. It is typically used in conjunction with 802.1X for identity management and enforcement.


**Vlan hopping**
One way to identify a LAN is to say that all the devices in the same LAN have a common Layer 3 IP network address and that they also are all located in the same Layer 2 broadcast domain. A virtual LAN (VLAN) is another name for a Layer 2 broadcast domain. A VLAN is controlled by a switch. The switch also controls which ports are associated with which VLANs. In Figure 5-12, if the switches are in their default configuration, all ports by default are assigned to VLAN 1, which means all the devices, including the two users and the router, are in the same broadcast domain, or VLAN.

Most organizations run DHCP servers. The two most popular attacks against DHCP servers and infrastructure are _DHCP starvation_ and _DHCP spoofing_ (which involves rogue DHCP servers). In a DHCP starvation attack, an attacker broadcasts a large number of DHCP REQUEST messages with spoofed source MAC addresses

Most organizations run DHCP servers. The two most popular attacks against DHCP servers and infrastructure are _DHCP starvation_ and _DHCP spoofing_ (which involves rogue DHCP servers). In a DHCP starvation attack, an attacker broadcasts a large number of DHCP REQUEST messages with spoofed source MAC addresses









