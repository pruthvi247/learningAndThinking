 [OpenVAS (Open Vulnerability Assessment System)](https://www.google.com/search?q=OpenVAS+%28Open+Vulnerability+Assessment+System%29&rlz=1C5CHFA_en&oq=openvas&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg8MgYIAhBFGDwyBggDEEUYPDIGCAQQRRg8MgYIBRBFGEHSAQgxNTM5ajBqMagCALACAA&sourceid=chrome&ie=UTF-8&mstk=AUtExfARpXr4K3dPwg8OkeDnvWuolLPb8wANVCAMB9aQuMnYYdIuhBnacdZGNdyE698WzEK-xRbFDph0t41LlD6nCYghf0P_K88x4IK-H_juovr-5rzCT88G_-_fIREoX0JFa1E&csui=3&ved=2ahUKEwip2NfJmqaSAxUw1TgGHXk5IMYQgK4QegQIARAB) is  a comprehensive, open-source framework for network-based vulnerability scanning and management, commonly used by IT and security teams to detect, analyze, and remediate security weaknesses. Now part of the [Greenbone Vulnerability Manager (GVM)](https://www.google.com/search?q=Greenbone+Vulnerability+Manager+%28GVM%29&rlz=1C5CHFA_en&oq=openvas&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg8MgYIAhBFGDwyBggDEEUYPDIGCAQQRRg8MgYIBRBFGEHSAQgxNTM5ajBqMagCALACAA&sourceid=chrome&ie=UTF-8&mstk=AUtExfARpXr4K3dPwg8OkeDnvWuolLPb8wANVCAMB9aQuMnYYdIuhBnacdZGNdyE698WzEK-xRbFDph0t41LlD6nCYghf0P_K88x4IK-H_juovr-5rzCT88G_-_fIREoX0JFa1E&csui=3&ved=2ahUKEwip2NfJmqaSAxUw1TgGHXk5IMYQgK4QegQIARAD), it identifies over 26,000+ vulnerabilities (CVEs) through credentialed and unauthenticated testing.

**Vulnerability assesment tools** #tools 
- OpenVAS
- Nessus
- Qualys
**Pentesting tools** #tools 
- Metasploit
- Cobalt Strike

## GVM Core Concepts and Terminology

This reading introduces the foundational concepts of Greenbone Vulnerability Management (GVM), the framework behind OpenVAS. It explains GVM's modular architecture, key components, terminology, and real-world applications. A solid understanding of these elements is essential for conducting effective vulnerability scans and managing risks using open-source or enterprise-grade GVM deployments.

## Overview

GVM is the integrated framework that powers OpenVAS — an open-source vulnerability scanning engine. This reading provides a foundational understanding of GVM’s architecture, essential components, and terminology. Mastering these concepts is critical for using OpenVAS effectively during vulnerability assessments.

## What is GVM?

GVM is a comprehensive, modular framework designed to manage the full lifecycle of vulnerability assessment, from scanning to reporting and remediation planning. Developed by Greenbone Networks, GVM integrates multiple components—each responsible for specific tasks—to ensure accurate detection of security flaws, flexible deployment, and enterprise-grade performance.

GVM powers both:

- The **Greenbone Community Edition (GCE)** – A free, open-source solution suitable for SMBs, labs, and educational use.
- The **Greenbone Enterprise Edition (GEE)** – A commercial variant offering professional support, expanded feeds, and tighter integration options for large-scale deployments.

GVM stands out in the vulnerability management ecosystem for its transparency, customizability, and alignment with open standards like CVE, CPE, CVSS, SCAP, and OVAL.

## Core components of GVM

|Component|Function|
|---|---|
|openvas-scanner|The engine that executes vulnerability tests (NVTs) on targets.|
|Gvmd|Greenbone Vulnerability Manager Daemon — manages users, scan tasks, results.|
|Gsad|Greenbone Security Assistant Daemon — provides the web interface.|
|Feeds|Regular updates of NVTs, CVEs, CPEs, and security advisories.|

These components communicate internally to support scanning operations, result management, and reporting.

## Key terminology

|Term|Definition|
|---|---|
|Network vulnerability test (NVT)|A script that tests for a specific vulnerability. Thousands are included in the feed.|
|Common vulnerabilities and exposures (CVE)|A globally recognized identifier for a known vulnerability.|
|Common platform enumeration (CPE)|A standardized way of naming software/hardware to match vulnerabilities.|
|VT family|A category of related NVTs (e.g., FTP checks, web servers).|
|Scan task|A defined job that includes scan targets, configurations, and schedules.|
|Result|The output from an NVT includes severity, impact, and references.|
|Override|Manual adjustment of the severity level of a result (e.g., for accepted risk).|
|Severity (CVSS)|The numerical risk score often derived from the CVSS (v3.x) system.|

## GVM workflow

The typical GVM vulnerability assessment flow includes:

1. **Configure target**  
    Define the asset to be scanned using an IP address, CIDR range, or hostname.
2. **Select scan config**  
    Choose a scan profile (e.g., _Full and Fast_, _Host Discovery_) tailored for depth, performance, or compliance.
3. **Run task**  
    The system launches the scan, invoking the openvas-scanner through the manager.
4. **Review report**  
    gvmd processes and scores the findings using CVSS, and gsad presents them through an interactive web UI.
5. **Export or remediate**  
    Users can export reports in formats like PDF, XML, or HTML, and begin patching or mitigation.

## Real-world example: CVE-2023-0669 – GoAnywhere MFT zero-day

In February 2023, attackers exploited a critical remote code execution (RCE) flaw in GoAnywhere MFT, a secure managed file transfer solution. Designated CVE-2023-0669, the vulnerability allowed unauthenticated attackers to execute arbitrary commands on vulnerable servers.

**How GVM helped:**

- Greenbone released updated **NVTs** within hours of public disclosure.
- Organizations that regularly synced their feeds detected affected systems before threat actors could exploit them.
- Systems were remediated before exfiltration or ransomware deployment occurred.

This example illustrates the **value of timely scan scheduling and up-to-date feeds** in mitigating zero-day risks.

## Importance of feeds

Feeds are the lifeblood of any vulnerability scanner. In GVM, they include:

- **NVTs**: Detection scripts for known vulnerabilities.
- **CVE mappings**: Link results to standardized identifiers.
- **CPEs**: Enable accurate asset identification.
- **SCAP/OVAL**: Support regulatory compliance and benchmark testing (e.g., CIS standards).

## Feed types

|Feed|Access level|Details|
|---|---|---|
|Greenbone community feed (GCF)|Free and open-source|Regular updates, but may lag behind emerging CVEs.|
|Greenbone enterprise feed (GEF)|Commercial license required|Faster NVT releases, extended checks, better zero-day support.|

## Summary

In this reading, you learned that:

- GVM is the ecosystem that powers OpenVAS, combining scanning, analysis, and reporting.
- Terms like NVT, CVE, CPE, and Severity Scores form the vocabulary of effective vulnerability management.
- GVM’s modular components allow for flexible deployment and automation.
- Real-world vulnerabilities like CVE-2023-0669 highlight the value of timely scan updates.
----------------------
# GVM Core Concepts and Terminology

This reading introduces the foundational concepts of Greenbone Vulnerability Management (GVM), the framework behind OpenVAS. It explains GVM's modular architecture, key components, terminology, and real-world applications. A solid understanding of these elements is essential for conducting effective vulnerability scans and managing risks using open-source or enterprise-grade GVM deployments.

## Overview

GVM is the integrated framework that powers OpenVAS — an open-source vulnerability scanning engine. This reading provides a foundational understanding of GVM’s architecture, essential components, and terminology. Mastering these concepts is critical for using OpenVAS effectively during vulnerability assessments.

## What is GVM?

GVM is a comprehensive, modular framework designed to manage the full lifecycle of vulnerability assessment, from scanning to reporting and remediation planning. Developed by Greenbone Networks, GVM integrates multiple components—each responsible for specific tasks—to ensure accurate detection of security flaws, flexible deployment, and enterprise-grade performance.

GVM powers both:

- The **Greenbone Community Edition (GCE)** – A free, open-source solution suitable for SMBs, labs, and educational use.
- The **Greenbone Enterprise Edition (GEE)** – A commercial variant offering professional support, expanded feeds, and tighter integration options for large-scale deployments.

GVM stands out in the vulnerability management ecosystem for its transparency, customizability, and alignment with open standards like CVE, CPE, CVSS, SCAP, and OVAL.

## Core components of GVM

|Component|Function|
|---|---|
|openvas-scanner|The engine that executes vulnerability tests (NVTs) on targets.|
|Gvmd|Greenbone Vulnerability Manager Daemon — manages users, scan tasks, results.|
|Gsad|Greenbone Security Assistant Daemon — provides the web interface.|
|Feeds|Regular updates of NVTs, CVEs, CPEs, and security advisories.|

These components communicate internally to support scanning operations, result management, and reporting.

## Key terminology

|Term|Definition|
|---|---|
|Network vulnerability test (NVT)|A script that tests for a specific vulnerability. Thousands are included in the feed.|
|Common vulnerabilities and exposures (CVE)|A globally recognized identifier for a known vulnerability.|
|Common platform enumeration (CPE)|A standardized way of naming software/hardware to match vulnerabilities.|
|VT family|A category of related NVTs (e.g., FTP checks, web servers).|
|Scan task|A defined job that includes scan targets, configurations, and schedules.|
|Result|The output from an NVT includes severity, impact, and references.|
|Override|Manual adjustment of the severity level of a result (e.g., for accepted risk).|
|Severity (CVSS)|The numerical risk score often derived from the CVSS (v3.x) system.|

## GVM workflow

The typical GVM vulnerability assessment flow includes:

1. **Configure target**  
    Define the asset to be scanned using an IP address, CIDR range, or hostname.
2. **Select scan config**  
    Choose a scan profile (e.g., _Full and Fast_, _Host Discovery_) tailored for depth, performance, or compliance.
3. **Run task**  
    The system launches the scan, invoking the openvas-scanner through the manager.
4. **Review report**  
    gvmd processes and scores the findings using CVSS, and gsad presents them through an interactive web UI.
5. **Export or remediate**  
    Users can export reports in formats like PDF, XML, or HTML, and begin patching or mitigation.

## Real-world example: CVE-2023-0669 – GoAnywhere MFT zero-day

In February 2023, attackers exploited a critical remote code execution (RCE) flaw in GoAnywhere MFT, a secure managed file transfer solution. Designated CVE-2023-0669, the vulnerability allowed unauthenticated attackers to execute arbitrary commands on vulnerable servers.

**How GVM helped:**

- Greenbone released updated **NVTs** within hours of public disclosure.
- Organizations that regularly synced their feeds detected affected systems before threat actors could exploit them.
- Systems were remediated before exfiltration or ransomware deployment occurred.

This example illustrates the **value of timely scan scheduling and up-to-date feeds** in mitigating zero-day risks.

## Importance of feeds

Feeds are the lifeblood of any vulnerability scanner. In GVM, they include:

- **NVTs**: Detection scripts for known vulnerabilities.
- **CVE mappings**: Link results to standardized identifiers.
- **CPEs**: Enable accurate asset identification.
- **SCAP/OVAL**: Support regulatory compliance and benchmark testing (e.g., CIS standards).

## Feed types

|Feed|Access level|Details|
|---|---|---|
|Greenbone community feed (GCF)|Free and open-source|Regular updates, but may lag behind emerging CVEs.|
|Greenbone enterprise feed (GEF)|Commercial license required|Faster NVT releases, extended checks, better zero-day support.|

## Summary

In this reading, you learned that:

- GVM is the ecosystem that powers OpenVAS, combining scanning, analysis, and reporting.
- Terms like NVT, CVE, CPE, and Severity Scores form the vocabulary of effective vulnerability management.
- GVM’s modular components allow for flexible deployment and automation.
- Real-world vulnerabilities like CVE-2023-0669 highlight the value of timely scan updates.

--------------------

# OpenVAS vs Nessus vs Qualys

## Tool overview

|Scanner|Developer|License type|Deployment|
|---|---|---|---|
|OpenVAS|Greenbone Networks|Open-source (GPL)|On-premise|
|Nessus|Tenable, Inc.|Commercial with free tier|On-premise|
|Qualys|Qualys, Inc.|Commercial (SaaS only)|Cloud (SaaS-based)|

## Architecture and components

|Feature|OpenVAS|Nessus|Qualys|
|---|---|---|---|
|Core engine|openvas-scanner + GVM stack|Tenable Nessus Scanner|Qualys Cloud Platform|
|UI/Web access|GSAD (Greenbone Security Assistant)|Local web UI or via Tenable.io|Web-based portal|
|Feed/Database updates|Greenbone Community or Enterprise Feed|Tenable plugin feed|Continuous cloud-based feed|
|Scan management|Local via GSA or GVM tools|Via local UI or Tenable.io|Cloud dashboard|
|Automation/API|Yes (GVM-Tools, Python bindings)|Yes (REST API, CLI)|Yes (RESTful API, CI/CD integration)|

## Features comparison

|Capability|OpenVAS|Nessus|Qualys|
|---|---|---|---|
|CVSS scoring|Yes|Yes|Yes|
|Custom scan policies|Yes|Yes|Yes|
|Compliance checks (CIS, SCAP)|Partial (in GEF)|Yes (via Tenable.sc)|Yes|
|Credentialed scanning|Yes|Yes|Yes|
|Cloud asset discovery|No (manual entry)|Partial (via integrations)|Yes (built-in asset inventory)|
|Container security|No|Yes (with Tenable.io)|Yes|
|Cost|Free (Community Edition)|Paid (starts ~$3K/year)|Paid (quote-based)|

## Real-World Application Scenarios

**OpenVAS in academia and SMBs**

Used extensively in labs and smaller enterprises, OpenVAS supports customized scans and is ideal for teaching vulnerability management without licensing overhead. In 2023, multiple European universities deployed OpenVAS as part of student-run SOC simulations, reinforcing its value in training and low-cost deployments.

**Nessus in hybrid environments**

Nessus is often deployed in hybrid cloud/on-premises infrastructures. For instance, a mid-sized healthcare provider used Nessus to uncover CVE-2022-22965 (Spring4Shell) in a vulnerable Java-based API server.

**Qualys for enterprise compliance**

In 2023, a Fortune 500 logistics company leveraged Qualys's automated policy compliance and asset discovery to meet ISO 27001 and SOC 2 audits across distributed AWS and Azure workloads.

## Strengths and limitations

|Scanner|Strengths|Limitations|
|---|---|---|
|OpenVAS|Free, open source, customizable, strong CLI tooling|Less polished UI, fewer integrations, slower feed updates|
|Nessus|Intuitive interface, strong vulnerability coverage|Paid only, limited automation in base version|
|Qualys|Scalable, compliance-focused, excellent asset mapping|SaaS only, lacks offline/on-prem scanning options|


-------------------


--------------

# Install and configure OpenVAS

### Task A: Update the Kali system

Start by making sure your Kali VM is up to date using the following command.

1. `sudo apt update`
2. `sudo apt upgrade -y`
3. `sudo apt dist-upgrade -y`

This might take some time.  
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/Aa1xEpV_VNg6b_OXYal67g/Update.png)

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/2IYuOd8RkTsFl9Ljpe_kGA/Upgrade.png)

