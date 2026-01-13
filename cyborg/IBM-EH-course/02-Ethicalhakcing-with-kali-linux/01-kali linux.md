## Objectives

Securing a Kali Linux system requires a proactive approach. This basic guide outlines essential steps, such as enabling secure SSH access, performing regular data backups, and deploying Intrusion Detection and Prevention Systems (IDPS). Each recommendation helps strengthen system security and ensures operational continuity in the event of an incident.

After completing this reading, you will be able to:

- Apply best practices to secure a Kali Linux installation

## Best Practices

|Best Practice|Explanation|Commands and Tools|
|---|---|---|
|Update operating system|Regularly updating Kali Linux ensures the operating system remains secure, stable, and equipped with the latest tools and features. Updates often include patches for vulnerabilities, improvements to performance, and compatibility with new or updated tools. Keeping the system up to date minimizes risk and ensures optimal functionality for penetration testing and security research.|`$ sudo apt update`  <br>`$ sudo apt upgrade`|
|Manage user access and privileges|Properly managing user access and privileges prevents unauthorized access and reduces the risk of accidental or intentional modifications to the system. Using the principle of least privilege, you can ensure that users and services only have the permissions vital for their roles, limiting potential damage in the event of a breach.|`$ sudo adduser <username>`  <br>`$ sudo usermod -aG sudo <username>`  <br>`$ sudo chmod <permissions> <file/directory>`  <br>`$ sudo chown <user>:<group> <file/directory>`|
|Use Two-Factor Authentication|Implementing Two-Factor Authentication (2FA) adds an extra layer of security by requiring a password and a second factor, such as a hardware token or a verification code sent to a mobile device. It helps prevent unauthorized access, even in cases where passwords are compromised.|Google Authenticator  <br>FreeOTP|
|Disable services that are not in use|Unused services running on a system can create vulnerabilities and expose unnecessary attack surfaces. Turning off such services minimizes system resource consumption and reduces potential security risks by eliminating unneeded entry points for attackers.|`@ systemctl list-unit-files \| grep enabled`  <br>`$systemctl disable <service_name>`  <br>`$sudo service <service_name> stop`|
|Configure a firewall|A properly configured firewall acts as a protective barrier between your system and external threats by controlling incoming and outgoing network traffic. It prevents unauthorized access while ensuring legitimate communication. Tools like **ufw** make managing firewalls straightforward, even for less experienced users.|`$ sudo apt install ufw`  <br>`$ sudo ufw enable`  <br>`$ sudo ufw default deny incoming`  <br>`$ sudo ufw default allow outgoing`  <br>`$ sudo ufw allow <port/service>`|
|Encrypt sensitive data|Encrypting sensitive data ensures that critical information remains protected from unauthorized access, even if the system is compromised. Encryption tools transform data into unreadable formats only accessible by authorized users with the correct decryption key.|VeraCrypt  <br>GPG (GNU Privacy Guard)|
|Secure remote access|Securing remote access ensures that connections to your machine from remote locations are safe from eavesdropping, interception, or unauthorized access. Protocols like SSH (Secure Shell) provide encrypted communication, preventing sensitive data from being intercepted during transit.|`$ sudo apt install openssh-server`  <br>Edit **/etc/ssh/sshd_config** to disable root login and change the default SSH port  <br>`$ sudo systemctl restart ssh`|
|Backup data|Regular backups protect against data loss caused by hardware failure, accidental deletion, or cyberattacks such as ransomware. A comprehensive backup strategy ensures quick recovery and continuity in critical situations.|Rsync  <br>Timeshift  <br>Backup utilities included with Kali|
|Intrusion detection and prevention systems|Intrusion Detection and Prevention Systems (IDPS) monitor network traffic and system activity to identify and thwart malicious actions. These systems serve as an early warning system and actively block potential threats, providing a robust layer of defense against attacks.|Snort  <br>Suricata  <br>OSSEC|


Regular maintenance, monitoring, and the right tools can significantly reduce risks and help maintain a secure and reliable environment. Protecting your system is an ongoing process that you should continuously review and improve.

