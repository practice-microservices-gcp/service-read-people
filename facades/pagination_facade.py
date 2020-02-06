import re

class PaginationFacade():

    def offsetLimitValidation(self, offset, limit):
        numberPatter = re.compile(r"^([\s\d]+)$")

        if (numberPatter.match(offset) and numberPatter.match(limit)):
            return { "offset": int(offset), "limit": int(limit) }
        else:
            return False



paginationFacade = PaginationFacade()