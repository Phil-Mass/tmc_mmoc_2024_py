# Write your solution here
def longest(strings: list) ->str:
    length = 0
    return_string =""
    for word in strings:
        if len(word) > length:
            length = len(word)
            return_string = word
    return return_string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))