## Tools
#tools
- **Metasploit** for pen testing
- **Nmap** for network scanning
- **Wireshark** for traffic analysis
- **Splunk** for log collectoin and analysis
- **Nessus** or **openVAS** for scanning for vulnerabilities
- **OWASP Juice shop** for web application vulnerabilities
- **Snort** intrusion detection system (IDS) and intrusion prevention system (IPS)
- _Suricata_ is a high performance, open source network analysis and threat detection software used by most private and public organizations.
- _Zeek_ (formerly _Bro_) is the world's leading platform for network security monitoring. Flexible, open source, and powered by defenders.
- OSSEC is a full platform to monitor and control your systems. It mixes together all the aspects of HIDS (host-based intrusion detection), log monitoring and SIM/SIEM together in a simple, powerful and open source solution.
- **ClamAV** is **an open-source (general public license [GPL]) antivirus engine used in a variety of situations, including email and web scanning, and endpoint security**.
- _Rootkit Hunter_ is a command-line scanner for Unix-like systems that looks for known rootkits, backdoors, and local exploits.


**Open source intelligence** (OSINT) is the process of gathering and analyzing publicly available information to assess threats, make decisions or answer specific questions. Many organizations use OSINT as a cybersecurity tool to help gauge security risks and identify vulnerabilities in their IT systems.


### Automating OSINT - #tools
- TheHarvester
- Whois database
- Recon-ng
- Maltego
- SET - social engineering toolkit
- BeEF - Browser exploitation Framework

## Internet Information Gathering
#tools

|**Tool Name**|**Interface**|**Description**|
|---|---|---|
|theHarvester|Command line|Collects emails, subdomains, and hostnames from public sources like search engines and social media.|
|Maltego|GUI|Provides a graphical interface to map relationships between entities like domains, people, and networks.|
|Recon-ng|Command line|A modular framework for gathering OSINT (Open-Source Intelligence) data from various sources.|
|Whois|Command line|Queries domain registration data to retrieve publicly available information about domain ownership.|
|Dig|Command line|Queries DNS servers to retrieve DNS records (IP address, Mail Exchange, CNAME, etc.)|

## Social Engineering Attacks

|**Tool Name**|**Interface**|**Description**|
|---|---|---|
|Social Engineering Toolkit (SET)|Command line|A framework for simulating social engineering attacks, including phishing and credential harvesting.|
|BeEF (Browser Exploitation Framework)|GUI|Exploits browser vulnerabilities to perform social engineering and gather information.|

## Network Host Scanning

|**Tool Name**|**Interface**|**Description**|
|---|---|---|
|Nmap|Command line|Scans networks to discover hosts, open ports, and services. Helps identify ports, enumerate services, and fingerprint operating systems.|
|Netdiscover|Command line|Identifies live hosts on a network using ARP requests.|
|Masscan|Command line|A high-speed port scanner capable of scanning large networks.|
|Wireshark|GUI|A network protocol analyzer captures and analyzes network traffic, helping identify hosts and network issues.|
|Ping|Command line|Sends an ICMP echo request packet to a host and waits for an ICMP echo reply to check if the host is active.|
|ARP-scan|Command line|Maps IP addresses to MAC addresses within a network by sending ARP requests to identify active hosts.|
|Zenmap|GUI|A user-friendly version of Nmap designed for both new and advanced users.|

## Digital Forensics Tools
#tools 
The following list is just some of the digital forensics tools available with Kali Linux:

### Forensic Carving Tools

|Tool Name|Interface|Description|
|---|---|---|
|MagicRescue|Command line|A file carving tool that recovers deleted files by searching for specific file type signatures.|
|Scalpel|Command line|A file carving tool used to recover deleted files based on header/footer patterns.|
|Scrounge-NTFS|Command line|A recovery tool designed to reconstruct NTFS file systems and recover files from damaged or corrupted partitions.|

### Forensic Imaging Tools

|Tool Name|Interface|Description|
|---|---|---|
|Guymager|GUI|A forensic imaging tool for creating exact copies of digital storage devices while ensuring data integrity.|

### PDF Forensics Tools

