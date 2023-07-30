import requests
import os
from PIL import Image
from pypdf import PdfMerger

def get_first_line(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        lines = response.text.split('\n')
        first_line = lines[0]
        return first_line
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None


website_url = input('Enter the slideshare url: ')

first_line_variable = get_first_line(website_url)

link_list = []
if first_line_variable is not None:
    break_line = first_line_variable.split()
    for link in break_line:
        if link.startswith("https://image.slidesharecdn.com/"):
            jpg_link = link.split('?')[0]
            if '2048.jpg' in jpg_link:
                link_list.append(jpg_link)

else:
    print("Failed to fetch the website.")

final_list = []
for item in link_list:
    if item not in final_list:
        final_list.append(item)
end = len(final_list)

i = 1
while i <= end:
    for url in final_list:
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
merger.write("Output.pdf")
merger.close()
k = 1
pdf_list = []
while k <= end:
    os.remove(f"{k}.pdf")
    k += 1
print("Successful")
