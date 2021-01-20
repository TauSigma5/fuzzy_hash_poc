import os
from PIL import Image
import imagehash

# Imagine a database of fuzzy hashes of login sites of commonly used sites
# with their proper URLs attached to them.
hashedImage = imagehash.average_hash(Image.open("real_site.png"))
real_site_url = "account.protonmail.com"

# Screenshotted from phishing link website and its associated link
check_image = imagehash.average_hash(Image.open("image3.png"))
suspicious_url = "account.protonemail.com"

# Add a check to see if the link is from the appropriate website
# If url is from the official site, don't show as phishing
# however, if url is not correct, yet the site still looks
# very similar, then mark as phishing.
if suspicious_url != real_site_url:
    if check_image == hashedImage:
        print("Phishing Link")
    else:
        print("Safe")
else:
    print("Safe")
