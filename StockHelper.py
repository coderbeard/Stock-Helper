class Finance:
    def lookup(self, name):
        pass

    def CleverAlgorithm(self, name):
        if self.lookup(name) > 500:
            return "I think so"
        else:
            return "Sorry, I think my midichlorians have deserted me"

class GoogleFinance(Finance):
    def lookup(self, name):
        # talk to google
        return 501 # <== actual data

class YahooFinance(Finance):
    def lookup(self, name):
        # talk to yahoo
        return 500 # <== actual data

finances = { "google": GoogleFinance(), "yahoo": YahooFinance() }

type = input("Hi, who do you want to ask (google or yahoo): ").lower()
endpoint = finances[type]
therefore = input("What do you wanna lookup? ").upper()
print(endpoint.CleverAlgorithm(therefore))