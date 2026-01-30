def justify_paragraphs(N, Max, paragraphs):
    for paragraph in paragraphs:
        words = paragraph.split()
        current_line = []
        current_length = 0

        for word in words:
            # Check if adding the current word exceeds the Max length
            if current_length + len(word) + len(current_line) > Max:
                # Output the left-justified line
                print(' '.join(current_line))
                # Reset for the next line
                current_line = []
                current_length = 0

            current_line.append(word)
            current_length += len(word)

        # Output the last line left-justified
        print(' '.join(current_line))

        # Output the right-justified paragraph
        if len(words) > 1:
            spaces_needed = Max - current_length - (len(current_line) - 1)
            space_between_words = spaces_needed // (len(current_line) - 1) if len(current_line) > 1 else 0

            # Output right-justified lines
            for i in range(len(current_line) - 1):
                print(current_line[i] + ' ' * space_between_words, end='')
                if i < spaces_needed % (len(current_line) - 1):
                    print(' ', end='')

            # Output the last word left-justified
            print(current_line[-1])

if __name__ == "__main__":
    # Input: number of paragraphs (N), maximum length of a line (Max)
    N, Max = map(int, input().split())

    # Input: paragraphs
    paragraphs = [input() for _ in range(N)]

    # Call the function to justify paragraphs
    justify_paragraphs(N, Max, paragraphs)