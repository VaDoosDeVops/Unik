 ### 1 ###
vadooos_s@DESKTOP-U60R4GV:~$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.2  0.1 165892 12944 ?        Ss   12:29   0:00 /sbin/init
root           2  0.0  0.0   2616  1440 ?        Sl   12:29   0:00 /init
root           6  0.0  0.0   2616   132 ?        Sl   12:29   0:00 plan9 --control-socket 6 --log-level 4 --
root          62  0.0  0.1  39544 14252 ?        S<s  12:29   0:00 /lib/systemd/systemd-journald
root          86  0.1  0.0  21840  5736 ?        Ss   12:29   0:00 /lib/systemd/systemd-udevd
systemd+     165  0.0  0.1  26200 13324 ?        Ss   12:29   0:00 /lib/systemd/systemd-resolved
systemd+     169  0.0  0.0  89364  6592 ?        Ssl  12:29   0:00 /lib/systemd/systemd-timesyncd
root         183  0.0  0.0   4308  2684 ?        Ss   12:29   0:00 /usr/sbin/cron -f -P
message+     185  0.0  0.0   8584  4708 ?        Ss   12:29   0:00 @dbus-daemon --system --address=systemd:
root         190  0.0  0.2  30108 19728 ?        Ss   12:29   0:00 /usr/bin/python3 /usr/bin/networkd-dispat
syslog       191  0.0  0.0 222404  7368 ?        Ssl  12:29   0:00 /usr/sbin/rsyslogd -n -iNONE
root         194  0.0  0.0  15332  7468 ?        Ss   12:29   0:00 /lib/systemd/systemd-logind
root         219  0.0  0.0   3240  1144 hvc0     Ss+  12:29   0:00 /sbin/agetty -o -p -- \u --noclear --keep
root         221  0.0  0.0   3196  1116 tty1     Ss+  12:29   0:00 /sbin/agetty -o -p -- \u --noclear tty1 l
root         233  0.0  0.2 107164 21092 ?        Ssl  12:29   0:00 /usr/bin/python3 /usr/share/unattended-up
root         301  0.0  0.0   2624   120 ?        Ss   12:29   0:00 /init
root         302  0.0  0.0   2624   128 ?        R    12:29   0:00 /init
vadooos+     303  0.0  0.0   6200  5104 pts/0    Ss   12:29   0:00 -bash
root         304  0.0  0.0   7528  4896 pts/1    Ss   12:29   0:00 /bin/login -f
vadooos+     394  0.0  0.1  16968  9288 ?        Ss   12:29   0:00 /lib/systemd/systemd --user
vadooos+     395  0.0  0.0 168816  3416 ?        S    12:29   0:00 (sd-pam)
vadooos+     401  0.0  0.0   6104  4896 pts/1    S+   12:29   0:00 -bash
vadooos+     432  0.0  0.0   7484  3204 pts/0    R+   12:34   0:00 ps aux

