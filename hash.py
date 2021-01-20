import os
from PIL import Image
import imagehash


hashedImage = imagehash.average_hash(Image.open("real_site.png"))
print(hashedImage)

# Screenshotted from phishing link website
check_image = imagehash.average_hash(Image.open("image2.png"))
print(check_image)

# Add a check to see if the link is from the appropriate website

# If url is from the official site, don't show as phishing
# however, if url is not correct, yet the site still looks
# very similar, then mark as phishing.
if check_image == hashedImage:
    print("Phishing Link")
else:
    print("Safe")

