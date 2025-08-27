import qrcode

url = input("enter your gitup url : ").strip()
file_name = input("enter your file name : ").strip()
qr = qrcode.QRCode(box_size=20, border=6)
qr.add_data(url)
img = qr.make_image(fill_color='black', back_color='white')
img.save(f'{file_name}.png')
print(img)