**Why this matters:** Updating ensures compatibility and security before installing any major software components.

### Task B: Install OpenVAS

Use the following command to install OpenVAS and its dependencies:

1. `sudo apt install gvm`

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/4g5PlczmzdqlwoCuXif4EQ/Install%20openvas.png)

**Why this matters:** OpenVAS is part of the GVM suite. Installing it pulls in the scanner and related components needed for setup.

### Task C: Set up OpenVAS for first-time use

Initialize OpenVAS and download required definitions (this may take several minutes):

1. `sudo gvm-setup`

**Error**  
If you get an error due to a PostgreSQL collation version mismatch, which is preventing the gvmd database from being created and used, breaking the entire Greenbone Vulnerability Management (GVM) setup.

Run the following commands:

1. `sudo -u postgres psql -c "ALTER DATABASE template1 REFRESH COLLATION VERSION;"`

2. `sudo gvm-setup`

This step can take very long, up to an hour.

**NOTE: Please note the generated admin password. (This is important.)**

That should allow it to finally create the gvmd database and complete successfully.

**Why this matters:** This command sets up vulnerability feeds, creates internal databases, and generates admin credentials for the web interface.

> Save the admin password displayed at the end of setup. You'll use it to log into the GSA web interface.

### Task D: Reset admin password (if needed)

