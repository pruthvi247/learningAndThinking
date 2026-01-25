
# Vulnerability Detection with OpenVAS

This reading provides a comprehensive recap of using OpenVAS (Open Vulnerability Assessment Scanner) as a cornerstone tool for vulnerability detection. In earlier modules, you explored OpenVAS from an offensive perspective, using it to discover weaknesses before exploiting them. That exercise demonstrated how attackers leverage vulnerability scanners to plan intrusion attempts.

Now, you will revisit OpenVAS from the perspective of a defender. The focus shifts from "How do I exploit this?" to "How do I detect and remediate this before it is exploited?" This mindset shift mirrors the real-world distinction between penetration testing teams and security operations teams. While attackers see scan results as opportunities, defenders view them as urgent warnings and priorities for remediation.

In this recap, we will review OpenVAS configuration options, scan types, and interpretation strategies. By mastering these elements, you will strengthen your ability to detect vulnerabilities and reduce exposure proactively. The guiding principle is simple but powerful: detection is prevention. Identifying weaknesses early and interpreting them in context allows defenders to prioritize resources and remediate issues before adversaries can act.

## OpenVAS as a defensive tool

OpenVAS is a free, open-source vulnerability scanner developed by Greenbone Networks. It is capable of detecting over 50,000 known vulnerabilities across operating systems, applications, and network services. Its core value lies in two factors:

- **Configurability**: Analysts can adjust scan depth, timing, and target scope to suit different environments.
- **Vulnerability intelligence**: OpenVAS is continuously updated with plugins linked to Common Vulnerabilities and Exposures (CVE) identifiers. This ensures that it aligns with current industry knowledge about software flaws, misconfigurations, and exploitable conditions.
    

Because OpenVAS provides a defender's view of potential system weaknesses, it is a widely adopted tool in both enterprise security operations centers (SOCs) and academic training environments.

## Scan types in OpenVAS

The flexibility of OpenVAS lies in the variety of scans it supports. Each scan type serves a distinct purpose in both detection and defense:

- **Full and fast scans**: Provide rapid assessments of common weaknesses. They are ideal for quick checks, such as validating whether recently patched systems remain vulnerable to known exploits. However, they may miss subtle misconfigurations.
- **Custom scans**: Can be configured to target specific hosts, ports, or services. This is useful when an investigation has already identified suspicious activity and the team wants to focus narrowly on one vector.
- **Credentialed scans**: Use valid system credentials to log in and evaluate internal configurations. Credentialed scans often uncover vulnerabilities invisible to external attackers but critical for system hardening, such as weak file permissions or outdated libraries.
The choice of scan type is situational. During incident response, a rapid, full, and fast scan may be prioritized to quickly assess system exposure. For long-term security posture management, credentialed scans provide deeper visibility.
## The role of configuration in visibility

In defensive operations, scan configuration directly impacts what analysts can see. A poorly configured scan may overlook critical weaknesses. Conversely, a carefully tuned scan maximizes detection without overwhelming analysts with false positives.

- **Port range selection**: Limiting scans to default ports may miss services running on non-standard ports, a common attacker tactic. Comprehensive port ranges improve detection accuracy.
- **Timing and performance**: Aggressive scans can disrupt system performance. Defenders must balance thoroughness with operational stability, often scheduling scans during maintenance windows.
- **Exclusions**: Some services, such as highly sensitive production databases, may need to be excluded from intrusive checks. However, defenders must document these exceptions to ensure that risks are still understood.
    
Real-world security programs rely on this balance: scan deeply enough to detect, but carefully enough to avoid self-inflicted downtime.

## Interpreting scan results
Once an OpenVAS scan completes, results are categorized by severity: Low, Medium, High, and Critical. Each finding typically includes:

- A CVE identifier linking it to a publicly known vulnerability
- A CVSS score (Common Vulnerability Scoring System) rating severity numerically
- Exploitability information, sometimes with references to proof-of-concept code

Analysts must go beyond the raw numbers. A vulnerability's contextual risk is as important as its technical severity. For example:

- A medium vulnerability in an internet-facing web server could pose a greater immediate threat than a high vulnerability on an isolated test machine.
- A critical flaw in outdated software may not be exploitable if the service is disabled. However, leaving it unpatched still creates risk if that service is re-enabled in the future.
Contextual interpretation is what transforms scan results into actionable security decisions.
## Connecting OpenVAS results to earlier exploitation

In earlier modules, you exploited vulnerabilities after scanning with OpenVAS. From the attacker’s perspective, these vulnerabilities were entry points. From the defender’s perspective, they are early warning signs.

As part of this recap, you will:
- Compare the vulnerabilities detected now with the ones you previously exploited.
- Recognize that the very same scan output can serve both attacker reconnaissance and defender detection.
- Reinforce that analysts and adversaries often look at the same data but apply different objectives. Attackers plan an intrusion, while defenders plan remediation.
    

