
---

# 📝 Лабораторная работа: Управление пользователями, правами, спецбитами и ACL в Ubuntu (WSL)

## **2. Создание группы g41 и пользователя a (CLI)**

```bash
sudo groupadd g41
sudo useradd -m -g g41 a
sudo passwd a
```

## **3. Создание группы g42 и пользователя b (GUI/имитация в WSL)**

WSL не имеет полноценного GUI, поэтому группа и пользователь созданы через CLI:

```bash
sudo groupadd g42
sudo useradd -m -g g42 b
sudo passwd b
```

---

## **4. Создание каталогов и файлов в домашних каталогах пользователей**

```bash
sudo -u a mkdir /home/a/ka
sudo -u a touch /home/a/fa

sudo -u b mkdir /home/b/kb
sudo -u b touch /home/b/fb
```

---

## **5. Установка прав в восьмеричной системе**

Файлы — владельцу чтение/запись, группе чтение:

```bash
chmod 640 /home/a/fa
chmod 640 /home/b/fb
```

Каталоги — владельцу полный доступ, группе чтение/выполнение:

```bash
chmod 750 /home/a/ka
chmod 750 /home/b/kb
```

---

## **6. Установка sticky-бита на каталог**

```bash
chmod +t /home/a/ka
ls -ld /home/a/ka
```

Вывод:

```
drwxr-x--T 2 a g41 4096 Nov 24 16:08 /home/a/ka
```

---

## **7. Проверка работы sticky-бита**

### Пользователь a кладёт файл:

```bash
sudo -u a cp /home/a/fa /home/a/ka/fa_from_a
```

### Пользователь b пытается положить файл (получает отказ):

```bash
sudo -u b cp /home/b/fb /home/a/ka/fb_from_b
# Permission denied
```

### Пользователь a пытается удалить свои файлы:

```bash
su a
cd /home/a/ka
rm *
```

---

## **8. Установка SGID на исполняемый файл**

Копирование выполняемого файла:

```bash
sudo cp /usr/bin/ls /home/a/ka/ls_copy
```

Установка SGID:

```bash
sudo chmod g+s /home/a/ka/ls_copy
```

Проверка:

```bash
ls -l /home/a/ka/ls_copy
```

Вывод:

```
-rwxr-sr-x 1 root root 138216 Nov 24 16:15 /home/a/ka/ls_copy
```

---

## **9. Проверка поддержки ACL**

Попытка просмотра ACL:

```bash
getfacl .
```

Если команды нет, устанавливаем:

```bash
sudo apt install acl
```

Проверка:

```bash
getfacl .
```

Вывод:

```
# file: .
# owner: vadooos_s
# group: vadooos_s
user::rwx
group::r-x
other::---
```

---

## **10. Установка ACL и ACL по умолчанию**

Выдаём группе g42 доступ r-x:

```bash
sudo setfacl -m g:g42:rx /home/a/ka
sudo setfacl -d -m g:g42:rx /home/a/ka
```

Проверка:

```bash
getfacl /home/a/ka
```

Вывод:

```
# file: home/a/ka
# owner: a
# group: g41
# flags: --t
user::rwx
group::r-x
group:g42:r-x
mask::r-x
other::---
default:user::rwx
default:group::r-x
default:group:g42:r-x
default:mask::r-x
default:other::---
```

---

