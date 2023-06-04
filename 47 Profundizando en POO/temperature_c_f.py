class Temp_Converter:

    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 213

    @classmethod
    def c_f(cls, celsius):
        if celsius > cls.MAX_CELSIUS:
            raise ValueError(f'Temperatura en C demasiado alta: {celsius}')
        return celsius * 9/5 + 32

    @classmethod
    def f_c(cls, fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f'Temperatura en F demasiado alta: {fahrenheit}')
        return (fahrenheit - 32) * 5/9


if __name__ == '__main__':
    print(f'15 C a F: {Temp_Converter.c_f(15):.2f}')
    print(f'10 F a C: {Temp_Converter.f_c(10):.2f}')
