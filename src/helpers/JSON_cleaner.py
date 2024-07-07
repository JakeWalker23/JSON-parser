class JSONCleaner:

    @staticmethod
    def clean_json_string(json_string: str) -> list:
        formatted_json_list = []

        json_string_split = json_string.split(',')

        for key_value in json_string_split:
            formatted_key_value = key_value.replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace('"', '').replace(' ', '').split(':')

            formatted_json_list.append(formatted_key_value)

        return formatted_json_list