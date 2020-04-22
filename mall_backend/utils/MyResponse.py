from werkzeug.exceptions import HTTPException
import json


class APIException(HTTPException):

    def get_body(self, environ=None):
        """Get the HTML body."""
        return json.dumps(dict(
            code=self.code,
            name=self.name,
            description=self.get_description(environ)
        ))
