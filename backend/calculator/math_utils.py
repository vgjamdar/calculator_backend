import numexpr as ne


def perform_math_operations(query: str) -> str:
    """
    This function evaluate the input query expression
    :param query: Math Expression
    :return: Result of Expression
    """
    result = ne.evaluate(query)
    result = str(result)
    return result
