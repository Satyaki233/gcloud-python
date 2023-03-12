publicImages = [
            {
                "NAME": "ubuntu-1804-bionic-v20230308",
                "PROJECT": "ubuntu-os-cloud",
                "FAMILY": "ubuntu-1804-lts",
            },
            {
                "NAME": "debian-11-bullseye-v20230306",
                "PROJECT": "debian-cloud",
                "FAMILY": "debian-11",
            }
        ]

for i in publicImages:
    print(i)

print(publicImages[0].get("NAME"))