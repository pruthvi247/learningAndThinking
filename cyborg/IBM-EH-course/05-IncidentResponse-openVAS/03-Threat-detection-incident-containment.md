![[Pasted image 20260125204440.png]]

## OpenVAS alerts

Each scan executed by OpenVAS generates a structured set of results for every identified vulnerability or misconfiguration. These are contextual security alerts that include multiple critical fields:

- **CVE references** to align with international vulnerability databases
- **CVSS v3.x scores**, offering quantitative risk prioritization
- **Technical summaries** that describe the issue in both administrative and exploitative terms
- **Detection mechanisms**, indicating the specific NVT script used
- **Remediation advice**, which may include vendor patch links or configuration hardening steps

These alerts are automatically classified based on severity thresholds (for example, Common Vulnerability Scoring System (CVSS) ≥ 9.0 is usually deemed _Critical_), allowing security teams to apply filters and sort by exploitability or operational risk.

## Types of alerts and what they reveal

Each alert OpenVAS generates can belong to one or more operational categories. OpenVAS maps these alerts to known services and open ports, giving analysts service-aware insight into what type of threat is most likely, where it resides, and how it could be exploited in the kill chain. Each type of alert represents a different type of exposure or risk vector:

|**Alert category**|**Sample CVE or condition**|**Security implication**|
|---|---|---|
|**Exploitable CVEs**|CVE-2021-44228 (Log4Shell)|Remote code execution without authentication; immediate threat|
|**Weak defaults**|Anonymous file transfer protocol (FTP) enabled; MySQL default credentials|Entry point for brute-force or lateral movement|
|**Unsafe protocols**|Telnet, server message block version 1 (SMBv1), or deprecated secure sockets layer/transport layer security (SSL/TLS) versions|Facilitates downgrade attacks, sniffing, or Man-in-the-Middle exploitation|
|**Outdated software**|Apache Struts version < 2.5.26|Known vulnerabilities tied to published exploit kits|

## Enhancing detection with threat intelligence feeds

Real-time threat intelligence (TI) involves ingesting structured data on:

- Malicious IPs, domain names, and uniform resource locators (URLs)
- Cryptographic hash values (for example, MD5 and SHA256) of malware binaries
- Indicators of compromise (IOCs) from recent campaigns
- Threat actor tactics, techniques, and procedures (TTPs), often mapped to the MITRE ATT&CK framework

## Why combine this with OpenVAS alerts?

