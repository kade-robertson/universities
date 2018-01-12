class University():
    def __init__(self, json):
        self.name = json['name']
        self.domains = json['domains']
        self.web_pages = json['web_pages']
        self.country_code = json['alpha_two_code']
        self.stateprov = json['state-province']
        self.country = json['country']
