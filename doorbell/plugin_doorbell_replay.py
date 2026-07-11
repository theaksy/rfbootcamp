#!/usr/bin/env python3
from rflib import RfCat, MOD_ASK_OOK

def main():
    # CC1111‑safe padded payload
    #hex_payload = "e4d26893468d113444da"
    hex_payload = "d4474474447474744474447740"
    data = bytes.fromhex(hex_payload)

    d = RfCat()

    d.setFreq(434_124_064)
    d.setMdmModulation(MOD_ASK_OOK)
    d.setMdmSyncMode(0)
    d.setMaxPower()

    # Disable Manchester
    d.poke(0x12, b"\x30")

    # Disable whitening + CRC
    d.poke(0x08, b"\x00")
    d.poke(0x07, b"\x04")

    # Match doorbell timing
    d.setMdmDRate(4200)

    print("Transmitting…")
    d.RFxmit(data)
    print("Done.")

if __name__ == "__main__":
    main()
