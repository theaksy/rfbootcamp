#!/usr/bin/env python3
# https://www.youtube.com/watch?v=uIVBVd6yi_A
import time
from rflib import RfCat, MOD_ASK_OOK

CODES = [
    "aedaeb6adad55a80",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab6b55740",
    "ad6d6adab76aad40",
    "ad6d6adab6b556a0",
    "ad6d75b56d6aad40",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab76aad40",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab76aad40",
    "ad6d6adab6b556a0",
    "ad6d6adab6baad40",
    "ad6d6af56ed55a80",
    "aedad5b56d6aad40",
    "ad6d6adab6b556a0",
    "ad7ad5b56d6aad40",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab6b556a0",
    "ad6d6adab6b55680",
]

def main():
    d = RfCat()

    d.setFreq(433_923_000)
    d.setMdmModulation(MOD_ASK_OOK)
    d.setMdmSyncMode(0)
    d.setMaxPower()

    # Disable Manchester encoding
    d.poke(0x12, b"\x30")   # MDMCFG2: ASK/OOK, no Manchester

    # Keep packet engine stable (no whitening, no CRC)
    d.poke(0x08, b"\x00")   # PKTCTRL0
    d.poke(0x07, b"\x04")   # PKTCTRL1

    d.setMdmDRate(1900)

    for idx, hex_payload in enumerate(CODES, start=1):
        data = bytes.fromhex(hex_payload)
        print(f"Transmitting code {idx}/{len(CODES)}: {hex_payload}")
        d.RFxmit(data)
        time.sleep(0.01)  # ~300 ms pause between bursts

    print("Done.")

if __name__ == "__main__":
    main()