To create a new user, use the following command:

1. `sudo runuser -u _gvm -- gvmd --create-user=admin2 --new-password=12345`

If you forgot to save the auto-generated password, reset it using the following command:

1. `sudo runuser -u _gvm -- gvmd --user=admin --new-password='new_password'`
### Task E: Verify setup

Run the following command to verify installation status:

1. `sudo gvm-check-setup`

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/iqw11RUghFDTQqXt3UUzUw/sudo%20gvm-check-setup.png)

**Why this matters:** This command checks for missing components or setup errors. Resolve any warnings that appear.
### Task F: Start the GVM services

Start OpenVAS services:

1. `sudo gvm-start`

To stop the services when you are done, use the following command:

1. `sudo gvm-stop`
Once started, open a browser and go to:

2. `https://localhost:9392`


---------
# GVM core services and their roles

|Service|Function|
|---|---|
|openvas-scanner|Executes Network Vulnerability Tests (NVTs) against configured targets.|
|gvmd|Manages scan configurations, schedules, credentials, and reporting.|
|gsad|Provides the HTTPS-based Greenbone Security Assistant web interface.|
|PostgreSQL|Stores scan results, tasks, and user accounts using gvmd.|

These services must be running and properly communicating for the scanner to function.

## Startup logic

1. **Environment preparation**
    
    - Dependencies (GnuPG, rsync, PostgreSQL) must be pre-installed.
    - Certificates and local file structure are created using:  
        sudo gvm-setup
