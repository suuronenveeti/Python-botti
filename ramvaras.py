import sys

def kaynnista_vuoto():
    print("\nNyt sinun RAM on minun. Ei keskeytyksiä.")
    
    muistisyoppo = []
    blokin_koko_tavuina = 256 * 1024 * 1024  
    blokki = bytearray(blokin_koko_tavuina)
    
    blokit = 0
    
    while True:
        try:
            muistisyoppo.append(bytes(blokki))
            blokit += 1
            
            otettu_gb = (blokit * blokin_koko_tavuina) / (1024 ** 3)
            print(f"RAM otettu {otettu_gb:.2f} GB.")
            
        except (KeyboardInterrupt, BaseException):
            continue

if __name__ == "__main__":
    kaynnista_vuoto()
