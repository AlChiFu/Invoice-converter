import xmltodict, json


with open("sample.xml") as mex_inv:
    obj = xmltodict.parse(mex_inv.read())
    data = json.dumps(obj, indent=4)

    with open("sample.json", "w") as mex_json:
        mex_json.write(data)

    mex_json.close()
mex_inv.close()

with open("sample2.xml", encoding="utf8") as mex_inv2:
    obj2 = xmltodict.parse(mex_inv2.read())
    data2 = json.dumps(obj2, indent=4)

    with open("sample2.json", "w") as mex_json2:
        mex_json2.write(data2)

    mex_json2.close()
mex_inv2.close()