2. **Service initialization**
    
    - Services are started using:  
        sudo gvm-start
    - gsad, gvmd, and openvas-scanner are launched and linked through local Unix sockets or TCP.
3. **Service check and validation**
    
    - Use the following to confirm readiness:  
        sudo gvm-check-setup  
        sudo gvm-start
4. **Access the web interface**
    ```
    - By default: https://<host-ip>:9392
    - Admin password is either shown during setup or reset through:  
        sudo gvmd –create-user=<username> –password=<password>
    ```

## Feed synchronization: What, why, and how

**What feeds include**

- **NVTs (Network Vulnerability Tests):** Scripts that detect vulnerabilities based on CVEs.
- **SCAP Data:** Security Content Automation Protocol files for compliance checking.
- **CERT Advisories:** Community vulnerability advisories from trusted agencies.
- **CVE and CPE Mappings:** Ensure scan results are mapped to known vulnerabilities and products.

**Why feed sync matters**

Without up-to-date feeds, scans may miss:

- Recently disclosed zero-days
- Newly added detection logic
- Updated severity scores (for example, CVSS v3 updates)

## Real-world example: CVE-2023-34362 – MOVEit Transfer SQLi

In June 2023, attackers exploited this zero-day SQL injection flaw in MOVEit. OpenVAS users who synced their feeds detected vulnerable assets using newly released NVTs. Delayed syncs meant missed detections resulting in public data breaches.