|Tool Name|Interface|Description|
|---|---|---|
|PDFiD|Command line|A lightweight PDF scanning tool that detects suspicious elements such as JavaScript or embedded files for quick analysis.|
|PDF-Parser|Command line|A detailed PDF analysis tool that allows in-depth inspection of a PDF\'s objects, streams, and potentially malicious content.|

### The SLeuth Kit

| Tool Name | Interface    | Description                                                                                                                           |
| --------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| Autopsy   | GUI          | A user-friendly forensic platform built on The Sleuth Kit, offering easy access to forensic tools for analyzing disk images and data. |
| Blkcat    | Command line | A Sleuth Kit tool that extracts specific blocks from file systems for forensic analysis.                                              |
| Blkls     | Command line | A Sleuth Kit tool that retrieves unallocated file system space to recover deleted files.                                              |
| Blkstat   | Command line | A Sleuth Kit utility that provides detailed information about file system blocks for investigative purposes.                          |
| img_cat   | Command line | A Sleuth Kit tool to extract raw data from disk images for further analysis.                                                          |
| img_stat  | Command line | A Sleuth Kit utility that provides metadata and detailed statistics about disk images.                                                |
| mactime   | Command line | A Sleuth Kit tool that creates timelines based on file timestamps (Modification, Access, Change) for chronological analysis.          |

## Network Vulnerability Analysis

Network vulnerability tools identify weaknesses in a network's infrastructure, such as open ports, misconfigured firewalls, or outdated protocols.

|**Tool Name**|**Interface**|**Description**|
|---|---|---|
|Nmap|Command line|Scans networks to identify open ports, misconfigurations, and protocol vulnerabilities.|
|Nessus|GUI|Performs in-depth vulnerability scanning to identify security risks in the network environment.|
|OpenVAS|GUI|Detects misconfigurations, open ports, and protocol vulnerabilities across networks.|
|Wireshark|GUI|Captures and inspects live data traffic to diagnose issues or detect potential security threats.|

## Web Application Vulnerability Analysis

Web application vulnerability analysis targets weaknesses in web applications such as SQL injection, cross-site scripting (XSS), or insecure authentication methods.

|**Tool Name**|**Interface**|**Description**|
|---|---|---|
|Burp Suite|GUI|Tests web applications for vulnerabilities like SQL injection, cross-site scripting (XSS), and insecure authentication mechanisms.|
|Nikto|Command line|Scans web servers for dangerous files, outdated software, and common security issues.|
|OWASP ZAP|GUI|Identifies vulnerabilities in web applications, including XSS and SQL injection.|

## Wireless Network Analysis

Wireless network analysis examines the security of wireless networks, including Wi-Fi encryption and authentication protocols. It also evaluates susceptibility to attacks like de-authentication or key cracking.

| **Tool Name** | **Interface** | **Description**                                                                      |
| ------------- | ------------- | ------------------------------------------------------------------------------------ |
| Aircrack-ng   | Command line  | Analyzes wireless networks, focusing on weak encryption (e.g., WEP vulnerabilities). |
| Kismet        | GUI           | Monitors wireless networks and detects unauthorized access points.                   |

## System Vulnerability Analysis

System vulnerability analysis focuses on identifying vulnerabilities in operating systems, such as unpatched software, weak passwords, or privilege escalation risks.

|**Tool Name**|**Interface**|**Description**|
|---|---|---|
|Lynis|Command line|Audits operating systems and installed software for outdated versions, misconfigurations, and missing security patches.|
|SQLmap|Command line|Automates detecting and exploiting SQL injection flaws in database systems, analyzing permissions and configurations.|
|Metasploit|GUI|Identifies, exploits, and validates vulnerabilities in systems and networks.|

## Database Vulnerability Analysis

Database vulnerability analysis targets weaknesses in database systems, such as misconfigurations, weak credentials, or SQL injection vulnerabilities.

| **Tool Name**  | **Interface** | **Description**                                                                      |
| -------------- | ------------- | ------------------------------------------------------------------------------------ |
| SQLmap         | Command line  | Used for detecting and exploiting SQL injection vulnerabilities in web applications. |
| SQLninja       | GUI           | Used for data extraction, database fingerprinting, and detecting SQL injections.     |
| jSQL Injection | GUI           | Used for detecting and exploiting SQL injection vulnerabilities in web applications. |

