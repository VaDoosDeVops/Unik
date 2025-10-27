### Номер 4 ###
powershell -NoProfile -Command "Get-ChildItem 'C:\Windows' -File -Recurse -Filter *.bmp -ErrorAction SilentlyContinue | Where-Object Length -gt 50000 | Sort-Object Length | Select-Object Name,Length,CreationTime,Attributes | Format-Table -AutoSize | Out-Host"

Name      Length CreationTime        Attributes
----      ------ ------------        ----------
guest.bmp 401464 01.04.2024 10:22:32    Archive
user.bmp  401464 01.04.2024 10:22:42    Archive
guest.bmp 401464 01.04.2024 10:22:32    Archive
user.bmp  401464 01.04.2024 10:22:42    Archive


### Номер 5 ###
C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "$p=Get-Process | Select-Object -First 1; $props=($p|Get-Member -MemberType Property).Name | Sort-Object; $props | Set-Content -Encoding UTF8 '.\task5_getprocess_properties.txt'; Write-Host ('Количество свойств объекта Get-Process: ' + $props.Count)"
Количество свойств объекта Get-Process: 52


### Номер 6 ###
C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "Get-Process | Where-Object { $_.BasePriority -gt 7 } | Sort-Object ProcessName | Select-Object @{n='ProcessName';e={$_.ProcessName}}, @{n='BasePriority';e={$_.BasePriority}}, @{n='Company';e={ try { $_.MainModule.FileVersionInfo.CompanyName } catch { '' } }} | Format-Table -AutoSize | Tee-Object -FilePath '.\task6_processes_sorted_by_name_basepriority_gt7.txt'"

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


~~~


xray                                   8
Яндекс Музыка                          8 Яндекс Музыка
Яндекс Музыка                         10 Яндекс Музыка
Яндекс Музыка                          8 Яндекс Музыка
Яндекс Музыка                          8 Яндекс Музыка

### Номер 7 ###
C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "$head='<style>body{font-family:Segoe UI,Arial,sans-serif}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ddd;padding:6px;text-align:left}th{background:#f3f3f3}</style>'; $d=Get-Process | Sort-Object ProcessName | Select-Object @{n='ProcessName';e={$_.ProcessName}}, @{n='BasePriority';e={$_.BasePriority}}, @{n='Company';e={ try { $_.MainModule.FileVersionInfo.CompanyName } catch { '' } }}; $d | ConvertTo-Html -Head $head -Title 'Задание 7: Процессы (сортировка по ProcessName)' -PreContent '<h2>Задание 7: Процессы (сортировка по ProcessName)</h2>' | Set-Content -Encoding UTF8 '.\task7_processes_sorted_by_name.html'; Write-Host 'HTML сохранён: .\task7_processes_sorted_by_name.html'"
HTML сохранён: .\task7_processes_sorted_by_name.html

### Номер 8 ###

C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "$f1=Get-ChildItem 'C:\Windows' -Recurse -File -Filter *.bmp -ErrorAction SilentlyContinue; $f2=Get-ChildItem 'C:\Windows' -Recurse -File -Filter *.jpg -ErrorAction SilentlyContinue; $bytes=($f1+$f2 | Measure-Object Length -Sum).Sum; $mb=[Math]::Round($bytes/1MB,3); Write-Host ('Суммарный объём BMP+JPG: ' + $bytes + ' байт (~ ' + $mb + ' МБ)')"
Суммарный объём BMP+JPG: 102873673 байт (~ 98.108 МБ)

### Номер 9 ###

C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "Get-CimInstance Win32_Processor | Select-Object Name,Manufacturer,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed,L2CacheSize,L3CacheSize,ProcessorId,Architecture,AddressWidth | Format-List"


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

### Номер 10 ###


C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "$n=10; $dir=@(); for($i=1;$i -le $n;$i++){ $t=Measure-Command { Get-ChildItem | Out-Null }; $dir+=[Math]::Round($t.TotalMilliseconds,3) } ; $ps=@(); for($i=1;$i -le $n;$i++){ $t=Measure-Command { Get-Process | Out-Null }; $ps+=[Math]::Round($t.TotalMilliseconds,3) } ; function S($a){$min=($a|Measure-Object -Minimum).Minimum; $max=($a|Measure-Object -Maximum).Maximum; $avg=[Math]::Round(($a|Measure-Object -Average).Average,3); 'Min: '+$min+' | Max: '+$max+' | Avg: '+$avg} ; Write-Host ('dir -> ' + (S $dir)) ; Write-Host ('ps  -> ' + (S $ps))"
dir -> Min: 0.905 | Max: 74.83 | Avg: 8.445
ps  -> Min: 13.765 | Max: 46.781 | Avg: 18.753