## Feed update commands

**Manual update options (if gvm-setup fails or is skipped):**

```sh
sudo greenbone-feed-sync –type GVMD_DATA

sudo greenbone-feed-sync –type SCAP

sudo greenbone-feed-sync –type CERT
```
**To update NVTs (vulnerability tests):**
```sh
sudo greenbone-nvt-sync
```
**To check update status:**
```sh
sudo gvm-feed-update-status
```
**Tip:** Automate feed updates using cron or systemd timers for continuous protection.

## Troubleshooting common issues

|Issue|Cause|Fix|
|---|---|---|
|"No NVTs available" error|NVT feed not synchronized or corrupted|Run greenbone-nvt-sync, then restart services|
|Login fails on GSA|Admin user not initialized|Create/reset user with gvmd –create-user|
|Web interface inaccessible|gsad not running or blocked by firewall|Run gvm-start, check port 9392|
|Feed sync fails (HTTP error)|Proxy, DNS, or firewall issues|Test with curl, configure /etc/environment|

## Real-world use case

In 2023, a European telecommunications firm responded to the discovery of CVE-2023-0669 affecting GoAnywhere MFT. Systems running OpenVAS with outdated feeds missed the initial exposure window. After synchronizing, updated NVTs flagged multiple exposed instances, reinforcing how delays in feed updates directly impact threat visibility.

-------------
# openVAS dashboard

![[Pasted image 20260125190938.png]]

## GVM Overview

Greenbone Vulnerability Management (GVM) is the suite of tools that powers **OpenVAS**, providing a scalable and flexible framework for vulnerability scanning, management, and reporting. This reading introduces learners to the architecture, workflow, and key components of GVM, helping them understand how OpenVAS functions within a larger ecosystem of services and databases.

### What is GVM?

