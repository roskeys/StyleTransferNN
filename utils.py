LANGs = ["EN", "SG", "CN"]
states = ["START", "B-negative", "B-neutral", "B-positive", "O", "I-negative", "I-neutral", "I-positive", "STOP"]


class Buffer:
    def __init__(self, size):
        self.__buffer = {}
        for i in range(size):
            self.__buffer[i] = {
                'probability': -1,
                "previous_state": None,
                "from_k_th": -1
            }

    def push(self, probability, previous_state, from_k_th):
        for i in range(len(self.__buffer)):
            # if we find one probability that is higher than one of those in the current dict,
            # then we insert it into the right position, and shift rest to the right
            if probability > self.__buffer[i]["probability"]:
                for j in range(len(self.__buffer) - 1, i, -1):
                    self.__buffer[j] = self.__buffer[j - 1]
                self.__buffer[i] = {
                    'probability': probability,
                    "previous_state": previous_state,
                    "from_k_th": from_k_th
                }
                break

    def getBuffer(self):
        return self.__buffer

    def getProbability(self, k):
        return self.__buffer[k]["probability"]

    def getPrevious(self, k):
        return self.__buffer[k]["previous_state"]

    def __str__(self):
        return self.__buffer
