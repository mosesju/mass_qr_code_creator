import qrcode

# list of objects
code_list = [
    {
        'link':'',
        'name':''
    }
   
]
for item in code_list: 
    qr = qrcode.QRCode(
        version=1,  
        error_correction = qrcode.constants.ERROR_CORRECT_L,  
        box_size = 10,  
        border = 4,  
    )
    qr.add_data(item['link'])
    qr.make(fit=True)
    file_name = item['name']+'.png'
    print(file_name)
    qr_img = qr.make_image(fill_color='black', back_color='white')
    print(qr_img)
    qr_img.save(file_name)