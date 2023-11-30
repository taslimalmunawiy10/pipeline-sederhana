# average_calculator.py

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

def get_user_input():
    user_input = input("Masukkan sejumlah angka, pisahkan dengan spasi: ")
    numbers = [float(x) for x in user_input.split()]
    return numbers

def main():
    numbers = get_user_input()
    average = calculate_average(numbers)
    print(f"Rata-rata dari angka-angka tersebut adalah: {average}")

if __name__ == "__main__":
    main()

