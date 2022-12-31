import json
# nejspise nepouziji, zatim jen pro pozdeji 
#           - ukazka jak prekladat veci dle jsonu - jako slovniku
# from fastapi.responses import JSONResponse


class LocalResponse:
    """
        Class for localized messages from API
    """
    def __init__(self) -> None:
        self.data: dict = self.__load_localisation_data()

    def __load_localisation_data(self) -> dict:
        """
        Description:
            Loads json localisation file data
        Returns:
            dict: Loaded json data
        """
        with open("localisation.json", "r", encoding="utf-8") as f:
            data: dict = json.load(f)
        return data

    def normal_get_text(self, text: str, language: str) -> str:
        translated_text: str = self.data.get(language[:2], {}).get(text, text)

        return translated_text

    def get_text(self, text: str, language: str, *args, **kwargs) -> str:
        """
        Description:
            Returns loaded text, if text is not found returns text passed
            as argument
        Args:
            text (str): Localisation key
            language (str): Target localisation language
        Returns:
            if key and language exists: Returns localised text
            if key and language doesnt exists: Returns localisation key
        """
        translated_text: str = self.data.get(language, {}).get(text, text)
        return translated_text % (kwargs)

    def get_response(self, status_code: int, message: str, locale: str, *args, extra=None, **kwargs) -> JSONResponse:
        """
        Description:
            Returns localized response
        Args:
            status_code (int): HTTP status code
            message (str): Localisation key string
            locale (str): Language
            extra (any): Mostly dictionaries but can by any, it´s additional data for front end
        Returns:
            JSONResponse: Localized JSON response
        """
        locale: str = locale[:2]
        return JSONResponse(
            status_code=status_code,
            content={
                "message": self.get_text(message, locale, args, kwargs) if locale != "en" else message,
                "extra": extra
            }
        )
