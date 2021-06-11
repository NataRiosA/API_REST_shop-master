import urllib.parse
import urllib.request
import json

def Buy_product():
    url = 'http://localhost:5000/api/post/clients'
    values = [
    {
        'nombre': "leche",
        'cantidad': "3"
    },
    {
        'nombre': "Azucar",
        'cantidad': "1"
    }, 
]

    params = json.dumps(values).encode('utf-8')
    req = urllib.request.Request(url, data=params,
                                headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(req)
    result = response.read()

    # print (result)
    listJson = json.loads(result)
    # print (listJson)
    print("\nCOMPRAR\n")
    # print("\n")
    for i in listJson:
        # print (listJson[i])
        # print ("\n")
        for x in listJson[i]:
            for j in x:
                print(j,":",x[j])
            print ("\n")

    print("\nCompra realizada")