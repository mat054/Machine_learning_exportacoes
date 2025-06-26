import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """Instala as dependências necessárias"""
    print("Instalando dependências...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements_mlflow.txt"
        ])
        print(" Dependências instaladas com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f" Erro ao instalar dependências: {e}")
        return False
    return True

def run_experiments():
    """Executa os experimentos MLflow"""
    print("Executando experimentos MLflow...")
    try:
        subprocess.check_call([sys.executable, "spice_mlflow_experiments.py"])
        print(" Experimentos executados com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f" Erro ao executar experimentos: {e}")
        return False

def start_mlflow_ui():
    """Inicia a interface web do MLflow"""
    print("Iniciando MLflow UI...")
    print("Acesse: http://localhost:5000")
    print("Pressione Ctrl+C para parar o servidor")
    
    try:
        subprocess.run(["mlflow", "ui", "--host", "0.0.0.0", "--port", "5000"])
    except KeyboardInterrupt:
        print("\nServidor MLflow parado.")
    except Exception as e:
        print(f" Erro ao iniciar MLflow UI: {e}")

def main():
    """Função principal"""
    print("="*60)
    print("MLFLOW EXPERIMENTOS - ESPECIARIAS")
    print("="*60)
    
    # Verifica se estamos no diretório correto
    if not Path("datasets").exists():
        print(" Diretório 'datasets' não encontrado!")
        print("Certifique-se de estar no diretório correto.")
        return
    
    # Menu de opções
    while True:
        print("\nOpções:")
        print("1. Instalar dependências")
        print("2. Executar experimentos")
        print("3. Iniciar MLflow UI")
        print("4. Executar tudo (instalar + experimentos)")
        print("5. Sair")
        
        choice = input("\nEscolha uma opção (1-5): ").strip()
        
        if choice == "1":
            install_requirements()
        
        elif choice == "2":
            if run_experiments():
                print("\n Resultados salvos em 'mlflow_results.txt'")
                print(" Para visualizar detalhes, execute a opção 3")
        
        elif choice == "3":
            start_mlflow_ui()
        
        elif choice == "4":
            if install_requirements():
                if run_experiments():
                    print("\n Resultados salvos em 'mlflow_results.txt'")
                    print(" Iniciando MLflow UI...")
                    start_mlflow_ui()
        
        elif choice == "5":
            print("Saindo...")
            break
        
        else:
            print(" Opção inválida!")

if __name__ == "__main__":
    main() 