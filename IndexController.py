import requests

def submitController(input):
    print(input)
    format= "&format=text"
    baseUrl = "https://baconipsum.com/api/"
    type = "type={0}".format(input.get('type', [])[0])
    paras = "&paras={0}".format(input.get('paras', []))
    if('1' in input.get('lorem', [])):
        start_with_lorem = "&start-with-lorem={}".format(input.get('lorem', [])[0]) 
        finalUrl = "{0}?{1}{2}{3}{4}".format(baseUrl,type,paras,start_with_lorem,format)
    else:
        finalUrl = "{0}?{1}{2}{3}".format(baseUrl,type,paras,format)

    r = requests.get(finalUrl)
    baseText = r.text
    return baseText

