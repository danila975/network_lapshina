# запуск tshark


C:\Program Files\Wireshark>tshark tshark
Capturing on 'Подключение по локальной сети* 9'
tshark: Invalid capture filter "tshark" for interface 'Подключение по локальной сети* 9'.

That string isn't a valid capture filter (can't parse filter expression: syntax error).
See the User's Guide for a description of the capture filter syntax.
0 packets captured


C:\Program Files\Wireshark>ipconfig

Настройка протокола IP для Windows


Адаптер беспроводной локальной сети Подключение по локальной сети* 1:

   Состояние среды. . . . . . . . : Среда передачи недоступна.
   DNS-суффикс подключения . . . . . :

Адаптер беспроводной локальной сети Подключение по локальной сети* 10:

   Состояние среды. . . . . . . . : Среда передачи недоступна.
   DNS-суффикс подключения . . . . . :

Адаптер беспроводной локальной сети Беспроводная сеть:

   DNS-суффикс подключения . . . . . : lan
   IPv6-адрес. . . . . . . . . . . . : 2a02:2168:8050:5000::d45
   IPv6-адрес. . . . . . . . . . . . : 2a02:2168:8050:5000:a4c4:d924:d08a:31f4
   IPv6-адрес. . . . . . . . . . . . : fd3b:2ec7:92f1::d45
   IPv6-адрес. . . . . . . . . . . . : fd3b:2ec7:92f1:0:e7d2:97ed:c3c1:a8bf
   Временный IPv6-адрес. . . . . . . : 2a02:2168:8050:5000:a0e9:197b:4b14:5e6c
   Временный IPv6-адрес. . . . . . . : fd3b:2ec7:92f1:0:a0e9:197b:4b14:5e6c
   Локальный IPv6-адрес канала . . . : fe80::3fee:8ab9:1ff9:b1a6%3
   IPv4-адрес. . . . . . . . . . . . : 192.168.1.157
   Маска подсети . . . . . . . . . . : 255.255.255.0
   Основной шлюз. . . . . . . . . : fe80::faf0:82ff:fefc:df0%3
                                       192.168.1.1

C:\Program Files\Wireshark>tshark -D
1. \Device\NPF_{283D56B8-A712-4C0F-AD5B-B93959F0C1A9} (Подключение по локальной сети* 9)
2. \Device\NPF_{FF55D602-F435-4893-932A-6814C1D12B13} (Подключение по локальной сети* 8)
3. \Device\NPF_{DD82B4B6-E499-49A8-A36A-B594FBC7E4B1} (Подключение по локальной сети* 7)
4. \Device\NPF_{2227CC4B-85E9-45BA-B858-377F9A64FDC5} (Беспроводная сеть)
5. \Device\NPF_{955DF176-091C-426E-A949-E8DB5A15B94E} (Подключение по локальной сети* 10)
6. \Device\NPF_{632A2C0B-8DAC-4970-91DF-8901B0C8469B} (Подключение по локальной сети* 1)
7. \Device\NPF_Loopback (Adapter for loopback traffic capture)
8. \\.\USBPcap1 (USBPcap1)
9. ciscodump (Cisco remote capture)
10. etwdump (Event Tracing for Windows (ETW) reader)
11. randpkt (Random packet generator)
12. sshdump.exe (SSH remote capture)
13. udpdump (UDP Listener remote capture)
14. wifidump.exe (Wi-Fi remote capture)


# резултаты прослушивания протокола arp
C:\Program Files\Wireshark>tshark -i 4 arp
Capturing on 'Беспроводная сеть'
    1   0.000000 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
    2   2.969669 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
    3   6.041596 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
    4   9.011550 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
    5  11.673375 SamsungElect_c1:5c:ce → Broadcast    ARP 42 Who has 192.168.1.157? Tell 192.168.1.185
    6  11.673396 Intel_ab:ca:8e → SamsungElect_c1:5c:ce ARP 42 192.168.1.157 is at d0:ab:d5:ab:ca:8e
    7  11.981077 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
    8  15.052645 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
    9  20.992173 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   10  24.069989 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   11  27.033785 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   12  30.004706 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   13  32.114013 Nagtech_fc:0d:f0 → Intel_ab:ca:8e ARP 42 Who has 192.168.1.157? Tell 192.168.1.1
   14  32.114023 Intel_ab:ca:8e → Nagtech_fc:0d:f0 ARP 42 192.168.1.157 is at d0:ab:d5:ab:ca:8e
   15  32.972894 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   16  36.044652 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   17  39.014225 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   18  41.984192 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   19  45.055867 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   20  48.025869 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   21  50.995104 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   22  54.067921 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   23  57.036635 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   24  60.006080 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   25  63.078143 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   26  66.047759 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   27  67.688307 SamsungElect_c1:5c:ce → Intel_ab:ca:8e ARP 42 Who has 192.168.1.157? Tell 192.168.1.185
   28  67.688321 Intel_ab:ca:8e → SamsungElect_c1:5c:ce ARP 42 192.168.1.157 is at d0:ab:d5:ab:ca:8e
   29  69.017511 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   30  72.089663 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   31  72.973812 Nagtech_fc:0d:f0 → Intel_ab:ca:8e ARP 42 Who has 192.168.1.157? Tell 192.168.1.1
   32  72.973827 Intel_ab:ca:8e → Nagtech_fc:0d:f0 ARP 42 192.168.1.157 is at d0:ab:d5:ab:ca:8e
   33  75.059352 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   34  78.028518 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   35  81.100540 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185
   36  84.070205 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185


# разбор одного пакета arp

пакет:    36  84.070205 SamsungElect_c1:5c:ce → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.185

В данном пакете протокола ARP (Address Resolution Protocol) можно выделить следующие атрибуты:

1. Отправитель: SamsungElect_c1:5c:ce
2. Получатель: Broadcast
3. Тип ARP-запроса: Who has 192.168.1.1?
4. IP-адрес отправителя: 192.168.1.185

ARP используется для сопоставления IP-адресов с физическими MAC-адресами в локальной сети. В данном случае устройство с IP-адресом 192.168.1.185 запрашивает MAC-адрес устройства с IP-адресом 192.168.1.1.
