# Longest Common Subsequence (LCS)
# Dynamic Programming - Tabulation

def build_lcs_table(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    # Create DP table with extra row and column
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if seq1[i - 1] == seq2[j - 1]:
                # Characters match
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                # Characters do not match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp


def reconstruct_lcs(dp, seq1, seq2):
    i = len(seq1)
    j = len(seq2)

    result = []

    # Trace the table backwards
    while i > 0 and j > 0:

        if seq1[i - 1] == seq2[j - 1]:
            result.append(seq1[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    # Reverse because we traced backwards
    result.reverse()

    return "".join(result)


def lcs(seq1, seq2):
    dp = build_lcs_table(seq1, seq2)

    length = dp[len(seq1)][len(seq2)]

    subsequence = reconstruct_lcs(dp, seq1, seq2)

    return length, subsequence, dp


def print_dp_table(dp, seq1, seq2):
    print("\nDP Table:")

    print("      ", end="")
    for ch in seq2:
        print(f"{ch:>3}", end="")
    print()

    for i in range(len(dp)):
        if i == 0:
            print("  ", end="")
        else:
            print(f"{seq1[i - 1]:>2}", end="")

        for value in dp[i]:
            print(f"{value:>3}", end="")

        print()


# Main Program
seq1 = input("Enter first sequence: ")
seq2 = input("Enter second sequence: ")

length, subsequence, dp = lcs(seq1, seq2)

print_dp_table(dp, seq1, seq2)

print("\nLongest Common Subsequence:", subsequence)
print("Length of LCS:", length)