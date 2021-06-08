import psutil
import platform
from datetime import datetime
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_system_info():
    #SYS INFO
    uname = platform.uname()
    print("="*40, "System Information", "="*40)
    print(f"Machine Code: {uname.node}")
    print(f"System: {uname.system} {uname.version}")
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

    # let's print CPU information
    print("="*40, "CPU Info", "="*40)
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    cpufreq = psutil.cpu_freq()
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

    print("="*40, "Memory Information", "="*40)
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")

    # Disk info
    print("="*40, "Disk Information", "="*40)
    print("Partitions and Usage:")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    now = datetime.now()
    year = int(now.year)
    month = int(now.month)
    day = int(now.day)
    speak(f'Hoy es {day}/{month}/{year}')

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Escuchando')
        r.pause_threshold = 1
        audio = r.listen(source)

    try: 
        print('Reconociendo...')
        query = r.recognize_google(audio, language = 'es')
        print(query)
    except Exception as e:
        print(e)
        return 'None'
    
    return query