import tiktoken


def count_tokens(text: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))


def inspect_tokens(text: str, encoding_name: str = "cl100k_base") -> list[str]:
    encoding = tiktoken.get_encoding(encoding_name)
    return [encoding.decode([token_id]) for token_id in encoding.encode(text)]


if __name__ == "__main__":
    value = input("Enter text: ")
    print("Token count:", count_tokens(value))
    print("Token pieces:", inspect_tokens(value))
