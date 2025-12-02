- **DevHints Bash Shell Programming Cheat Sheet:** [_https://devhints.io/bash_](https://devhints.io/bash)
- **Linux Config Bash Scripting Tutorial:** [_https://linuxconfig.org/bash-scripting-tutorial_](https://linuxconfig.org/bash-scripting-tutorial)

- **Ruby in Twenty Minutes tutorial**: [_https://www.ruby-lang.org/en/documentation/quickstart/_](https://www.ruby-lang.org/en/documentation/quickstart/)
- **Learn Ruby Online interactive Ruby tutorial**: [_https://www.learnrubyonline.org_](https://www.learnrubyonline.org/)
- **A GitHub repository that includes a community-driven collection of awesome Ruby libraries, tools, frameworks, and software**: [_https://github.com/markets/awesome-ruby_](https://github.com/markets/awesome-ruby)

**Nslookup, Host, and Dig**

You can use DNS-based tools like **_Nslookup_**, Host, and Dig to perform passive reconnaissance. Example 10-1 shows Nslookup output for store.h4cker.org. This domain is a canonical name (CNAME) that is associated with pentestplus.github.io. The website is hosted on GitHub, and there are a few IP addresses that resolve to that name (185.199.108.153, 185.199.109.153, 185.199.110.153, and 185.199.111.153).

**Whois**

The Internet Corporation for Assigned Names and Numbers (ICANN) is the organization that supervises the Internet’s domains and that created the **_Whois_** Data Problem Reporting System (WDPRS). Most Linux, Windows, and macOS versions support the Whois utility for querying the Whois database. You can also use Whois for reconnaissance. Unfortunately, because of the European Union’s General Data Protection Regulation (GDPR), the Whois database has been restricted to protect privacy. Example 10-3 shows the output of the Whois utility when querying the h4cker.org domain.

**FOCA**

**_Fingerprinting Organization with Collected Archives (FOCA)_** is a tool designed to find metadata and hidden information in documents. FOCA can analyze websites as well as Microsoft Office, Open Office, PDF, and other documents. You can download FOCA from _[https://github.com/ElevenPaths/FOCA](https://github.com/ElevenPaths/FOCA)_. FOCA analyzes files by extracting **_EXIF_** (exchangeable image file format) information from graphics files, as well as information discovered through the URL of a scanned website.

**ExifTool**

ExifTool is a popular tool for extracting EXIF information from images. EXIF is a standard that defines the formats for images, sound, and ancillary tags used by digital equipment such as digital cameras, mobile phones, and tablets. You can download ExifTool from _[https://exiftool.org](https://exiftool.org/)_. Example 10-4 shows output from ExifTool when it is run against an image called omar_pic.jpg.

**theHarvester**

**_theHarvester_** is a tool that can be used to enumerate DNS information about a given hostname or IP address. It can query several data sources, including Baidu, Google, LinkedIn, public Pretty Good Privacy (PGP) servers, Twitter, vhost, Virus Total, ThreatCrowd, CRT.SH, Netcraft, and Yahoo. Example 10-5 shows the different options of the theHarvester tool.

**Shodan**

**_Shodan_** is a search engine for devices connected to the Internet. Shodan continuously scans the Internet and exposes its results to users via its website ([_https:// www.shodan.io_](http://www.shodan.io/)) and via an API. Attackers can use this tool to identify vulnerable and exposed systems on the Internet (for example, misconfigured IoT devices, infrastructure devices). Penetration testers can use this tool to gather information about potentially vulnerable systems exposed to the Internet without actively scanning their victims. Figure 10-5 shows the results of a Shodan search for Cisco Smart Install client devices exposed to the Internet.

****Maltego**

**_Maltego_**, which gathers information from public records, is one of the most popular tools for passive reconnaissance. It supports numerous third-party integrations. There are several versions of Maltego, including a community edition (which is free) and several commercial Maltego client and server options. You can download and obtain more information about Maltego from [_https://www.paterva.com_](https://www.paterva.com/). Maltego can be used to find information about companies, individuals, gangs, educational institutions, political movement groups, religious groups, and so on. Maltego organizes query entities within the Entity Palette, and the search options are called “transforms.” Figure 10-6 shows a screenshot of the search results for a Person entity (in this case a search against this book’s coauthor Omar Santos). The results are hierarchical in nature, and you can perform additional queries/searches on the results (entities).

**Recon-ng**

**_Recon-ng_** is a menu-based tool that can be used to automate the information gathering of OSINT. Recon-ng comes with Kali Linux and several other penetration testing Linux distributions, and it can be downloaded from [_https://github.com/lanmaster53/recon-ng_](https://github.com/lanmaster53/recon-ng). Figure 10-8 shows the Recon-ng welcome menu.

**Censys**

**_Censys_**, a tool developed by researchers at the University of Michigan, can be used for passive reconnaissance to find information about devices and networks on the Internet. It can be accessed at [_https://censys.io_](https://censys.io/). Censys provides a free web and API access plan that limits the number of queries a user can perform. It also provides several other paid plans that allow for premium support and additional queries. Figure 10-9 shows a screenshot of the Censys website. Figure 10-9 displays the results for a query for 8.8.8.8 (Google’s public DNS server).

Zenmap is a graphical unit interface (GUI) tool for Nmap

**Enum4linux**

Enum4linux is a great tool for enumerating SMB shares, vulnerable Samba implementations, and corresponding users. Example 10-14 shows the output of a detailed scan using Enum4linux against the host with IP address 10.1.1.14 that was discovered by Nmap


# Common tools for vulnerability scanning
There are numerous vulnerability scanning tools, including open-source and commercial vulnerability scanners, as well as cloud-based services and tools. The following are some of the most popular vulnerability scanners:

- OpenVAS
- Nessus
- Nexpose
- Qualys
- SQLmap
- Nikto
- OWASP Zed Attack Proxy (ZAP)
- w3af
- DirBuster
- Brakeman
- Open Security Content Automation Protocol (SCAP) scanners
- Wapiti
- Scout Suite
- WPScan (Wordpress scanner)

**OpenVAS**

OpenVAS is an open-source vulnerability scanner that was created by Greenbone Networks. The OpenVAS framework includes several services and tools that enable you to perform detailed vulnerability scanning against hosts and networks.

Scout Suite 

Scout suite is a vulnerability scanner designed to assess the security posture of cloud environments.
The following are several additional tools that can be used to perform cloud-based assessments:

- **ScoutSuite:** This collection of tools can be used to reveal vulnerabilities in AWS, Azure, Google Cloud Platform, and other cloud platforms. You can download ScoutSuite from [_https://github.com/nccgroup/ScoutSuite_](https://github.com/nccgroup/ScoutSuite).
- **CloudBrute:** You can download this cloud enumeration tool from [_https://github.com/0xsha/CloudBrute_](https://github.com/0xsha/CloudBrute).
- **Pacu:** This is a framework for AWS exploitation that can be downloaded from [_https://github.com/RhinoSecurityLabs/pacu_](https://github.com/RhinoSecurityLabs/pacu).
- **Cloud Custodian:** This cloud security, governance, and management tool can be downloaded from [_https://cloudcustodian.io_](https://cloudcustodian.io/).

**Nexpose**

Nexpose is a vulnerability scanner created by Rapid7 that is very popular among professional penetration testers. It supports integrations with other security products. Rapid7 also has several vulnerability scanning solutions that are used for vulnerability management, continuous monitoring, and secure development lifecycle.

**Qualys**

Qualys is a security company that created one of the most popular vulnerability scanners in the industry. It also has a cloud-based service that performs continuous monitoring, vulnerability management, and compliance checking. This cloud solution interacts with cloud agents, virtual scanners, scanner appliances, and Internet scanners.

**SQLmap**

**_SQLmap_** is often considered a web vulnerability and SQL injection tool. It helps automate the enumeration of vulnerable applications, as well as the exploitation of SQL injection techniques that you learned in Module 6, “Exploiting Application-Based Vulnerabilities.” You can download SQLmap from [_http://sqlmap.org_](http://sqlmap.org/).
#lookup 
>You can practice your penetration testing skills by using tools such as SQLmap against vulnerable applications. The Art of Hacking GitHub repository includes a list of vulnerable servers and applications that you can download and use to practice your skills in a safe environment; see [_https://github.com/The-Art-of-Hacking/art-of-hacking/tree/master/vulnerable_servers_](https://github.com/The-Art-of-Hacking/art-of-hacking/tree/master/vulnerable_servers).

**Nikto**

**_Nikto_** is an open-source web vulnerability scanner that can be downloaded from [_https://github.com/sullo/nikto_](https://github.com/sullo/nikto). Nikto’s official documentation can be accessed at [_https://cirt.net/nikto2-docs_](https://cirt.net/nikto2-docs) . Example 10-18 shows the first few lines of Nikto’s man page.

**OWASP Zed Attack Proxy (ZAP)**

According to OWASP, **_OWASP Zed Attack Proxy (ZAP)_** “is one of the world’s most popular free security tools and is actively maintained by hundreds of international volunteers.” Many offensive and defensive security engineers around the world use ZAP, which not only provides web vulnerability scanning capabilities but also can be used as a sophisticated web proxy. ZAP comes with an API and also can be used as a fuzzer. You can download and obtain more information about OWASP ZAP from [_https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project_](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project).

**w3af**

Another popular open-source web application vulnerability scanner is **_w3af_**. w3af can be downloaded from [_https://github.com/andresriancho/w3af_](https://github.com/andresriancho/w3af), and its documentation can be obtained from [_https://docs.w3af.org/en/latest/_](https://docs.w3af.org/en/latest/). w3af is a vulnerability scanner that can also perform exploits.

**DirBuster**

_DirBuster_ is a tool that was designed to brute force directory names and filenames on web application servers. DirBuster is currently an inactive project, and its functionality has been integrated into and enhanced in OWASP ZAP as an add-on.DirBuster is a Java application designed to brute force directories and filenames on web/application servers. Often what looks like a web server with a default installation actually has pages and applications hidden within it. DirBuster attempts to find these. Two few additional alternatives to DirBuster are **_gobuster_** ([_https://github.com/OJ/gobuster_](https://github.com/OJ/gobuster)) and ffuf ([_https://github.com/ffuf/ffuf_](https://github.com/ffuf/ffuf)). Keep in mind that tools of this nature are often as only good as the directory and file lists they come with.

# Credential Attacks
The following are some of the most popular tools that can be used to brute force, crack, and compromise user credentials:

- John the Ripper
- Cain and Abel
- Hashcat
- Hydra
- RainbowCrack
- Medusa and Ncrack
- CeWL
- Mimikatz
- Patator

**John the Ripper**

**_John the Ripper_** is a very popular tool for offline password cracking. John the Ripper (or john for short) can use search patterns as well as password files (or wordlists) to crack passwords. It supports different cracking modes and understands many ciphertext formats, including several DES variants, MD5, and Blowfish. John the Ripper does not support AES and SHA-2. To list the supported formats, you can use the **john --list=formats** command, as shown in Example 10-25. John the Ripper can also be used to extract Kerberos AFS and Windows passwords. John the Ripper can be downloaded from [_https://www.openwall.com/john_](https://www.openwall.com/john).

#lookup 
> One of the most popular wordlists is the _rockyou_ wordlist, which includes thousands of passwords that have been exposed in real-world breaches. In addition, the following two sites have comprehensive lists of wordlists containing millions of passwords: [_https://www.openwall.com/wordlists_](https://www.openwall.com/wordlists) and [_https://github.com/berzerk0/Probable-Wordlists_](https://github.com/berzerk0/Probable-Wordlists).

**Cain**

**_Cain_** (or Cain and Abel) is a tool that can be used to “recover” passwords of Windows-based systems. Cain and Abel can be used to decipher and recover user credentials by performing packet captures (sniffing); cracking encrypted passwords by using dictionary, brute-force, and cryptanalysis attacks; and using many other techniques. Cain and Abel is a legacy tool, and archived information about it can be obtained from [_https://sectools.org/tool/cain/_](https://sectools.org/tool/cain/).

**Hashcat**

**_Hashcat_** is another password-cracking tool that is very popular among pen testers. It allows you to use graphical processing units (GPUs) to accelerate the password-cracking process. Hashcat comes with Kali Linux and other penetration testing Linux distributions. You can also download it from [_https://hashcat.net/hashcat_](https://hashcat.net/hashcat).

**Hydra**

**_Hydra_** is another tool that can be used to guess and crack credentials. Hydra is typically used to interact with a victim server (for example, web server, FTP server, SSH server, file server) and try a list of username/password combinations. For example, say you know that an FTP user’s username is omar. You can then try a file that contains a list of passwords against an FTP server (10.1.2.3). The Hydra tool, which is similar to Medusa, can be used to challenge remote logins using lists of usernames and passwords. In addition, it can target specific services, such as RDP. It differs from John the Ripper, which is used to crack already obtained lists of password hashes offline.

**RainbowCrack**

Attackers can use **_rainbow tables_** – precomputed tables for reversing cryptographic hash functions – to accelerate password cracking. It is possible to use a rainbow table to derive a password by looking at the hashed value. The tool RainbowCrack can be used to automate the cracking of passwords using rainbow tables. You can download RainbowCrack from [_http://project-rainbowcrack.com_](http://project-rainbowcrack.com/).

**Medusa and Ncrack**

The **_Medusa_** and Ncrack tools, which are similar to Hydra, can be used to perform brute-force credential attacks against a system. You can install Medusa by using the **apt install medusa** command in a Debian-based Linux system (such as Ubuntu, Kali Linux, or Parrot OS). You can download Ncrack from [_https://nmap.org/ncrack_](https://nmap.org/ncrack) or install it by using the **apt install ncrack** command.

**CeWL**

**_CeWL_** is a great tool that can be used to create wordlists. You can use CeWL to crawl websites and retrieve words. Example 10-38 shows how to use CeWL to create the wordlist words.txt by crawling the website [_https://theartofhacking.org_](https://theartofhacking.org/). You can download CeWL from [_https://digi.ninja/projects/cewl.php_](https://digi.ninja/projects/cewl.php)
**Mimikatz**

**_Mimikatz_** is a tool that many penetration testers and attackers (and even malware) use for retrieving password hashes from memory. It is also a useful post-exploitation tool. The Mimikatz tool can be downloaded from [_https://github.com/gentilkiwi/mimikatz_](https://github.com/gentilkiwi/mimikatz). Metasploit also includes Mimikatz as a Meterpreter script to facilitate exploitation without the need to upload any files to the disk of the compromised host. You can obtain more information about the Mimikatz and Metasploit integration at [_https://www.offsec.com/metasploit-unleashed/mimikatz/_](https://www.offsec.com/metasploit-unleashed/mimikatz/).

**Patator**

**_Patator_** is another tool that can be used for brute-force attacks on enumerations of SNMPv3 usernames, VPN passwords, and other types of credential attacks. You can download Patator from [_https://github.com/lanjelot/patator_](https://github.com/lanjelot/patator). Example 10-39 shows all the Patator modules.

In a pen testing engagement, you typically want to maintain stealth and try to evade and circumvent any security controls that the organization may have in place. Several tools and techniques can be used for evasion, including the following:

- Veil
- Tor
- Proxychains
- Encryption
- Encapsulation and tunneling using DNS and protocols such as NTP

**Veil**

Veil is a framework that can be used with Metasploit to evade antivirus checks and other security controls. You can download Veil from [_https://github.com/Veil-Framework/Veil_](https://github.com/Veil-Framework/Veil)

**Tor**

Many people use tools such as Tor for privacy. Tor is a free tool that enables its users to surf the Web anonymously. Tor works by “routing” IP traffic through a free worldwide network consisting of thousands of Tor relays. It constantly changes the way it routes traffic in order to obscure a user’s location from anyone monitoring the network. Tor’s name is an acronym of the original software project’s name, “The Onion Router.”

**Proxychains**

Proxychains can be used for evasion, as it is a tool that forces any TCP connection made by a specified application to use Tor or any other SOCKS4, SOCKS5, HTTP, or HTTPS proxy. You can download Proxychains from [_https://github.com/haad/proxychains_](https://github.com/haad/proxychains).


Several utilities have been created to perform DNS tunneling (for good reasons as well as harmful). The following are a few examples:

- **DeNiSe:** This Python tool is for tunneling TCP over DNS. You can download DeNiSe from [_https://github.com/mdornseif/DeNiSe_](https://github.com/mdornseif/DeNiSe).
- **dns2tcp:** Written by Olivier Dembour and Nicolas Collignon in C, dns2tcp supports KEY and TXT request types. You can download dns2tcp from [_https://github.com/alex-sector/dns2tcp_](https://github.com/alex-sector/dns2tcp).
- **DNScapy:** Created by Pierre Bienaimé, this Python-based Scapy tool for packet generation even supports SSH tunneling over DNS, including a SOCKS proxy. You can download DNScapy from [_https://github.com/FedericoCeratto/dnscapy_](https://github.com/FedericoCeratto/dnscapy).
- **DNScat or DNScat-P:** This Java-based tool, created by Tadeusz Pietraszek, supports bidirectional communication through DNS. You can download DNScat from [_https://github.com/iagox86/dnscat2_](https://github.com/iagox86/dnscat2).
- **DNScat2 (DNScat-B):** Written by Ron Bowes, this tool runs on Linux, macOS, and Windows. DNScat2 encodes DNS requests in NetBIOS encoding or hex encoding. You can download DNScat2 from [_https://github.com/iagox86/dnscat2_](https://github.com/iagox86/dnscat2).
- **Heyoka:** This Windows-based tool written in C supports bidirectional tunneling for data exfiltration. You can download Heyoka from [_http://heyoka.sourceforge.net_](http://heyoka.sourceforge.net/).
- **iodine:** Written by Bjorn Andersson and Erik Ekman in C, iodine runs on Linux, macOS, and Windows, and it can even be ported to Android. You can download iodine from [_https://code.kryo.se/iodine/_](https://code.kryo.se/iodine/).
- **sods:** Originally written in Perl by Dan Kaminsky, this tool is used to set up an SSH tunnel over DNS or for file transfer. The requests are Base32 encoded, and responses are Base64-encoded TXT records. You can download sods from [_https://github.com/msantos/sods_](https://github.com/msantos/sods).
- **psudp:** Developed by Kenton Born, this tool injects data into existing DNS requests by modifying the IP/UDP header lengths. You can obtain additional information about psudp from [_https://pdfs.semanticscholar.org/0e28/637370748803bcefa5b89ce8b48cf0422adc.pdf_](https://pdfs.semanticscholar.org/0e28/637370748803bcefa5b89ce8b48cf0422adc.pdf).
- **Feederbot and Moto:** Attackers have used this malware with DNS to steal sensitive information from many organizations. You can obtain additional information about these tools from [_https://chrisdietri.ch/post/feederbot-botnet-using-dns-command-and-control/_](https://chrisdietri.ch/post/feederbot-botnet-using-dns-command-and-control/).


**Metasploit**

**_Metasploit_** is by far the most popular exploitation framework in the industry. It was created by a security researcher named H. D. Moore and then sold to Rapid7. There are two versions of Metasploit: a community (free) edition and a professional edition.

Metasploit has several modules:

- auxiliary
- encoders
- exploits
- nops
- payloads
- post (for post-exploitation)

**BeEF**

BeEF is an exploitation framework for web application testing. BeEF exploits browser vulnerabilities and interacts with one or more web browsers to launch directed command modules. Each browser can be configured in a different security context. BeEF allows you to launch a set of unique attack vectors and select specific modules in real time to target each browser and context.

**OllyDbg**

**_OllyDbg_** is a debugger created to analyze Windows 32-bit applications. It is included in Kali Linux and other penetration testing distributions; it can also be downloaded from [_https://www.ollydbg.de_](https://www.ollydbg.de/).


**edb Debugger**

The edb debugger (often called Evan’s debugger) is a cross-platform debugger that supports AArch32, x86, and x86-64 architectures. It comes by default with Kali Linux, and it can be downloaded from [_https://github.com/eteran/edb-debugger_](https://github.com/eteran/edb-debugger).

**Ghidra**

**_Ghidra_** is a powerful and free tool popular among security researchers for reverse engineering and binary analysis. Developed by the NSA, Ghidra provides comprehensive capabilities for dissecting and understanding complex software, including malware analysis and vulnerability research. Its standout feature is a built-in decompiler that makes analyzing binary code more accessible. While it does not directly support exploit development, Ghidra's extensive scripting capabilities (with Java and Python-based APIs) allow users to create custom analysis scripts. You can download Ghidra from [_https://www.ghidra-sre.org/_](https://www.ghidra-sre.org/).

**Interactive Disassembler (IDA)**

**_Interactive Disassembler (IDA)_** is one of the most popular disassemblers, debuggers, and decompilers on the market. IDA is a commercial product of Hex-Rays, and it can be purchased from [_https://www.hex-rays.com/products/ida/index.shtml_](https://www.hex-rays.com/products/ida/index.shtml).

**Objdump**

Objdump is a Linux program that can be used to display information about one or more object files. You can use Objdump to do quick checks and disassembly of binaries

The following are a few examples of tools and Linux distributions that can be used for forensics:

- **ADIA (Appliance for Digital Investigation and Analysis)**: ADIA is a VMware-based appliance used for digital investigation and acquisition that is built entirely from public domain software. Among the tools contained in ADIA are Autopsy, the Sleuth Kit, the Digital Forensics Framework, log2timeline, Xplico, and Wireshark. Most of the system maintenance uses Webmin. ADIA is designed for small to medium-sized digital investigations and acquisitions. The appliance runs under Linux, Windows, and macOS. Both i386 (32-bit) and x86_64 (64-bit) versions are available. You can download ADIA from [_https://forensics.cert.org/#ADIA_](https://forensics.cert.org/#ADIA).
- **CAINE**: The Computer Aided Investigative Environment (CAINE) contains numerous tools that help investigators with analyses, including forensic evidence collection. You can download CAINE from [_http://www.caine-live.net/index.html_](http://www.caine-live.net/index.html).
- **Skadi**: This all-in-one solution to parsing collected data makes the data easily searchable with built-in common searches and enables searching of single and multiple hosts simultaneously. You can download Skadi from [_https://github.com/orlikoski/Skadi_](https://github.com/orlikoski/Skadi).
- **PALADIN**: PALADIN is a modified Linux distribution for performing various evidence collection tasks in a forensically sound manner. It includes many open source forensics tools. You can download PALADIN from [_https://sumuri.com/software/paladin/_](https://sumuri.com/software/paladin/).
- **Security Onion**: Security Onion, a Linux distro aimed at network security monitoring, features advanced analysis tools, some of which can help in forensic investigations. You can download Security Onion from [_https://github.com/Security-Onion-Solutions/security-onion_](https://github.com/Security-Onion-Solutions/security-onion).
- **SIFT Workstation**: The SANS Investigative Forensic Toolkit (SIFT) Workstation demonstrates that advanced incident response capabilities and deep-dive digital forensic techniques to intrusions can be accomplished using cutting-edge open source tools that are freely available and frequently updated. You can download SIFT Workstation from [_https://digital-forensics.sans.org/community/downloads_](https://digital-forensics.sans.org/community/downloads).

- _SpotBugs_ (previously known as Findbugs) is a static analysis tool designed to find bugs in applications created in the Java programming language. You can download and obtain more information about SpotBugs at [_https://spotbugs.github.io_](https://spotbugs.github.io/).
- _Findsecbugs_ is another tool designed to find bugs in applications created in the Java programming language. It can be used with continuous integration systems such as Jenkins and SonarQube. Findsecbugs provides support for popular Java frameworks, including Spring-MCV, Apache Struts, and Tapestry. You can download and obtain more information about Findbugs at [_https://find-sec-bugs.github.io_](https://find-sec-bugs.github.io/).
- _SonarQube_ is a tool that can be used to find vulnerabilities in code, and it provides support for continuous integration and DevOps environments. You can obtain additional information about SonarQube at [_https://www.sonarqube.org_](https://www.sonarqube.org/).
- _Fuzz testing_, or _fuzzing_ , is a technique that can be used to find software errors (or bugs) and security vulnerabilities in applications, operating systems, infrastructure devices, IoT devices, and other computing device. Fuzzing involves sending random data to the unit being tested in order to find input validation issues, program failures, buffer overflows, and other flaws. Tools that are used to perform fuzzing are referred to as _fuzzers_. Examples of popular fuzzers are Peach, Mutiny Fuzzing Framework, and American Fuzzy Lop.
- Peach is one of the most popular fuzzers in the industry. There is a free (open-source) version, the Peach Fuzzer Community Edition, and a commercial version. You can download the Peach Fuzzer Community Edition and obtain additional information about the commercial version at [_https://sourceforge.net/projects/peachfuzz/files/Peach/_](https://sourceforge.net/projects/peachfuzz/files/Peach/).
- The Mutiny Fuzzing Framework is an open-source fuzzer created by Cisco. It works by replaying packet capture files (pcaps) through a mutational fuzzer. You can download and obtain more information about Mutiny Fuzzing Framework at [_https://github.com/Cisco-Talos/mutiny-fuzzer_](https://github.com/Cisco-Talos/mutiny-fuzzer).
- American Fuzzy Lop (AFL) is a tool that provides features of compile-time instrumentation and genetic algorithms to automatically improve the functional coverage of fuzzing test cases. You can obtain information about AFL from [_https://lcamtuf.coredump.cx/afl/_](https://lcamtuf.coredump.cx/afl/).

## Wireless Tools

“Exploiting Wired and Wireless Networks,” discusses how to hack wireless networks. It discusses tools like Aircrack-ng, Kismet, KisMAC, and other tools that can be used to perform assessments of wireless networks. Refer to Module 5 for additional information about those tools.

The following are several wireless hacking tools that can help in testing wireless networks:

- **Wifite2:** This is a Python program to test wireless networks that can be downloaded from [_https://github.com/derv82/wifite2_](https://github.com/derv82/wifite2).
- **Rogue access points:** You can easily create rogue access points by using open-source tools such as hostapd. Omar Santos has a description of how to build your own wireless hacking lab and use hostapd at [_https://github.com/The-Art-of-Hacking/h4cker/blob/master/wireless_resources/virtual_adapters.md_](https://github.com/The-Art-of-Hacking/h4cker/blob/master/wireless_resources/virtual_adapters.md).
- **EAPHammer:** This tool, which you can use to perform evil twin attacks, can be downloaded from [_https://github.com/s0lst1c3/eaphammer_](https://github.com/s0lst1c3/eaphammer).
- **mdk4:** This tool is used to perform fuzzing, IDS evasions, and other wireless attacks. mdk4 can be downloaded from [_https://github.com/aircrack-ng/mdk4_](https://github.com/aircrack-ng/mdk4).
- **Spooftooph:** This tool is used to spoof and clone Bluetooth devices. It can be downloaded from [_https://gitlab.com/kalilinux/packages/spooftooph_](https://gitlab.com/kalilinux/packages/spooftooph).
- **Reaver:** This tool is used to perform brute-force attacks against Wi-Fi Protected Setup (WPS) implementations. Reaver can be downloaded from [_https://gitlab.com/kalilinux/packages/reaver_](https://gitlab.com/kalilinux/packages/reaver).
- **Wireless Geographic Logging Engine (WiGLE):** You can learn about this war driving tool at [_https://wigle.net_](https://wigle.net/).
- **Fern Wi-Fi Cracker:** This tool is used to perform different attacks against wireless networks, including cracking WEP, WPA, and WPS keys. You can download Fern Wi-Fi Cracker from [_https://gitlab.com/kalilinux/packages/fern-wifi-cracker_](https://gitlab.com/kalilinux/packages/fern-wifi-cracker).


## Steganography Tools
steganography is the act of hiding information in images, videos, and other files. You also learned about tools such as steghide. The following are a few additional tools that can be used to perform steganography:

- **OpenStego:** You can download this steganography tool from [_https://www.openstego.com_](https://www.openstego.com/).
- **snow:** This is a text-based steganography tool that can be downloaded from [_https://github.com/mattkwan-zz/snow_](https://github.com/mattkwan-zz/snow).
- **Coagula:** This program, which can be used to make sound from an image, can be downloaded from [_https://www.abc.se/~re/Coagula/Coagula.html_](https://www.abc.se/~re/Coagula/Coagula.html).
- **Sonic Visualiser:** This tool can be used to analyze embedded information in music or audio recordings. It can be downloaded from [_https://www.sonicvisualiser.org_](https://www.sonicvisualiser.org/).
- **TinEye:** This is a reverse image search website at [_https://tineye.com_](https://tineye.com/).
- **metagoofil:** This tool can be used to extract metadata information from documents and images. You can download metagoofil from [_https://github.com/laramies/metagoofil_](https://github.com/laramies/metagoofil).

## Cloud/IoT Tools

“Cloud, Mobile, and IoT Security,” you learned about a variety of tools that can be used to test cloud-based solutions. The following are several additional tools that can be used to perform cloud-based assessments:

- **ScoutSuite:** This collection of tools can be used to reveal vulnerabilities in AWS, Azure, Google Cloud Platform, and other cloud platforms. You can download ScoutSuite from [_https://github.com/nccgroup/ScoutSuite_](https://github.com/nccgroup/ScoutSuite).
- **CloudBrute:** You can download this cloud enumeration tool from [_https://github.com/0xsha/CloudBrute_](https://github.com/0xsha/CloudBrute).
- **Pacu:** This is a framework for AWS exploitation that can be downloaded from [_https://github.com/RhinoSecurityLabs/pacu_](https://github.com/RhinoSecurityLabs/pacu).
- **Cloud Custodian:** This cloud security, governance, and management tool can be downloaded from [_https://cloudcustodian.io_](https://cloudcustodian.io/).













