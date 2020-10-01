

def word_count(s):
    """
    - seperate the words into a key and add a count variable for each time it shows up
    - possibly a set or dictionary
    """
    # Your code here
    counter = {}    # make an empty dictionary for the words
    # characters to ignore
    # ignore_chars = ['"', ':', ';', ',', '.', '-', '+', '=', '/',
    #                 '\\', ' | ', '[', ']' '{', '}', '(', ')', '*', ' ^ ', ' &']
    # ignore_chars = ':,;.-+=/\|[]{\\r}()*^&"'
    # make trans( translate this, to this, delete this)
    ignoreThis = s.maketrans('', '', ':,;.-+=/\|[]{\}()*^&"')
    # translate makes new string so store into variable
    s = s.translate(ignoreThis)
    words = s.lower().split()  # split the sentence up

    # for x in words:  # makes words an iterable object (enumerate)
    # for char in ignore_chars:  # for each character in the ignore array / list
    #     # replace the special characters with an empty space
    #     x = x.replace(char, '')

    for x in words:  # looking at all the words
        if x == '':  # if empty retrun an empty dictionary
            return {}
        if x in counter:  # if already in the counter dictionary add 1
            counter[x] += 1
        else:  # otherwise
            counter[x] = 1  # add to counter and set to 1
    print(counter)
    return counter  # return the counter


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