Greenbone Vulnerability Management (GVM) is a comprehensive vulnerability assessment framework developed by Greenbone Networks. While OpenVAS is the scanning engine, GVM includes additional services for managing scans, interpreting results, and maintaining data feeds. GVM is available in both Community and Enterprise editions.

### Core components of GVM

|Component|Function|
|---|---|
|openvas-scanner|Executes vulnerability tests (NVTs) on target systems.|
|Gvmd|Manages tasks, stores scan results, handles user accounts.|
|Gsad|Greenbone Security Assistant – provides the HTTPS web interface.|
|PostgreSQL|Backend database for scan configurations, users, and reports.|
|Feed Services|Deliver updated NVTs, CVEs, and CPE data used in scans.|

### Workflow summary

1. User logs into GSA (web interface)
2. A target and scan task are defined
3. Task is managed by gvmd
4. Scan is executed by openvas-scanner using feed data
5. Results are returned, stored in the database, and visualized in GSA

This separation ensures modularity and scalability — scans can run in the background while results are processed independently.

### Understanding feed dependencies

GVM relies on regularly updated feeds to detect known vulnerabilities. These include:

- **Network vulnerability tests (NVTs):** Scripts for detecting specific CVEs or misconfigurations.
- **CVEs:** Public identifiers for known vulnerabilities (from MITRE/NVD).
- **Common platform enumeration (CPE):** Used to match vulnerabilities to software and hardware versions.
- **SCAP/OVAL data:** For compliance and benchmark assessments.

Feeds are synchronized using greenbone-feed-sync or gvm-setup.

### Real-world use case

In February 2023, OpenVAS with GVM 22.4 detected **CVE-2023-0669**, a critical vulnerability in GoAnywhere MFT, after Greenbone released an updated NVT. Organizations that synced their feeds through GVM immediately detected vulnerable instances on internal networks, prompting patching efforts and firewall rule updates.

### Key advantages of GVM

- **Open-source** and widely supported in the security community.
- **Modular architecture** allows for independent scaling and upgrades.
- **Standards-based**: Uses CVE, CPE, CVSS, and OVAL for transparent scoring and tracking.
- **API integration** is available for automation via gvm-tools.

### Use in security operations

GVM is widely used by:

- **Security Operations Centers (SOCs)** for asset and vulnerability management.
- **Compliance teams** for routine scanning and reporting.
- **Red teams** for target discovery and risk assessment during engagements.
- **Education labs** for safe, cost-effective vulnerability assessment training.


---------
# GVM Daemon components

| Daemon          | Function                                                                    |
| --------------- | --------------------------------------------------------------------------- |
| openvas-scanner | Executes Network Vulnerability Tests (NVTs) on targets.                     |
| gvmd            | Greenbone Vulnerability Manager - schedules tasks and manages scan results. |
| gsad            | Greenbone Security Assistant Daemon - serves the web interface (GSA).       |
| postgresql      | Database backend for gvmd (stores users, tasks, reports, configs).          |

### Dependency sequence

The daemons must be started and connected in a specific order. Here's a simplified view of how they depend on each other:

1. **PostgreSQL**
    
    - Must be running before gvmd starts, as it stores all data (tasks, users, reports).
    - Configuration file: /etc/postgresql/12/main/postgresql.conf (path may vary)
2. **gvmd**
    
    - Reads from the database and provides task scheduling.
    - Requires feeds to be present (gvmd_data from Greenbone feed).
    - Communicates with openvas-scanner via Unix socket or TCP.
3. **openvas-scanner**
    
    - Relies on synced NVTs from the greenbone-nvt-sync utility.
    - Configuration: /etc/openvas/openvas.conf (for socket and logging parameters)
4. **gsad**
    
    - Connects to gvmd and renders the GSA web UI.
    - Listens on port 9392 (HTTPS)

Important: If any daemon fails, others dependent on it may crash or fail to load correctly. This often causes "502 Bad Gateway" or "Could not connect to manager" errors in the web UI.

### Key service management commands

# Check daemon status  
sudo gvm-check-setup

# Start services  
sudo gvm-start

# Manually restart an individual daemon  
sudo systemctl restart openvas-scanner  
sudo systemctl restart gvmd  
sudo systemctl restart gsad

# Check logs  
sudo journalctl -u gvmd  
sudo tail -f /var/log/gvm/gvmd.log

### Common issues and fixes

