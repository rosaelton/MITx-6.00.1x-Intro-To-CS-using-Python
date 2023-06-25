def bissection_cbrt(min: float, max:float, n:float, epsilon: float) -> float:
    guess = (min + max) / 2.0

    print(f"Min: {min}; Max: {max}; Guess: {guess}")
    
    if abs(guess ** 3 - n) <= epsilon:
        return guess
    if guess ** 3 > n:
        return bissection_cbrt(min, guess, n, epsilon)
    return bissection_cbrt(guess, max, n, epsilon)

if __name__ == "__main__":
    print(bissection_cbrt(1, 27, 27, 0.0001))
