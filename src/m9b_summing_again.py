"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Mark Hays, Amanda Stouder,
         their colleagues and Joey Hatfield.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_powers()
    run_test_sum_powers_in_range()


def run_test_sum_powers():
    """ Tests the   sum_powers   function. """
    # ------------------------------------------------------------------
    # done: 2. Implement this function.
    #   It TESTS the  sum_powers  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers   function:')
    print('--------------------------------------------------')

    #Test 1:
    expected = 4.33659
    answer = sum_powers(4, .1)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    #Test 2:
    expected = 2.67329
    answer = sum_powers(3, -.2)
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    #Test 3:
    expected = 55
    answer = sum_powers(5, 2)
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

def sum_powers(n, p):
    """
    What comes in:  A non-negative integer n
                    and a number p.
    What goes out:  The sum   1**p + 2**p + 3**p + ... + n**p
       for the given numbers n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:   None.
    Examples:
      -- sum_powers(5, -0.3) returns about 3.80826
      -- sum_powers(100, 0.1) returns about 144.45655
    """
    # ------------------------------------------------------------------
    # done: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------

    if n>=0 & isinstance(n, int):
        z = 0
        y = 1
        for k in range(n):
            z = z + (y**p)
            y = y + 1
        return z
    else:
        return None

def run_test_sum_powers_in_range():
    """ Tests the   sum_powers_in_range   function. """
    # ------------------------------------------------------------------
    # done: 4. Implement this function.
    #   It TESTS the  sum_powers_in_range  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers_in_range   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 3.33659
    answer = sum_powers_in_range(2, 4, .1)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # Test 2:
    expected = 2.67329
    answer = sum_powers_in_range(1, 3, -.2)
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    # Test 3:
    expected = 55
    answer = sum_powers_in_range(0, 5, 2)
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

def sum_powers_in_range(m, n, p):
    """
    What comes in:  Non-negative integers m and n, with n >= m,
                    and a number p.
    What goes out:  the sum
           m**p + (m+1)**p + (m+2)**p + ... + n**p
       for the given numbers m, n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:  None.
    Example:
      -- sum_powers_in_range(3, 100, 0.1) returns about 142.384776
    """
    # ------------------------------------------------------------------
    # done: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers_in_range  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------

    if n>=0 & isinstance(n, int) & isinstance(m, int) & m<n:
        z = 0
        y = m
        for k in range(n-m+1):
            z = z + (y**p)
            y = y + 1
        return z
    else:
        return None

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
