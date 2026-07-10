#!/usr/bin/env python3
from rflib import RfCat, MOD_ASK_OOK

def main():
    hex_payload = "93a3ba744ee89dd1d249d2"
    hex_payload = "ad6d6adab6b556a0"
    data = bytes.fromhex(hex_payload)

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

    # Use the timing that matched your waveform
    d.setMdmDRate(1800)

    print("Transmitting…")
    d.RFxmit(data)
    d.RFxmit(data)
    print("Done.")

if __name__ == "__main__":
    main()