### Номер 11 ###

Самый большой файл:

C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "Get-ChildItem 'C:\Users\VadoooS_S\Desktop' -File | Sort-Object Length -Descending | Select-Object -First 1 | Format-Table FullName,Length,CreationTime -AutoSize"

FullName                                  Length CreationTime
--------                                  ------ ------------
C:\Users\VadoooS_S\Desktop\Wordpess.zip 31008002 12.06.2025 18:12:04

Три самых маленьких файла:

C:\Users\VadoooS_S\Documents\уник1курс\laba3occt>powershell -NoProfile -Command "Get-ChildItem 'C:\Users\VadoooS_S\Desktop' -File | Sort-Object Length | Select-Object


    Каталог: C:\Users\VadoooS_S\Desktop


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        24.10.2025     20:17            219 Dota 2.url
-a----        29.12.2024     15:34            219 Counter-Strike 2.url
-a----        04.09.2025     22:35            222 Dead Cells.url
-a----        31.08.2025     23:25            222 Terraria.url
-a----        23.10.2024     16:54            416 test_topic.sh
-a----        14.06.2024     14:55           1044 Telegram.lnk
-a----        14.06.2024     16:23           1125 DBeaver.lnk
-a----        14.06.2024     16:06           1332 WinSCP.lnk
-a----        14.06.2024     15:55           1416 Visual Studio Code.lnk
-a----        14.08.2024     21:26           1430 для екита.txt
-a----        25.09.2024     18:40           1468 MobaXterm_Personal_24.0 — ярлык.lnk
-a----        16.09.2024     11:31           1532 v2rayN — ярлык (2).lnk
-a----        03.02.2025     11:12           1899 uTorrent Web.lnk
-a----        14.06.2024     15:58           2140 Docker Desktop.lnk
-a----        25.10.2025     10:50           2209 Postman.lnk
-a----        09.08.2024     15:39           2257 Tabby Terminal.lnk
-a----        24.11.2024     20:06           2367 MongoDBCompass.lnk
-a----        24.04.2025     16:06           2428 balenaEtcher.lnk
-a----        14.06.2024     16:05           2493 Яндекс Музыка.lnk
-a----        27.10.2025      0:01           2553 Yandex.lnk
-a----        22.10.2024     19:05           5136 old pg bot.py
-a----        25.06.2025     16:59           6258 полезное.txt
-a----        26.06.2024     18:45         164207 photo_2024-06-25_16-12-54.jpg
-a----        20.06.2024     12:05         167191 photo_2024-02-22_19-41-09.jpg
-a----        25.06.2024     17:07         181055 photo_2024-06-25_17-07-16.jpg
-a----        25.06.2024     17:07         209027 photo_2024-06-25_17-07-06.jpg
-a----        26.10.2025     14:05         336904 1812896.jpg
-a----        30.05.2025     19:13        1240587 forest_trees_fog_110131_3840x2400.jpg
-a----        20.03.2024     12:50        1437204 img1.akspic.ru-macbook-macbook_pro-apple-macos_catalina-yabloko-4000x
                                                  4000.jpg
-a----        05.01.2025      0:53        2246259 coastline-horizon-cold-seascape-rocks-macos-big-sur-stock-5k-3840x216
                                                  0-3989.jpg
-a----        28.04.2024     19:54        2390152 macos-big-sur-stock-daytime-lone-tree-sedimentary-rocks-3840x2160-378
                                                  3.jpg
-a----        05.01.2025      0:51        2455144 macos-big-sur-stock-sedimentary-rocks-evening-starry-sky-3840x2160-37
                                                  81.jpg
-a----        05.01.2025      0:54        2923908 macos-big-sur-stock-daytime-sedimentary-rocks-daylight-3840x2160-3778
                                                  .jpg
-a----        12.06.2025     18:13       31008002 Wordpess.zip

