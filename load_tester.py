from urllib.request import urlopen
from urllib.error import URLError
import time

url = input("Enter URL: ")
requests = int(input("Enter number of requests: "))

success = 0
failed = 0

print("\nSending requests...\n")

for _ in range(requests):
    try:
        response = urlopen(url)
        if response.getcode() == 200:
            success += 1
        else:
            failed += 1
    except URLError:
        failed += 1

    time.sleep(0.5)

print("\nResults:")
print("Success:", success)
print("Failed:", failed)
