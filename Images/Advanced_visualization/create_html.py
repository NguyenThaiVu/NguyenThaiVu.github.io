import base64

# List of image file paths
image_paths = [r"2016/Anaheim Ducks.jpg",\
               r"2016/Arizona Coyotes.jpg",\
                r"2016/Boston Bruins.jpg"]

# Open and read each image, encode it to base64
image_data = [base64.b64encode(open(image_path, "rb").read()).decode("utf-8") for image_path in image_paths]

# Create the HTML file
with open("final_output.html", "w") as html_file:
    # Write the HTML header
    html_file.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>Embedded Images</title>\n</head>\n<body>\n')

    # Embed each image in the HTML
    for image in image_data:
        html_file.write(f'<img src="data:image/jpeg;base64,{image}" alt="Embedded Image">\n')

    # Write the HTML footer
    html_file.write('</body>\n</html>')
