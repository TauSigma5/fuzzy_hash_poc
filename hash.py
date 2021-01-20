from PIL import Image
import imagehash

def phishing_check(suspicious_url, suspicious_image):
    # A check to see if the link is from the appropriate website
    # If url is from the official site, don't show as phishing
    # however, if url is not correct, yet the site still looks
    # very similar, then mark as phishing.

    check_image = imagehash.average_hash(Image.open(suspicious_image))
    
    # Imagine a database of fuzzy hashes of login sites of commonly used sites
    # with their proper URLs attached to them.
    hashedImage = imagehash.average_hash(Image.open("real_site.png"))
    real_site_url = "account.protonmail.com"

    if suspicious_url != real_site_url:
        if check_image == hashedImage:
            print("Phishing Link")
        else:
            print("Safe")
    else:
        print("Safe")

# A malformed ProtonMail phishing website using a fake link
phishing_check("account.protonemail.com", "image3.png")

# A more subtle phishing site with fewer differences (an extra "c" in English)
phishing_check("account.protonemail.com", "image4.png")

# The same login page, different format, but from correct domain
phishing_check("account.protonmail.com", "image5.png")

# A completely different site
phishing_check("account.google.com", "image2.png")