```sh
nmap -A scanme.nmap.org
```
2. Analyze the output:
    
    - **Port:** Provides the same port information as the aggressive scan
    - **State:** Provides the same state information as the aggressive scan
    - **Service:** Probes deeply to confirm and detail the services running on each port
    - **Version:** Focuses on service version detection
    - **Operating system fingerprinting:** Provides an estimate of the OS running on the target system, based on observed behaviors during the scan
    - **Traceroute:** Maps the network path from the scanning machine to the target device, identifying network hops


## Password Attack Tools
#tools 

Password attack tools are designed to crack passwords. These passwords can be used to gain unauthorized access to systems or data. They often use techniques like brute force, dictionary attacks, and rainbow tables.

|Tool Name|Interface|Description|
|---|---|---|
|Cewl|Command line|A custom word list generator that spiders a given URL and returns a list of words that can be used for password cracking.|
|Crunch|Command line|A wordlist generator that lets users create lists of words by combining and mixing any set of characters they choose.|
|Hashcat|Command line|A password cracker that works with different hashing methods and attack types, such as dictionary, brute-force, and custom attacks.|
|Hydra|Command line|A fast login cracker that supports numerous protocols to attack. Hydra is parallelized, meaning the tool can perform multiple tasks simultaneously rather than sequentially, making it process faster and more efficiently.|
|John|Command line|A password-cracking tool that supports many encryption technologies and can autodetect the encryption for common formats.|
|Medusa|Command line|A fast, parallel login brute-force tool that supports many remote authentication services. It allows security professionals to test multiple login credentials simultaneously, efficiently identifying weak passwords.|
|Ncrack|Command line|A high-speed network authentication cracking tool designed to help companies secure their networks by testing for poor passwords.|
|Ophcrack|GUI/Command line|A Windows password cracker that uses rainbow tables to recover most alphanumeric passwords quickly.|
|Wordlists|N/A|A collection of wordlists used for password cracking, including the popular rockyou.txt.|

### Exploitation Tools

Exploitation tools exploit vulnerabilities in systems, applications, or networks. They help gain unauthorized access, escalate privileges, or maintain access. The following exploitation tools are included with the Kali Linux system:

|Tool Name|Interface|Description|
|---|---|---|
|CrackMapExec|Command line|A versatile tool for testing Windows/Active Directory security. It can list users, scan shared files, run remote commands, and perform other security tests.|
|Metasploit-framework|GUI/Command line|A widely used framework for developing, testing, and executing exploits.|
|MSFvenom Payload Creator (MSFPC)|Command line|A tool to generate Metasploit payloads for various platforms.|
|Netexec|Command line|A tool for executing commands on remote systems over the network.|
|SearchSploit|Command line|Searchsploit is a tool that lets you quickly find exploits and vulnerabilities in the Exploit-DB database using the command line. It helps security professionals locate relevant exploits for testing systems.|
|Setoolkit|GUI/Command line|The Social-Engineer Toolkit is designed for social engineering attacks, including phishing, credential harvesting, and more.|
|SQLmap|Command line|An open-source penetration testing tool that automates detecting and exploiting SQL injection flaws.|
## Types of Sniffing

Sniffing can be either Active or Passive in nature.

### Passive Sniffing

In passive sniffing, the traffic is locked but it is not altered in any way. Passive sniffing allows listening only. It works with Hub devices. On a hub device, the traffic is sent to all the ports. In a network that uses hubs to connect systems, all hosts on the network can see the traffic. Therefore, an attacker can easily capture traffic going through.

The good news is that hubs are almost obsolete nowadays. Most modern networks use switches. Hence, passive sniffing is no more effective.
- Monitor network traggic with out detection
- Diagnose network issues
- Analyze traffic patterns
- Identiry potential anomalies non-invasively

### Active Sniffing

In active sniffing, the traffic is not only locked and monitored, but it may also be altered in some way as determined by the attack. Active sniffing is used to sniff a switch-based network. It involves injecting **address resolution packets** (ARP) into a target network to flood on the switch **content addressable memory** (CAM) table. CAM keeps track of which host is connected to which port.

