"""import threading
import time

def rakamlari_yazdir():
    for i in range(1, 6):
        time.sleep(1)  
        print(i)

def harfleri_yazdir():
    for harf in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(1.5)  
        print(harf)

t1 = threading.Thread(target=rakamlari_yazdir)
t2 = threading.Thread(target=harfleri_yazdir)

t1.start()  
t2.start()  

t1.join()  
t2.join()

#daemon threading

import threading
import time

def arkaplan_gorevi():
    while True:
     print("Arka plan görevi çalışıyor...")    
     time.sleep(2)


daemon_thread = threading.Thread(target=arkaplan_gorevi)
daemon_thread.daemon = True  
daemon_thread.start()

time.sleep(5)  
print("Ana program tamamlandı")"""


#THREAD SENKRONİZASYONU#

#LOCK

"""

import threading
import time

# Global değişken
counter = 0
lock = threading.Lock()  # Lock oluşturuluyor

def increment():
    global counter
    for _ in range(100000):
        with lock:  # Lock al ve işlem yap
            counter += 1

# Thread'leri oluşturma
threads = []
for _ in range(5):
    t = threading.Thread(target=increment)
    t.start()
    threads.append(t)

for t in threads:
    t.join()  # Thread'lerin bitmesini bekle

print(f"Counter: {counter}")


"""
#RLOCK
"""
import threading

rlock = threading.RLock()

def task():
    with rlock:
        print("Task started")
        with rlock:  # Aynı thread tekrar rlock alabilir
            print("Task in progress")
        print("Task completed")

# Thread oluşturma
thread = threading.Thread(target=task)
thread.start()
thread.join()


"""
# SEMAPHORE
"""import threading
import time

semaphore = threading.Semaphore(3)  # 3 thread'e kadar kaynak erişimi

def task():
    with semaphore:
        print(f"Thread {threading.current_thread().name} is using the resource")
        time.sleep(2)
        print(f"Thread {threading.current_thread().name} is releasing the resource")

# Thread'leri oluşturma
threads = []
for i in range(5):
    t = threading.Thread(target=task)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
"""

#CONDITION

"""import threading

condition = threading.Condition()

def waiter():
    with condition:
        print("Waiting for the signal...")
        condition.wait()  # Koşulu bekler
        print("Received signal!")

def signaler():
    time.sleep(2)
    with condition:
        print("Sending signal...")
        condition.notify()  # Koşulu sağla

# Thread'leri oluşturma
t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=signaler)
t1.start()
t2.start()

t1.join()
t2.join()
"""

#EVENT

"""import threading
import time

event = threading.Event()

def wait_for_event():
    print("Waiting for event to be set...")
    event.wait()  # Olayın tetiklenmesini bekler
    print("Event has been set!")

def trigger_event():
    time.sleep(3)
    print("Setting event...")
    event.set()  # Olayı tetikler

# Thread'leri oluşturma
t1 = threading.Thread(target=wait_for_event)
t2 = threading.Thread(target=trigger_event)
t1.start()
t2.start()

t1.join()
t2.join()
"""

#THREADING POOL     

from concurrent.futures import ThreadPoolExecutor
import time

def dosya_indir(dosya_adi):
    print(f"{dosya_adi} indiriliyor...")
    time.sleep(2)
    print(f"{dosya_adi} indirildi.")

dosyalar= ["dosya1.jpg", "dosya2.jpg", "dosya3.jpg", "dosya4.jpg", "dosya5.jpg"]

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(dosya_indir, dosyalar)

print("Bütün dosyalar indirildi.")