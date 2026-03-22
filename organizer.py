import os
import shutil
from datetime import datetime

class FileOrganizer:
    def __init__(self):
        # Definição das categorias e suas extensões
        self.extensions = {
            'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
            'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
            'Executaveis': ['.exe', '.msi'],
            'Compactados': ['.zip', '.rar', '.7z'],
            'Scripts': ['.py', '.js', '.html', '.css', '.cpp']
        }

    def organize(self, directory_path):
        # Verifica se o diretório existe
        if not os.path.exists(directory_path):
            print(f"Erro: O caminho '{directory_path}' não foi encontrado.")
            return

        print(f"Iniciando organização em: {directory_path}...")
        
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

        for file in files:
            file_path = os.path.join(directory_path, file)
            extension = os.path.splitext(file)[1].lower()
            moved = False

            for category, exts in self.extensions.items():
                if extension in exts:
                    self._move_file(directory_path, category, file, file_path)
                    moved = True
                    break
            
            # Se a extensão não estiver mapeada, vai para 'Outros'
            if not moved:
                self._move_file(directory_path, 'Outros', file, file_path)

        print("Organização concluída com sucesso!")

    def _move_file(self, base_path, category, file_name, old_path):
        target_dir = os.path.join(base_path, category)
        
        # Cria a pasta da categoria se não existir
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        target_path = os.path.join(target_dir, file_name)
        
        # Move o arquivo
        shutil.move(old_path, target_path)
        print(f"[OK] {file_name} -> {category}/")

if __name__ == "__main__":
    organizer = FileOrganizer()
    
    # Substitua pelo caminho da pasta que você quer organizar
    # Exemplo: "C:/Users/Moreira/Downloads"
    caminho_alvo = input("Digite o caminho da pasta para organizar: ")
    organizer.organize(caminho_alvo)