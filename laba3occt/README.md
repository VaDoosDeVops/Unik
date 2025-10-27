# 📘 Лабораторная работа №3 (OCCT)

**Тема:** PowerShell — командлеты, фильтры, сортировка и вывод информации.

---

### № 4
```powershell
powershell -NoProfile -Command "Get-ChildItem 'C:\Windows' -File -Recurse -Filter *.bmp -ErrorAction SilentlyContinue | Where-Object Length -gt 50000 | Sort-Object Length | Select-Object Name,Length,CreationTime,Attributes | Format-Table -AutoSize | Out-Host"
```

```
Name      Length CreationTime        Attributes
----      ------ ------------        ----------
guest.bmp 401464 01.04.2024 10:22:32 Archive
user.bmp  401464 01.04.2024 10:22:42 Archive
guest.bmp 401464 01.04.2024 10:22:32 Archive
user.bmp  401464 01.04.2024 10:22:42 Archive
```

---

### № 5
```powershell
C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "$p=Get-Process | Select-Object -First 1; $props=($p|Get-Member -MemberType Property).Name | Sort-Object; $props | Set-Content -Encoding UTF8 '.\task5_getprocess_properties.txt'; Write-Host ('Количество свойств объекта Get-Process: ' + $props.Count)"
```

```
Количество свойств объекта Get-Process: 52
```

---

### № 6
```powershell
C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "Get-Process | Where-Object { $_.BasePriority -gt 7 } | Sort-Object ProcessName | Select-Object @{n='ProcessName';e={$_.ProcessName}}, @{n='BasePriority';e={$_.BasePriority}}, @{n='Company';e={ try { $_.MainModule.FileVersionInfo.CompanyName } catch { '' } }} | Format-Table -AutoSize | Tee-Object -FilePath '.\task6_processes_sorted_by_name_basepriority_gt7.txt'"
```

```
ProcessName                 BasePriority Company
-----------                 ------------ -------
AccountsControlHost                    8 Microsoft Corporation
AggregatorHost                         8
amdfendrsr                             8
AMDRSServ                              8
AMDRSSrcExt                            8 Advanced Micro Devices, Inc.
AnyDesk                                8 AnyDesk Software GmbH
AnyDesk                                8 AnyDesk Software GmbH
AnyDesk                               13 AnyDesk Software GmbH
ApplicationFrameHost                   8 Microsoft Corporation
AsusAppService                         8
AsusInputlocaleMonitor                 8 ASUSTek COMPUTER INC.
AsusNumPadService                      8
AsusOptimization                       8
AsusOptimizationStartupTask            8 ASUSTeK COMPUTER INC.
xray                                   8
Яндекс Музыка                          8 Яндекс Музыка
Яндекс Музыка                         10 Яндекс Музыка
Яндекс Музыка                          8 Яндекс Музыка
Яндекс Музыка                          8 Яндекс Музыка
```

---

### № 7
```powershell
C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "$head='<style>body{font-family:Segoe UI,Arial,sans-serif}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ddd;padding:6px;text-align:left}th{background:#f3f3f3}</style>'; $d=Get-Process | Sort-Object ProcessName | Select-Object @{n='ProcessName';e={$_.ProcessName}}, @{n='BasePriority';e={$_.BasePriority}}, @{n='Company';e={ try { $_.MainModule.FileVersionInfo.CompanyName } catch { '' } }}; $d | ConvertTo-Html -Head $head -Title 'Задание 7: Процессы (сортировка по ProcessName)' -PreContent '<h2>Задание 7: Процессы (сортировка по ProcessName)</h2>' | Set-Content -Encoding UTF8 '.\task7_processes_sorted_by_name.html'; Write-Host 'HTML сохранён: .\task7_processes_sorted_by_name.html'"
```

```
HTML сохранён: .\task7_processes_sorted_by_name.html
```

---

### № 8
```powershell
C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "$f1=Get-ChildItem 'C:\Windows' -Recurse -File -Filter *.bmp -ErrorAction SilentlyContinue; $f2=Get-ChildItem 'C:\Windows' -Recurse -File -Filter *.jpg -ErrorAction SilentlyContinue; $bytes=($f1+$f2 | Measure-Object Length -Sum).Sum; $mb=[Math]::Round($bytes/1MB,3); Write-Host ('Суммарный объём BMP+JPG: ' + $bytes + ' байт (~ ' + $mb + ' МБ)')"
```

```
Суммарный объём BMP+JPG: 102873673 байт (~ 98.108 МБ)
```

---

### № 9
```powershell
C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "Get-CimInstance Win32_Processor | Select-Object Name,Manufacturer,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed,L2CacheSize,L3CacheSize,ProcessorId,Architecture,AddressWidth | Format-List"
```

```
Name                      : AMD Ryzen 5 7530U with Radeon Graphics
Manufacturer              : AuthenticAMD
NumberOfCores             : 6
NumberOfLogicalProcessors : 12
MaxClockSpeed             : 2000
L2CacheSize               : 3072
L3CacheSize               : 16384
ProcessorId               : 178BFBFF00A50F00
Architecture              : 9
AddressWidth              : 64
```

---

### № 10
```powershell
C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "$n=10; $dir=@(); for($i=1;$i -le $n;$i++){ $t=Measure-Command { Get-ChildItem | Out-Null }; $dir+=[Math]::Round($t.TotalMilliseconds,3) } ; $ps=@(); for($i=1;$i -le $n;$i++){ $t=Measure-Command { Get-Process | Out-Null }; $ps+=[Math]::Round($t.TotalMilliseconds,3) } ; function S($a){$min=($a|Measure-Object -Minimum).Minimum; $max=($a|Measure-Object -Maximum).Maximum; $avg=[Math]::Round(($a|Measure-Object -Average).Average,3); 'Min: '+$min+' | Max: '+$max+' | Avg: '+$avg} ; Write-Host ('dir -> ' + (S $dir)) ; Write-Host ('ps  -> ' + (S $ps))"
```

```
dir -> Min: 0.905 | Max: 74.83 | Avg: 8.445
ps   -> Min: 13.765 | Max: 46.781 | Avg: 18.753
```

---

### № 11

**Самый большой файл**
```powershell
C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "Get-ChildItem 'C:\Users\VadoooS_S\Desktop' -File | Sort-Object Length -Descending | Select-Object -First 1 | Format-Table FullName,Length,CreationTime -AutoSize"
```

```
FullName                                  Length   CreationTime
--------                                  ------   ------------
C:\Users\VadoooS_S\Desktop\Wordpess.zip   31008002 12.06.2025 18:12:04
```

**Три самых маленьких файла**
```powershell
C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "Get-ChildItem 'C:\Users\VadoooS_S\Desktop' -File | Sort-Object Length | Select-Object"
```

```
Каталог: C:\Users\VadoooS_S\Desktop

Mode   LastWriteTime          Length Name
----   -------------          ------ ----
-a---- 24.10.2025 20:17          219 Dota 2.url
-a---- 29.12.2024 15:34          219 Counter-Strike 2.url
-a---- 04.09.2025 22:35          222 Dead Cells.url
...
-a---- 12.06.2025 18:13      31008002 Wordpess.zip
```