|Symptom|Likely cause|Suggested fix|
|---|---|---|
|GSA shows "503 Service Unavailable"|gvmd not running or failed to connect to DB|Restart gvmd and check PostgreSQL connection|
|No NVTs available|NVT feed not synced or scanner not started|Run greenbone-nvt-sync, restart scanner|
|Login works, but scans can't start|gvmd can't communicate with scanner|Check socket/TCP settings and permissions|
|Reports not saving|PostgreSQL misconfigured or disk space full|Validate DB settings and disk capacity|

# Glossary


| Term                                                     | Definition                                                                                                                                             |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Alive test                                               | A method used to determine if a host is active and reachable before initiating a vulnerability scan. Options include ICMP Ping, TCP ACK Ping, and ARP. |
| Address Resolution Protocol (ARP)                        | A protocol used to map IP addresses to MAC addresses within a local network.                                                                           |
| Common Platform Enumeration (CPE)                        | A naming scheme that identifies hardware, software, and operating systems affected by vulnerabilities.                                                 |
| Common Vulnerabilities and Exposures (CVE)               | A catalog of publicly known cybersecurity vulnerabilities, maintained by MITRE and referenced by OpenVAS during scans.                                 |
| Common Vulnerability Scoring System (CVSS)               | A standardized method for scoring the severity of vulnerabilities on a scale from 0.0 (low) to 10.0 (critical).                                        |
| Credentialed scan                                        | A scan that uses provided login credentials (for example, SSH or SMB) to inspect the internal configuration and software of a system.                  |
| Feed synchronization                                     | The process of updating OpenVAS with the latest NVTs, CVEs, and scan-related metadata via greenbone-feed-sync.                                         |
| Greenbone community feed                                 | A free vulnerability feed available to OpenVAS users, containing NVTs, CVEs, and configuration data for non-commercial scanning.                       |
| Greenbone Security Assistant (GSA)                       | The web-based interface of OpenVAS for managing scans, targets, and vulnerability reports.                                                             |
| Greenbone Security Assistant Daemon (gsad)               | Provides the web-based GUI to interact with OpenVAS (typically via port 9392).                                                                         |
| Greenbone Vulnerability Management (GVM)                 | A collection of services that includes OpenVAS, gvmd, gsad, and supporting tools for managing, executing, and reporting vulnerability scans.           |
| Greenbone Vulnerability Manager Daemon (gvmd)            | Manages scan tasks, credentials, configurations, and report storage.                                                                                   |
| Internet Control Message Protocol (ICMP) Ping            | A network tool that sends echo requests to check if a host is reachable and measure response time.                                                     |
| Network vulnerability test (NVT)                         | A script used by OpenVAS to detect specific vulnerabilities on target systems. These tests are updated via feed synchronization.                       |
| OpenVAS                                                  | An open-source vulnerability scanning engine, now part of the Greenbone Vulnerability Management (GVM) suite.                                          |
| Override                                                 | A manual change to the severity or status of a scan finding (e.g., marking a known false positive as "Fixed" or lowering severity).                    |
| Port list                                                | A predefined list of ports to be scanned during a task. Examples include "OpenVAS Default" or "All TCP and Nmap Top 100 UDP."                          |
| Report                                                   | The structured output of a completed scan task, including identified vulnerabilities, affected hosts, severity scores, and CVE references.             |
| Scan task                                                | A configured operation that defines what OpenVAS should scan, using a specific target, port list, credentials, and scan profile.                       |
| Secure Shell (SSH)                                       | A secure protocol for remote login and command-line access over encrypted connections.                                                                 |
| Server Message Block (SMB)                               | A protocol for sharing files, printers, and resources over a network, mainly in Windows environments.                                                  |
| Severity class                                           | A label such as Low, Medium, High, or Critical applied to scan results based on their CVSS scores.                                                     |
| Target                                                   | A defined IP address, hostname, or network range that serves as the focus of a scan task.                                                              |
| Task wizard                                              | A GSA feature that allows quick scan configuration with minimal inputs (target and scan profile).                                                      |
| Transmission Control Protocol Acknowledgment (TCPA) Ping | A scanning method that sends TCP ACK packets to detect live hosts, often bypassing firewalls that block ICMP.                                          |
| Unauthenticated scan                                     | A scan that inspects a system's exposed services and ports without using credentials. It typically detects external vulnerabilities only.              |