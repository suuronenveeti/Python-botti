import sys
import time


def kaynnista_vuoto():
    print("\nNyt sinun ram on minun.")

    muistisyoppo = []
    blokit = 0

    while True:
        try:
            for _ in range(80):
                isodata = ["RAM_ON_MINUN_NYT"] * 200000
                muistisyoppo.append(isodata)
                blokit += 1

            otettu_gb = blokit * 0.0014901
            
            print(f"Ram otettu {otettu_gb:.2f}GB.")
            time.sleep(1)

        except (KeyboardInterrupt, BaseException):
            continue


if __name__ == "__main__":
    kaynnista_vuoto()
