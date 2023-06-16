import time
import psutil
import colorama


last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total= last_received + last_sent


def display_usage(cpu_usage, mem_usage, bars=50, color= colorama.Fore.YELLOW):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '▉' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))

    mem_percent = (mem_usage / 100.0)
    mem_bar = '▉' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    print(color + f"CPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  ", end="")
    print(colorama.Fore.RESET)
    print(colorama.Fore.GREEN + f"MEMORY Usage: |{mem_bar}| {mem_usage:.2f}%", end="")
    print(colorama.Fore.RESET)


while True:
    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_received + bytes_sent

    new_received = bytes_received - last_received
    new_sent = bytes_sent - last_sent
    new_total = bytes_total - last_total

    mb_new_received = new_received / 1024 / 1024
    mb_new_sent = new_sent / 1024 / 1024
    mb_new_total = new_total / 1024 / 1024

    print(colorama.Fore.RED + f"{mb_new_received:.2f} MB_Received, {mb_new_sent:.2f} MB_Sent, {mb_new_total:.2f} MB_Total")
    print(colorama.Fore.RESET)

    last_received = bytes_received
    last_sent = bytes_sent
    last_total = bytes_total


    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 25)
    time.sleep(0.5)



