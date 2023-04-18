def compute_sum(n):
    '''
    The recursive function that returns the sum of the values from k = 1
    to the n number entered according to the formula (-1)^(k+1)/k.

    This function is a recursive function.
    The function first checks whether n is 0 or less than 0.
    If n is not 0 or less it starts checking recursively as compute_sum(n - 1).
    This process continues until the n parameter drops to 0. When the n parameter is 0,
    the result variable is set to 0 and the function begins to be restored.
    When n parameter is 0, the process ends and when n parameter is 1,
    it continues from where it left off.
    The line "result += (-1)**(n + 1) / n" runs up to the original n count,
    and the result is cumulatively incremented from 0 to the required value.

    Parameters
    ----------
    n: int
        The upper limit of the sum (non-negative integer).
    result: float
        A global variable to store the intermediate results during recursion.
    
    Return Type
    -------
    None
        The function does not return any value.

    Returns
    -------
    float
        The sum according to the given formula for n.

    Example
    -------
    >>> compute_sum(3)
    0.8333333333333333
    >>> compute_sum(100)
    0.688172179310195
    >>> compute_sum(0)
    0
    >>> compute_sum(-35)
    0
    '''
    global result
    if n <= 0:
        result = 0
    else:
        compute_sum(n - 1)
        result += (-1)**(n + 1) / n

n = int(input("Please enter n as an integer:"))
compute_sum(n)
print("Sum: %s" %result)