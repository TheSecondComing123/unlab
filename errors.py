import sys


class NoxanErrorBase:
    """
    Base class for all Errorss.
    """

    def __init__(self, mes=None):
        self.mes = mes or ""

    def raiserr(self):
        errmessage = f"""Noxan {type(self).__name__} {{
    {self.mes}
}}"""

        sys.stderr.write(errmessage)


class InvalidSyntaxError(NoxanErrorBase):
    pass
