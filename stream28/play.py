import streamlit as st

st.title('Calculadora Simple')

# Entrada de números
num1 = st.number_input('Ingrese el primer número', value=0.0)
num2 = st.number_input('Ingrese el segundo número', value=0.0)

# Selección de operación
operacion = st.selectbox('Seleccione una operación', ['Suma', 'Resta', 'Multiplicación', 'División'])

# Realizar la operación
resultado = None
if operacion == 'Suma':
    resultado = num1 + num2
elif operacion == 'Resta':
    resultado = num1 - num2
elif operacion == 'Multiplicación':
    resultado = num1 * num2
elif operacion == 'División':
    resultado = num1 / num2 if num2 != 0 else 'Error: División por cero'

# Mostrar resultado
if st.button('Calcular'):
    st.write(f'Resultado: {resultado}')
