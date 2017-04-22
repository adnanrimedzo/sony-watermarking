import qrcode, numpy, cv2


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
    qrimg = cv2.cvtColor(qrimg, cv2.COLOR_GRAY2BGR)
    qrimg = cv2.resize(qrimg, (height, width), interpolation=cv2.INTER_NEAREST) #todo: do interpoletion by downsampling or upsampling
    return qrimg