This dual perspective is a cornerstone of cybersecurity education: understanding how the other side uses tools sharpens defensive skills.

## Integrating OpenVAS into defensive workflows

Modern security teams rarely rely on a single tool. OpenVAS is often integrated into broader workflows:

- **SIEM integration**: OpenVAS results feed into Security Information and Event Management systems, where they are correlated with log data and network alerts.
- **Patch management**: Findings guide IT teams on which systems need urgent patching, reducing overall exposure.
- **Continuous monitoring**: Scheduled scans provide ongoing assurance, highlighting new vulnerabilities as soon as they appear in updated CVE records.

These integrations reflect the professional expectation that vulnerability scanning is not a one-time event but part of continuous security operations.

## Key takeaway

OpenVAS is both an attacker reconnaissance tool and a defender detection system. Its value lies in translating raw scan results into actionable insights. For attackers, the tool highlights exploitable weaknesses. For defenders, it highlights remediation priorities. By configuring scans appropriately, interpreting results in context, and integrating findings into broader workflows, security teams can turn vulnerability detection into a proactive shield against compromise.

## Summary

In summary, this activity reinforces how OpenVAS serves as both a detection tool for defenders and a reconnaissance tool for attackers, and how the way results are used determines whether an organization stays secure or becomes compromised.

- Review OpenVAS as a defensive tool with configurable options and updated vulnerability intelligence.
- Understand different scan types, including full and fast, custom, and credentialed scans.
- Recognize how configuration choices such as port ranges, timing, and exclusions impact visibility.
- Learn to interpret scan results in context by considering severity, exploitability, and system exposure.
- Compare current OpenVAS results with earlier exploitation to reinforce attacker versus defender perspectives.
- See how OpenVAS integrates into workflows such as SIEM, patch management, and continuous monitoring.

--------------------
# Lab: Detection and Log Analysis

**Estimated time needed:** 60 minutes

## Overview

The defensive counterpart to exploitation is detection. SOC analysts depend heavily on logs to uncover intrusions, from authentication attempts to suspicious process launches. In the real world, rapid log analysis can mean the difference between stopping an intrusion early or suffering data exfiltration. This lab places you in the role of a Blue Team analyst, correlating vulnerability scan data with log evidence to extract Indicators of Compromise (IOCs). It mirrors real IR workflows where detection begins with combining threat intelligence and system evidence.

In this lab, you will act as a Blue Team analyst to confirm and understand compromise on a host machine targeted in earlier labs. You will combine a vulnerability scan using OpenVAS with manual log analysis to extract a concrete Indicator of Compromise (IOC). By the end, you will have both tool‑driven context (OpenVAS report) and forensic proof (logs) connecting a plausible exploit path to actual system activity.

> **Lab safety:** Perform all scans only in your controlled lab network. Do not scan systems you do not own or manage.

## Learning objectives

After completing this lab, you will be able to:

- Run an OpenVAS scan to identify high‑risk vulnerabilities on a target host
- Filter vulnerability results to focus on likely intrusion vectors
- Analyze authentication and system logs to confirm attacker activity
- Map observed behaviors to MITRE ATT&CK techniques
## Exercise 0: Pre‑checks

1. Verify that OpenVAS (GVM) is installed on your Kali VM:
    
    1. `gvm-check-setup`
    
2. Ensure the target VM is reachable by ping or nmap discovery:
    
    1. `ping -c 2 <target_ip>`
### Why this step is important:

Confirming the scanner and target connectivity ensures the scan produces meaningful results.
## Exercise 1: Run an OpenVAS Scan

1. Start Greenbone services and log into the GSA web interface:
    
    1. `sudo gvm-start`
    If it fails to start, please keep running the "sudo gvm-check-setup" command and follow the fix instructions until the installation was successful, if you are having difficulty, please see lab "Set Up OpenVAS in a Virtual Machine" from the Incident Response and Defense with OpenVAS course.
    
    Wait for the "GSA is available at …" message, then open the provided URL (default: `https://127.0.0.1:9392`) and log in.
    
1. Create a new scan target:
    - Navigate: **Configuration → Targets → New Target**
    - Name: `Compromised-Host`
    - Host(s): `<target_ip>`
    - Port list: `All TCP`
    - Alive test: `Consider Alive` (ensures scan runs even if ICMP is filtered)
    - Save
2. Create and start a scan task:
    - Navigate: **Scans → Tasks → New Task**
    - Name: `Quick Assessment - Compromised-Host`
    - Scan Config: `Full and fast`
    - Target: `Compromised-Host`
    - Save, then click **Start**

### Why this step is important:

"Full and fast" provides broad coverage while completing within the lab's time window.
## Exercise 2: Review vulnerability results

