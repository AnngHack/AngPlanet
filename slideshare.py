import os
from PIL import Image
import requests
from pypdf import PdfMerger
i = 1
end = 51 #CHANGE THIS TO THE MAXIMUM NUMBER OS SLIDE
while i <= end:
    url = f"https://image.slidesharecdn.com/datasciencecorner-221130165458-60b0d249/75/introduction-to-data-science-{i}-2048.jpg"
    #..../75/...{i}-2048.jpg
    response = requests.get(url)
    open(f"{i}.jpg", "wb").write(response.content)
    output_dir = '../slideshare'
    source_dir = '../slideshare'
    for file in os.listdir(source_dir):
        if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
            image = Image.open(os.path.join(source_dir, file))
            image_converted = image.convert('RGB')
            image_converted.save(os.path.join(output_dir, '{0}.pdf'.format(file.split('.')[-2])))
    os.remove(f"{i}.jpg")
    print(f"{i} slide downloaded...")
    i += 1
j = 1
pdf_list = []
while j <= end:
    pdf_list.append(f"{j}.pdf")
    j += 1
merger = PdfMerger()
for pdf in pdf_list:
    merger.append(pdf)
merger.write("result.pdf")
merger.close()
k = 1
pdf_list = []
while k <= end:
    os.remove(f"{k}.pdf")
    k += 1
print("Successful")
