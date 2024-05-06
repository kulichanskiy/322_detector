# TEST SCRIPT FOR ANALYSIS
# Не продумана логика, тестовый файл для временного анализа

coef_1 = 2.02  # 12:00
coef_2 = 2.01  # 14:00
coef_3 = 1.92  # 16:00

def coef_analysis(coef1,coef2,coef3):
    coef_slope1_2 = coef1-coef2
    coef_slope2_3 = coef2-coef3
    if coef_slope1_2 < coef_slope2_3:
        slope = 1
    else:
        slope = 0
    return slope

analusis = coef_analysis(coef_1,coef_2,coef_3)
print(analusis)
