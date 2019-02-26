# Basic program showing how to perform a GET request
# Packages to allow parsing and requesting
import urllib.request
import urllib.parse

# 1. Simple request
# x = urllib.request.urlopen('https://www.google.com')
# print(x.read())

# 2. Simple GET REQUEST using URL Encoding (values from search)
# url = 'https://pythonprogramming.net'
# values = {
#     's': 'basic',
#     'submit': 'Search'
# }

# Performing the encoding and request
# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8')
# req = urllib.request.Request(url, data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()
# Print results
# print(respData)

# 3. Simple GET REQUEST using ERL Encoding (write results to file)
# url2 = 'https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3'
# data2 = urllib.parse.urlencode()
# data2 = data2.encode('utf-8')
# req2 = urllib.request.Request(url)
# resp2 = urllib.request.urlopen(url)
# respData2 = resp2.read()
# fileToWrite = open('test.html', 'wb')
# fileToWrite.write(respData2)
# fileToWrite.close()


# 4. Simple GET Request, URL encoding, and accessing sites restricted
# for robot/program access
try:
    u = 'https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3'
    # contains metadata like browser, IP, user agents, etc.
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) '
                             'Chrome/24.0.1312.27 Safari/537.17'}
    rq = urllib.request.Request(u, headers=headers)
    rs = urllib.request.urlopen(rq)
    rData = rs.read()

    doFile = open('DigitalOceanwithHeader.html', 'wb')
    doFile.write(rData)
    doFile.close()
    print('Results written to DigitalOceanwithHeader.html')
except Exception as e:
    print("Program encountered an error: " + str(e))
