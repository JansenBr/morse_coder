
class MorseStringFormatingError(Exception):
    def __init__(
        self,
        string:str,
        white_spaces:dict,
        error_message:str='The string: "{string}"\n is not formated correctly, check for those white spaces: {white_spaces}'
    ) -> None:
        if white_spaces:
            self.error_message = error_message.format(
                string=string, white_spaces=white_spaces
            )
        else:
            self.error_message = 'The string: "{string}"\n is not formated correctly, check the white spaces'
        super().__init__(self.error_message)

