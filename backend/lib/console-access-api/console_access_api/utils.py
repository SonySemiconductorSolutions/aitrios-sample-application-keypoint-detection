import base64


class Utils:
    @staticmethod
    def Base64Decoder(data):
        if type(data) is str:
            data = data.encode("utf-8")
        decoded_data = base64.decodebytes(data)
        return decoded_data

    @staticmethod
    def Base64EncodedStr(data):
        if type(data) is str:
            data = data.encode("utf-8")
        encoded_data = base64.b64encode(data)
        encoded_str = str(encoded_data).replace("b'", "").replace("'", "")
        return str(encoded_str)
