import os
import base64
from pathlib import Path

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        base64_data = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_data

def create_html_with_images(image_folder, path_output_html_file):
    images_folder = Path(image_folder)
    images = {image.stem: image_to_base64(image) for image in images_folder.glob("*.jpg")}

    dropdown_options = "\n".join([f'<option value="{image_name}">{image_name}</option>' for image_name in images])

    html_content = f"""
    <html>
    <head>
    </head>
    <body>
        <select id="image-dropdown">
            {dropdown_options}
        </select>
        <br>
        <img id="display-image" src="" alt="Selected Image">
        <script>
            var images = {images};  // This should be a dictionary of image names and Base64 data
            document.getElementById('image-dropdown').addEventListener('change', function() {{
                var selectedImage = this.value;
                var imageElement = document.getElementById('display-image');
                imageElement.src = 'data:image/jpeg;base64,' + images[selectedImage];
            }});
        </script>
    </body>
    </html>
    """

    with open(path_output_html_file, "w") as html_file:
        html_file.write(html_content)


def main():

    list_season = ["2016", "2017", "2018", "2019", "2020"]

    for season in list_season:
        path_output_html_file = os.path.join(f"shot_map_{season}.html")
        create_html_with_images(season, path_output_html_file)

main()
