## Скрипты на Shell (POSIX sh)

---

## 1. Получить полный список ключей команды `stat`

```sh
stat --help
```

---

## 2. Факториал числа с проверкой ввода

**factorial.sh**

```sh
#!/bin/sh

printf "Введите целое неотрицательное число: "
read n

echo "$n" | grep -Eq '^[0-9]+$'
if [ $? -ne 0 ]; then
    echo "Ошибка: нужно ввести целое неотрицательное число."
    exit 1
fi

fact=1
i=1

while [ "$i" -le "$n" ]; do
    fact=$((fact * i))
    i=$((i + 1))
done

echo "Факториал числа $n равен $fact"
```

---

## 3. Первые N чисел Фибоначчи (заданные A0, A1)

**fib.sh**

```sh
#!/bin/sh

printf "Введите первое число A0: "
read a0
printf "Введите второе число A1: "
read a1
printf "Введите количество чисел N: "
read n

echo "$n" | grep -Eq '^[0-9]+$'
if [ $? -ne 0 ] || [ "$n" -le 0 ]; then
    echo "Ошибка: N должно быть положительным целым."
    exit 1
fi

a_prev=$a0
a_curr=$a1

if [ "$n" -ge 1 ]; then
    echo "$a_prev"
fi
if [ "$n" -ge 2 ]; then
    echo "$a_curr"
fi

i=3
while [ "$i" -le "$n" ]; do
    a_next=$((a_curr + a_prev))
    echo "$a_next"
    a_prev=$a_curr
    a_curr=$a_next
    i=$((i + 1))
done
```

---

## 4. Индивидуальные задания (5–12)

---

## 5. Суммарный объём выполняемых файлов в текущем каталоге

```sh
#!/bin/sh

total=$(find . -maxdepth 1 -type f -perm -111 -printf '%s\n' |
        awk '{s+=$1} END{print s+0}')

echo "Суммарный размер исполняемых файлов: $total байт"
```

---

## 6. Найти выполняемый файл наибольшего размера

```sh
#!/bin/sh

file=$(find . -maxdepth 1 -type f -perm -111 -printf '%s %f\n' |
       sort -nr | head -n1)

if [ -z "$file" ]; then
    echo "Исполняемых файлов нет."
    exit 0
fi

size=$(echo "$file" | awk '{print $1}')
name=$(echo "$file" | awk '{print $2}')

echo "Самый большой исполняемый файл: $name ($size байт)"
```

---

## 7. Файлы на `a` или `b`, доступные для записи

```sh
#!/bin/sh
find . -maxdepth 1 -type f \( -name 'a*' -o -name 'b*' \) -writable -printf '%f\n'
```

---

## 8. Файл, изменённый позже всех

```sh
#!/bin/sh

res=$(find . -maxdepth 1 -type f -printf '%T@ %TY-%Tm-%Td %TT %f\n' |
      sort -nr | head -n1)

if [ -z "$res" ]; then
    echo "Нет файлов."
    exit 0
fi

date=$(echo "$res" | awk '{print $2, $3}')
name=$(echo "$res" | awk '{print $4}')

echo "Последним изменён файл: $name"
echo "Дата: $date"
```

---

## 9. Проверка одинаковых имён файлов в двух каталогах

```sh
#!/bin/sh

if [ $# -ne 2 ]; then
    echo "Использование: $0 dir1 dir2"
    exit 1
fi

ls "$1" 2>/dev/null | sort > /tmp/dir1.$$
ls "$2" 2>/dev/null | sort > /tmp/dir2.$$

common=$(comm -12 /tmp/dir1.$$ /tmp/dir2.$$)

if [ -z "$common" ]; then
    echo "Совпадающих имён нет."
else
    echo "Количество совпадающих файлов: $(echo "$common" | wc -l)"
    echo "$common"
fi

rm -f /tmp/dir1.$$ /tmp/dir2.$$
```

---

## 10. Для каждого подкаталога — количество файлов

```sh
#!/bin/sh

for d in */; do
    [ -d "$d" ] || continue
    count=$(find "$d" -maxdepth 1 -type f | wc -l)
    echo "$d — файлов: $count"
done
```

---

## 11. Файлы разных имён, но одинаковых размеров

```sh
#!/bin/sh

find . -maxdepth 1 -type f -printf '%s %f\n' | sort -n > /tmp/sizes.$$

awk '
{
    sz=$1; nm=$2
    names[sz] = names[sz] " " nm
    count[sz]++
}
END {
    for (s in count) {
        if (count[s] > 1) {
            print "Размер:", s, "байт"
            print "Файлы:" names[s]
            print ""
        }
    }
}
' /tmp/sizes.$$

rm -f /tmp/sizes.$$
```

---

## 12. Файлы, изменённые за последнюю неделю

```sh
#!/bin/sh
echo "Файлы, изменённые за последнюю неделю:"
find . -type f -mtime -7 -print
```

---

## 13. Перевод введённого числа в 8- и 16-ричные системы через `printf`

**convert_base.sh**

```sh
#!/bin/sh

printf "Введите положительное число: "
read n

echo "$n" | grep -Eq '^[0-9]+$'
if [ $? -ne 0 ] || [ "$n" -le 0 ]; then
    echo "Ошибка: нужно целое положительное число."
    exit 1
fi

printf "Десятичное:      %d\n" "$n"
printf "Восьмеричное:    %o\n" "$n"
printf "Шестнадцатеричное: %X\n" "$n"
```

---