1. When the task completes (or while it is still running), go to **Scans → Reports** and open the latest report.
2. Filter results by severity:
    - Critical (CVSS v3.1 ≥ 9.0)
    - High (7.0–8.9)
3. Identify 2–3 plausible root causes of compromise. For example:
    - Outdated OpenSSH allowing brute‑force or info disclosure.
    - Web service misconfigurations enabling directory traversal or RCE.
    - Weak credentials flagged by OpenVAS plugins.

**Action:** Document names/IDs and a short rationale:  
"Relevant because SSH was targeted and we later saw brute‑force attempts in logs."

### Why this step is important:

OpenVAS findings provide theoretical intrusion paths. You must correlate them with log data to confirm exploitation.
## Exercise 3: Analyze authentication logs

1. SSH into the compromised host:
    
    1. `ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa 			[msfadmin@192.168.1](mailto:msfadmin@192.168.1).49`
    2. `#use any password, we want this to fail`
    
    3. `ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa [msfadmin@192.168.1](mailto:msfadmin@192.168.1).49`
    4. `#password: msfadmin`
2. Review failed login attempts:
    1. `sudo grep "Failed password" /var/log/auth.log | tail -20`    
3. Review successful logins:
    1. `sudo grep "Accepted password" /var/log/auth.log | tail -20`
**Expected pattern:**
- Many failed attempts from one IP, followed by a successful login from the same IP.
### Why this step is important:

Authentication logs reveal brute‑force patterns and identify valid account compromise.

> **Alternative (journalctl):**
> 
> 1. `sudo journalctl -u ssh -S "today" | tail -50`
> 2. `sudo journalctl -t sshd | grep -E "Failed|Accepted"`
## Exercise 4: Analyze system logs for suspicious activity

1. Review session openings and privilege escalation attempts:
    1. `sudo grep "session opened" /var/log/syslog | tail -20`
    2. `sudo grep -E "sudo:|su\[" /var/log/auth.log | tail -30`
2. Look for suspicious commands (reverse shells, downloads):
    1. `sudo grep -E "bash|/dev/tcp|nc |ncat |curl |wget " /var/log/syslog | tail -30`
    2. `sudo grep -E "bash|/dev/tcp|nc |ncat |curl |wget " /var/log/auth.log | tail -30`
3. Check for persistence attempts:
    1. `sudo grep -i cron /var/log/syslog | tail -30`
    2. `systemctl list-unit-files --type=service | grep enabled`
### Why this step is important:

System logs confirm attacker actions after login, such as privilege escalation or persistence.
## Exercise 5: Select and document an IOC

Acceptable IOC types include:
- Source IP of suspicious successful login
- Malicious path or filename (`/tmp/.update.sh`)
- Unexpected process (`nc`, `bash`, `curl`)
- New or unexpected user

**Action:** Record the exact log line and timestamp of your IOC for later hashing.
### Why this step is important:

A concrete IOC connects OpenVAS findings to observable system activity, building an evidence‑based incident narrative.

-----------------------------

# Lab2: IOC Hunt and Containment Drill


## Overview

This lab simulates defender activity after an intrusion. You will identify persistence mechanisms (cron jobs, autostart files, malicious temp scripts, rogue services), contain them safely by quarantining rather than deleting, verify remediation, and document findings.

> **Safety Note:** Perform these steps only on the lab VM. Always move (quarantine) instead of deleting so evidence is preserved.
## Learning objectives

After completing this lab, you will be able to:

- Enumerate persistence across cron, init systems, autostart profiles, and temp directories
- Apply containment best practices (quarantine, disable, document)
- Verify remediation by re-checking processes and sockets
- Document findings and map to MITRE ATT&CK
## Exercise 0: Environment and pre-checks

**Command:**

1. `whoami`
2. `id`
3. `sudo -l 2>/dev/null || echo "No sudo or not permitted"`
4. `mkdir -p /tmp/ioc_evidence`
### Why this step is important:

Confirm that you are operating on the compromised host with sufficient privileges. The evidence directory ensures outputs and copies are preserved.
**Expected output:**
- Your current user (for example, `root` or `msfadmin`)
- User/group IDs
- Sudo permissions (if available)

**Verification:**  
Check that `/tmp/ioc_evidence` exists and is writable.
## Exercise 1: Hunt for persistence mechanisms

### Task A: Cron-based persistence

**Command:**
1. `sudo crontab -l 2>/dev/null || echo "No root crontab"`
2. `sudo ls -la /etc/cron.* /etc/cron.d 2>/dev/null`
3. `sudo ls -la /var/spool/cron /var/spool/cron/crontabs 2>/dev/null`
4. `crontab -l 2>/dev/null || echo "No user crontab"`
### Why this step is important:

