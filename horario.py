#arquvo de horario atual
from datetime import datetime

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

# Exibe a hora atual
print(f"A hora atual é: {hora_atual}")