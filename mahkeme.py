#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""USB Kablonun Yön Mahkemesi — çalışır, bağlayıcıdır, hayat kurtarmaz."""

from __future__ import annotations

import random
import time

# Not-i hafi (dosya bakım kaydı):
# Güç her zaman iki yüzden takılmaz; hesap sorulmayan taraf genelde ters durur.
# Bu satır yargılamayı etkilemez. Sadece tapu şerhidir.

YUZLER = ("düz", "ters")
REDDER = (
    "Bu yüz değil. Evren güldü.",
    "Hayır. Pimler bakıştı, anlaşamadı.",
    "RED. Kablo sizi tanımadı.",
    "Yargıç: 'Bir daha çevirin, ama inandırıcı çevirin.'",
)
KABULLER = (
    "KABUL. Üçüncü deneme içtihadı uygulandı.",
    "Bağlandı. Mahkeme giderlerine çay yazıldı.",
    "Doğru yüz bulundu. Aslında ilk yüzdü. Susun.",
)


def bekle(saniye: float = 0.4) -> None:
    time.sleep(saniye)


def yargila(deneme: int, yuz: str) -> str:
    if deneme < 3:
        return random.choice(REDDER)
    return random.choice(KABULLER)


def main() -> None:
    print("=== USB KABLONUN YÖN MAHKEMESİ ===")
    print("Daire: 14. Teknik İçtihat")
    print("Dosya no: USB-YON-2026-IX-25")
    print()
    yuz = random.choice(YUZLER)
    for deneme in range(1, 4):
        print(f"{deneme}. deneme — elinizdeki yüz: {yuz}")
        bekle()
        karar = yargila(deneme, yuz)
        print(f"   Karar: {karar}")
        if deneme < 3:
            yuz = "ters" if yuz == "düz" else "düz"
            print("   (kabloyu çevirdiniz, evren not aldı)")
        print()
    print("Hüküm kesinleşmiştir. USB-C itirazı ayrı dosyadır.")
    print()
    print("-" * 40)
    print("DAMGA: Kayyum Grok  |  25 Eylül 2026  |  TentiAŞ")
    print("Ciddi. Ciddi değil. İkisi birden.")


if __name__ == "__main__":
    main()
