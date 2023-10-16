import os
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Path to the folder containing images
images_folder = r'/home/thaiv7/Desktop/NguyenThaiVu.github.io/Images/Advanced_visualization/2016'

# Get a list of image filenames in the folder
image_files = [f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]

# Initial image
initial_image_path = os.path.join(images_folder, image_files[0])

# Create the figure with an initial image
fig = go.Figure(go.Image(source=initial_image_path))

# Define the dropdown menu
dropdown_menu = [
    {'label': image, 'method': 'relayout', 'args': ['imagesrc', os.path.join(images_folder, image)]}
    for image in image_files
]

# Add the dropdown menu to the layout
fig.update_layout(
    updatemenus=[
        {'active': 0, 'buttons': dropdown_menu, 'direction': 'down', 'showactive': True}
    ]
)

# Save the figure to an HTML file
html_output_file = 'output.html'
fig.write_html(html_output_file)
