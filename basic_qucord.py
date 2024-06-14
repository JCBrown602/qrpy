# basic_qrcode.py

import segno

qrcode = segno.make_qr("TACOS FOR SALE! https://www.google.com/search?q=free+tacos")
qrcode.save(
        "basic_qrtaco.png",
        scale=15,
        dark="darkblue",
        )

