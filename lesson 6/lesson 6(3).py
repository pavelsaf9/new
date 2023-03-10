def main():
    word = input("Введите слово: ")
    compare = lambda x: "Это слово больше, чем predator" if x > "predator" \
        else "Это слово меньше, чем predator"
    result = compare(word)
    print(result)


if __name__ == "__main__":
    main()
