---

# Отчёт по работе с процессами 7 laba

## 1. Вывод списка всех процессов системы

Команда:

```bash
ps aux
```

Вывод (фрагмент):

```text
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
...
vadooos+     432  0.0  0.0   7484  3204 pts/0    R+   12:34   0:00 ps aux
```

Альтернативный вывод списка процессов:

```bash
ps -e
```

Фрагмент вывода:

```text
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
    ...
    433 pts/0    00:00:00 ps
```

## 2. Вывод дерева процессов

Команда:

```bash
ps auxf
```

Фрагмент вывода:

```text
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
...
```

## 3. Получение списка процессов, потребляющих наибольшее количество CPU (через `top`)

Команда запуска:

```bash
top
```

Фрагмент вывода (после сортировки по CPU, режим дерева `V`):

```text
    944 vadooos+  20   0    7792   3600   2996 R   0.3   0.0   0:00.02 top
      1 root      20   0  165892  10936   7996 S   0.0   0.1   0:00.83 systemd
      2 root      20   0    2616   1440   1320 S   0.0   0.0   0:00.01 init-systemd(Ub
      6 root      20   0    2616    132    132 S   0.0   0.0   0:00.00 init
     62 root      19  -1   47740  14604  13520 S   0.0   0.2   0:00.25 systemd-journal
```

## 4. Поиск процессов, имеющих более двух потоков

Команда:

```bash
ps -eo pid,comm,nlwp --sort=-nlwp | awk '$3 > 2' | head -n 2
```

Вывод:

```text
    PID COMMAND         NLWP
    191 rsyslogd           4
```

## 5. Изменение приоритета процессов (nice) через `top`

Алгоритм:

1. Открыть `top`:

   ```bash
   top
   ```
2. Нажать клавишу `r` (renice).
3. Ввести PID процесса.
4. Указать новый nice, например:

   ```text
   10
   ```

После этого приоритет процесса будет изменён.

## 6. Получение списка открытых файлов пользователя `aa`

Команда:

```bash
lsof -u aa
```

Вывод (ошибка, так как пользователь `aa` не найден):

```text
lsof: can't get UID for aa
lsof 4.93.2
 latest revision: https://github.com/lsof-org/lsof
 latest FAQ: https://github.com/lsof-org/lsof/blob/master/00FAQ
 latest (non-formatted) man page: https://github.com/lsof-org/lsof/blob/master/Lsof.8
 usage: [-?abhKlnNoOPRtUvVX] [+|-c c] [+|-d s] [+D D] [+|-E] [+|-e s] [+|-f[gG]]
 [-F [f]] [-g [s]] [-i [i]] [+|-L [l]] [+m [m]] [+|-M] [-o [o]] [-p s]
 [+|-r [t]] [-s [p:s]] [-S [t]] [-T [t]] [-u s] [+|-w] [-x [fl]] [--] [names]
Use the ``-h'' option to get more help information.
```

## 7. Получение текущего состояния системной памяти

Команда:

```bash
free -h
```

Вывод:

```text
               total        used        free      shared  buff/cache   available
Mem:           7.5Gi       398Mi       6.9Gi       3.0Mi       180Mi       6.9Gi
Swap:          2.0Gi          0B       2.0Gi
```

## 8. Получение информации об использовании дискового пространства

Команда:

```bash
df -h
```

Вывод (фрагмент):

```text
Filesystem      Size  Used Avail Use% Mounted on
none            3.8G     0  3.8G   0% /usr/lib/modules/5.15.167.4-microsoft-standard-WSL2
none            3.8G  4.0K  3.8G   1% /mnt/wsl
drivers         477G  424G   53G  90% /usr/lib/wsl/drivers
/dev/sdc       1007G  3.0G  953G   1% /
...
C:\             477G  424G   53G  90% /mnt/c
```

## 9. Получение информации о процессе из каталога `/proc`

Команда (для процесса с PID 301):

```bash
cat /proc/301/status
```

Фрагмент вывода:

```text
Name:   SessionLeader
Umask:  0022
State:  S (sleeping)
Tgid:   301
Ngid:   0
Pid:    301
PPid:   2
...
Threads:        1
voluntary_ctxt_switches:        2
nonvoluntary_ctxt_switches:     0
```

## 10. Получение информации о процессоре из каталога `/proc`

Команда:

```bash
cat /proc/cpuinfo
```

Фрагмент вывода:

```text
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
...
address sizes   : 48 bits physical, 48 bits virtual
power management:
```

(дальше повторяются блоки для процессоров 1–11).

## 11. Вывод списка модулей ядра

Команда:

```bash
lsmod
```

Начало вывода:

```text
Module                  Size  Used by
```

(далее следует перечень загруженных модулей ядра и счётчики использования).

---

