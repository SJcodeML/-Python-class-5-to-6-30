


def fareheit_to_celsius (far):
    celsius = (far - 32) * 5/9
    return celsius




def main():
    far = float(input("Enter your degree in farenheit  "))
    value = fareheit_to_celsius(far)
    print(value)


if __name__ == "__main__":
    main()