- Penetrate network to uncover vulnerabilities
- Apply in controlled env
- Simulate real world attacks

### Spoofing
Impersonate another device,system or user
- IP spoofing
- DNS spoofing
- MAC address spoofing


# Spoofing
Spoofing is a type of cybercriminal activity where someone or something forges the sender's information and pretends to be a legitimate source, business, colleague, or other trusted contact for the purpose of gaining access to personal information, acquiring money, spreading malware, or stealing data.

These tools are designed to capture, analyze, and monitor network traffic, helping security professionals identify vulnerabilities and optimize network performance. Let's explore the descriptions of the key sniffing tools.
#tools 

|Tool Name|Interface|Description|
|---|---|---|
|Dnschef|Command line|A DNS proxy tool intercepts and manipulates DNS traffic for testing or redirection during penetration tests.|
|Dsniff|Command line|A collection of network auditing and penetration testing tools specializing in capturing and analyzing plaintext data.|
|Netsniff-ng|Command line|A high-performance network analyzer and packet sniffer for capturing traffic with minimal system resource usage.|

## Spoofing and MITM Tools

Tools in this category simulate identity deception and man-in-the-middle attacks to test system defenses against interception and manipulation of network communications.  
Let's explore the descriptions of the key spoofing and MITM tools.

|Tool Name|Interface|Description|
|---|---|---|
|DNS-rebind|Command line|A testing tool that exploits DNS rebinding vulnerabilities to simulate cross-origin attacks on vulnerable systems.|
|Sslsplit|Command line|A tool to perform man-in-the-middle (MITM) attacks on SSL/TLS connections by intercepting and decrypting encrypted traffic.|
|tcpreplay|Command line|A network traffic replay tool that allows testers to replicate captured traffic to test and validate network configurations.|

## Other Sniffing and Spoofing Tools

This collection features versatile tools that perform advanced network analysis, packet manipulation, and system spoofing to expose security gaps and strengthen defenses.

| Tool Name       | Interface                  | Description                                                                                                             |
| --------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Ettercap-plexec | Command line               | A network security tool capable of conducting MITM attacks, packet sniffing, and active protocol dissection.            |
| Macchanger      | Command line               | A utility to change MAC addresses of network interfaces to test network security or bypass access controls.             |
| Minicom         | Text-based UI              | A serial communication tool used for debugging and interacting with connected devices over serial ports.                |
| Mitmproxy       | Command line/Text-based UI | An interactive HTTPS proxy tool for intercepting, inspecting, and modifying HTTP and HTTPS requests and responses.      |
| Responder       | Command line               | A tool for spoofing authentication responses and collecting credentials in LAN environments during penetration testing. |
| Scapy           | Command line               | A packet manipulation tool used for creating, sending, and analyzing custom network packets for security testing.       |
| Tcpdump         | Command line               | A command-line packet analyzer for capturing and diagnosing network traffic.                                            |
| Wireshark       | GUI                        | A packet capture and analysis tool with a GUI interface for inspecting detailed network traffic.                        |

## Summary

In this reading, you learned about sniffing and spoofing tools in Kali Linux:

- Sniffing tools capture and analyze network traffic to identify vulnerabilities.
- Tools such as Dnschef and Dsniff monitor DNS and plaintext data.
- MITM tools simulate interception attacks to test system defenses.
- Sslsplit and DNS-rebind perform encrypted traffic manipulation.
- Versatile tools such as Wireshark, Scapy, and Responder enhance packet analysis and credential testing.
- These tools help penetration testers uncover security gaps and optimize network defenses.

# Mobile tools
## Kali NetHunter

NetHunter tools are used in ethical hacking scenarios to assess system and network vulnerabilities.

## Tools in Kali NetHunter

Let's explore the key tools in Kali NetHunter.

