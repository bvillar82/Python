import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# Função para calcular a data com base na quantidade de dias inserida pelo usuário
def calculate_date():
    input_date = date_entry.get()
    try:
        # Modifique para aceitar o formato DDMMYYYY
        start_date = datetime.strptime(input_date, '%d%m%Y')

        # Obtenha a quantidade de dias inserida pelo usuário
        days_to_add = int(days_entry.get())

        # Adicione a quantidade de dias inserida pelo usuário à data inicial
        end_date = start_date + timedelta(days=days_to_add)

        # Modifique para exibir o resultado no formato DD/MM/YYYY
        result.config(text=end_date.strftime('%d/%m/%Y'))

        # Traduza o nome do dia da semana para português brasileiro
        day_of_week_pt_br = {
            'Monday': 'Segunda-feira',
            'Tuesday': 'Terça-feira',
            'Wednesday': 'Quarta-feira',
            'Thursday': 'Quinta-feira',
            'Friday': 'Sexta-feira',
            'Saturday': 'Sábado',
            'Sunday': 'Domingo'
        }
        day_of_week = end_date.strftime('%A')
        day_of_week_label.config(text=day_of_week_pt_br.get(day_of_week, ''))

        result_frame.config(borderwidth=2, relief="solid")  # Adicione a borda quando o resultado for gerado
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira uma data válida no formato DDMMYYYY")

# Função para apagar os campos de data e quantidade de dias
def clear_fields():
    date_entry.delete(0, tk.END)
    days_entry.delete(0, tk.END)
    result.config(text="")
    day_of_week_label.config(text="")
    result_frame.config(borderwidth=0)  # Remova a borda quando os campos forem apagados

# Criação da janela principal
window = tk.Tk()
window.title("Calculadora de Dias")

# Defina um tamanho mínimo e máximo
window.geometry('500x320')  # Aumente a altura da janela para acomodar o novo campo
window.minsize(500, 320)  # Tamanho mínimo
window.maxsize(500, 320)  # Tamanho máximo

# Não permita o redimensionamento da janela
window.resizable(False, False)

# Use grid em vez de pack para melhor organização
date_label = tk.Label(window, text="Insira a data (DDMMYYYY):")
date_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

date_entry = tk.Entry(window)
date_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# Novo rótulo e entrada para a quantidade de dias
days_label = tk.Label(window, text="Quantidade de dias a adicionar:")
days_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

days_entry = tk.Entry(window)
days_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

# Botão para enviar
submit_button = tk.Button(window, text="Enviar", command=calculate_date)
submit_button.grid(row=2, column=0, columnspan=2, padx=180, pady=10, sticky='e')  # Posiciona o botão abaixo do campo de entrada

# Botão para apagar os campos
clear_button = tk.Button(window, text="Apagar", command=clear_fields)
clear_button.grid(row=2, column=1, padx=90, pady=10, sticky='e')  # Posiciona o botão ao lado do botão "Enviar" e alinha à direita
submit_button.grid_configure(pady=10)  # Ajuste o espaçamento do botão "Enviar"
clear_button.grid_configure(pady=10)  # Ajuste o espaçamento do botão "Apagar"

# Label para o resultado e dia da semana
result_frame = tk.Frame(window, borderwidth=0)  # Crie um frame para o resultado e o dia da semana
result_frame.grid(row=3, column=0, padx=35, pady=20, columnspan=4, sticky='w')
result = tk.Label(result_frame, text="", font=('Arial', 12))
result.pack(side='left', padx=35, pady=10)

day_of_week_label = tk.Label(result_frame, text="", font=('Arial', 12, 'bold'))
day_of_week_label.pack(side='left', padx=40)

# Crie uma Label para a declaração
statement_frame = tk.Frame(window, borderwidth=2, relief="solid")
statement_frame.grid(row=4, column=0, columnspan=4, padx=35, pady=20, sticky='w')
statement = tk.Label(statement_frame, text="A calculadora considera dias corridos para apresentar a data.", justify='left', wraplength=450)
statement.pack(padx=10, pady=10)

# Iniciar a janela
window.mainloop()
