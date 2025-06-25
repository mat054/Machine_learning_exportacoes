import os
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import warnings
warnings.filterwarnings('ignore')

# Configuração do MLflow
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("spice_prediction_models")

def preprocess_data(file_path):
    """Pré-processa os dados removendo outliers e preparando features"""
    df = pd.read_csv(file_path)
    
    # Remove outliers
    df = df[(df["is_outlier_Import"] == False) & 
            (df["is_outlier_Export"] == False) & 
            (df["is_outlier_Production"] == False)]
    
    # Seleciona colunas relevantes
    df = df[["Area", "Year", "Item", "Import", "Export", "Production"]]
    
    return df

def run_benchmark_experiment(df, filename, target):
    """Executa benchmark de modelos para uma especiaria e target específicos"""
    
    print(f"Benchmarking da especiaria {filename} para {target}")
    
    # Preparação dos dados
    X = df.drop(columns=[target])
    X = pd.get_dummies(X, columns=["Area", "Item"])
    y = df[target]
    
    # Split dos dados
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Padronização
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Definição dos modelos
    modelos = {
        "LinearRegression": LinearRegression(),
        "DecisionTreeRegressor": DecisionTreeRegressor(random_state=42),
        "RandomForestRegressor": RandomForestRegressor(random_state=42),
        "SVR": SVR(),
    }
    
    best_model_name = None
    best_r2 = -float('inf')
    
    for nome, modelo in modelos.items():
        with mlflow.start_run(run_name=f"benchmark_{filename}_{target}_{nome}"):
            # Log dos parâmetros
            mlflow.log_param("especiaria", filename)
            mlflow.log_param("target", target)
            mlflow.log_param("modelo", nome)
            mlflow.log_param("test_size", 0.2)
            mlflow.log_param("random_state", 42)
            
            # Treinamento e predição
            modelo.fit(X_train_scaled, y_train)
            y_pred = modelo.predict(X_test_scaled)
            
            # Cálculo das métricas
            mae = mean_absolute_error(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            # Log das métricas
            mlflow.log_metric("MAE", mae)
            mlflow.log_metric("MSE", mse)
            mlflow.log_metric("R2", r2)
            mlflow.log_metric("RMSE", np.sqrt(mse))
            
            # Log do modelo
            mlflow.sklearn.log_model(modelo, f"model_{nome}")
            
            # Log das features
            mlflow.log_param("n_features", X.shape[1])
            mlflow.log_param("n_samples", len(df))
            
            print(f"  {nome}: R² = {r2:.4f}, MAE = {mae:.2f}, MSE = {mse:.2f}")
            
            # Atualiza o melhor modelo
            if r2 > best_r2:
                best_r2 = r2
                best_model_name = nome
    
    return best_model_name, best_r2

def run_refinement_experiment(df, filename, target="Import"):
    """Executa refinamento com GridSearchCV para Random Forest"""
    
    print(f"\n### Refinamento para {filename} - Target: {target} ###")
    
    # Preparação dos dados
    X = df.drop(columns=[target])
    X = pd.get_dummies(X, columns=["Area", "Item"])
    y = df[target]
    
    # Split dos dados
    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Padronização
    scaler = StandardScaler()
    X_train_val_scaled = scaler.fit_transform(X_train_val)
    X_test_scaled = scaler.transform(X_test)
    
    # Grade de hiperparâmetros
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5]
    }
    
    with mlflow.start_run(run_name=f"refinement_{filename}_{target}"):
        # Log dos parâmetros
        mlflow.log_param("especiaria", filename)
        mlflow.log_param("target", target)
        mlflow.log_param("modelo", "RandomForestRegressor")
        mlflow.log_param("cv_folds", 5)
        mlflow.log_param("test_size", 0.2)
        mlflow.log_param("random_state", 42)
        
        # Log da grade de hiperparâmetros
        for param, values in param_grid.items():
            mlflow.log_param(f"param_grid_{param}", str(values))
        
        # K-Fold Cross Validation
        kfold = KFold(n_splits=5, shuffle=True, random_state=42)
        model = RandomForestRegressor(random_state=42)
        
        grid_search = GridSearchCV(
            model,
            param_grid,
            cv=kfold,
            scoring='r2',
            n_jobs=-1
        )
        
        # Treinamento
        grid_search.fit(X_train_val_scaled, y_train_val)
        
        # Melhor modelo
        best_model = grid_search.best_estimator_
        best_params = grid_search.best_params_
        
        # Avaliação final
        y_pred = best_model.predict(X_test_scaled)
        
        # Métricas
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        # Log das métricas
        mlflow.log_metric("MAE", mae)
        mlflow.log_metric("MSE", mse)
        mlflow.log_metric("R2", r2)
        mlflow.log_metric("RMSE", np.sqrt(mse))
        mlflow.log_metric("best_cv_score", grid_search.best_score_)
        
        # Log dos melhores hiperparâmetros
        for param, value in best_params.items():
            mlflow.log_param(f"best_{param}", value)
        
        # Log do modelo
        mlflow.sklearn.log_model(best_model, "best_model")
        
        # Log das features
        mlflow.log_param("n_features", X.shape[1])
        mlflow.log_param("n_samples", len(df))
        
        print(f"Melhores hiperparâmetros: {best_params}")
        print(f"R² no teste: {r2}")
        print(f"MAE: {mae}")
        print(f"MSE: {mse}")
        
        return best_params, r2, mae, mse

