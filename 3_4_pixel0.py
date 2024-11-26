def find_closest_factors(n):
    closest_pair = (None, None)
    min_diff = float('inf')

    # Ищем делители числа n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            # i - делитель, n // i - соответствующий делитель
            j = n // i
            
            # Проверяем, чтобы оба делителя были кратны 3
            if i % 3 == 0 and j % 3 == 0:
                # Если найденная пара делителей ближе друг к другу
                diff = abs(i - j)
                if diff < min_diff:
                    min_diff = diff
                    closest_pair = (i, j)

    if closest_pair[0] is not None and closest_pair[1] is not None:
        return closest_pair
    else:
        return None

if __name__ == "__main__":
    try:
        user_input = int(input("Введите число: "))
        result = find_closest_factors(user_input)

        if result:
            print(f"Два числа, максимально близкие друг к другу, которые делятся на 3 и при умножении дают {user_input}: {result[0]} и {result[1]}")
        else:
            print(f"Не удалось найти такие числа, которые делятся на 3 и дают в произведении {user_input}.")
    except ValueError:
        print("Пожалуйста, введите целое число.")
