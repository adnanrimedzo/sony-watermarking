import qrcode, numpy, utils, zbar


def generate(data, height, width):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qrimg = qr.make_image()
    qrimg = numpy.array(qrimg, numpy.float32)
    qrimg = utils.fixShape(qrimg, [height, width, 1])
    return qrimg


def readQRMessage(img):
    scanner = zbar.Scanner()
    result = scanner.scan(img)
    return result[0].data

