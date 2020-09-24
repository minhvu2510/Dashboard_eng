def check_require(list_data,data):
    list_require = []
    for key in list_data:
        if not data[key]:
            list_require.append(key)
    if list_require:
        return {"status": False, "message": "Enter {}".format(", ".join(list_require))}
    return {"status": True}
