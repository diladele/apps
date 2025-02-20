import json
import codecs

#
#
#
def is_found(app, apps):

    for item in apps:
        if item["id"] == app:
            return True

    return False

#
#
#
def verify_category(cat, apps):

    cat_id = cat["id"]

    print(f"verifying category {cat_id} ...")

    for app in cat["apps"]:

        if is_found(app, apps):
            continue

        raise Exception(f"app {app} is undefined")

#
#
#
def verify_categories(cats, apps):

    for cat in cats:
        verify_category(cat, apps)

#
#
#
def verify():

    # load apps as json
    with codecs.open("apps.json", "r", encoding="utf-8") as fin:
        apps = json.load(fin)

    # load categories as json
    with codecs.open("categories.json", "r", encoding="utf-8") as fin:
        cats = json.load(fin)

    verify_categories(cats, apps)

    print("SUCCESS!!!")

#
#
#
def main():

    verify()

main()