Attackers often hide persistence in cron jobs. Enumerating all cron locations helps spot malicious scheduling.

**Expected output:**

- Cron entries listed, possibly showing suspicious commands (for example, `/tmp/.update.sh`)

**Verification:**  
Copy any suspicious cron files to `/tmp/ioc_evidence` with preserved metadata.
### Task B: Init/service persistence

**Command:**

1. `command -v systemctl >/dev/null && {`
2.   `sudo systemctl list-unit-files --type=service | grep enabled`
3.   `sudo systemctl --type=service --state=running`
4. `} || {`
5.   `sudo ls -la /etc/init.d | head -n 50`
6.   `sudo service --status-all 2>/dev/null | head -n 50 || true`
7. `}`
### Why this step is important:

Services that auto-start give attackers resilience. Checking systemd or SysV init scripts reveals hidden backdoors.

**Expected output:**

- List of enabled/running services. Suspicious ones might appear out of place.

**Verification:**  
Copy suspicious unit files or init scripts to `/tmp/ioc_evidence`.
### Task C: Autostart and profile

**Command:**

1. `sudo test -f /etc/rc.local && sudo sed -n '1,200p' /etc/rc.local || echo "no /etc/rc.local"`
2. `sudo sed -n '1,200p' ~/.bashrc ~/.profile /root/.bashrc 2>/dev/null`
3. `ls -la ~/.config/autostart 2>/dev/null || true`
### Why this step is important:

Attackers might modify shell profiles or autostart files to reinfect a user session.

**Expected output:**
- Lines in `.bashrc` or `/etc/rc.local` launching scripts from `/tmp` or hidden dirs.
### Task D: Temp directories

**Command:**

1. `ls -la /tmp /var/tmp | head -n 100`
2. `sudo find /tmp /var/tmp -maxdepth 2 -type f -printf '%M %u %g %s %TY-%Tm-%Td %TH:%TM %p\n' 2>/dev/null | sort -k6`
### Why this step is important:

Attackers frequently drop scripts in temp directories. Looking at permissions and timestamps uncovers hidden artifacts.

**Expected output:**

- Suspicious files such as `/tmp/.update.sh`
## Exercise 2: Contain malicious artifacts

**Command (examples):**

1. `sudo mkdir -p /root/quarantine`
2. `sudo chmod 700 /root/quarantine`

3. `sudo mv /etc/cron.d/sneaky /root/quarantine/sneaky.disabled 2>/dev/null || true`
4. `(crontab -l | sed '/\/tmp\/\.update\.sh/d') | crontab -`

5. `if command -v systemctl >/dev/null; then`
6.   `sudo systemctl stop suspicious.service 2>/dev/null || true`
7.   `sudo systemctl disable suspicious.service 2>/dev/null || true`
8.   `sudo mv /etc/systemd/system/suspicious.service /root/quarantine/suspicious.service.disabled 2>/dev/null || true`
9. `else`
10.   `sudo service suspicious stop 2>/dev/null || true`
11.   `sudo mv /etc/init.d/suspicious /root/quarantine/suspicious.init.disabled 2>/dev/null || true`
12. `fi`

13. `sudo cp --preserve=mode,ownership,timestamps /tmp/.update.sh /root/quarantine/.update.sh.disabled 2>/dev/null || true`
14. `sudo rm -f /tmp/.update.sh || true`
### Why this step is important:

Quarantining instead of deleting preserves forensic evidence while removing the active threat.

**Expected output:**

- Files moved into `/root/quarantine`
## Exercise 3: Verify remediation

**Command:**

1. `sudo crontab -l 2>/dev/null || echo "No root crontab"`
2. `crontab -l 2>/dev/null || echo "No user crontab"`

3. `command -v systemctl >/dev/null && {`
4.   `sudo systemctl is-enabled suspicious.service 2>/dev/null || echo "not enabled"`
5. `} || {`
6.   `sudo service suspicious status 2>/dev/null || echo "service status unknown"`
7. `}`

8. `ps aux | egrep -i "update|persist|sneaky|\.update\.sh" || echo "No suspicious processes"`
9. `sudo ss -tulpn | egrep -i "update|persist|sneaky" || sudo netstat -tulpn | egrep -i "update|persist|sneaky" || echo "No suspicious sockets"`
### Why this step is important:

Verification ensures that persistence is no longer active and the system is clean.

**Expected output:**

- No suspicious processes or sockets. Services are disabled.
## Exercise 4: Document & MITRE ATT&CK

**Command:**

1. `nano /tmp/ioc_evidence/ioc_containment.txt`
**Add content:**

- Summary of findings
- Timeline of discovery and actions
- Persistence artifacts quarantined
- Containment actions
- Verification results
- ATT&CK mapping (T1053.003, T1543.002, T1070.006, T1564.001)
