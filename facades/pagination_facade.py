

class PaginationFacade():

    def offsetLimitValidation(self, offset, limit):
        return isinstance(offset, int) and isinstance(limit, int)



paginationFacade = PaginationFacade()