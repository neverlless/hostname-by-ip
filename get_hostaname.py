import subprocess

with open("ip.txt", "r") as f:
    for line in f:
        # получаем IP-адрес из первой колонки
        ip_address = line.strip().split()[0]
        try:
            output = subprocess.run(
                ["ssh", "-o", "ConnectTimeout=5", ip_address, "cat /etc/hostname"],
                check=True,
                capture_output=True,
                text=True,
                timeout=10  # тайм-аут ожидания ответа от процесса в секундах
            )  # получаем имя хоста по SSH
            # удаляем лишние пробелы и символы переноса строки
            hostname = output.stdout.strip()
            print(f"{ip_address}: {hostname}")
        except subprocess.TimeoutExpired:
            print(f"{ip_address}: Connection timed out")
        except subprocess.CalledProcessError:
            print(f"{ip_address}: Unable to connect via SSH")
