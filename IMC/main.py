def display_imc(imc: float) -> str:
    imc_display: str = "Seu IMC é de "+"%.2f"%imc+" - Está classificado como "
    res = ""
    if imc < 18.5:
        res = "Magreza"
    elif imc >= 18.5 and imc < 24.9:
        res = "Normal"
    elif imc >= 24.9 and imc < 29.9:
        res = "Sobrepeso"
    elif imc >= 29.9 and imc < 39.9:
        res = "Obesidade"
    elif imc >= 39.9:
        res = "Obesidade extrema"


    return imc_display + res

def main():
    print("===== CALCULADORA IMC! =====")
    print("Ofereça-nos seu peso (kg): ")
    peso: float = float(input())
    print("Ofereça-nos sua altura (m):" )
    altura: float = float(input())
    

    imc = peso / (altura * altura)

    print(display_imc(imc))
    return

main()