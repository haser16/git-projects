import qrcode


def get_qr(url):
    qr1 = qrcode.make(url)
    qr1.save('qr_code.jpg')


if __name__ == "__main__":
    get_qr('https://haser16.pythonanywhere.com/game/rools/')
