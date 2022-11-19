import requests

class Guess:
    def __init__(self) -> None:
        # creates Guess class #
        self.geoguessr_url = str()
        self.latitude = float()
        self.longitude = float()
    
    def create_guess(self, url: str, lat: float, lng: float) -> None:
        # inits variables #
        self.geoguessr_url = url
        self.latitude = lat
        self.longitude = lng

    def make_guess(self) -> bool:
        # makes guess #
        # variables
        content = ""
        token = ""
        data = {
            "token": token,
            "lat": self.latitude,
            "lng": self.longitude,
            "timeOut": False
        }
        headers = {
            "Content-Type": "application/json",
            "Cookie": f"devicetoken={content}; G_ENABLED_IDPS=google; _ncfa={content};"
        }
        # request
        response = requests.post(self.geoguessr_url, json=data, headers=headers)
        if (response.status_code == 200):
            return True
        return False