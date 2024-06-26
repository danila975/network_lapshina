# подключаем библиотеку subprocess
import subprocess

# проверяем подключение к shel
def run_command(command):
    subprocess.run(command, shell=True, check=True)

# функция реализующая dmz
def setup_dmz():    
# убираем все существующие правила
    run_command("iptables -F")
    run_command("iptables -X")
    run_command("iptables -t nat -F")
    run_command("iptables -t nat -X")
    run_command("iptables -t mangle -F")
    run_command("iptables -t mangle -X")
    run_command("iptables -t raw -F")
    run_command("iptables -t raw -X")
# Устанавливаем политику по умолчанию для всех цепочек
    run_command("iptables -P INPUT DROP")
    run_command("iptables -P FORWARD DROP")
    run_command("iptables -P OUTPUT ACCEPT")
# Разрешаем loopback (внутренней) трафик
    run_command("iptables -A INPUT -i lo -j ACCEPT")
    run_command("iptables -A OUTPUT -o lo -j ACCEPT")
# Разрешаем уже установленные соединения
    run_command("iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")
    run_command("iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")
# Разрешаем трафик из внутренней сети в DMZ и обратно
    run_command("iptables -A FORWARD -i eth1 -o eth2 -j ACCEPT")
    run_command("iptables -A FORWARD -i eth2 -o eth1 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")
# в качестве примера открываем dmz для порта 443, так как его использует https протокол
    run_command("iptables -A FORWARD -i eth0 -o eth2 -p tcp --dport 443 -j ACCEPT")
    run_command("iptables -A FORWARD -i eth2 -o eth0 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")
# Запретить доступ из DMZ во внутреннюю сеть
    run_command("iptables -A FORWARD -i eth2 -o eth1 -j REJECT")
# Настраиваем NAT для внутренней сети и DMZ
    run_command("iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE")
    run_command("iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT")
    run_command("iptables -A FORWARD -i eth0 -o eth1 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")
    run_command("iptables -A FORWARD -i eth2 -o eth0 -j ACCEPT")
    run_command("iptables -A FORWARD -i eth0 -o eth2 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")

if name == "main":
    setup_dmz()
