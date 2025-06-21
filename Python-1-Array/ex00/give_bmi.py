#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀              𓐓  give_mi.py 𓐔           
#  ⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
#  ⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀       Dev: oezzaou </var/spool/mail/oezzaou>
#  ⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
#  ⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#  ⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       Created: 2025/06/21 16:51:48 by oezzaou
#  ⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       Updated: 2025/06/21 19:01:55 by oezzaou
#  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
#  ⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀                             𓆩♕𓆪
#  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀                     𓄂 oussama ezzaou𓆃
#  ⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# ===[ Imports: ]==============================================================
import numpy as np
# from numpy.typing import NDArray

# INFO:========================================================================
# - BMI: stands for 'Body Mass Index', which is simple way to estimate whether
#   a person has hearlthy weight for their height.
#       BMI =  weight(kg) / (height(m))^2


# ===[ give_bmi: ]=============================================================
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    allowed_dtypes = [np.int32, np.int64, np.float32, np.float64]
    height_array = np.array(height)
    weight_array = np.array(weight)

    if height_array.shape != weight_array.shape:
        raise Exception("Error: Invalid Size:")
    if (height_array.dtype not in allowed_dtypes or
            weight_array.dtype not in allowed_dtypes):
        raise Exception("Error: Invalid dtype:")
    if np.any(height_array == 0):
        raise Exception("Errror: Division By Zero")

    bmi_array = weight_array / (height_array ** 2)
    np.set_printoptions(precision=13)
    return bmi_array.tolist()


# ===[ apply_limit:]===========================================================
def apply_limit(bmi: np.ndarray, limit: int) -> np.ndarray:
    return np.array(bmi) >= limit


# ===[ main ]==================================================================
def main():
    height = np.array([2.71, 1.15])
    wieght = np.array([164.3, 38.4])
    bmi = give_bmi(height, wieght)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == '__main__':
    main()

# QUESTION:[ Why using NDArray over ndarray ? ]================================
# - np.ndarray class does not support 'precise typeing', (like specifyin the
#   dtypes or shape), So numpy introduced:
#    [ from numpy.typing import NDArray ]
# - It was added in Numpy 1.20 as part of the 'numpy.typing' module to support
# 'type checkers' like 'mypy' or 'Pyright'.
# - > [ When to use `NDArray` ]
#   . 'Hint Numpy Arrays' in your functions
#   . Specify the data type (e.g, `np.int64`, np.`np.int64`, etc)
#   . Comibe it with 'typing Annotated' or 'Literal (advaced typing)'
#     (optional)
# ==============================================================================