vadooos_s@DESKTOP-U60R4GV:~$ ps -e
    PID TTY          TIME CMD
      1 ?        00:00:00 systemd
      2 ?        00:00:00 init-systemd(Ub
      6 ?        00:00:00 init
     62 ?        00:00:00 systemd-journal
     86 ?        00:00:00 systemd-udevd
    165 ?        00:00:00 systemd-resolve
    169 ?        00:00:00 systemd-timesyn
    183 ?        00:00:00 cron
    185 ?        00:00:00 dbus-daemon
    190 ?        00:00:00 networkd-dispat
    191 ?        00:00:00 rsyslogd
    194 ?        00:00:00 systemd-logind
    219 hvc0     00:00:00 agetty
    221 tty1     00:00:00 agetty
    233 ?        00:00:00 unattended-upgr
    301 ?        00:00:00 SessionLeader
    302 ?        00:00:00 Relay(303)
    303 pts/0    00:00:00 bash
    304 pts/1    00:00:00 login
    394 ?        00:00:00 systemd
    395 ?        00:00:00 (sd-pam)
    401 pts/1    00:00:00 bash
    433 pts/0    00:00:00 ps

### 2 ####
vadooos_s@DESKTOP-U60R4GV:~$ ps auxf
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.1 165892 10936 ?        Ss   13:42   0:00 /sbin/init
root           2  0.0  0.0   2616  1440 ?        Sl   13:42   0:00 /init
root           6  0.0  0.0   2616   132 ?        Sl   13:42   0:00  \_ plan9 --control-socket 6 --log-le
root         301  0.0  0.0   2624   120 ?        Ss   13:42   0:00  \_ /init
root         302  0.0  0.0   2624   128 ?        S    13:42   0:00  |   \_ /init
vadooos+     303  0.0  0.0   6200  5104 pts/0    Ss   13:42   0:00  |       \_ -bash
vadooos+     939  0.0  0.0   7484  3152 pts/0    R+   14:12   0:00  |           \_ ps auxf
root         304  0.0  0.0   7528  4896 pts/1    Ss   13:42   0:00  \_ /bin/login -f
vadooos+     401  0.0  0.0   6104  4896 pts/1    S+   13:42   0:00      \_ -bash
root          62  0.0  0.1  47740 14604 ?        S<s  13:42   0:00 /lib/systemd/systemd-journald
root          86  0.0  0.0  21840  5736 ?        Ss   13:42   0:00 /lib/systemd/systemd-udevd
systemd+     165  0.0  0.1  26200 13324 ?        Ss   13:42   0:00 /lib/systemd/systemd-resolved
systemd+     169  0.0  0.0  89364  6592 ?        Ssl  13:42   0:00 /lib/systemd/systemd-timesyncd
root         183  0.0  0.0   4308  2684 ?        Ss   13:42   0:00 /usr/sbin/cron -f -P
message+     185  0.0  0.0   8584  4708 ?        Ss   13:42   0:00 @dbus-daemon --system --address=syste
root         190  0.0  0.2  30108 19728 ?        Ss   13:42   0:00 /usr/bin/python3 /usr/bin/networkd-di
syslog       191  0.0  0.0 222404  7368 ?        Ssl  13:42   0:00 /usr/sbin/rsyslogd -n -iNONE
root         194  0.0  0.0  15332  7468 ?        Ss   13:42   0:00 /lib/systemd/systemd-logind
root         219  0.0  0.0   3240  1144 hvc0     Ss+  13:42   0:00 /sbin/agetty -o -p -- \u --noclear --
root         221  0.0  0.0   3196  1116 tty1     Ss+  13:42   0:00 /sbin/agetty -o -p -- \u --noclear tt
root         233  0.0  0.2 107164 21092 ?        Ssl  13:42   0:00 /usr/bin/python3 /usr/share/unattende
vadooos+     394  0.0  0.1  16968  9288 ?        Ss   13:42   0:00 /lib/systemd/systemd --user
vadooos+     395  0.0  0.0 168816  3416 ?        S    13:42   0:00  \_ (sd-pam)
root         768  0.0  0.2 293024 22368 ?        Ssl  13:48   0:00 /usr/libexec/packagekitd
root         772  0.0  0.0 234512  6912 ?        Ssl  13:48   0:00 /usr/libexec/polkitd --no-debug

### 3 ###
 top +v
     944 vadooos+  20   0    7792   3600   2996 R   0.3   0.0   0:00.02 top
      1 root      20   0  165892  10936   7996 S   0.0   0.1   0:00.83 systemd
      2 root      20   0    2616   1440   1320 S   0.0   0.0   0:00.01 init-systemd(Ub
      6 root      20   0    2616    132    132 S   0.0   0.0   0:00.00 init
     62 root      19  -1   47740  14604  13520 S   0.0   0.2   0:00.25 systemd-journal

#### 4 ####

vadooos_s@DESKTOP-U60R4GV:~$ ps -eo pid,comm,nlwp --sort=-nlwp | awk '$3 > 2' | head -n 2
    PID COMMAND         NLWP
    191 rsyslogd           4

### 5 ###
Через top:
открыть top
нажать r
ввести PID
указать новый nice (например 10)

### 6 ###
vadooos_s@DESKTOP-U60R4GV:~$ lsof -u aa
lsof: can't get UID for aa
lsof 4.93.2
 latest revision: https://github.com/lsof-org/lsof
 latest FAQ: https://github.com/lsof-org/lsof/blob/master/00FAQ
 latest (non-formatted) man page: https://github.com/lsof-org/lsof/blob/master/Lsof.8
 usage: [-?abhKlnNoOPRtUvVX] [+|-c c] [+|-d s] [+D D] [+|-E] [+|-e s] [+|-f[gG]]
 [-F [f]] [-g [s]] [-i [i]] [+|-L [l]] [+m [m]] [+|-M] [-o [o]] [-p s]
 [+|-r [t]] [-s [p:s]] [-S [t]] [-T [t]] [-u s] [+|-w] [-x [fl]] [--] [names]
Use the ``-h'' option to get more help information.

### 7 ###
vadooos_s@DESKTOP-U60R4GV:~$ free -h
               total        used        free      shared  buff/cache   available
Mem:           7.5Gi       398Mi       6.9Gi       3.0Mi       180Mi       6.9Gi
Swap:          2.0Gi          0B       2.0Gi

### 8 ###
vadooos_s@DESKTOP-U60R4GV:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
none            3.8G     0  3.8G   0% /usr/lib/modules/5.15.167.4-microsoft-standard-WSL2
none            3.8G  4.0K  3.8G   1% /mnt/wsl
drivers         477G  424G   53G  90% /usr/lib/wsl/drivers
/dev/sdc       1007G  3.0G  953G   1% /
none            3.8G  104K  3.8G   1% /mnt/wslg
none            3.8G     0  3.8G   0% /usr/lib/wsl/lib
rootfs          3.8G  2.2M  3.8G   1% /init
none            3.8G  508K  3.8G   1% /run
none            3.8G     0  3.8G   0% /run/lock
none            3.8G     0  3.8G   0% /run/shm
tmpfs           4.0M     0  4.0M   0% /sys/fs/cgroup
none            3.8G   96K  3.8G   1% /mnt/wslg/versions.txt
none            3.8G   96K  3.8G   1% /mnt/wslg/doc
C:\             477G  424G   53G  90% /mnt/c

### 9 ###
vadooos_s@DESKTOP-U60R4GV:~$ cat /proc/301/status
Name:   SessionLeader
Umask:  0022
State:  S (sleeping)
Tgid:   301
Ngid:   0
Pid:    301
PPid:   2
TracerPid:      0
Uid:    0       0       0       0
Gid:    0       0       0       0
FDSize: 128
Groups:
NStgid: 301
NSpid:  301
NSpgid: 301
NSsid:  301
VmPeak:     2624 kB
VmSize:     2624 kB
VmLck:         0 kB
VmPin:         0 kB
VmHWM:       120 kB
VmRSS:       120 kB
RssAnon:             120 kB
RssFile:               0 kB
RssShmem:              0 kB
VmData:      332 kB
VmStk:       132 kB
VmExe:      1484 kB
VmLib:         8 kB
VmPTE:        40 kB
VmSwap:        0 kB
HugetlbPages:          0 kB
CoreDumping:    0
THP_enabled:    1
Threads:        1
SigQ:   0/30538
SigPnd: 0000000000000000
ShdPnd: 0000000000000000
SigBlk: 0000000000000000
SigIgn: fffffffc7ff8fefe
SigCgt: 0000000000010000
CapInh: 0000000000000000
CapPrm: 000001ffffffffff
CapEff: 000001ffffffffff
CapBnd: 000001ffffffffff
CapAmb: 0000000000000000
NoNewPrivs:     0
Seccomp:        0
Seccomp_filters:        0
Speculation_Store_Bypass:       thread vulnerable
SpeculationIndirectBranch:      conditional enabled
Cpus_allowed:   fff
Cpus_allowed_list:      0-11
Mems_allowed:   1
Mems_allowed_list:      0
voluntary_ctxt_switches:        2
nonvoluntary_ctxt_switches:     0

### 10 ###

vadooos_s@DESKTOP-U60R4GV:~$ cat /proc/cpuinfo
processor       : 0
vendor_id       : AuthenticAMD
cpu family      : 25
model           : 80
model name      : AMD Ryzen 5 7530U with Radeon Graphics
stepping        : 0
microcode       : 0xffffffff
cpu MHz         : 1996.204
cache size      : 512 KB
physical id     : 0
siblings        : 12
core id         : 0
cpu cores       : 6
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid extd_apicid pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw topoext perfctr_core ssbd ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip vaes vpclmulqdq rdpid fsrm
bugs            : sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass srso
bogomips        : 3992.40
TLB size        : 2560 4K pages
clflush size    : 64
cache_alignment : 64
address sizes   : 48 bits physical, 48 bits virtual
power management:

processor       : 1
vendor_id       : AuthenticAMD
cpu family      : 25
model           : 80
model name      : AMD Ryzen 5 7530U with Radeon Graphics
stepping        : 0
microcode       : 0xffffffff
cpu MHz         : 1996.204
cache size      : 512 KB
physical id     : 0
siblings        : 12
core id         : 0
cpu cores       : 6
apicid          : 1
initial apicid  : 1
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid extd_apicid pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw topoext perfctr_core ssbd ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip vaes vpclmulqdq rdpid fsrm
bugs            : sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass srso
bogomips        : 3992.40
TLB size        : 2560 4K pages
clflush size    : 64
cache_alignment : 64
address sizes   : 48 bits physical, 48 bits virtual
power management:

processor       : 2
vendor_id       : AuthenticAMD
cpu family      : 25
model           : 80
model name      : AMD Ryzen 5 7530U with Radeon Graphics
stepping        : 0
microcode       : 0xffffffff
cpu MHz         : 1996.204
cache size      : 512 KB
physical id     : 0
siblings        : 12
core id         : 1
cpu cores       : 6
apicid          : 2
initial apicid  : 2
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid extd_apicid pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw topoext perfctr_core ssbd ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip vaes vpclmulqdq rdpid fsrm
bugs            : sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass srso
bogomips        : 3992.40
TLB size        : 2560 4K pages
clflush size    : 64
cache_alignment : 64
address sizes   : 48 bits physical, 48 bits virtual
power management:

processor       : 3
vendor_id       : AuthenticAMD
cpu family      : 25
model           : 80
model name      : AMD Ryzen 5 7530U with Radeon Graphics
stepping        : 0
microcode       : 0xffffffff
cpu MHz         : 1996.204
cache size      : 512 KB
physical id     : 0
siblings        : 12
core id         : 1
cpu cores       : 6
apicid          : 3
initial apicid  : 3
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid extd_apicid pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw topoext perfctr_core ssbd ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip vaes vpclmulqdq rdpid fsrm
bugs            : sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass srso
bogomips        : 3992.40
TLB size        : 2560 4K pages
clflush size    : 64
cache_alignment : 64
address sizes   : 48 bits physical, 48 bits virtual
power management:

processor       : 4
vendor_id       : AuthenticAMD
cpu family      : 25
model           : 80
model name      : AMD Ryzen 5 7530U with Radeon Graphics
stepping        : 0
microcode       : 0xffffffff
cpu MHz         : 1996.204
cache size      : 512 KB
physical id     : 0
siblings        : 12
core id         : 2
cpu cores       : 6
apicid          : 4
initial apicid  : 4
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid extd_apicid pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw topoext perfctr_core ssbd ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip vaes vpclmulqdq rdpid fsrm
bugs            : sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass srso
bogomips        : 3992.40
TLB size        : 2560 4K pages
clflush size    : 64
cache_alignment : 64
address sizes   : 48 bits physical, 48 bits virtual
power management:

processor       : 5
vendor_id       : AuthenticAMD
cpu family      : 25
model           : 80
model name      : AMD Ryzen 5 7530U with Radeon Graphics
stepping        : 0
microcode       : 0xffffffff
cpu MHz         : 1996.204
cache size      : 512 KB
physical id     : 0
siblings        : 12
core id         : 2
cpu cores       : 6
apicid          : 5
initial apicid  : 5
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid extd_apicid pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw topoext perfctr_core ssbd ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip vaes vpclmulqdq rdpid fsrm
bugs            : sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass srso
bogomips        : 3992.40
TLB size        : 2560 4K pages
clflush size    : 64
cache_alignment : 64
address sizes   : 48 bits physical, 48 bits virtual
power management:

processor       : 6
vendor_id       : AuthenticAMD
cpu family      : 25
model           : 80
model name      : AMD Ryzen 5 7530U with Radeon Graphics
stepping        : 0
microcode       : 0xffffffff
cpu MHz         : 1996.204
cache size      : 512 KB
physical id     : 0
siblings        : 12
core id         : 3
cpu cores       : 6
apicid          : 6
initial apicid  : 6
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid extd_apicid pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw topoext perfctr_core ssbd ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip vaes vpclmulqdq rdpid fsrm
bugs            : sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass srso
bogomips        : 3992.40
TLB size        : 2560 4K pages
clflush size    : 64
cache_alignment : 64
address sizes   : 48 bits physical, 48 bits virtual
power management:

processor       : 7
vendor_id       : AuthenticAMD
cpu family      : 25
model           : 80
model name      : AMD Ryzen 5 7530U with Radeon Graphics
stepping        : 0
microcode       : 0xffffffff
cpu MHz         : 1996.204
cache size      : 512 KB
physical id     : 0
siblings        : 12
core id         : 3
cpu cores       : 6
apicid          : 7
initial apicid  : 7
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid extd_apicid pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw topoext perfctr_core ssbd ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip vaes vpclmulqdq rdpid fsrm
bugs            : sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass srso
bogomips        : 3992.40
TLB size        : 2560 4K pages
clflush size    : 64
cache_alignment : 64
address sizes   : 48 bits physical, 48 bits virtual
power management:

processor       : 8
vendor_id       : AuthenticAMD
cpu family      : 25
model           : 80
model name      : AMD Ryzen 5 7530U with Radeon Graphics
stepping        : 0
microcode       : 0xffffffff
cpu MHz         : 1996.204
cache size      : 512 KB
physical id     : 0
siblings        : 12
core id         : 4
cpu cores       : 6
apicid          : 8
initial apicid  : 8
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid extd_apicid pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw topoext perfctr_core ssbd ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip vaes vpclmulqdq rdpid fsrm
bugs            : sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass srso
bogomips        : 3992.40
TLB size        : 2560 4K pages
clflush size    : 64
cache_alignment : 64
address sizes   : 48 bits physical, 48 bits virtual
power management:

processor       : 9
vendor_id       : AuthenticAMD
cpu family      : 25
model           : 80
model name      : AMD Ryzen 5 7530U with Radeon Graphics
stepping        : 0
microcode       : 0xffffffff
cpu MHz         : 1996.204
cache size      : 512 KB
physical id     : 0
siblings        : 12
core id         : 4
cpu cores       : 6
apicid          : 9
initial apicid  : 9
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid extd_apicid pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw topoext perfctr_core ssbd ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip vaes vpclmulqdq rdpid fsrm
bugs            : sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass srso
bogomips        : 3992.40
TLB size        : 2560 4K pages
clflush size    : 64
cache_alignment : 64
address sizes   : 48 bits physical, 48 bits virtual
power management:

processor       : 10
vendor_id       : AuthenticAMD
cpu family      : 25
model           : 80
model name      : AMD Ryzen 5 7530U with Radeon Graphics
stepping        : 0
microcode       : 0xffffffff
cpu MHz         : 1996.204
cache size      : 512 KB
physical id     : 0
siblings        : 12
core id         : 5
cpu cores       : 6
apicid          : 10
initial apicid  : 10
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid extd_apicid pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw topoext perfctr_core ssbd ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip vaes vpclmulqdq rdpid fsrm
bugs            : sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass srso
bogomips        : 3992.40
TLB size        : 2560 4K pages
clflush size    : 64
cache_alignment : 64
address sizes   : 48 bits physical, 48 bits virtual
power management:

processor       : 11
vendor_id       : AuthenticAMD
cpu family      : 25
model           : 80
model name      : AMD Ryzen 5 7530U with Radeon Graphics
stepping        : 0
microcode       : 0xffffffff
cpu MHz         : 1996.204
cache size      : 512 KB
physical id     : 0
siblings        : 12
core id         : 5
cpu cores       : 6
apicid          : 11
initial apicid  : 11
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid extd_apicid pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw topoext perfctr_core ssbd ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip vaes vpclmulqdq rdpid fsrm
bugs            : sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass srso
bogomips        : 3992.40
TLB size        : 2560 4K pages
clflush size    : 64
cache_alignment : 64
address sizes   : 48 bits physical, 48 bits virtual
power management:

### 11 ###
vadooos_s@DESKTOP-U60R4GV:~$ lsmod
Module                  Size  Used by