def main():
    """Função principal que executa todos os experimentos"""
    
    # Configuração dos caminhos
    datasets_path = "datasets"
    datasets_tratados_path = "datasets_tratados"
    targets = ["Import", "Export", "Production"]
    
    # Cria diretório para datasets tratados
    os.makedirs(datasets_tratados_path, exist_ok=True)
    
    # Resultados do benchmark
    benchmark_results = {}
    
    # Processa cada arquivo de dataset
    for filename in os.listdir(datasets_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(datasets_path, filename)
            
            # Pré-processa os dados
            df = preprocess_data(file_path)
            
            # Salva o dataframe tratado
            output_path = os.path.join(datasets_tratados_path, filename)
            df.to_csv(output_path, index=False)
            
            # Executa benchmark para cada target
            for target in targets:
                best_model, best_r2 = run_benchmark_experiment(df, filename, target)
                
                if filename not in benchmark_results:
                    benchmark_results[filename] = {}
                benchmark_results[filename][target] = {
                    'best_model': best_model,
                    'best_r2': best_r2
                }
    
    # Executa refinamento para Import (como no notebook original)
    print("\n" + "="*60)
    print("EXECUTANDO REFINAMENTO COM GRIDSEARCHCV")
    print("="*60)
    
    refinement_results = {}
    
    for filename in os.listdir(datasets_tratados_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(datasets_tratados_path, filename)
            df = pd.read_csv(file_path)
            
            best_params, r2, mae, mse = run_refinement_experiment(df, filename, "Import")
            
            refinement_results[filename] = {
                'best_params': best_params,
                'r2': r2,
                'mae': mae,
                'mse': mse
            }
    
    # Salva resultados em arquivo
    with open("mlflow_results.txt", "w", encoding="utf-8") as f:
        f.write("RESULTADOS DO MLFLOW EXPERIMENT\n")
        f.write("="*50 + "\n\n")
        
        f.write("BENCHMARK RESULTS:\n")
        f.write("-"*20 + "\n")
        for filename, targets_dict in benchmark_results.items():
            f.write(f"\n{filename}:\n")
            for target, results in targets_dict.items():
                f.write(f"  {target}: {results['best_model']} (R² = {results['best_r2']:.4f})\n")
        
        f.write("\n\nREFINEMENT RESULTS:\n")
        f.write("-"*20 + "\n")
        for filename, results in refinement_results.items():
            f.write(f"\n{filename}:\n")
            f.write(f"  Best Params: {results['best_params']}\n")
            f.write(f"  R²: {results['r2']:.4f}\n")
            f.write(f"  MAE: {results['mae']:.2f}\n")
            f.write(f"  MSE: {results['mse']:.2f}\n")
    
    print(f"\nExperimentos concluídos! Resultados salvos em 'mlflow_results.txt'")
    print(f"Para visualizar os experimentos, execute: mlflow ui")

if __name__ == "__main__":
    main()
