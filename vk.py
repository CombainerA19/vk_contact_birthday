"""
Get clint credential
"""
import json
import requests

def cred():
    """
    Not needed for this app
    """
    CLIENT_ID = 7741733
    CLIENT_SECRET = "C0mIYmcwBAYxG1Mfw8RV"
    url = f"https://oauth.vk.com/access_token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&v=5.126&grant_type=client_credentials"
    req = requests.get(url)
    return req.json()["access_token"]

def make_call(id):
    """
    Get info about users friends

    id: str - ID of user to get friends birthday
    return: obj - json of birthday data
    """
    ACCESS_TOKEN = "df5492eddf5492eddf5492ed82df22b3c8ddf54df5492edbf4439ef0061baab63390e39"
    fields = "bdate,sex,city,country"
    user_id = id # 607235444
    url = f"https://api.vk.com/method/friends.get?user_id={user_id}&fields={fields}&access_token={ACCESS_TOKEN}&v=5.126"
    req = requests.get(url)
    data = []
    try:    # Error - maybe invalid user 
        for friend in req.json()["response"]["items"]:
            # Only access user with birthday available(user made it public to access)
            if "bdate" in friend:
                first_name = friend["first_name"]
                last_name = friend["last_name"]
                id = friend["id"]
                bdate = friend["bdate"] # DD.MM.YYYY
                tmp_bdate = bdate.split(".")
                tmp_data = {
                    "name": {
                        "first_name": first_name,
                        "last_name": last_name
                    },
                    "id": id,
                    "bday": {
                        "day": tmp_bdate[0],
                        "month": tmp_bdate[1]
                    }
                }
                data.append(tmp_data)
    except:
        pass
    return data

def main():
    print(make_call("607235444"))

if __name__ == "__main__":
    main()
