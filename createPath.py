from firebase import Firebase


class CreatePath:
    def __init__(self):
        config = {
            "apiKey": "AIzaSyAl0sJD8bl30gnWH9juh6pywzOzsuzSdso",
            "authDomain": "wear-by-weather.firebaseapp.com",
            "databaseURL": "https://wear-by-weather.firebaseio.com",
            "storageBucket": "wear-by-weather.appspot.com",
            "serviceAccount": "wear-by-weather.json"
        }
        self.fir = Firebase(config)

        self.minus_temperature = ["1-3", "4-6", "7-9", "10-12", "13-15", "16-18", "19-21", "22-24", "25-27", "28-30"]
        self.plus_temperature = ["0-5", "6-11", "12-17", "18-23", "24-30"]
        self.styles = ["Casual", "JeanStyle", "SportStyle", "OfficialStyle", "BeachStyle"]
        self.skies = ["Rain", "Snow", "Clouds", "Thunderstorm", "Mist, Fog", "Clear", "Drizzle"]
        self.body_weights = ["1stDegreeObesity", "2ndDegreeObesity", "3rdDegreeObesity", "BodyMassDeficiency",
                             "NormalBodyWeight", "Overweight", "Underweight"]

        self.create_paths_minus()
        self.create_paths_plus()

    def create_paths_minus(self):
        for gender in ["Men", "Female"]:
            for body_weight in self.body_weights:
                for style in self.styles:
                    for temp in self.minus_temperature:
                        for sky in self.skies:
                            self.fir.storage().child(
                                "{2}/Underweight/{0}/MinusTemperature/{1}/{3}/1.txt".format(style, temp, gender,
                                                                                    sky, body_weight)).put(
                                "1.txt")

    def create_paths_plus(self):
        for gender in ["Men", "Female"]:
            for body_weight in self.body_weights:
                for style in self.styles:
                    for temp in self.plus_temperature:
                        for sky in self.skies:
                            self.fir.storage().child(
                                "{2}/{4}/{0}/PlusTemperature/{1}/{3}/1.txt".format(style, temp, gender,
                                                                                   sky, body_weight)).put(
                                "1.txt")


if __name__ == "__main__":
    CreatePath()
