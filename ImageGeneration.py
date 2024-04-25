from requests import post #pip install requests
from PIL import Image #pip install pillow
from io import BytesIO #pip install io

#Model Link: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0

b=post("https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1",
       headers={
    "Authorization":"Bearer YOUR_HUGGINGFACE_ACCESS_TOKEN",
},json={
    "inputs":"A sunlit indoor lounge area with a pool containing a flamingo"
})

i=Image.open(BytesIO(b.content))
i.save("1.png")

#Image-1
#A sunlit indoor lounge area with a pool containing a flamingo
#Image-2
#An underwater steampunk laboratory where mermaids study ancient artifacts.