| Tool Name             | Interface        | Description                                                                                                                                                  |
| --------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Metasploit            | Command line/GUI | An exploitation framework optimized for NetHunter, allowing ethical hackers to create and deploy payloads directly from mobile devices.                      |
| Network analysis tool | GUI              | A packet analysis tool adapted for NetHunter, enabling real-time traffic capture and inspection for uncovering network vulnerabilities.                      |
| Wireshark             | Command line     | A network scanner tailored for NetHunter, used to map network structures, identify active hosts, and discover open ports.                                    |
| Nmap                  | Command line     | A password-cracking tool in NetHunter, designed to perform brute force and dictionary attacks on various protocols to test password robustness.              |
| Hydra                 | Command line     | A password-cracking tool in NetHunter, designed to perform brute force and dictionary attacks on various protocols to test password robustness.              |
| Crunch                | Command line     | A password list generator optimized for NetHunter, capable of creating custom wordlists for targeted penetration tests.                                      |
| Aircrack-ng           | Command line     | A wireless security tool integrated into NetHunter, used for cracking Wi-Fi encryption and testing wireless network defenses.                                |
| Reaver                | Command line     | A Wi-Fi security tool configured for NetHunter, allowing ethical hackers to perform advanced WPS attacks and assess wireless vulnerabilities.                |
| Apktool               | Command line     | A reverse engineering tool in NetHunter used to decompile and recompile Android applications, assisting in identifying vulnerabilities.                      |
| JADX                  | GUI              | A graphical tool in NetHunter that simplifies the analysis of Android application code by decompiling APKs into readable formats.                            |
| Netcat                | Command line     | A networking tool optimized for NetHunter to perform port scanning, banner grabbing, and crafting raw network connections for exploitation testing.          |
| BusyBox               | Command line     | A lightweight utility suite adapted for NetHunter, providing essential Unix tools for managing filesystems and executing system commands during assessments. |


a powerful mobile penetration testing platform, and its key tools used in ethical hacking.

- Metasploit enables payload creation and deployment for exploitation testing.
- Network analysis tools help inspect real-time traffic and identify vulnerabilities.
- Password-cracking tools like Hydra and Crunch test password strength and generate wordlists.
- Wireless security tools such as Aircrack-ng and Reaver assess Wi-Fi network defenses.
- Reverse engineering tools like Apktool and JADX decompile Android apps to detect flaws.
- Utility tools like Netcat and BusyBox support scanning and command execution during assessments.



#cheatsheet #tools 
Kali Linux tools are generally categorized as follows:

- **Information gathering**
    
    - **Social engineering attacks:** Techniques to manipulate individuals into disclosing sensitive information through psychological tactics.
    - **Network host scanning:** Identifying active devices and services on a network to gather information.
- **Vulnerability analysis**
    
    - **Network vulnerability analysis:** The identification of weaknesses in network configurations or defenses.
    - **Web application vulnerability analysis:** The assessment of web applications to uncover flaws that could be exploited.
    - **Wireless network analysis:** The evaluation of wireless network security to identify encryption weaknesses or unauthorized access points.
    - **System vulnerability analysis:** The detection of vulnerabilities within operating systems and applications.
    - **Database vulnerability analysis:** The examination of database systems for misconfigurations or exploitable security flaws.
- **Exploitation**
    
    - **Password Attack Tools:** Tools designed to crack or guess passwords to gain access to systems or accounts.
    - **Exploitation Tools:** Utilities that exploit system, network, or application vulnerabilities to perform actions like privilege escalation or unauthorized access.
- **Sniffing and Spoofing**
    
    - **Network Sniffers:** Tools that capture and analyze network traffic without altering it.
    - **Spoofing and MITM Tools:** Tools used to impersonate devices or intercept and manipulate traffic in a man-in-the-middle attack.
    - **Other Sniffing and Spoofing Tools:** Additional utilities that support traffic monitoring and manipulation.
- **Forensics**
    
    - **Forensic Carving Tools:** Utilities that extract specific data types from storage media using file signatures.
    - **Forensic Imaging Tools:** Tools that create exact bit-by-bit copies of digital storage devices for analysis.
    - **PDF Forensic Tools:** Applications that analyze and extract information from PDF files to identify malicious content or recover data.
    - **The Sleuth Kit:** A collection of command-line tools for investigating and analyzing disk images and file systems.