A known common vulnerabilities and exposures (CVE) alone does not tell you if it is being used _right now_. By comparing CVEs flagged by OpenVAS with threat intel data (for example, from Malware Information Sharing Platform and Threat Sharing (MISP), Greenbone's Enterprise Feed, or commercial threat intelligence (TI) providers), defenders gain contextual relevance:

_If a vulnerability is actively being exploited by an advanced persistent threat (APT) or ransomware campaign, its priority should be escalated, even if its base CVSS score is below the threshold._

## Integration scenario example

Let's assume OpenVAS detects a high-severity vulnerability in a webmail application. In parallel, a commercial threat feed reports that this CVE is now part of an exploit kit used in a botnet campaign. This cross-correlation elevates the risk posture of that asset dramatically. The enriched alert no longer just indicates risk; it triggers an operational response.

Actionable responses include:

- Immediate patching or network isolation
- Setting up custom SIEM queries to detect post-exploitation activity
- Monitoring for related command and control (C2) behavior or lateral movement attempts

## Real-time feed synchronization in OpenVAS

Keeping OpenVAS detection capabilities updated is crucial. Feed synchronization ensures the scanner is aware of:

- Newly published CVEs and CVSS metrics
- Updated network vulnerability test (NVT) detection scripts
- Refined exploit references or proof-of-concept changes
- Security advisories from trusted sources (Computer Emergency Response Teams (CERTs) and vendors)

|**Feed**|**Cost**|**Update frequency**|**Benefits**|
|---|---|---|---|
|**GCF (Community Feed)**|Free|Daily (may lag new CVEs)|Suitable for testing, educational use, and small organizations|
|**GEF (Enterprise Feed)**|Subscription|Near real-time|Faster access to zero days, curated TTP data, more NVTs|

Use these commands to keep OpenVAS feeds automated for vulnerability detection:

greenbone-feed-sync --type GVMD_DATA

greenbone-feed-sync --type SCAP

greenbone-feed-sync --type CERT

These should be automated via cron or scheduling services to maintain daily updates.

## Real-world example: CVE-2023-0669—GoAnywhere MFT zero-day

In Q1 2023, CVE-2023-0669, an unauthenticated RCE flaw in Fortra's GoAnywhere MFT platform, was rapidly weaponized by ransomware groups. Within days of its disclosure:

- Greenbone released an updated NVT to detect it
- Security teams that had daily feed syncs identified the flaw in production environments
- Alerts were correlated with real-time IDS logs showing outbound HTTPS traffic to attacker infrastructure

**Result**: Organizations that acted on OpenVAS alerts, informed by threat intel, isolated or patched affected systems before data was exfiltrated. Others, without timely scanning or intelligence correlation, experienced active compromise.

## Best practices for operational use

To maximize the benefit of OpenVAS + Threat Intel workflows:

- **Automate feed syncs** every 24 hours to maintain relevance
- **Correlate high-severity OpenVAS alerts** with network logs, especially for services exposed to the internet
- **Label and tag alerts** that match known exploited CVEs or indicators from threat intel
- **Integrate into SIEMs and SOAR platforms** for escalation, auto-tagging, and policy-based isolation workflows
- **Use enrichment scripts or APIs** to fetch TI context from MISP, AbuseIPDB, AlienVault OTX, or Greenbone Enterprise Feed (GEF)

## Summary

- OpenVAS alerts are more than scan results; they're early warning signals when matched with behavioral indicators and threat context.
- Real-time threat intelligence turns passive detection into active defense by validating which vulnerabilities are being targeted.
- Organizations fusing OpenVAS data with live TI feeds are better positioned to quickly detect, prioritize, and contain threats.
----------
# Network Behaviour and Anomalies
## Overview

In today's cybersecurity ecosystem, malicious traffic is crafted to appear legitimate, evading traditional detection techniques such as signature-based intrusion prevention or static vulnerability scanning. Therefore, network behavior analysis, the practice of modeling expected activity patterns and detecting deviations, has become a frontline method for identifying covert intrusions, such as living-off-the-land tactics or zero-day exploits.

This reading expands on how organizations can define baseline activity, detect meaningful deviations, and then correlate these anomalies with open vulnerability assessment system (OpenVAS) scan data to triage incidents rapidly and confidently.

## Defining "normal" network behavior: Establishing a baseline

Every IT environment has its rhythm, patterns of communication, authentication, and system usage. Recognizing "normal" behavior is about adaptive profiling over time using continuous monitoring tools. Characteristics of baseline behavior are:

|**Behavioral component**|**Examples observed in most environments**|
|---|---|
|**Traffic patterns**|Scheduled cloud syncs (for example, OneDrive, Dropbox), nightly data backups, software updates|
|**Protocol usage**|Encrypted web traffic (Hypertext Transfer Protocol Secure (HTTPS), Domain Name System (DNS) lookups, internal Server Message Block (SMB) shares, secure shell (SSH) access for maintenance|
|**Throughput volume**|Regular outbound upload sizes from backup servers; known download rates for patching or software delivery|
|**Known destinations**|Connections to whitelisted internet protocol addresses (IPs) or domains like update.microsoft.com, internal git servers, or mail relays|

_Important:_ "Normal" sets a reference point for flagging behavioral outliers.

## Tools that help establish a baseline

A well-established baseline gives defenders a lens to detect behavioral drift, often a precursor to compromise.

- **Zeek (formerly Bro):** Extracts high-level insights like DNS patterns, secure sockets layer (SSL) handshake summaries, and user-agent strings
- **Suricata or Snort:** Tracks protocol behaviors and packet anomalies
- **NetFlow/IPFIX:** Provides flow-based traffic summaries for behavioral modeling
- **Security information and event management (SIEM):** Correlates network, host, and identity telemetry across time

## Recognizing high-signal anomalies

When deviations appear on systems known to be vulnerable, the signal-to-noise ratio becomes actionable. Correlating anomalies with OpenVAS findings helps validate whether a vulnerable service is being actively misused. Key anomaly indicators and their implications are:

|**Observed behavior**|**What it might indicate**|
|---|---|
|**Increased outbound bandwidth**|Potential data staging or exfiltration by malware|
|**Persistent contact with unknown IPs**|C2 (command and control) infrastructure communication|
|**Unusual east-west traffic (RDP/SMB)**|Lateral movement or worm propagation|
|**Repeated port scanning by an internal host**|Attacker reconnaissance or compromised asset mapping the network|
|**Usage of legacy services**|Exploitation of old protocols (for example, Telnet, file transfer protocol (FTP) often enabled on legacy systems|

## Using OpenVAS to contextualize network signals

While OpenVAS provides a snapshot of technical debt (unpatched services or weak configurations), its real value is unlocked when these findings are mapped to observable behavior.

### Examples of effective correlation

- If OpenVAS flags a server running **Apache 2.4.49** as vulnerable to **CVE-2021-41773** and firewall logs show suspicious GET requests to unusual paths (../../etc/passwd), this strongly suggests exploitation is underway.
- A scan reveals **anonymous FTP** is enabled. Concurrently, NetFlow data shows large outbound transfers over port 21. This raises immediate concerns about **unauthorized data leakage**.
- OpenVAS identifies **Telnet** enabled on a legacy manufacturing system. Logs later reveal an interactive session initiated from a foreign IP during non-operational hours, suggesting **unauthorized remote access** using a weak protocol.

## Case study: Log4Shell detection via network behavior (2021–2022)

The exploitation of **CVE-2021-44228 (Log4Shell)** demonstrated how **network behavior analytics**, combined with vulnerability awareness, plays a crucial role in early detection.

### Attack summary:

- Attackers injected crafted Java Naming and Directory Interface (JNDI) payloads into HTTP headers, triggering remote lookups via Lightweight Directory Access Protocol (LDAP) to attacker-controlled servers.
- These LDAP connections were visible as **unexpected outbound traffic**, especially to nonstandard domains or ports.

### Detection workflow:

1. **OpenVAS identified** Java-based services using vulnerable Log4j libraries.
2. **Network logs showed** new LDAP traffic from those systems, often during off-hours.
3. **DNS queries revealed** domains used in active exploitation campaigns.
4. Analysts **correlated IPs and behavior** with threat data, leading to isolation and forensic triage before ransomware payloads could deploy.

## Tactical recommendations for behavior-based threat detection

Behavior becomes meaningful only when compared to expected patterns and known weaknesses. To maximize detection capabilities and minimize false positives:

- **Continuously baseline** each host, segment, and application's expected network behavior.
- **Integrate OpenVAS findings** with behavioral tools to prioritize anomaly triage.
- **Correlate anomaly sources** (for example, rare DNS lookups and payload transfers) with systems flagged by OpenVAS as vulnerable.
- **Automate alerting thresholds** based on deviation magnitude and common vulnerability scoring system (CVSS) severity.
- **Review during low-noise periods** (for example, nights and weekends), where anomalies stand out more starkly.
---------------------
# Mapping Scan Results to MITRE ATT&CK Tactics

## Overview

The MITRE adversarial tactics, techniques, and common knowledge (MITRE ATT&CK) framework has redefined how security teams conceptualize, categorize, and counteract real-world cyber threats. Rather than focusing only on isolated vulnerabilities or static defense measures, ATT&CK allows defenders to understand why attackers may exploit a particular weakness, how they are likely to do it, and what happens next.

When organizations integrate open vulnerability assessment system (OpenVAS) scan data with MITRE ATT&CK tactics and techniques, they transition from passive vulnerability management to active, intelligence-driven defense. This process surfaces security flaws and contextualizes them within a proven adversary playbook.

## Why map vulnerabilities to MITRE ATT&CK?

Traditional vulnerability management often isolates vulnerability reports from actual detection or response workflows. This fragmentation limits the usefulness of scan results during real-time incidents. By mapping vulnerabilities detected by OpenVAS to ATT&CK tactics and techniques, defenders gain several strategic advantages:

- **Threat-informed defense**: Organizations can anticipate likely attacker behavior and implement preemptive defenses by tying common vulnerabilities and exposures (CVE) to an ATT&CK technique (for example, T1190—Exploit Public-Facing Application).
- **Enhanced detection engineering**: Security operations center (SOC) teams can design better log queries, security information and event management (SIEM) rules, and endpoint detection and response (EDR) alerts by focusing on _how_ attackers will attempt to exploit flagged vulnerabilities.
- **Red & purple team synergy**: Security teams simulating adversary behavior (red teams) or validating detections (purple teams) can align their efforts with real-world attack chains, ensuring that OpenVAS scan outputs contribute to scenario planning and detection rule testing.

## Common OpenVAS findings mapped to ATT&CK

To illustrate this integration, consider how specific vulnerability types discovered by OpenVAS correspond to MITRE ATT&CK tactics and techniques:

|**OpenVAS finding**|**ATT&CK tactic**|**Mapped technique**|
|---|---|---|
|Apache RCE (for example, CVE-2021-41773)|Initial access|T1190 – Exploit public-facing application|
|SMBv1 + No authentication|Lateral movement|T1210 – Exploitation of remote services|
|Default/Weak SSH Passwords|Credential access|T1110 – Brute force|
|SQL injection in a web form|Collection/exfiltration|T1213 – Data from information repositories|
|Open an FTP server with anonymous access|C2 & collection|T1021 – Remote services|
|JBoss RCE vulnerability|Execution / Persistence|T1068 – Exploitation for privilege escalation|

**Key insight**: Many OpenVAS vulnerabilities, especially those with a common vulnerability scoring system (CVSS) ≥ 8.0-can be mapped to high-impact techniques in ATT&CK, allowing security teams to move from _what is vulnerable_ to _how the attack will unfold_.

## Real-world case study: MOVEit transfer breach (CVE-2023-34362)

In 2023, the **CL0P ransomware group** exploited a critical SQL injection vulnerability in MOVEit Transfer, affecting numerous organizations worldwide. OpenVAS quickly integrated detection for CVE-2023-34362 into its scan feeds.

Mapping the incident into MITRE ATT&CK provides a more actionable story:

- **Initial access**: T1190 – Exploit Public-Facing Application
- **Collection**: T1074 – Data Staged (preparation for exfiltration)
- **Exfiltration**: T1567 – Exfiltration Over Web Service

This mapping allowed affected organizations to proactively adjust SIEM queries, review logs for corresponding behavior, and contain web servers _before_ payload execution escalated. Organizations that adopted ATT&CK-based detection strategies localized and stopped lateral movement within hours, limitingdamage compared to peers who relied solely on patching timelines.

## Enriching workflows with ATT&CK context

To operationalize this approach, a repeatable workflow can be applied:

1. **Scan assets using OpenVAS**  
    Perform credentialed and unauthenticated scans to identify all exploitable weaknesses.
2. **Map CVEs to ATT&CK TTPs**  
    Use common vulnerabilities and exposures (CVE) to tactics, techniques, and procedures (TTP) mapping tools or scripts (for example, MITRE STIX/TAXII feeds, ATT&CK Navigator overlays).
3. **Update SIEM and EDR rules**  
    Focus alerting on relevant ATT&CK techniques already aligned to current campaigns or past incident behavior.
4. **Prioritize patching by threat relevance**  
    Don't just patch based on CVSS. Prioritize vulnerabilities that align with the techniques used by current threat actors.
5. **Train incident responders**  
    Equip SOC analysts and blue teams with attacker-contextual knowledge so that investigations align with realistic exploitation chains.

## Tooling to support MITRE mapping

These tools ensure vulnerability findings are integrated into proactive detection pipelines, improving incident response agility.

|**Tool/platform**|**Functionality**|
|---|---|
|**MITRE ATT&CK navigator**|Visual tool to highlight coverage of ATT&CK techniques and TTP mappings.|
|**OpenVAS XML + CVE Parsers**|Enables exporting scan results for automated enrichment and ATT&CK mapping.|
|**SIEM integrations (for example, ELK, Splunk)**|Allows creation of detection rules mapped directly to ATT&CK IDs.|
|**STIX/TAXII feeds**|Provides up-to-date technique data for programmatic enrichment and automation.|

## Summary

- **OpenVAS + MITRE ATT&CK**: A powerful combination that transforms static vulnerability data into dynamic threat intelligence.
- **TTP awareness**: Mapping vulnerabilities to adversarial behaviors helps prioritize alerts, focus detection, and streamline response.
- **Beyond CVSS**: A high CVSS alone doesn't explain the full risk. Pairing with ATT&CK reveals _how_ and _why_ a vulnerability matters in an adversary context.
- **Real-world use cases**: Breaches like MOVEit demonstrate how ATT&CK-based mapping improves readiness and reduces dwell time.

---------
# Lab: Detect Threats Using Logs and OpenVAS Data

## Overview

Simulate how a SOC analyst identifies an active compromise by correlating OpenVAS vulnerability scan data with suspicious system and firewall logs.

## Learning objectives

After completing this lab, you will be able to:

- Analyze scan results to identify critical vulnerabilities
- Examine system and firewall logs to detect suspicious behavior
- Correlate evidence to determine if an attack is in progress
- Map findings to MITRE ATT&CK tactics and techniques

---

## Step 1: Review the scan report

### Target details:

- **IP Address:** 10.0.10.20
- **Hostname:** app-server-02.internal.local

### Vulnerabilities identified in OpenVAS:

|CVE ID|Title|CVSS|Notes|
|---|---|---|---|
|CVE-2023-34362|MOVEit SQL Injection (RCE)|9.8|Critical RCE—actively exploited|
|CVE-2017-0144|EternalBlue SMBv1 RCE|8.1|Legacy wormable flaw linked to WannaCry|
|FTP Misconfig|Anonymous FTP access allowed|5.0|Allows unrestricted login|

> **Why this matters:** The OpenVAS scan shows exploitable vulnerabilities, including a critical RCE. This sets the stage for identifying actual exploitation in logs.

---

## Step 2: Analyze suspicious logs

### Firewall logs – Suspicious outbound connections:

1. 1
2. 2

3. `May 18 10:12:08 ACCEPT TCP dst=185.199.110.153 dport=443 src=10.0.10.20 sport=50823`
4. `May 18 10:13:44 ACCEPT TCP dst=31.13.70.52 dport=443 src=10.0.10.20 sport=50833`

Copied!Wrap Toggled!

- Repeated HTTPS connections to external IPs from the target server
- Indicates possible **Command-and-Control (C2)** or data exfiltration

### System auth logs – Privilege escalation observed:

1. 1
2. 2

3. `May 18 10:09:50 sudo: www-data : USER=root ; COMMAND=/bin/bash`
4. `May 18 10:09:52 su: session opened for user root`

Copied!Wrap Toggled!

- Web service account `www-data` ran a root shell
- Sign of **privilege escalation**, likely post-exploitation

---

## Step 3: Correlate evidence and identify threats

### Correlation summary:

- OpenVAS confirms a critical MOVEit RCE vulnerability
- Logs show:
    - Web service privilege escalation (T1068)
    - Suspicious outbound traffic (potential C2)

### MITRE ATT&CK mapping:

|Phase|Technique|ID|
|---|---|---|
|Initial Access|Exploit Public-Facing App|T1190|
|Privilege Escalation|Exploitation for Privilege Esc.|T1068|
|Command and Control|Encrypted Channel|T1071.001|

---

## Step 4: Recommend a response

### Suggested incident response actions:

1. **Isolate** the affected server from the network
2. **Block** outbound connections to suspicious IPs at the firewall
3. **Review** user account activity and logs for lateral movement
4. **Patch** CVE-2023-34362 immediately
5. **Re-image** system if compromise is confirmed
6. **Monitor** for reoccurrence via IDS and log monitoring

> **Real-world tie-in:** This type of analysis mirrors threat detection workflows in real SOC environments—combining vulnerability intelligence and log correlation.

---

## Challenge: Write an analyst summary

Write a short SOC Analyst summary (3–5 sentences) based on what you've seen in the scan and logs. Your report should:

- Identify if a compromise likely occurred
- Name the exploited vulnerability
- Describe suspicious behavior
- Recommend a priority response

Save this as part of your lab evidence.

-------------
# Containment Strategies

## Learning objectives

1. Define the strategic importance and core purposes of containment in cybersecurity incident response.
2. List containment timeframes, standard techniques for threat containment, and key factors to evaluate before executing containment actions.

## Strategic importance of containment

Containment is the first critical step to halt the progression of the attack when a threat is discovered in an enterprise environment, whether by log correlation, vulnerability scanning such as open vulnerability assessment system (OpenVAS), or third-party alerts. It serves as a temporary firewall between compromise and catastrophe.

Rather than immediately eradicating malware or rebuilding affected systems, containment seeks to **"freeze the battlefield."** It gives security teams the time and control to assess damage, collect forensic evidence, and plan further response steps without allowing the threat actor more room to maneuver.

## Core purposes of containment

At its essence, containment strategies are designed to reduce the attacker's ability to:

- **Spread laterally** to other internal systems (for example, pivot from an infected endpoint to a domain controller)
- **Exfiltrate sensitive data** such as customer records, credentials, or intellectual property
- **Maintain persistence or command-and-control** through outbound connections
- **Exploit vulnerable services** across the environment

Simultaneously, containment ensures that:

- Evidence is preserved for digital forensics
- The business impact is minimized
- Compliance obligations (for example, incident notification timelines) can be met
- Mitigation can proceed in a controlled and verified manner

Containment must be **surgical:** too slow, and the breach escalates; too broad, and critical services may be needlessly interrupted.

## Containment timeframes and their functions

Containment actions typically fall into two temporal categories with distinct purposes and escalation paths:

|**Containment type**|**Window of execution**|**Goal**|
|---|---|---|
|**Short-term**|Immediate (minutes–hours)|Stop threat propagation and isolate the active vector or endpoint|
|**Long-term**|Intermediate (hours–days)|Stabilize operations, support investigation, enable patching, or reimaging|

### Short-term containment

Tactical, immediate, and often disruptive. These responses prioritize security over continuity and are generally **automated or semi-automated** in mature environments. Its typical actions are:

- Block IPs or domains using firewalls
- Revoke compromised credentials or admin tokens
- Isolate infected endpoints using endpoint detection and response (EDR)

### Long-term containment

Strategic and stabilization-focused. This phase balances **ongoing service delivery** with **security hardening** and **threat eradication**. Its typical actions are:

- Rebuild infected systems or restore clean backups
- Implement firewall or web application firewall (WAF) rules
- Audit and reset access control configurations

_Case in Point:_ During the 2023 MOVEit breach, short-term containment included turning off public access to the file transfer portal. The long-term phase involved rebuilding application environments and bolstering input sanitization protections at the edge layer.

## Techniques for threat containment

Containment methods are not one-size-fits-all. They should be **chosen based on threat type, system criticality, and available tooling**. Below is a breakdown of techniques and the security contexts they serve:

|**Technique**|**Description**|**Applied when...**|
|---|---|---|
|**Network isolation**|Cut off inbound/outbound network access for a system or segment|Suspected malware activity, command and control (C2) communication, ransomware spread|
|**Virtual local area network (VLAN) segmentation**|Relocate affected hosts into a restricted subnet or isolated VLAN|Multiple infections in a single zone or to support passive monitoring|
|**Account/access revocation**|Disable tokens, passwords, or privileged user accounts|Suspected insider threats or stolen credentials|
|**Indicator of compromise (IOC) blocking**|Use threat intel indicators to block malicious internet protocol addresses (IPs), file hashes, and domains.|Known indicators seen in telemetry or threat reports|
|**Domain name system (DNS) sinkholing**|Redirect DNS lookups for malicious domains to internal honeypots or blackholes|Malware uses DNS-based C2 resolution (for example, domain generation algorithm (DGA) based malware)|
|**Host-based controls**|Disable specific services or ports on targeted systems (for example, SMBv1 and Telnet)|Exploitable services found by OpenVAS or known vulnerabilities|
|**EDR quarantine**|Use endpoint security tools to remotely fence compromised hosts|When malware is detected, the host must be preserved for forensics|

These containment actions can be orchestrated manually, via **playbooks**, or automatically through Security Orchestration, Automation, and Response (SOAR) platforms that integrate with Security Information and Event Management (SIEM), OpenVAS, and EDR.

## Case study: MOVEit exploitation and the value of containment discipline

In June 2023, attackers exploited **CVE-2023-34362**, a SQL injection flaw in MOVEit Transfer, to deploy web shells and steal sensitive files from numerous organizations.

Organizations that implemented structured containment workflows responded quickly:

- **First response:** Blocked external access, disabled known exploitation vectors, and monitored outbound data channels
- **Escalation:** Applied endpoint isolation to servers showing lateral movement behavior
- **Sustained measures:** Decommissioned affected servers, rebuilt infrastructure using hardened configurations, and introduced WAFs.

Impact difference: Enterprises with **predefined containment standard operating procedures (SOPs)** minimized data loss and recovered faster than those who responded reactively without clear guidance.

## Factors to evaluate before executing containment

Blind containment can backfire. Before acting, teams must assess key operational and legal factors:

|**Consideration**|**Key questions**|
|---|---|
|**Operational impact**|Will isolation disrupt business services or critical workflows?|
|**Adversary awareness**|Could containment tip off the attacker, prompting them to destroy data or escalate?|
|**Evidence preservation**|Is it possible to capture volatile memory, log data, and session artifacts first?|
|**Compliance obligations**|Are regulators or legal stakeholders required to be informed before action?|

_Best Practice:_ All containment actions, whether script-driven or manual, must be documented and timestamped for legal defensibility, post-mortem review, and chain-of-custody verification.

----------
# when to isolate a host

![[Pasted image 20260125210926.png]]
![[Pasted image 20260125211048.png]]
![[Pasted image 20260125211117.png]]

### Disconnecting a host: Stopping the spread in real time

Isolation, or disconnection, is the first line of defense when signs of compromise unfold. It means severing a system's ability to communicate physically (unplugging network cables) or logically (through endpoint security tools, firewall policies, or VLAN restrictions).

**Situations warranting immediate disconnection:**

|Detection trigger|Purpose of disconnection|
|---|---|
|**Data leakage in progress**|Prevent the attacker from exfiltrating sensitive assets to an external host.|
|**Confirmed malware communicating with command and control (C2)**|Stop malware from receiving instructions or sending stolen data.|
|**Encryption behavior indicating ransomware**|Interrupt encryption routines before they can impact critical file systems.|
|**Internal scans or authentication abuse**|Block adversary lateral movement within the enterprise network.|

_Be aware_: Disconnecting too soon may alert the attacker, prompting them to shift tactics, delete evidence, or trigger destructive actions (like wiping logs or encrypting files). Disconnection should ideally follow initial triage and covert evidence collection.

### Reimaging a host: Restoring integrity after deep compromise

Reimaging refers to wiping the existing operating system and deploying a clean build, often from a golden image or secured baseline. This action is not containment; it’s eradication and recovery. It assumes the host is too compromised to be trusted.

**Scenarios demanding reimaging:**

|Scenario|Why reimaging is necessary|
|---|---|
|**Kernel/rootkit-level malware**|Such threats can hide in memory or bootloaders and persist through a reboot.|
|**Privilege escalation to SYSTEM/root**|System integrity can no longer be guaranteed; malicious changes may be hidden.|
|**Tampered system logs or evidence destruction**|Inconclusive forensics signal attacker manipulation-clean rebuild ensures safety.|
|**Low-value asset with high-speed redeployment**|Reimaging is more efficient than complex manual remediation.|

_Caution_: Never reimage before capturing volatile memory, open connections, and log snapshots, especially when legal action, data breach investigation, or regulatory reporting may follow. Forensics lost at this stage cannot be recovered.

### Disconnect vs. reimage: Making the right call

Choosing between isolation and reimaging is based on context, not just symptoms. Here's a comparative model to assist defenders in applying the correct strategy:

|Aspect|Disconnection|Reimaging|
|---|---|---|
|Primary goal|Halt threat activity|Eliminate hidden persistence or unknown compromise|
|Evidence preservation|Preserves memory and logs|Risk of loss unless collected beforehand|
|Downtime impact|Moderate-the system can be restored|High-requires rebuilding, validation, and patching|
|Speed of execution|Fast-can be automated or scripted|Slower-depends on imaging process and post-restore testing|
|When to use|During active infection or data exfiltration|Post-analysis, when trust in the system's integrity is gone|

_Tip_: For high-value servers, consider isolating first, capturing forensic artifacts, and reimaging after evidence is secured.

### Real-world case: Log4Shell (CVE-2021-44228) in internal java services

During the late 2021–2022 exploitation wave of Log4Shell, internal-facing applications, often assumed to be safe, were targeted via Java Naming and Directory Interface (JNDI) injection vulnerabilities. One enterprise uncovered beaconing behavior from a development host.

Incident response flow:

1. **Detection**: Unusual outbound Lightweight Directory Access Protocol (LDAP) traffic from a development server
2. **OpenVAS findings**: CVE-2021-44228 confirmed on multiple internal Java services
3. **Action taken**:
    - Endpoint was immediately disconnected using automated endpoint detection and response (EDR) quarantine
    - Volatile memory was captured, including active processes and sockets
    - Forensic triage revealed artifacts consistent with reverse shell deployment
    - Due to uncertainty around persistence mechanisms, the system was reimaged and redeployed from a secure template

This incident demonstrated how strategic containment,and fast decision-making can mitigate threats even after exploitation begins.

### Tactical recommendations for disconnection and reimaging

**For disconnecting**

- Use Security Information and Event Management (SIEM) or EDR-based detection rules to trigger disconnection workflows (for example, excessive connections to known malicious Internet Protocol addresses (IPs)
- Employ Security Orchestration, Automation, and Response (SOAR) playbooks that include manual checkpoints for critical assets
- Ensure logging of isolation events, timestamps, and responsible personnel

**For reimaging**

- Build preapproved golden images that include current patches, hardening baselines, and logging agents
- Maintain automated provisioning tools (for example, preboot execution environment (PXE), Ansible, System Center Configuration Manager (SCCM) to reduce downtime
- Label reimaged systems for post-recovery observation to detect reinfection or attacker return attempts

**For both**

- Notify IT, compliance, and legal teams when actions affect regulated systems (for example, those storing personally identifiable information (PII) or financial records)
- Keep an isolation/rebuild register as part of your incident documentation package
- Regularly test both isolation and reimaging procedures to ensure readiness

-----------

# Lab: Practice Incident Response Using Tools

> **Note:**  
> This is an analysis-based scenario lab. You are **not executing any operations on an OpenVAS environment**. Instead, you will review simulated logs, scan outputs, and system evidence to practice incident response analysis and decision-making.

## Learning objectives

After completing this lab, you will be able to:

- Analyze a simulated incident scenario using provided evidence and recommend response actions
- Select the best tool-based containment strategy based on real-world limitations

---

## Scenario summary

In this lab, you'll step into the role of a Security Operations Center (SOC) analyst facing an active security incident on a key business server.

- **System:** `192.168.10.50` – File transfer server (DMZ)
- **Vulnerability:** `CVE-2023-34362` (MOVEit SQL Injection, CVSS 9.8)
- **Evidence:**
    - OpenVAS scan flagged a critical SQL injection vulnerability
    - System logs show repeated POST requests to a suspicious IP: `185.199.108.153:443`
    - User escalation from `www-data` (web service) to `root` (full control)
- **Status:** The server is still operational and in production, so immediate and careful action is required.

**Why this matters:**  
Being able to analyze and interpret real incident evidence is foundational for cyber defense. You'll build skills that mirror real-world SOC operations, moving beyond “button-clicking” to develop judgment and incident triage skills that are valued in every security team.

---

## Available (simulated) tools

You have access to several common containment and response options, each with trade-offs:

|Tool|Use|Limitation|
|---|---|---|
|Firewall ACL|Block host traffic|Needs NetOps coordination|
|EDR (SentinelOne)|Isolate + memory capture|Windows-only|
|OpenVAS + SIEM Script|Tag + quarantine (auto)|Needs manual approval|
|VLAN Segmentation|Move to quarantine network|Disrupts service|
|Manual Shutdown|Hard stop|High impact, risk of data loss|

**Why this matters:**  
Incident response always requires balancing technical solutions with business needs, operational risk, and resource constraints. Recognizing the strengths and weaknesses of each tool is critical to choosing the best response.

---

## Step-by-step instructions

### Step 1: Review findings

**Instructions:**  
Begin by consolidating all available threat intelligence. Carefully review logs, scan results, and any suspicious activity. This process is the foundation of incident response, helping you confirm what's happening, how severe it is, and what might happen next.

|Data type|Finding|
|---|---|
|OpenVAS Scan|CVE-2023-34362 – SQLi vulnerability|
|System Log|`www-data` user escalated to `root`|
|Firewall Log|Repeated outbound POSTs to suspicious IP via HTTPS|

**Why this matters:**  
Quickly synthesizing data from multiple sources (scans, logs, network activity) is the first step in any real-world incident response. Analysts must build a clear, evidence-based understanding before taking action, mistakes here can lead to missed threats or business disruption.

---

### Step 2: Identify the threat phase

**Instructions:**  
Classify what stage of the attack you're seeing. Use the [MITRE ATT&CK](https://attack.mitre.org/) framework, a global standard for mapping attacker behaviors, to name the tactics and techniques in play. This helps you assess urgency and select the right response.

**Analysis:**

- **Most likely phase:** Command and Control (C2)
- **Justification:** Outbound POSTs to an external IP and privilege escalation from a web user to root suggest the attacker has already compromised the server and is trying to maintain remote control.

**Why this matters:**  
Accurately identifying the threat phase informs your next steps, whether to focus on containment, eradication, or recovery. The MITRE ATT&CK framework is used by SOCs globally to ensure a common language and better prioritization of threats.

---

### Step 3: Choose a containment action

**Instructions:**  
Evaluate the containment options provided in the tool table. Weigh each action for its speed, impact, and ability to preserve evidence. Consider both the technical and business side, what's the least disruptive, most effective response you can take?

**Analysis:**

- **Best option:** Firewall ACL (block outgoing communication)
- **Rationale:**
    - Blocks attacker's remote control immediately
    - Keeps the system online for forensic analysis
    - Less business disruption than immediate shutdown or VLAN changes
    - Doesn't require special EDR software or disrupt all users

**Why this matters:**  
Containment is often the most critical and time-sensitive phase in incident response. Choosing an action that stops the attack, while preserving evidence and minimizing operational impact, separates novice responders from professionals.

---

### Step 4: Long-term recovery plan

**Instructions:**  
Containment stops the immediate threat, but you must restore system trust before returning to business as usual. Propose a recovery plan that fully addresses the root cause and ensures similar systems aren't vulnerable.

**Recommended plan:**

1. **Reimage the host:** Completely rebuild the affected server from trusted backups or a clean image, since root compromise means the attacker could have left backdoors or altered system files.
2. **Patch MOVEit Transfer:** Apply all relevant security patches to the affected application across your environment to prevent repeat attacks.

**Why this matters:**  
Recovery is about more than “fixing” a system, it's about restoring business operations, rebuilding trust, and preventing future compromise. Incomplete recovery can leave organizations exposed to repeated incidents.

---

## Reflection questions

Use these questions to deepen your understanding and reflect on incident response best practices:

1. **What evidence justified immediate containment?**  
    → POST traffic to an external IP and root access following a critical SQLi vulnerability, indicating active attacker presence.
    
2. **Why reimage instead of just cleaning malware?**  
    → Once an attacker has root (administrator) access, you cannot trust the system's integrity. Backdoors and hidden changes may persist if you simply “clean” malware.
    
3. **What MITRE ATT&CK tactics were used?**  
    →
    
    - T1190 – Exploit Public-Facing App
    - T1068 – Privilege Escalation
    - T1071.001 – C2 over Web Protocols

**Why this matters:**  
Reflection and critical thinking are essential for developing security judgment. These questions help you connect scenario details to best practices and common frameworks, building confidence for real-world roles.

---

## Real-world connection

This lab simulates a real-world SOC incident where logs, scan data, and system behavior must be correlated quickly to contain a threat before data exfiltration or lateral movement occurs. Containment decisions must be weighed against operational risk and service availability, a common tension in enterprise security operations.

**Why this matters:**  
Cybersecurity incidents don't happen in a vacuum, responders must make difficult decisions under time pressure, balancing security with business needs. Practicing analysis and containment with real evidence prepares you for what you'll face in the workplace.

## Glossary

**Note:** If the glossary doesn't download, right-click and open the link in a new tab.

|Term|Definition|
|---|---|
|Command and Control (C2)|The infrastructure used by adversaries to manage compromised systems remotely. C2 channels often employ encryption or stealth protocols to evade detection and are used to deploy malware, execute commands, or exfiltrate data.|
|Common Vulnerabilities and Exposures (CVE)|A catalog of publicly known cybersecurity vulnerabilities, maintained by MITRE and referenced by OpenVAS during scans.|
|Common Vulnerability Scoring System (CVSS)|A standardized method for scoring the severity of vulnerabilities on a scale from 0.0 (low) to 10.0 (critical).|
|Containment|A tactical response aimed at isolating or limiting a threat to prevent further harm. The actions include isolating infected systems, blocking network access, or deactivating compromised accounts.|
|Endpoint Detection and Response (EDR)|An endpoint protection solution that goes beyond antivirus. EDR platforms continuously monitor endpoint behavior and enable defenders to investigate incidents, quarantine devices, or respond in real time.|
|Feed synchronization|The process of updating OpenVAS with the latest Network Vulnerability Tests (NVTs), CVEs, and scan-related metadata via greenbone-feed-sync.|
|Greenbone Security Assistant (GSA)|The web-based interface of OpenVAS for managing scans, targets, and vulnerability reports.|
|Greenbone Security Assistant Daemon (gsad)|A web server that provides the web-based GUI to interact with OpenVAS (typically via port 9392).|
|Greenbone Vulnerability Management (GVM)|A collection of services that includes OpenVAS, gvmd, gsad, and supporting tools for managing, executing, and reporting vulnerability scans.|
|Greenbone Vulnerability Manager Daemon (gvmd)|A central management service that manages scan tasks, credentials, configurations, and report storage.|
|MITRE Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK)|A comprehensive framework documenting real-world attack behavior, categorized by tactics such as persistence or lateral movement and by techniques such as credential dumping. Security tools map detections to ATT&CK for strategic coverage.|
|Network Vulnerability Test (NVT)|A script used by OpenVAS to detect specific vulnerabilities on target systems. These tests are updated via feed synchronization.|
|OpenVAS|An open-source vulnerability scanning engine, now part of the Greenbone Vulnerability Management (GVM) suite.|
|Privilege escalation|The process where an attacker moves from a lower permission level, such as user, to a higher one, such as admin or root, allowing more destructive capabilities such as system modification or data exfiltration.|
|Reimaging|A recovery method that involves completely replacing an operating system (OS) from a clean, trusted image. This is used when a system’s integrity is in question or persistent threats such as rootkits cannot be cleanly removed.|
|Security Information and Event Management (SIEM)|A central system that ingests and analyzes logs from multiple sources—firewalls, servers, endpoints, scanners like OpenVAS—to detect patterns that may indicate a breach or anomaly.|
|Security Orchestration, Automation, and Response (SOAR)|A platform that unifies detection systems such as SIEM, EDR, OpenVAS, and threat intel into a single workflow engine, allowing incident response tasks to be orchestrated and executed automatically or semiautomatically.|
## Detection essentials

- **Scan for external exposure**
    
    - Run unauthenticated scans against internet-facing assets to uncover services exposed to the public, such as web applications, FTP servers, or mail gateways
- **Perform authenticated scanning**
    
    - Use credentials via SSH or SMB to detect hidden risks such as insecure configurations, unpatched software, or improper privilege assignments
- **Update vulnerability feeds**
    
    - Run `greenbone-feed-sync` regularly to ensure OpenVAS is current with the latest CVEs and exploit data. This is especially critical during fast-evolving threat events such as Log4Shell and MOVEit.

## Trigger indicators for containment

Containment should be initiated when any of the following are observed, particularly if multiple indicators coincide.

- **Outbound traffic to suspicious IPs**
    
    - Flag unusual external traffic, particularly to known C2 servers or TOR exit nodes—it may indicate malware or exfiltration
- **Unauthorized privilege escalation**
    
    - Contain systems showing unexplained elevation of user or process privileges, such as a user gaining admin access without a clear cause
- **Critical vulnerability + abnormal behavior**
    
    - Escalate incidents where OpenVAS flags CVSS ≥ 9.0 and the host generates anomalous logs or traffic patterns emerge

## Containment techniques by layer

|**Technique**|**Details**|
|---|---|
|**EDR quarantine**|- Instant endpoint isolation via tools like CrowdStrike, Defender, or SentinelOne<br>- Blocks network access while preserving local data for investigation|
|**Firewall ACLs**|- Network-layer containment<br>- Blocks specific IP addresses, services, or ports related to compromised systems. Especially useful when EDR is not present|
|**VLAN segmentation**|- Logically separates suspicious or infected systems from the main network<br>- Allows controlled access for analysis or remediation while limiting spread|

## When to choose reimaging

Consider reimaging a host when:

- **Compromise** reaches the system kernel, firmware, or bootloader level
- **Root/SYSTEM access** has been achieved by unauthorized users
- There is evidence of **log tampering** or forensic obfuscation
- The **system is noncritical,** and rebuilding is faster than manual remediation

> Note: Always perform memory and disk capture before reimaging if forensic analysis or legal reporting is required.

## MITRE ATT&CK technique mapping

Use OpenVAS CVE findings and behavioral observations to map incidents to adversarial techniques for better detection and red team validation.

| **Technique ID** | **Description**                       | **Context example**                                                |
| ---------------- | ------------------------------------- | ------------------------------------------------------------------ |
| **T1190**        | Exploit a public-facing application   | OpenVAS detects Apache Struts CVE on the external web server       |
| **T1068**        | Exploitation for privilege escalation | CVE exploited to gain SYSTEM/root on Windows or Linux endpoint     |
| **T1071.001**    | Command and control via web protocols | Observed outbound HTTPS to non-whitelisted domains post-compromise |