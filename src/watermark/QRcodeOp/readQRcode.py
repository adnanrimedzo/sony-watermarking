import zbarlight


def readQRcode(image):
    codes = zbarlight.scan_codes('qrcode', image);
    return codes;
