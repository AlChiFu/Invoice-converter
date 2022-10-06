import xmltodict, json


# Converting the first xml file into json file #
with open("sample.xml") as mex_inv: # Opening the first xml file #
    obj = xmltodict.parse(mex_inv.read()) # Turning the file as a python object #
    data = json.dumps(obj, indent=4) # Turning the python object into a json #

    with open("sample.json", "w") as mex_json: # Creating a new json file #
        mex_json.write(data) # Inserting the json data into the new file #

    mex_json.close()
mex_inv.close()

# Converting the second xml file into json file #
with open("sample2.xml", encoding="utf8") as mex_inv2: # Opening the second xml file #
    obj2 = xmltodict.parse(mex_inv2.read()) # Turning the file as a python object #
    data2 = json.dumps(obj2, indent=4) # Turning the python object into a json #

    with open("sample2.json", "w") as mex_json2: # Creating a new json file #
        mex_json2.write(data2) # Inserting the json data into the new file #

    mex_json2.close()
mex_inv2.close()